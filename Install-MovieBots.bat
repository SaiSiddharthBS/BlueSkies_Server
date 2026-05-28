@echo off
title BlueSkies Cloud Movie Fetcher Installer
echo ==========================================================
echo Starting installation of qBittorrent, Radarr, and Prowlarr
echo ==========================================================
echo Please wait patiently. This usually takes 2-3 minutes.
echo If Windows pops up a yellow shield asking for permissions, click "Yes".
echo.
winget install qBittorrent.qBittorrent --silent --accept-package-agreements --accept-source-agreements
winget install TeamRadarr.Radarr --silent --accept-package-agreements --accept-source-agreements
winget install TeamProwlarr.Prowlarr --silent --accept-package-agreements --accept-source-agreements
echo.
echo ==========================================================
echo Installation Complete!
echo You can now access your new robots in your browser at:
echo Radarr:       http://localhost:7878
echo Prowlarr:     http://localhost:9696
echo qBittorrent:  Will be placed on your Start Menu/Desktop!
echo ==========================================================
pause
