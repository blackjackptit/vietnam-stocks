@echo off
cd /d D:\Working\vn-stock-analytics
start "" /B cloudflared.exe tunnel --url http://localhost:5000 >> D:\Docker\vnstock\logs\tunnel.log 2>&1
