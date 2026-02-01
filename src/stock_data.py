"""
Vietnamese Stock Data Fetcher
Fetches real-time stock data from Vietnamese exchanges (HSX, HNX, UPCOM)
"""

import requests
import json
from datetime import datetime
from typing import Dict, List, Optional
import time


class VNStockData:
    """Fetch Vietnamese stock data from public APIs"""

    # API endpoints
    VNDIRECT_API = "https://finfo-api.vndirect.com.vn/v4/stock_prices"
    SSI_API = "https://iboard-api.ssi.com.vn/statistics/charts/symbols"

    # Retry configuration
    MAX_RETRIES = 3
    RETRY_DELAY = 2  # seconds

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Accept': 'application/json',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://vndirect.com.vn/'
        })

    def _fetch_from_vndirect(self, symbol: str) -> Optional[Dict]:
        """Fetch data from VNDirect API with retry logic"""
        for attempt in range(self.MAX_RETRIES):
            try:
                url = f"{self.VNDIRECT_API}?symbols={symbol}&sort=date&size=1"
                response = self.session.get(url, timeout=30)  # Increased timeout

                if response.status_code == 200:
                    data = response.json()
                    if data.get('data') and len(data['data']) > 0:
                        stock_data = data['data'][0]
                        return {
                            'symbol': symbol,
                            'price': stock_data.get('close', 0),
                            'change': stock_data.get('change', 0),
                            'change_percent': stock_data.get('pctChange', 0),
                            'volume': stock_data.get('nmVolume', 0),
                            'high': stock_data.get('high', 0),
                            'low': stock_data.get('low', 0),
                            'open': stock_data.get('open', 0),
                            'timestamp': datetime.now().isoformat(),
                            'source': 'VNDirect'
                        }
            except requests.exceptions.Timeout:
                if attempt < self.MAX_RETRIES - 1:
                    wait_time = self.RETRY_DELAY * (2 ** attempt)  # Exponential backoff
                    time.sleep(wait_time)
                continue
            except Exception as e:
                if attempt == self.MAX_RETRIES - 1:
                    print(f"  VNDirect failed after {self.MAX_RETRIES} attempts: {str(e)[:50]}")
                break

        return None

    def _fetch_from_ssi(self, symbol: str) -> Optional[Dict]:
        """Fetch data from SSI API as fallback"""
        try:
            # SSI uses different endpoint structure
            url = f"https://iboard-api.ssi.com.vn/statistics/charts/stock"
            params = {
                'symbols': symbol,
                'resolution': 'D',  # Daily
                'limit': 1
            }
            response = self.session.get(url, params=params, timeout=30)

            if response.status_code == 200:
                data = response.json()
                if data and 'data' in data and len(data['data']) > 0:
                    stock_data = data['data'][0]
                    return {
                        'symbol': symbol,
                        'price': stock_data.get('close', stock_data.get('c', 0)),
                        'change': stock_data.get('change', 0),
                        'change_percent': stock_data.get('changePercent', stock_data.get('changePc', 0)),
                        'volume': stock_data.get('volume', stock_data.get('v', 0)),
                        'high': stock_data.get('high', stock_data.get('h', 0)),
                        'low': stock_data.get('low', stock_data.get('l', 0)),
                        'open': stock_data.get('open', stock_data.get('o', 0)),
                        'timestamp': datetime.now().isoformat(),
                        'source': 'SSI'
                    }
        except Exception as e:
            print(f"  SSI API error: {str(e)[:50]}")

        return None

    def get_stock_price(self, symbol: str) -> Optional[Dict]:
        """
        Get current price and info for a stock symbol

        Args:
            symbol: Stock symbol (e.g., 'VCB', 'VNM', 'HPG')

        Returns:
            Dictionary with stock data or None if failed
        """
        # Try VNDirect first
        data = self._fetch_from_vndirect(symbol)
        if data:
            return data

        # Fallback to SSI
        print(f"  Trying SSI API as fallback...")
        data = self._fetch_from_ssi(symbol)
        if data:
            return data

        return None

    def get_multiple_stocks(self, symbols: List[str]) -> Dict[str, Dict]:
        """
        Get data for multiple stocks

        Args:
            symbols: List of stock symbols

        Returns:
            Dictionary mapping symbols to their data
        """
        results = {}
        for symbol in symbols:
            print(f"Fetching {symbol}...")
            data = self.get_stock_price(symbol)
            if data:
                results[symbol] = data
            time.sleep(0.5)  # Rate limiting

        return results

    def get_historical_data(self, symbol: str, days: int = 30) -> List[Dict]:
        """
        Get historical price data

        Args:
            symbol: Stock symbol
            days: Number of days of history

        Returns:
            List of historical data points
        """
        try:
            url = f"{self.VNDIRECT_API}?symbols={symbol}&sort=date:desc&size={days}"
            response = self.session.get(url, timeout=10)

            if response.status_code == 200:
                data = response.json()
                return data.get('data', [])
        except Exception as e:
            print(f"Error fetching historical data for {symbol}: {e}")

        return []

    def search_stocks(self, query: str) -> List[Dict]:
        """
        Search for stocks by name or symbol

        Args:
            query: Search query

        Returns:
            List of matching stocks
        """
        try:
            url = f"https://finfo-api.vndirect.com.vn/v4/stocks?q=code:{query}~,companyName:{query}~&size=20"
            response = self.session.get(url, timeout=10)

            if response.status_code == 200:
                data = response.json()
                stocks = []
                for stock in data.get('data', []):
                    stocks.append({
                        'symbol': stock.get('code'),
                        'name': stock.get('companyName'),
                        'exchange': stock.get('exchange'),
                        'industry': stock.get('icbName')
                    })
                return stocks
        except Exception as e:
            print(f"Error searching stocks: {e}")

        return []

    def get_market_overview(self) -> Dict:
        """
        Get overall market statistics

        Returns:
            Market overview data
        """
        # Common index symbols
        indices = ['VNINDEX', 'HNX', 'UPCOM']
        overview = {}

        for index in indices:
            data = self.get_stock_price(index)
            if data:
                overview[index] = data

        return overview


# Comprehensive Vietnamese stock database (HSX, HNX, UPCOM)
STOCK_LISTS = {
    'commodities': ['GOLD', 'SILVER', 'XAU', 'XAG'],

    'blue_chips': ['VCB', 'VHM', 'VIC', 'VNM', 'HPG', 'GAS', 'MSN', 'TCB', 'VPB', 'MBB',
                   'BID', 'CTG', 'VRE', 'SAB', 'PLX', 'MWG', 'SSI', 'FPT', 'VJC', 'GVR'],

    'banks': ['VCB', 'TCB', 'MBB', 'VPB', 'CTG', 'BID', 'ACB', 'STB', 'HDB', 'TPB',
              'VIB', 'MSB', 'SHB', 'EIB', 'LPB', 'OCB', 'VBB', 'BVB', 'NVB', 'BAB',
              'ABB', 'PGB', 'SCB', 'SeABank', 'NAB', 'BaoVietBank', 'KLB', 'VietBank'],

    'real_estate': ['VHM', 'VIC', 'NVL', 'PDR', 'DXG', 'KDH', 'BCM', 'DIG', 'HDG', 'NLG',
                    'DXS', 'SCR', 'CEO', 'HDC', 'LDG', 'QCG', 'SZL', 'IJC', 'KBC', 'PPI',
                    'VPI', 'IDC', 'NBB', 'TDH', 'HUT', 'NHA', 'SJS', 'FCN', 'AGG', 'CII',
                    'PVL', 'TIX', 'ASM', 'PXI', 'CLG', 'CTD', 'VGC', 'DHC', 'SIP', 'TC6'],

    'tech': ['FPT', 'CMG', 'VGI', 'SAM', 'ITD', 'ELC', 'SGT', 'ICT', 'DGW', 'CTR',
             'FOX', 'VNT', 'SHI', 'SVT', 'VCS', 'HTC', 'TTN', 'ADS', 'ONE', 'VTC',
             'IFS', 'AMV', 'GTD', 'SGR', 'DPG', 'NET', 'VTV', 'MFS', 'VGT', 'CSM'],

    'consumer': ['VNM', 'MSN', 'MWG', 'PNJ', 'SAB', 'VHC', 'DGC', 'KDC', 'FRT', 'DBC',
                 'MCH', 'VCF', 'QNS', 'BBC', 'DRC', 'VTO', 'SBT', 'ANV', 'TNG', 'CAN',
                 'LAF', 'VIF', 'TAC', 'HAX', 'DHG', 'DMC', 'TRA', 'TRI', 'MPC', 'VOC'],

    'industrial': ['HPG', 'HSG', 'NKG', 'DCM', 'DPM', 'POW', 'PVD', 'VSH', 'GMD', 'AAA',
                   'GEG', 'VCS', 'VHC', 'DGC', 'PPC', 'NT2', 'REE', 'GEX', 'PVT', 'HT1',
                   'BWE', 'PVS', 'VSC', 'CSV', 'EVE', 'PVG', 'PVB', 'PVW', 'DHM', 'TMP'],

    'oil_gas': ['GAS', 'PLX', 'PVD', 'PVS', 'PVT', 'PVB', 'PVG', 'PVC', 'PVX', 'BSR',
                'OIL', 'PGD', 'PVL', 'PGC', 'PGI', 'PGN', 'PSH', 'PTL', 'PAN'],

    'securities': ['SSI', 'VND', 'VCI', 'HCM', 'BSI', 'MBS', 'VIX', 'SHS', 'AGR', 'FTS',
                   'CTS', 'BVS', 'TVS', 'APS', 'ORS', 'IVS', 'PSI', 'VDS', 'EVS'],

    'utilities': ['POW', 'NT2', 'REE', 'GEG', 'GEX', 'PC1', 'VSH', 'BWE', 'EVE', 'HT1',
                  'KHP', 'SBA', 'PGV', 'DTK', 'TBC', 'NBP', 'TPC', 'DRL', 'NTP', 'DHT'],

    'transport': ['VJC', 'HVN', 'GMD', 'ACV', 'HAH', 'PHP', 'VOS', 'VSC', 'STG', 'TMS',
                  'VTO', 'PVT', 'MVN', 'VFC', 'TCL', 'HAT', 'SFI', 'VIP', 'DVP', 'TCT'],

    'affordable': ['VPB', 'STB', 'HDB', 'SHB', 'MBB', 'ACB', 'FPT', 'POW', 'DGC', 'GEX',
                   'MSB', 'VIB', 'TPB', 'OCB', 'LPB', 'EIB', 'PVD', 'REE', 'PC1', 'FTS'],

    'all_stocks': [
        # Commodities
        'GOLD', 'SILVER', 'XAU', 'XAG',

        # HSX - Major stocks
        'VCB', 'VHM', 'VIC', 'VNM', 'HPG', 'GAS', 'MSN', 'TCB', 'VPB', 'MBB',
        'BID', 'CTG', 'VRE', 'SAB', 'PLX', 'MWG', 'SSI', 'FPT', 'VJC', 'GVR',
        'ACB', 'STB', 'HDB', 'TPB', 'VIB', 'MSB', 'SHB', 'EIB', 'LPB', 'OCB',
        'NVL', 'PDR', 'DXG', 'KDH', 'BCM', 'DIG', 'HDG', 'NLG', 'DXS', 'SCR',
        'POW', 'REE', 'NT2', 'GEG', 'GEX', 'PC1', 'VSH', 'BWE', 'EVE', 'HT1',
        'PVD', 'PVS', 'PVT', 'PVB', 'PVG', 'PVC', 'PVX', 'BSR', 'OIL', 'PGD',
        'HSG', 'NKG', 'DCM', 'DPM', 'GMD', 'AAA', 'PPC', 'CSV', 'DHM', 'TMP',
        'VND', 'VCI', 'HCM', 'BSI', 'MBS', 'VIX', 'SHS', 'AGR', 'FTS', 'CTS',
        'PNJ', 'DGC', 'KDC', 'FRT', 'DBC', 'MCH', 'VCF', 'QNS', 'BBC', 'DRC',
        'CMG', 'VGI', 'SAM', 'ITD', 'ELC', 'SGT', 'ICT', 'DGW', 'CTR', 'FOX',
        'ACV', 'HAH', 'PHP', 'VOS', 'STG', 'TMS', 'VTO', 'MVN', 'VFC', 'TCL',
        'HVN', 'VHC', 'SBT', 'ANV', 'TNG', 'CAN', 'LAF', 'VIF', 'TAC', 'HAX',
        'DHG', 'DMC', 'TRA', 'TRI', 'MPC', 'VOC', 'CEO', 'HDC', 'LDG', 'QCG',
        'SZL', 'IJC', 'KBC', 'PPI', 'VPI', 'IDC', 'NBB', 'TDH', 'HUT', 'NHA',
        'SJS', 'FCN', 'AGG', 'CII', 'PVL', 'TIX', 'ASM', 'PXI', 'CLG', 'CTD',

        # HNX - Secondary exchange
        'VCS', 'SHB', 'PVS', 'NVB', 'BAB', 'ABB', 'PGB', 'VBB', 'BVB', 'CLB',
        'DTK', 'TBC', 'NBP', 'TPC', 'DRL', 'NTP', 'DHT', 'SFC', 'PVI', 'BVH',
        'VNR', 'PLC', 'PVE', 'PVV', 'HHC', 'VTL', 'TNG', 'PTB', 'DTC', 'TMC',

        # UPCOM - Unlisted stocks
        'VTV', 'MFS', 'VGT', 'CSM', 'VNT', 'SHI', 'SVT', 'HTC', 'TTN', 'ADS',
        'ONE', 'IFS', 'AMV', 'GTD', 'SGR', 'DPG', 'NET', 'HAT', 'SFI', 'VIP'
    ]
}


# Stock names mapping (Symbol -> Full Name)
STOCK_NAMES = {
    # Commodities
    'GOLD': 'Gold - Vàng',
    'XAU': 'Gold - Vàng (XAU)',
    'SILVER': 'Silver - Bạc',
    'XAG': 'Silver - Bạc (XAG)',

    # Blue Chips & Banks
    'VCB': 'Vietcombank - Ngân hàng TMCP Ngoại thương Việt Nam',
    'BID': 'BIDV - Ngân hàng TMCP Đầu tư và Phát triển Việt Nam',
    'CTG': 'VietinBank - Ngân hàng TMCP Công thương Việt Nam',
    'TCB': 'Techcombank - Ngân hàng TMCP Kỹ thương Việt Nam',
    'MBB': 'MB Bank - Ngân hàng TMCP Quân đội',
    'VPB': 'VPBank - Ngân hàng TMCP Việt Nam Thịnh Vượng',
    'ACB': 'ACB - Ngân hàng TMCP Á Châu',
    'STB': 'Sacombank - Ngân hàng TMCP Sài Gòn Thương Tín',
    'HDB': 'HDBank - Ngân hàng TMCP Phát triển TP.HCM',
    'TPB': 'TPBank - Ngân hàng TMCP Tiên Phong',
    'VIB': 'VIB - Ngân hàng TMCP Quốc tế Việt Nam',
    'MSB': 'MSB - Ngân hàng TMCP Hàng hải',
    'SHB': 'SHB - Ngân hàng TMCP Sài Gòn - Hà Nội',
    'EIB': 'Eximbank - Ngân hàng TMCP Xuất Nhập khẩu',
    'LPB': 'LienVietPostBank - Ngân hàng TMCP Bưu điện Liên Việt',
    'OCB': 'OCB - Ngân hàng TMCP Phương Đông',
    'VBB': 'VietBank - Ngân hàng TMCP Việt Nam Thương Tín',
    'BVB': 'Bao Viet Bank - Ngân hàng TMCP Bảo Việt',
    'NVB': 'Navibank - Ngân hàng TMCP Nam Việt',
    'BAB': 'BAB - Ngân hàng TMCP Bắc Á',
    'ABB': 'ABBank - Ngân hàng TMCP An Bình',
    'PGB': 'PGBank - Ngân hàng TMCP Xăng dầu Petrolimex',
    'SCB': 'SCB - Ngân hàng TMCP Sài Gòn',
    'SeABank': 'SeABank - Ngân hàng TMCP Đông Nam Á',
    'NAB': 'Nam A Bank - Ngân hàng TMCP Nam Á',
    'KLB': 'Kienlongbank - Ngân hàng TMCP Kiên Long',

    # Real Estate
    'VHM': 'Vinhomes - CTCP Vinhomes',
    'VIC': 'Vingroup - Tập đoàn Vingroup',
    'VRE': 'Vincom Retail - CTCP Vincom Retail',
    'NVL': 'Novaland - CTCP Tập đoàn Đầu tư Địa ốc No Va',
    'PDR': 'Phát Đạt - CTCP Phát Đạt',
    'DXG': 'Đất Xanh - CTCP Tập đoàn Đất Xanh',
    'KDH': 'Khang Điền - CTCP Đầu tư và Kinh doanh nhà Khang Điền',
    'BCM': 'Becamex - CTCP Đầu tư và Phát triển Bất động sản',
    'DIG': 'DIC Corp - CTCP Đầu tư và Thương mại DIC',
    'HDG': 'Hodeco - CTCP Phát triển Nhà Bà Rịa - Vũng Tàu',
    'NLG': 'Nam Long - CTCP Đầu tư Nam Long',
    'DXS': 'Đông Á - CTCP Phát triển Bất động sản',
    'SCR': 'SC Realty - CTCP Địa ốc Sài Gòn Thương Tín',
    'CEO': 'CEO Group - CTCP Tập đoàn C.E.O',
    'HDC': 'Hodeco - CTCP Phát triển Nhà Bà Rịa',
    'LDG': 'LDG Investment - CTCP Đầu tư LDG',
    'QCG': 'Quốc Cường Gia Lai - CTCP Quốc Cường Gia Lai',
    'SZL': 'Sonadezi Long Thành - CTCP Sonadezi Long Thành',
    'IJC': 'IJC - CTCP Phát triển Hạ tầng Kỹ thuật',
    'KBC': 'KBC - CTCP Kinh Bắc',
    'PPI': 'Phước Hòa - CTCP Đầu tư Phát triển Phước Hòa',
    'VPI': 'VPI - CTCP Đầu tư Văn Phú - Invest',
    'IDC': 'IDICO - CTCP Đầu tư và Phát triển IDICO',
    'NBB': 'NBB Investment - CTCP Đầu tư NBB',
    'TDH': 'Thaiholdings - CTCP Thaiholdings',
    'HUT': 'Tasco - CTCP Đô thị và Khu công nghiệp',
    'NHA': 'Nhơn Hội - CTCP Nhơn Hội',
    'SJS': 'SJS - CTCP Đầu tư SJS',
    'FCN': 'Fecon - CTCP Xây dựng và Kinh doanh Địa ốc',
    'AGG': 'An Giang - CTCP Xuất nhập khẩu An Giang',
    'CII': 'HFIC - CTCP Đầu tư Hạ tầng Kỹ thuật TP.HCM',
    'PVL': 'PVLand - CTCP PVLand',
    'TIX': 'Tổng công ty Cổ phần Dịch vụ Kỹ thuật Dầu khí',
    'ASM': 'Sao Mai - CTCP Tập đoàn Sao Mai',
    'PXI': 'CTCP Xây lắp Dầu khí',
    'CLG': 'CTCP Cotec Land',
    'CTD': 'Coteccons - CTCP Xây dựng Coteccons',
    'VGC': 'Viglacera - CTCP Viglacera',
    'DHC': 'Đông Hải Bến Tre - CTCP Đông Hải Bến Tre',
    'SIP': 'SIP - CTCP Đầu tư Sài Gòn VRG',
    'TC6': 'TC6 - CTCP Xây dựng và Kinh doanh Vật tư',

    # Tech
    'FPT': 'FPT - CTCP FPT',
    'CMG': 'CMC - CTCP Tập đoàn Công nghệ CMC',
    'VGI': 'VGI - CTCP Đầu tư Thế Giới Di Động',
    'SAM': 'Sacom - CTCP Tập đoàn Sacom',
    'ITD': 'ITD - CTCP Đầu tư Công nghệ',
    'ELC': 'Elcom - CTCP Chứng khoán Điện tử',
    'SGT': 'SGT - CTCP Công nghệ Saigontel',
    'ICT': 'ICT - CTCP Viễn thông - Tin học Bưu điện',
    'DGW': 'Digiworld - CTCP Thế Giới Số',
    'CTR': 'CTR - CTCP Cổ phần Công nghệ Viễn thông',
    'FOX': 'Fox - CTCP Mạng trực tuyến MXH',
    'VNT': 'Viettel - CTCP Viễn thông - Tin học Viettel',
    'SHI': 'SHI - CTCP Quốc tế Sơn Hà',
    'SVT': 'Savimex - CTCP Savimex',
    'VCS': 'Vicostone - CTCP Vicostone',
    'HTC': 'HTC - CTCP Thương mại Hóc Môn',
    'TTN': 'TTN - CTCP Thép Tiến Lên',
    'ADS': 'ADS - CTCP Damsan',
    'ONE': 'ONE - CTCP Dược phẩm OPC',
    'VTC': 'VTC - CTCP Viễn thông VTC',
    'IFS': 'IFS - CTCP Thực phẩm Quốc tế',
    'AMV': 'AMV - CTCP AMV',
    'GTD': 'GTD - CTCP Giầy Thượng Đình',
    'SGR': 'SGR - CTCP Địa ốc Sài Gòn',
    'DPG': 'Đạt Phương - CTCP Nhựa Đạt Phương',
    'NET': 'NET - CTCP Bột giặt Net',
    'VTV': 'VTV - CTCP Năng lượng VTV',
    'MFS': 'MFS - CTCP Phân bón Miền Nam',
    'VGT': 'VGT - CTCP Dược Viễn Đông Vgreen',
    'CSM': 'CSM - CTCP Công nghiệp Cao su Miền Nam',

    # Consumer
    'VNM': 'Vinamilk - CTCP Sữa Việt Nam',
    'MSN': 'Masan - CTCP Tập đoàn Masan',
    'MWG': 'Mobile World - CTCP Đầu tư Thế Giới Di Động',
    'PNJ': 'PNJ - CTCP Vàng bạc Đá quý Phú Nhuận',
    'SAB': 'Sabeco - Tổng CTCP Bia - Rượu - NGK Sài Gòn',
    'VHC': 'Vĩnh Hoàn - CTCP Vĩnh Hoàn',
    'DGC': 'DGC - CTCP Tập đoàn Hóa chất Đức Giang',
    'KDC': 'Kinh Đô - CTCP Kinh Đô',
    'FRT': 'FRT - CTCP Bán lẻ Kỹ thuật số FPT',
    'DBC': 'Dabaco - CTCP Dabaco Việt Nam',
    'MCH': 'Masan Consumer - CTCP Hàng tiêu dùng Masan',
    'VCF': 'Vinaconex - CTCP Vinaconex',
    'QNS': 'QNS - CTCP Đường Quảng Ngãi',
    'BBC': 'BIBICA - CTCP Bánh Kẹo Biên Hòa',
    'DRC': 'DRC - CTCP Cao su Đà Nẵng',
    'VTO': 'Vitrans - CTCP Vận tải Xăng dầu VITRANS',
    'SBT': 'SBT - CTCP Thành Thành Công - Biên Hòa',
    'ANV': 'Nam Việt - CTCP Nam Việt',
    'TNG': 'TNG - CTCP Đầu tư và Thương mại TNG',
    'CAN': 'CAN - CTCP Đồ hộp Hạ Long',
    'LAF': 'Lazada - CTCP Long Hậu',
    'VIF': 'VIF - CTCP Lương thực Thực phẩm',
    'TAC': 'TAC - CTCP Dầu thực vật Tường An',
    'HAX': 'HAX - CTCP Dịch vụ Ô tô Hàng Xanh',
    'DHG': 'DHG Pharma - CTCP Dược Hậu Giang',
    'DMC': 'Domesco - CTCP Dược phẩm Cửu Long',
    'TRA': 'TRA - CTCP Traphaco',
    'TRI': 'TRI - CTCP Chứng khoán Trí Việt',
    'MPC': 'MPC - CTCP Tập đoàn Thủy sản Minh Phú',
    'VOC': 'VOC - CTCP Xây dựng và Đầu tư',

    # Industrial
    'HPG': 'Hòa Phát - CTCP Tập đoàn Hòa Phát',
    'HSG': 'HSG - CTCP Tập đoàn Hoa Sen',
    'NKG': 'NKG - CTCP Thép Nam Kim',
    'DCM': 'DCM - CTCP Phân bón Dầu khí Cà Mau',
    'DPM': 'DPM - CTCP Phân đạm và Hóa chất Dầu khí',
    'POW': 'POW - Tổng Công ty Điện lực Dầu khí',
    'PVD': 'PVD - Tổng Công ty Khoan và Dịch vụ Dầu khí',
    'VSH': 'VSH - CTCP Thủy điện Vĩnh Sơn - Sông Hinh',
    'GMD': 'GMD - CTCP Gemadept',
    'AAA': 'AAA - CTCP Nhựa và Môi trường Xanh',
    'GEG': 'GEG - CTCP Điện Gia Lai',
    'PPC': 'PPC - CTCP Nhiệt điện Phả Lại',
    'NT2': 'NT2 - CTCP Điện lực Dầu khí Nhơn Trạch 2',
    'REE': 'REE - CTCP Cơ Điện Lạnh',
    'GEX': 'GEX - CTCP Tập đoàn Gelex',
    'PVT': 'PVT - Tổng Công ty Vận tải Dầu khí',
    'HT1': 'HT1 - CTCP Xi măng Hà Tiên 1',
    'BWE': 'BWE - CTCP Nước - Môi trường Bình Dương',
    'PVS': 'PVS - Tổng Công ty Cổ phần Dịch vụ Kỹ thuật Dầu khí',
    'VSC': 'VSC - CTCP Container Việt Nam',
    'CSV': 'CSV - CTCP Hóa chất Cơ bản Miền Nam',
    'EVE': 'EVE - CTCP Everpia',
    'PVG': 'PVG - Tổng Công ty Phân bón và Hóa chất Dầu khí',
    'PVB': 'PVB - Tổng Công ty Tư vấn Thiết kế Dầu khí',
    'PVW': 'PVW - CTCP Xi măng Dầu khí PVC',
    'DHM': 'DHM - CTCP Định hướng Nam Hồng',
    'TMP': 'TMP - CTCP Thủy sản và Thương mại Thuận Phước',

    # Oil & Gas
    'GAS': 'PV Gas - Tổng Công ty Khí Việt Nam',
    'PLX': 'Petrolimex - Tập đoàn Xăng dầu Việt Nam',
    'PVC': 'PVC - Tổng Công ty Hóa chất và Dịch vụ Dầu khí',
    'PVX': 'PVX - CTCP Xi măng Dầu khí Cà Mau',
    'BSR': 'BSR - CTCP Lọc hóa dầu Bình Sơn',
    'OIL': 'OIL - Tổng Công ty Dầu Việt Nam',
    'PGD': 'PGD - CTCP Phân phối khí Đô thị',
    'PVL': 'PVL - CTCP PVLand',
    'PGC': 'PGC - Tổng Công ty Điện lực Dầu khí',
    'PGI': 'PGI - CTCP PGI',
    'PGN': 'PGN - CTCP Phân bón Dầu khí Ninh Bình',
    'PSH': 'PSH - CTCP Thương mại Đầu tư Dầu khí',
    'PTL': 'PTL - CTCP Đầu tư và Thương mại Dầu khí',
    'PAN': 'PAN - CTCP Xăng dầu Dầu khí Petrolimex',

    # Securities
    'SSI': 'SSI - CTCP Chứng khoán SSI',
    'VND': 'VND - CTCP Chứng khoán VNDirect',
    'VCI': 'VCI - CTCP Chứng khoán Vietcap',
    'HCM': 'HCM - CTCP Chứng khoán Thành phố Hồ Chí Minh',
    'BSI': 'BSI - CTCP Chứng khoán Ngân hàng Đầu tư',
    'MBS': 'MBS - CTCP Chứng khoán MB',
    'VIX': 'VIX - CTCP Chứng khoán VIX',
    'SHS': 'SHS - CTCP Chứng khoán Sài Gòn - Hà Nội',
    'AGR': 'AGR - CTCP Chứng khoán Agribank',
    'FTS': 'FTS - CTCP Chứng khoán FPT',
    'CTS': 'CTS - CTCP Chứng khoán Ngân hàng Công thương',
    'BVS': 'BVS - CTCP Chứng khoán Bảo Việt',
    'TVS': 'TVS - CTCP Chứng khoán Thiên Việt',
    'APS': 'APS - CTCP Chứng khoán APG',
    'ORS': 'ORS - CTCP Chứng khoán Tiên Phong',
    'IVS': 'IVS - CTCP Chứng khoán ISaigon',
    'PSI': 'PSI - CTCP Chứng khoán Dầu khí',
    'VDS': 'VDS - CTCP Chứng khoán Rồng Việt',
    'EVS': 'EVS - CTCP Chứng khoán Everest',

    # Utilities
    'PC1': 'PC1 - CTCP Điện lực Dầu khí 1',
    'KHP': 'KHP - CTCP Điện lực Khánh Hòa',
    'SBA': 'SBA - CTCP Sông Ba',
    'PGV': 'PGV - Tổng Công ty Phát điện 2',
    'DTK': 'DTK - CTCP Điện Tây Nguyên',
    'TBC': 'TBC - CTCP Thủy điện Thác Bà',
    'NBP': 'NBP - CTCP Nhiệt điện Ninh Bình',
    'TPC': 'TPC - CTCP Nhựa Tân Đại Hưng',
    'DRL': 'DRL - CTCP Thủy điện - Điện lực 3',
    'NTP': 'NTP - CTCP Nhựa Thiếu niên Tiền Phong',
    'DHT': 'DHT - CTCP Dược phẩm Hà Tây',

    # Transport
    'VJC': 'VietJet Air - CTCP Hàng không VietJet',
    'HVN': 'Vietnam Airlines - Tổng Công ty Hàng không Việt Nam',
    'ACV': 'ACV - Tổng Công ty Cảng hàng không Việt Nam',
    'HAH': 'HAH - CTCP Vận tải và Xếp dỡ Hải An',
    'PHP': 'PHP - CTCP Cảng Hải Phòng',
    'VOS': 'VOS - CTCP Vận tải Biển Việt Nam',
    'STG': 'STG - CTCP Kho vận Giao nhận Ngoại thương',
    'TMS': 'TMS - CTCP Kho vận Giao nhận Transimex',
    'MVN': 'MVN - CTCP Hàng hải Việt Nam',
    'VFC': 'VFC - CTCP Vinafco',
    'TCL': 'TCL - CTCP Đại lý Giao nhận Vận tải',
    'HAT': 'HAT - CTCP Thủy điện Hương Sơn',
    'SFI': 'SFI - CTCP Đầu tư Phát triển Vĩnh Phú',
    'VIP': 'VIP - CTCP Vận tải Xăng dầu Vipco',
    'DVP': 'DVP - CTCP Đầu tư và Phát triển Cảng',
    'TCT': 'TCT - CTCP Cáp Treo Núi Bà Tây Ninh',

    # Others
    'PVI': 'PVI - Tổng Công ty Cổ phần Bảo hiểm Petrolimex',
    'BVH': 'BVH - Tập đoàn Bảo Việt',
    'VNR': 'VNR - CTCP Tái bảo hiểm Quốc gia',
    'PLC': 'PLC - CTCP Licogi 13',
    'PVE': 'PVE - Tổng Công ty Tư vấn Thiết kế Dầu khí',
    'PVV': 'PVV - CTCP Vinaconex Dầu khí',
    'HHC': 'HHC - CTCP Bánh kẹo Hải Hà',
    'VTL': 'VTL - CTCP Vang Thăng Long',
    'PTB': 'PTB - CTCP Phú Tài',
    'DTC': 'DTC - CTCP Vinaconex Đạm và Hóa chất',
    'TMC': 'TMC - CTCP Thương mại Xuất nhập khẩu',
    'SFC': 'SFC - CTCP Nhiên liệu Sài Gòn',
    'CLB': 'CLB - CTCP Cường Lê Miền Bắc',
    'GVR': 'GVR - CTCP Tập đoàn Công nghiệp Cao su',
}


def get_stock_name(symbol: str) -> str:
    """Get full name for a stock symbol"""
    return STOCK_NAMES.get(symbol.upper(), symbol)


def get_all_symbols() -> list:
    """Get all unique stock symbols across all categories"""
    all_symbols = set()
    for stocks in STOCK_LISTS.values():
        all_symbols.update(stocks)
    return sorted(list(all_symbols))


def get_stocks_by_exchange(exchange: str) -> list:
    """
    Get stocks by exchange

    Args:
        exchange: 'HSX', 'HNX', or 'UPCOM'

    Returns:
        List of stock symbols
    """
    # Approximate categorization
    hsx_stocks = STOCK_LISTS['blue_chips'] + STOCK_LISTS['banks'] + STOCK_LISTS['real_estate']
    hnx_stocks = ['VCS', 'SHB', 'PVS', 'NVB', 'BAB', 'ABB', 'PGB', 'VBB', 'BVB']
    upcom_stocks = ['VTV', 'MFS', 'VGT', 'CSM', 'VNT', 'SHI', 'SVT', 'HTC']

    exchanges = {
        'HSX': list(set(hsx_stocks)),
        'HNX': hnx_stocks,
        'UPCOM': upcom_stocks
    }

    return exchanges.get(exchange.upper(), [])


if __name__ == "__main__":
    # Test the fetcher
    fetcher = VNStockData()

    print("Fetching VCB (Vietcombank)...")
    data = fetcher.get_stock_price('VCB')
    if data:
        print(json.dumps(data, indent=2))

    print("\nSearching for 'Vinamilk'...")
    results = fetcher.search_stocks('Vinamilk')
    for stock in results:
        print(f"{stock['symbol']}: {stock['name']} ({stock['exchange']})")
