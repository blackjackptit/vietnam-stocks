#!/bin/bash
echo "🚀 Starting Vietnamese Stock Monitor"
echo "📊 Monitoring every 15 minutes"
echo "📁 Logs: monitor_live.log"
echo "🛑 To stop: ./stop_monitor.sh or pkill -f demo_monitor"
echo ""

nohup python3 demo_monitor.py --interval 15 > monitor_live.log 2>&1 &
PID=$!
echo $PID > monitor.pid
echo "✅ Monitor started with PID: $PID"
echo ""
echo "Commands:"
echo "  tail -f monitor_live.log          # Watch live output"
echo "  cat logs/monitor_$(date +%Y%m%d).log  # View today's log"
echo "  ./stop_monitor.sh                  # Stop monitoring"
