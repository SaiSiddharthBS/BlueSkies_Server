# ☁️ BlueSkies Cloud

![Architecture](https://img.shields.io/badge/Architecture-Windows%20%7C%20iOS%20%7C%20Tailscale-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Operational-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**BlueSkies Cloud** is a zero-cost, private, and fully automated Home Server and Network Attached Storage (NAS) architecture. Engineered from the ground up to bypass commercial cloud storage limits (like iCloud or Google Photos paywalls), this system leverages native Windows protocols, iOS Shortcuts, and Tailscale's zero-trust mesh VPN to provide worldwide secure access to a 2TB local SSD.

---

## 🚀 Key Features

### 1. Zero-Cost Original Quality Photo Backup
Bypass the storage limitations of a 128GB iPhone. Utilizing native Apple Shortcuts and Windows Server Message Block (SMB3), BlueSkies Cloud performs automated, silent background backups of daily photos at original, uncompressed quality.
- **Trigger:** Automated chron-job (Nightly at 10:00 PM).
- **Transport:** SMB over encrypted Tailscale network.
- **Taxonomy:** Automated sorting into events and daily archives.

### 2. Zero-Trust Mesh VPN Security (Tailscale)
No risky port forwarding, no static IP requirements. 
- The server node is assigned a permanent, secure internal IP (`100.88.3.74`).
- End-to-end encrypted connection ensuring the server remains completely invisible to the public internet.

### 3. Automated Media Stack (MovieBots)
A fully integrated stack for automated media acquisition and management.
- **Radarr & Prowlarr:** Automated movie searching, filtering, and indexing.
- **qBittorrent:** Handled via custom installation batch scripts for seamless P2P fetching.
- **Access:** Web interfaces accessible locally or remotely via Tailscale (`http://localhost:7878`).

### 4. Telemetry & Hardware HUD Daemon
A custom Python daemon (`telemetry_daemon.py`) actively monitors hardware load and service health.
- **Metrics Tracked:** CPU Load, RAM Allocation, Disk Space, System Uptime.
- **Service Monitoring:** Validates runtime status for FileBrowser, Radarr, Prowlarr, and qBittorrent.
- **Cloud Sync:** Securely pushes live telemetry data to a GitHub Gist API for remote dashboard integration.

### 5. WebShare File Browser
Easily share and manage files via a sleek web GUI (`filebrowser.exe`). 
- Executed securely via `Start-WebShare-App.bat`.
- Accessible anywhere via Tailscale VPN at `http://100.88.3.74:8080`.

### 6. AI Rate Limit Monitor (Supplementary Blueprint)
Includes an architectural blueprint (`AI_Monitor_Blueprint.md`) for a Manifest V3 Chrome Extension. It's designed to passively monitor web subscriptions and dynamically check developer API usage via an innovative 1-token micro-ping protocol to Anthropic, OpenAI, and Gemini APIs without breaking ToS or CORS security blocks.

---

## 🏗️ Core Architecture & Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Storage Host** | Windows 10/11 | 2TB SSD utilizing native NTFS and SMB3 sharing |
| **Networking** | Tailscale | Zero-configuration WireGuard VPN mesh |
| **Client** | Apple iOS | Native Files App & iOS Shortcuts |
| **Telemetry** | Python (`psutil`) | OS-Agnostic hardware monitoring daemon |
| **Media Stack** | Radarr/Prowlarr | Automated via Windows Package Manager (`winget`) |

---

## 📂 Directory Structure

```text
D:\BlueSkies Cloud\
├── 📁 originals/            # Automated photo/media backups from iOS
├── 📁 Downloads/            # Target directory for media fetched by qBittorrent
├── 📁 Movies/               # Radarr managed movie library
├── 📁 TV Shows/             # Sonarr/Radarr managed television library
├── 📁 FileBrowser/          # Web UI executable and database for remote file access
├── 📜 BlueSkies_Project_Report.md # Detailed engineering and architecture report
├── 📜 AI_Monitor_Blueprint.md     # Blueprint for AI API monitoring extension
├── 📜 telemetry_daemon.py   # Hardware monitoring and API synchronization script
├── 📜 Install-MovieBots.bat # Automated installer for the media stack (winget)
└── 📜 Start-WebShare-App.bat# Launcher for the FileBrowser web interface
```

---

## ⚙️ Installation & Deployment

### Phase 1: Storage & Network Setup
1. Install **Tailscale** on both the Windows Host and the Client device (e.g., iPhone).
2. Authenticate both devices to the same Tailscale network to establish the secure tunnel.
3. Configure `D:\BlueSkies Cloud` as a shared network drive via Windows Properties > Sharing.
4. Set NTFS properties to allow "Everyone" Read/Write access (Secured behind Tailscale).

### Phase 2: Media Automation
Run the included batch script to automatically deploy the media automation stack via `winget`.
```cmd
.\Install-MovieBots.bat
```

### Phase 3: Telemetry Daemon
To monitor server health, ensure Python is installed along with the `psutil` library:
```cmd
pip install psutil
```
Edit `telemetry_daemon.py` to include your GitHub Token and Gist ID, then start the daemon:
```cmd
python telemetry_daemon.py
```

### Phase 4: Start Web Access
Launch the FileBrowser web interface to share files over HTTP by running:
```cmd
.\Start-WebShare-App.bat
```

---

## 🔒 Security Posture & Privacy

- **No Public Exposure:** The architecture deliberately avoids Docker complexities and port-forwarding vulnerabilities by leveraging Tailscale.
- **SMB Authentication:** Windows Control Panel "Password Protected Sharing" is disabled *only* for the Tailnet. The physical local machine remains protected via Windows Lock Screen.
- **Telemetry Anonymity:** Telemetry data is pushed securely over HTTPS and contains no Personal Identifiable Information (PII) or plaintext file names.

---
*Engineered by Saisi*
