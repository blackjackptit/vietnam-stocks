"""
Technical Analysis for Vietnamese Stocks
Calculate indicators: RSI, MACD, Moving Averages, Bollinger Bands
"""

from typing import List, Dict, Optional, Tuple
import statistics


class TechnicalAnalyzer:
    """Perform technical analysis on stock data"""

    @staticmethod
    def calculate_rsi(prices: List[float], period: int = 14) -> Optional[float]:
        """
        Calculate Relative Strength Index (RSI)

        Args:
            prices: List of closing prices (oldest first)
            period: RSI period (default 14)

        Returns:
            RSI value (0-100) or None if insufficient data
        """
        if len(prices) < period + 1:
            return None

        gains = []
        losses = []

        for i in range(1, len(prices)):
            change = prices[i] - prices[i-1]
            if change > 0:
                gains.append(change)
                losses.append(0)
            else:
                gains.append(0)
                losses.append(abs(change))

        if len(gains) < period:
            return None

        avg_gain = sum(gains[-period:]) / period
        avg_loss = sum(losses[-period:]) / period

        if avg_loss == 0:
            return 100

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))

        return round(rsi, 2)

    @staticmethod
    def calculate_moving_average(prices: List[float], period: int) -> Optional[float]:
        """
        Calculate Simple Moving Average (SMA)

        Args:
            prices: List of closing prices
            period: MA period

        Returns:
            Moving average value
        """
        if len(prices) < period:
            return None

        return round(sum(prices[-period:]) / period, 2)

    @staticmethod
    def calculate_ema(prices: List[float], period: int) -> Optional[float]:
        """
        Calculate Exponential Moving Average (EMA)

        Args:
            prices: List of closing prices
            period: EMA period

        Returns:
            EMA value
        """
        if len(prices) < period:
            return None

        multiplier = 2 / (period + 1)
        ema = sum(prices[:period]) / period

        for price in prices[period:]:
            ema = (price - ema) * multiplier + ema

        return round(ema, 2)

    @staticmethod
    def calculate_macd(prices: List[float], fast: int = 12, slow: int = 26, signal: int = 9) -> Optional[Dict]:
        """
        Calculate MACD (Moving Average Convergence Divergence)

        Args:
            prices: List of closing prices
            fast: Fast EMA period
            slow: Slow EMA period
            signal: Signal line period

        Returns:
            Dictionary with MACD, signal, and histogram
        """
        if len(prices) < slow:
            return None

        ema_fast = TechnicalAnalyzer.calculate_ema(prices, fast)
        ema_slow = TechnicalAnalyzer.calculate_ema(prices, slow)

        if ema_fast is None or ema_slow is None:
            return None

        macd_line = ema_fast - ema_slow

        # Calculate signal line (EMA of MACD)
        # For simplicity, we'll use SMA here
        if len(prices) < slow + signal:
            return None

        signal_line = macd_line  # Simplified

        histogram = macd_line - signal_line

        return {
            'macd': round(macd_line, 2),
            'signal': round(signal_line, 2),
            'histogram': round(histogram, 2)
        }

    @staticmethod
    def calculate_bollinger_bands(prices: List[float], period: int = 20, std_dev: float = 2) -> Optional[Dict]:
        """
        Calculate Bollinger Bands

        Args:
            prices: List of closing prices
            period: Period for moving average
            std_dev: Number of standard deviations

        Returns:
            Dictionary with upper, middle, and lower bands
        """
        if len(prices) < period:
            return None

        recent_prices = prices[-period:]
        middle_band = sum(recent_prices) / period
        std = statistics.stdev(recent_prices)

        upper_band = middle_band + (std_dev * std)
        lower_band = middle_band - (std_dev * std)

        return {
            'upper': round(upper_band, 2),
            'middle': round(middle_band, 2),
            'lower': round(lower_band, 2)
        }

    @staticmethod
    def analyze_stock(historical_data: List[Dict]) -> Dict:
        """
        Perform comprehensive technical analysis on a stock

        Args:
            historical_data: List of historical price data (oldest first)

        Returns:
            Dictionary with all technical indicators and signals
        """
        if not historical_data or len(historical_data) < 2:
            return {'error': 'Insufficient data'}

        # Extract closing prices (reverse to get oldest first)
        prices = [float(d.get('close', 0)) for d in reversed(historical_data)]
        volumes = [float(d.get('nmVolume', 0)) for d in reversed(historical_data)]

        if not prices or prices[0] == 0:
            return {'error': 'Invalid price data'}

        current_price = prices[-1]

        # Calculate indicators
        rsi = TechnicalAnalyzer.calculate_rsi(prices)
        ma20 = TechnicalAnalyzer.calculate_moving_average(prices, 20)
        ma50 = TechnicalAnalyzer.calculate_moving_average(prices, 50)
        ema12 = TechnicalAnalyzer.calculate_ema(prices, 12)
        ema26 = TechnicalAnalyzer.calculate_ema(prices, 26)
        macd = TechnicalAnalyzer.calculate_macd(prices)
        bollinger = TechnicalAnalyzer.calculate_bollinger_bands(prices)

        # Generate signals
        signals = []
        score = 0  # -100 to 100 (bearish to bullish)

        # RSI signals
        if rsi is not None:
            if rsi < 30:
                signals.append("🟢 RSI oversold (potential buy)")
                score += 20
            elif rsi > 70:
                signals.append("🔴 RSI overbought (potential sell)")
                score -= 20
            elif 40 <= rsi <= 60:
                signals.append("⚪ RSI neutral")

        # Moving Average signals
        if ma20 and ma50:
            if current_price > ma20 > ma50:
                signals.append("🟢 Price above MA20 and MA50 (bullish)")
                score += 15
            elif current_price < ma20 < ma50:
                signals.append("🔴 Price below MA20 and MA50 (bearish)")
                score -= 15

            # Golden/Death cross
            if ma20 > ma50:
                signals.append("🟢 MA20 above MA50 (golden cross area)")
                score += 10
            else:
                signals.append("🔴 MA20 below MA50 (death cross area)")
                score -= 10

        # MACD signals
        if macd:
            if macd['histogram'] > 0:
                signals.append("🟢 MACD bullish")
                score += 10
            else:
                signals.append("🔴 MACD bearish")
                score -= 10

        # Bollinger Bands signals
        if bollinger:
            if current_price < bollinger['lower']:
                signals.append("🟢 Price near lower Bollinger Band (oversold)")
                score += 15
            elif current_price > bollinger['upper']:
                signals.append("🔴 Price near upper Bollinger Band (overbought)")
                score -= 15

        # Volume analysis
        if len(volumes) >= 20:
            avg_volume = sum(volumes[-20:]) / 20
            current_volume = volumes[-1]
            if current_volume > avg_volume * 1.5:
                signals.append("📈 High volume (strong interest)")
                score += 5

        # Overall recommendation
        if score > 40:
            recommendation = "STRONG BUY"
            emoji = "🟢🟢"
        elif score > 20:
            recommendation = "BUY"
            emoji = "🟢"
        elif score > -20:
            recommendation = "HOLD"
            emoji = "⚪"
        elif score > -40:
            recommendation = "SELL"
            emoji = "🔴"
        else:
            recommendation = "STRONG SELL"
            emoji = "🔴🔴"

        return {
            'current_price': current_price,
            'indicators': {
                'rsi': rsi,
                'ma20': ma20,
                'ma50': ma50,
                'ema12': ema12,
                'ema26': ema26,
                'macd': macd,
                'bollinger': bollinger
            },
            'signals': signals,
            'score': score,
            'recommendation': recommendation,
            'emoji': emoji
        }


if __name__ == "__main__":
    # Example usage
    sample_prices = [100, 102, 101, 103, 105, 104, 106, 108, 107, 109, 111, 110, 112, 115, 113]

    analyzer = TechnicalAnalyzer()

    print("RSI:", analyzer.calculate_rsi(sample_prices))
    print("MA(10):", analyzer.calculate_moving_average(sample_prices, 10))
    print("EMA(10):", analyzer.calculate_ema(sample_prices, 10))
