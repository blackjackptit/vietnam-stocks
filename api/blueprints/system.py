"""
System and utility endpoints.
7 routes: /health, system-status, controls, jobs, activity-log
"""

from flask import Blueprint, jsonify, request
from datetime import datetime

from api.helpers import query_db
import api.extensions as ext

system_bp = Blueprint('system', __name__)


@system_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    try:
        # Test database connection
        result = query_db("SELECT COUNT(*) as count FROM stocks;", one=True)
        stock_count = result['count'] if result else 0

        return jsonify({
            "status": "healthy",
            "database": "connected",
            "stocks": stock_count,
            "timestamp": datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }), 500


@system_bp.route('/api/system-status', methods=['GET'])
def system_status():
    """Comprehensive system status check"""
    import subprocess
    import os

    status = {
        "timestamp": datetime.now().isoformat(),
        "api": {
            "status": "online",
            "message": "API server is running"
        },
        "database": {
            "status": "unknown",
            "message": "",
            "stock_count": 0,
            "latest_data": None
        },
        "scheduler": {
            "status": "unknown",
            "message": "",
            "pid": None
        },
        "data_collection": {
            "last_stock_update": None,
            "last_index_update": None,
            "last_macro_update": None,
            "stock_count_today": 0
        }
    }

    # Check database
    try:
        stock_count = query_db("SELECT COUNT(*) as count FROM stocks WHERE is_active = TRUE;", one=True)
        status["database"]["stock_count"] = stock_count['count']
        status["database"]["status"] = "connected"
        status["database"]["message"] = f"{stock_count['count']} active stocks"

        # Get latest stock data
        latest_stock = query_db("""
            SELECT MAX(date) as latest_date, COUNT(*) as count
            FROM stock_prices
            WHERE date = (SELECT MAX(date) FROM stock_prices);
        """, one=True)

        if latest_stock and latest_stock['latest_date']:
            status["data_collection"]["last_stock_update"] = latest_stock['latest_date'].isoformat()
            status["data_collection"]["stock_count_today"] = latest_stock['count']

        # Get latest index data
        latest_index = query_db("""
            SELECT MAX(date) as latest_date
            FROM market_indices;
        """, one=True)

        if latest_index and latest_index['latest_date']:
            status["data_collection"]["last_index_update"] = latest_index['latest_date'].isoformat()

        # Get latest macro data
        latest_macro = query_db("""
            SELECT MAX(date) as latest_date
            FROM macro_indicators;
        """, one=True)

        if latest_macro and latest_macro['latest_date']:
            status["data_collection"]["last_macro_update"] = latest_macro['latest_date'].isoformat()

    except Exception as e:
        status["database"]["status"] = "error"
        status["database"]["message"] = str(e)

    # Check scheduler process
    # In Docker environment, scheduler runs in separate container
    # Check for recent scheduler activity in logs as a heartbeat
    try:
        # Check if scheduler has logged activity in the last 5 minutes
        recent_activity = query_db("""
            SELECT COUNT(*) as count, MAX(timestamp) as last_seen
            FROM activity_log
            WHERE activity_type IN ('collection', 'scheduler')
            AND timestamp > NOW() - INTERVAL '5 minutes';
        """, one=True)

        if recent_activity and recent_activity['count'] > 0:
            status["scheduler"]["status"] = "running"
            status["scheduler"]["message"] = f"Scheduler is active (last seen: {recent_activity['last_seen']})"
            status["scheduler"]["pid"] = None  # Not available in Docker
        else:
            # No recent activity, check if container exists (Docker specific)
            try:
                result = subprocess.run(
                    ['docker', 'ps', '--filter', 'name=vnstock_scheduler', '--format', '{{.Status}}'],
                    capture_output=True,
                    text=True,
                    timeout=2
                )
                if result.returncode == 0 and 'Up' in result.stdout:
                    status["scheduler"]["status"] = "running"
                    status["scheduler"]["message"] = "Scheduler container is running"
                else:
                    status["scheduler"]["status"] = "stopped"
                    status["scheduler"]["message"] = "Scheduler container is not running"
            except:
                # Docker command not available or timeout
                status["scheduler"]["status"] = "unknown"
                status["scheduler"]["message"] = "Unable to check scheduler status (no recent activity)"
    except Exception as e:
        status["scheduler"]["status"] = "unknown"
        status["scheduler"]["message"] = f"Cannot check scheduler status: {str(e)}"

    # Overall status
    overall_status = "healthy"
    if status["database"]["status"] != "connected":
        overall_status = "degraded"
    if status["scheduler"]["status"] == "stopped":
        overall_status = "warning"

    status["overall"] = overall_status

    return jsonify(status)


@system_bp.route('/api/controls', methods=['GET'])
def get_controls():
    """Get all system controls and settings"""
    try:
        controls = query_db("""
            SELECT control_key, control_value, control_type, description, updated_at
            FROM system_controls
            ORDER BY control_type, control_key;
        """)

        # Group by type
        result = {
            'settings': [],
            'signals': [],
            'states': []
        }

        for control in controls:
            item = dict(control)
            if control['control_type'] == 'setting':
                result['settings'].append(item)
            elif control['control_type'] == 'signal':
                result['signals'].append(item)
            elif control['control_type'] == 'state':
                result['states'].append(item)

        return jsonify({
            "success": True,
            **result,
            "total": len(controls)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@system_bp.route('/api/controls/<key>', methods=['GET', 'PUT'])
def manage_control(key):
    """Get or update a specific control"""
    try:
        if request.method == 'GET':
            control = query_db("""
                SELECT * FROM system_controls WHERE control_key = %s;
            """, (key,), one=True)

            if control:
                return jsonify({"success": True, **control})
            else:
                return jsonify({"success": False, "error": "Control not found"}), 404

        elif request.method == 'PUT':
            data = request.get_json()
            new_value = data.get('value')

            if new_value is None:
                return jsonify({"success": False, "error": "Value required"}), 400

            conn = ext.db_pool.getconn()
            try:
                with conn.cursor() as cursor:
                    cursor.execute("""
                        UPDATE system_controls
                        SET control_value = %s, updated_at = NOW()
                        WHERE control_key = %s
                        RETURNING *;
                    """, (str(new_value), key))

                    result = cursor.fetchone()
                    conn.commit()

                    if result:
                        # Log the change
                        cursor.execute("""
                            INSERT INTO activity_log (activity_type, activity, details, status)
                            VALUES ('system', 'Control updated', %s, 'info');
                        """, (f"Updated {key} to {new_value}",))
                        conn.commit()

                        return jsonify({"success": True, "message": "Control updated"})
                    else:
                        return jsonify({"success": False, "error": "Control not found"}), 404
            finally:
                ext.db_pool.putconn(conn)

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@system_bp.route('/api/jobs/trigger', methods=['POST'])
def trigger_job():
    """Trigger a data collection job"""
    try:
        data = request.get_json()
        job_type = data.get('job_type')  # 'stock' or 'macro'

        if job_type not in ['stock', 'macro']:
            return jsonify({"success": False, "error": "Invalid job type"}), 400

        control_key = f'job.collect_{job_type}.trigger'

        conn = ext.db_pool.getconn()
        try:
            with conn.cursor() as cursor:
                # Set trigger signal
                cursor.execute("""
                    UPDATE system_controls
                    SET control_value = 'true', updated_at = NOW()
                    WHERE control_key = %s;
                """, (control_key,))

                # Log the action
                cursor.execute("""
                    INSERT INTO activity_log (activity_type, activity, details, status)
                    VALUES ('collection', 'Job triggered', %s, 'info');
                """, (f'{job_type.capitalize()} collection job triggered from UI',))

                conn.commit()

                return jsonify({
                    "success": True,
                    "message": f"{job_type.capitalize()} collection job triggered",
                    "job_type": job_type
                })
        finally:
            ext.db_pool.putconn(conn)

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@system_bp.route('/api/activity-log', methods=['GET'])
def get_activity_log():
    """Get recent activity log entries"""
    try:
        limit = request.args.get('limit', default=50, type=int)
        activity_type = request.args.get('type', default=None, type=str)

        if activity_type:
            logs = query_db("""
                SELECT * FROM activity_log
                WHERE activity_type = %s
                ORDER BY timestamp DESC
                LIMIT %s;
            """, (activity_type, limit))
        else:
            logs = query_db("""
                SELECT * FROM activity_log
                ORDER BY timestamp DESC
                LIMIT %s;
            """, (limit,))

        return jsonify({
            "success": True,
            "logs": logs,
            "total": len(logs)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
