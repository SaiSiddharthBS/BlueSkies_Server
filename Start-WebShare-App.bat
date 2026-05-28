@echo off
title BlueSkies Cloud Share Links Server
cd /d "D:\BlueSkies Cloud\FileBrowser"
echo ==========================================================
echo BlueSkies Cloud Web Sharing App
echo ==========================================================
echo Your server is starting...
echo.
echo IMPORTANT: If Windows Defender pops up asking to allow FileBrowser.exe through the firewall, click "Allow Access"!
echo.
echo Once started, anyone can access your shared folders by going to:
echo http://100.88.3.74:8080
echo.
filebrowser.exe
pause
