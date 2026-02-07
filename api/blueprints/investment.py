"""
Investment plans API endpoints.
3 routes: GET/POST /api/investment-plans, DELETE /api/investment-plans/<plan_id>
"""

from flask import Blueprint, jsonify, request, make_response
import uuid as uuid_lib

from api.helpers import query_db, get_or_create_session, get_or_create_plan_owner, log_activity
from api.extensions import PLAN_COOKIE_MAX_AGE

investment_bp = Blueprint('investment', __name__)


def _set_plan_cookie(response, owner_id):
    """Set the long-lived plan_owner_id cookie on a response."""
    response.set_cookie('plan_owner_id', owner_id, max_age=PLAN_COOKIE_MAX_AGE, samesite='Lax')
    return response


@investment_bp.route('/api/investment-plans', methods=['GET'])
def get_investment_plans():
    """Get all investment plans for the current user"""
    try:
        owner_id = get_or_create_plan_owner()
        session_id = get_or_create_session()
        log_activity(session_id, 'view', 'investment-plans', 'View saved plans')

        # Get all plans for this owner
        plans = query_db("""
            SELECT
                plan_id,
                name,
                notes,
                strategy,
                strategy_name,
                budget,
                expected_return,
                risk_level,
                sharpe_ratio,
                created_at,
                metadata
            FROM investment_plans
            WHERE session_id = %s
            ORDER BY created_at DESC
        """, [owner_id])

        # Get holdings for each plan
        result = []
        for plan in plans:
            holdings = query_db("""
                SELECT
                    symbol,
                    shares,
                    buy_price,
                    price_at_creation,
                    allocation_percent,
                    amount,
                    expected_return
                FROM investment_plan_holdings
                WHERE plan_id = %s
            """, [plan['plan_id']])

            result.append({
                'id': str(plan['plan_id']),
                'name': plan['name'],
                'notes': plan['notes'],
                'strategy': plan['strategy'],
                'strategyName': plan['strategy_name'],
                'budget': float(plan['budget']) if plan['budget'] else 0,
                'expectedReturn': float(plan['expected_return']) if plan['expected_return'] else 0,
                'risk': float(plan['risk_level']) if plan['risk_level'] else 0,
                'sharpeRatio': float(plan['sharpe_ratio']) if plan['sharpe_ratio'] else 0,
                'createdDate': plan['created_at'].isoformat() if plan['created_at'] else None,
                'holdings': [{
                    'symbol': h['symbol'],
                    'shares': float(h['shares']) if h['shares'] else 0,
                    'buyPrice': float(h['buy_price']) if h['buy_price'] else 0,
                    'priceAtCreation': float(h['price_at_creation']) if h['price_at_creation'] else 0,
                    'allocation': float(h['allocation_percent']) if h['allocation_percent'] else 0,
                    'amount': float(h['amount']) if h['amount'] else 0,
                    'expectedReturn': float(h['expected_return']) if h['expected_return'] else 0
                } for h in holdings]
            })

        response = make_response(jsonify({
            'success': True,
            'data': result,
            'count': len(result)
        }))
        _set_plan_cookie(response, owner_id)
        return response

    except Exception as e:
        print(f"Error getting investment plans: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@investment_bp.route('/api/investment-plans', methods=['POST'])
def save_investment_plan():
    """Save a new investment plan"""
    try:
        owner_id = get_or_create_plan_owner()
        session_id = get_or_create_session()
        data = request.get_json()

        # Validate required fields
        if not data.get('name'):
            return jsonify({'success': False, 'error': 'Plan name is required'}), 400

        # Insert plan (session_id column stores the owner_id)
        plan_id = str(uuid_lib.uuid4())
        query_db("""
            INSERT INTO investment_plans (
                plan_id, name, notes, strategy, strategy_name,
                budget, expected_return, risk_level, sharpe_ratio, session_id
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, [
            plan_id,
            data['name'],
            data.get('notes', ''),
            data.get('strategy', ''),
            data.get('strategyName', ''),
            data.get('budget', 0),
            data.get('expectedReturn', 0),
            data.get('risk', 0),
            data.get('sharpeRatio', 0),
            owner_id
        ])

        # Insert holdings
        if data.get('holdings'):
            for holding in data['holdings']:
                query_db("""
                    INSERT INTO investment_plan_holdings (
                        plan_id, symbol, shares, buy_price, price_at_creation,
                        allocation_percent, amount, expected_return
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, [
                    plan_id,
                    holding['symbol'],
                    holding.get('shares', 0),
                    holding.get('buyPrice', 0),
                    holding.get('priceAtCreation', 0),
                    holding.get('allocation', 0),
                    holding.get('amount', 0),
                    holding.get('expectedReturn', 0)
                ])

        log_activity(session_id, 'create', 'investment-plan', f'Created plan: {data["name"]}')

        response = make_response(jsonify({
            'success': True,
            'planId': str(plan_id),
            'message': 'Investment plan saved successfully'
        }))
        _set_plan_cookie(response, owner_id)
        return response

    except Exception as e:
        print(f"Error saving investment plan: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@investment_bp.route('/api/investment-plans/<plan_id>', methods=['DELETE'])
def delete_investment_plan(plan_id):
    """Delete an investment plan"""
    try:
        owner_id = get_or_create_plan_owner()
        session_id = get_or_create_session()

        # Verify the plan belongs to this owner
        plan = query_db("""
            SELECT name FROM investment_plans
            WHERE plan_id = %s AND session_id = %s
        """, [plan_id, owner_id])

        if not plan:
            return jsonify({'success': False, 'error': 'Plan not found'}), 404

        # Delete the plan (holdings will be cascade deleted)
        query_db("DELETE FROM investment_plans WHERE plan_id = %s", [plan_id])

        log_activity(session_id, 'delete', 'investment-plan', f'Deleted plan: {plan[0]["name"]}')

        response = make_response(jsonify({
            'success': True,
            'message': 'Investment plan deleted successfully'
        }))
        _set_plan_cookie(response, owner_id)
        return response

    except Exception as e:
        print(f"Error deleting investment plan: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500
