#!/bin/bash
# Scheduler Management Script

PLIST_NAME="com.vnstock.scheduler"
PLIST_FILE="$HOME/Library/LaunchAgents/${PLIST_NAME}.plist"
PROJECT_DIR="/Users/nghia.dinh/Projects/vietnam-stocks"

show_usage() {
    echo "📅 VNStock Scheduler Manager"
    echo ""
    echo "Usage: $0 [command]"
    echo ""
    echo "Commands:"
    echo "  install    - Install scheduler as LaunchAgent (auto-start on login)"
    echo "  uninstall  - Remove scheduler from LaunchAgent"
    echo "  start      - Start the scheduler"
    echo "  stop       - Stop the scheduler"
    echo "  restart    - Restart the scheduler"
    echo "  status     - Check if scheduler is running"
    echo "  logs       - View scheduler logs"
    echo "  test       - Run all jobs once for testing"
    echo "  test-stock - Test stock collection only"
    echo "  test-macro - Test macro collection only"
    echo "  settings   - View current configuration settings"
    echo "  schedule   - Preview collection schedule"
    echo ""
    echo "💡 Configuration:"
    echo "   Schedule and frequencies are configured in .env file"
    echo "   Run 'python jobs/manage_settings.py' to view/edit settings"
    echo ""
}

install_scheduler() {
    echo "📦 Installing scheduler as LaunchAgent..."

    # Make start script executable
    chmod +x "${PROJECT_DIR}/jobs/start_scheduler.sh"
    echo "✓ Made start script executable"

    # Copy plist to LaunchAgents
    cp "${PROJECT_DIR}/jobs/${PLIST_NAME}.plist" "$PLIST_FILE"
    echo "✓ Copied plist to LaunchAgents"

    # Load the service
    launchctl load "$PLIST_FILE"
    echo "✓ Loaded LaunchAgent"

    # Start the service
    launchctl start "$PLIST_NAME"
    echo "✓ Started scheduler"

    echo ""
    echo "✅ Scheduler installed and started!"
    echo "View logs: tail -f /tmp/stock_scheduler.log"
}

uninstall_scheduler() {
    echo "🗑️  Uninstalling scheduler..."

    # Stop the service
    launchctl stop "$PLIST_NAME" 2>/dev/null
    echo "✓ Stopped scheduler"

    # Unload the service
    launchctl unload "$PLIST_FILE" 2>/dev/null
    echo "✓ Unloaded LaunchAgent"

    # Remove plist
    rm -f "$PLIST_FILE"
    echo "✓ Removed plist file"

    echo ""
    echo "✅ Scheduler uninstalled!"
}

start_scheduler() {
    echo "▶️  Starting scheduler..."
    launchctl start "$PLIST_NAME"
    sleep 2
    check_status
}

stop_scheduler() {
    echo "⏹️  Stopping scheduler..."
    launchctl stop "$PLIST_NAME"
    echo "✅ Scheduler stopped"
}

restart_scheduler() {
    echo "🔄 Restarting scheduler..."
    stop_scheduler
    sleep 2
    start_scheduler
}

check_status() {
    echo "🔍 Checking scheduler status..."
    echo ""

    # Check if LaunchAgent is loaded
    if launchctl list | grep -q "$PLIST_NAME"; then
        echo "✅ LaunchAgent is loaded"

        # Get PID
        PID=$(launchctl list | grep "$PLIST_NAME" | awk '{print $1}')
        if [ "$PID" != "-" ]; then
            echo "✅ Scheduler is running (PID: $PID)"

            # Check process details
            ps -p "$PID" -o command= 2>/dev/null | head -1
        else
            echo "⚠️  Scheduler is loaded but not running"
        fi
    else
        echo "❌ LaunchAgent is not loaded"
        echo "   Run: $0 install"
    fi

    echo ""

    # Check recent log activity
    if [ -f "/tmp/stock_scheduler.log" ]; then
        echo "📄 Recent log activity:"
        tail -5 /tmp/stock_scheduler.log
    fi
}

view_logs() {
    echo "📄 Viewing scheduler logs (Ctrl+C to exit)..."
    echo ""

    if [ -f "/tmp/stock_scheduler.log" ]; then
        tail -f /tmp/stock_scheduler.log
    else
        echo "❌ Log file not found: /tmp/stock_scheduler.log"
        echo "   Scheduler may not have run yet"
    fi
}

test_jobs() {
    echo "🧪 Running all jobs (test mode)..."
    cd "$PROJECT_DIR"
    source venv/bin/activate
    python jobs/scheduler.py --now
    deactivate
}

test_stock() {
    echo "🧪 Testing stock collection..."
    cd "$PROJECT_DIR"
    source venv/bin/activate
    python jobs/scheduler.py --stock-only
    deactivate
}

test_macro() {
    echo "🧪 Testing macro collection..."
    cd "$PROJECT_DIR"
    source venv/bin/activate
    python jobs/scheduler.py --macro-only
    deactivate
}

show_settings() {
    echo "⚙️  Showing current configuration..."
    cd "$PROJECT_DIR"
    source venv/bin/activate
    python jobs/manage_settings.py
    deactivate
}

show_schedule() {
    echo "📅 Showing collection schedule..."
    cd "$PROJECT_DIR"
    source venv/bin/activate
    python jobs/manage_settings.py --schedule
    deactivate
}

# Main command handler
case "${1:-}" in
    install)
        install_scheduler
        ;;
    uninstall)
        uninstall_scheduler
        ;;
    start)
        start_scheduler
        ;;
    stop)
        stop_scheduler
        ;;
    restart)
        restart_scheduler
        ;;
    status)
        check_status
        ;;
    logs)
        view_logs
        ;;
    test)
        test_jobs
        ;;
    test-stock)
        test_stock
        ;;
    test-macro)
        test_macro
        ;;
    settings)
        show_settings
        ;;
    schedule)
        show_schedule
        ;;
    *)
        show_usage
        exit 1
        ;;
esac
