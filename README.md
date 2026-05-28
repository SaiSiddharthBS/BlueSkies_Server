<p align="center">
  <img src="assets/logo.png" width="600" alt="BlueSkies Logo"/>
</p>

<p align="center">
  <strong>A zero-cost, enterprise-grade private cloud server and NAS architecture</strong><br/>
  <em>Engineered to permanently bypass commercial cloud storage limits</em> <br>
  <br>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-OPERATIONAL-00ff00?style=for-the-badge&labelColor=0a0a0a&logo=statuspal&logoColor=00ff00" alt="Status"/>
  <img src="https://img.shields.io/badge/Architecture-Windows%20%7C%20iOS%20%7C%20Tailscale-0077ff?style=for-the-badge&labelColor=0a0a0a&logo=icloud&logoColor=0077ff" alt="Arch"/>
  <img src="https://img.shields.io/badge/Cost-$0.00%20Forever-00f0ff?style=for-the-badge&labelColor=0a0a0a&logo=zeromq&logoColor=00f0ff" alt="Cost"/>
  <img src="https://img.shields.io/badge/License-MIT-white?style=for-the-badge&labelColor=0a0a0a" alt="License"/>
</p>

---

## 📋 Table of Contents

- [Executive Summary](#-executive-summary)
- [Live Frontend Dashboard](#-live-frontend-dashboard)
- [System Architecture Overview](#-system-architecture-overview)
- [Network Topology](#-network-topology)
- [Data Flow & Automation Pipeline](#-data-flow--automation-pipeline)
- [Component Mind Map](#-component-mind-map)
- [Feature Breakdown](#-feature-breakdown)
- [Security Architecture](#-security-architecture)
- [Tech Stack](#-tech-stack)
- [Directory Structure](#-directory-structure)
- [Deployment Guide](#-deployment-guide)
- [Telemetry Pipeline](#-telemetry-pipeline)
- [Implementation Timeline](#-implementation-timeline)
- [Troubleshooting](#-troubleshooting)

---

## 📖 Executive Summary

**BlueSkies** is a fully operational, zero-cost private cloud storage and home server system designed to solve a real-world problem: the **128GB storage limitation** of an iPhone combined with the **recurring subscription costs** of iCloud, Google Photos, and Dropbox.

Instead of paying for third-party cloud services, this project engineers a complete NAS (Network Attached Storage) architecture from scratch using:
- A **Windows laptop with a 2TB SSD** as the storage host  
- **Tailscale** (WireGuard-based mesh VPN) for worldwide encrypted remote access  
- **Native Windows SMB3** file sharing for zero-latency LAN transfers  
- **Apple iOS Shortcuts** as a free cron-job engine for automated nightly backups  
- A **custom Python telemetry daemon** for real-time hardware monitoring  
- An **automated media management stack** (Radarr + Prowlarr + qBittorrent)  
- A **high-tech scrollytelling frontend** deployed on GitHub Pages with GSAP, Globe.gl, and glassmorphic UI

> **Result:** A fully automated "Safety Net" that backs up original-quality, uncompressed photos every night — without a single rupee spent on software licenses.

---

## 🌐 Live Frontend Dashboard

The project includes a production-deployed, high-performance frontend experience hosted on **GitHub Pages**:

**🔗 [https://saisiddharthbs.github.io/BlueSkies/](https://saisiddharthbs.github.io/BlueSkies/)**

### Frontend Tech Stack

| Technology | Purpose |
|:---|:---|
| **GSAP 3.12 + ScrollTrigger** | Scroll-driven parallax animations, horizontal scroll panels, immersive text reveals |
| **Globe.gl (Three.js)** | Interactive 3D WebGL globe with real-time data node visualization |
| **Vanilla Tilt.js** | 3D parallax tilt effects on glassmorphic pricing cards |
| **Lenis Smooth Scroll** | Butter-smooth scroll normalization across all browsers |
| **Custom Plasma Cursor** | GPU-accelerated trailing cursor with mix-blend-mode exclusion |

### Frontend Sections

| Section | Description |
|:---|:---|
| **Hero** | Cinematic full-screen parallax with animated title reveal |
| **Horizontal Scroll Panels** | GSAP-pinned panels showcasing Performance, Security, and Scalability |
| **Live Telemetry Widget** | Floating glassmorphic HUD with randomized real-time data simulation |
| **Globe.gl Node Map** | Interactive 3D earth with 5 global data center nodes and hover tooltips |
| **Compute Tiers** | 3D-tilting glassmorphic pricing cards (Sigma / Quantum / Zenith) |
| **Immersive Reveal** | Scroll-triggered opacity text animation: "The Future of Connectivity Starts Here" |
| **Magnetic CTA Footer** | Physics-based magnetic button with elastic snap-back |

---

## 🏗️ System Architecture Overview

```mermaid
graph TB
    subgraph INTERNET["☁️ PUBLIC INTERNET"]
        direction TB
        TAILSCALE_RELAY["Tailscale DERP Relay<br/><i>Coordination Server</i>"]
    end

    subgraph VPN_MESH["🔐 TAILSCALE MESH VPN (WireGuard)"]
        direction LR
        
        subgraph SERVER["🖥️ WINDOWS SERVER<br/>100.88.3.74"]
            direction TB
            SMB["SMB3 File Share<br/><i>D: BlueSkies Cloud</i>"]
            FB["FileBrowser<br/><i>:8080 Web UI</i>"]
            TEL["Telemetry Daemon<br/><i>Python + psutil</i>"]
            RADARR["Radarr<br/><i>:7878</i>"]
            PROWLARR["Prowlarr<br/><i>:9696</i>"]
            QB["qBittorrent<br/><i>P2P Client</i>"]
            SSD[("💾 2TB SSD<br/>D: Drive")]
            
            SMB --> SSD
            FB --> SSD
            RADARR --> QB
            PROWLARR --> RADARR
            QB --> SSD
            TEL --> GIST_API
        end

        subgraph CLIENT["📱 iPHONE CLIENT"]
            direction TB
            FILES["iOS Files App<br/><i>SMB Native Client</i>"]
            SHORTCUTS["iOS Shortcuts<br/><i>Nightly Cron Job</i>"]
            SHORTCUTS --> FILES
        end

        SERVER <--->|"End-to-End<br/>Encrypted"| CLIENT
    end

    TAILSCALE_RELAY -.->|"NAT Traversal<br/>Coordination"| VPN_MESH
    GIST_API["GitHub Gist API<br/><i>Telemetry Sync</i>"]
    PAGES["GitHub Pages<br/><i>Frontend Dashboard</i>"]

    style INTERNET fill:#1a1a2e,stroke:#0077ff,color:#fff
    style VPN_MESH fill:#0d1117,stroke:#00f0ff,color:#fff
    style SERVER fill:#161b22,stroke:#0077ff,color:#fff
    style CLIENT fill:#161b22,stroke:#00f0ff,color:#fff
    style SSD fill:#1a1a2e,stroke:#ffaa00,color:#fff
```

---

## 🌐 Network Topology

```mermaid
graph LR
    subgraph HOME_NETWORK["🏠 Local Network (Behind NAT/ISP)"]
        LAPTOP["🖥️ Windows Laptop<br/>Tailscale IP: 100.88.3.74<br/>2TB SSD"]
    end

    subgraph MOBILE["📱 Mobile (Any Network)"]
        IPHONE["iPhone<br/>Tailscale Client<br/>iOS Files + Shortcuts"]
    end

    subgraph CLOUD_SERVICES["☁️ Cloud Services"]
        TS_COORD["Tailscale<br/>Coordination Server"]
        GITHUB["GitHub<br/>Gist API + Pages"]
    end

    LAPTOP <-->|"WireGuard Tunnel<br/>AES-256 Encrypted<br/>Direct P2P when possible"| IPHONE
    LAPTOP -.->|"NAT Traversal<br/>Handshake Only"| TS_COORD
    IPHONE -.->|"NAT Traversal<br/>Handshake Only"| TS_COORD
    LAPTOP -->|"HTTPS POST<br/>Telemetry JSON"| GITHUB

    style HOME_NETWORK fill:#0d1117,stroke:#0077ff,color:#fff
    style MOBILE fill:#0d1117,stroke:#00f0ff,color:#fff
    style CLOUD_SERVICES fill:#1a1a2e,stroke:#888,color:#fff
```

> **Key Insight:** Tailscale only uses the coordination server for the initial NAT traversal handshake. Once the tunnel is established, all data flows **directly peer-to-peer** between the laptop and the iPhone. The coordination server never sees your files.

---

## 🔄 Data Flow & Automation Pipeline

### Nightly Photo Backup Flow

```mermaid
sequenceDiagram
    participant CRON as ⏰ iOS Shortcuts<br/>(10:00 PM Trigger)
    participant PHOTOS as 📷 iPhone Photos
    participant SMB as 📂 SMB3 Protocol
    participant TAILSCALE as 🔐 Tailscale VPN
    participant NAS as 💾 D: BlueSkies Cloud<br/>/originals/01_Daily_Archive

    CRON->>PHOTOS: Gather all photos where "Date is Today"
    PHOTOS-->>CRON: Returns raw photo bundle (HEIC/JPEG)
    CRON->>SMB: Push files to<br/>smb://100.88.3.74/BlueSkies Cloud/originals/01_Daily_Archive
    SMB->>TAILSCALE: Encrypt payload (WireGuard AES-256)
    TAILSCALE->>NAS: Deliver to D: drive via SMB3
    NAS-->>CRON: ✅ Write confirmed
    
    Note over CRON,NAS: Zero human intervention required.<br/>Runs every night automatically.
```

### Media Acquisition Pipeline

```mermaid
flowchart LR
    A["🔍 Prowlarr<br/><i>Indexer Manager</i><br/>Port 9696"] -->|"Search Results<br/>& Torrent Links"| B["🎬 Radarr<br/><i>Movie Manager</i><br/>Port 7878"]
    B -->|"Download<br/>Request"| C["⬇️ qBittorrent<br/><i>P2P Client</i>"]
    C -->|"Completed<br/>Downloads"| D["💾 D: Drive<br/><i>/Movies/ or /TV Shows/</i>"]
    D -->|"Served via<br/>FileBrowser"| E["🌐 WebShare<br/><i>HTTP :8080</i>"]

    style A fill:#1a1a2e,stroke:#0077ff,color:#fff
    style B fill:#1a1a2e,stroke:#00f0ff,color:#fff
    style C fill:#1a1a2e,stroke:#ffaa00,color:#fff
    style D fill:#161b22,stroke:#00ff00,color:#fff
    style E fill:#161b22,stroke:#0077ff,color:#fff
```

### Telemetry Data Pipeline

```mermaid
flowchart LR
    A["🐍 telemetry_daemon.py"] -->|"psutil<br/>every 30s"| B["📊 Collect Metrics<br/>CPU / RAM / Disk / Uptime"]
    B --> C["🔍 Service Health Check<br/>FileBrowser / Radarr<br/>Prowlarr / qBittorrent"]
    C --> D["📝 Format JSON<br/>Payload"]
    D -->|"HTTPS PATCH"| E["☁️ GitHub Gist API"]
    D -->|"Local Write"| F["💾 telemetry_backup.json"]
    E --> G["📈 Remote Dashboard<br/>Integration"]

    style A fill:#1a1a2e,stroke:#0077ff,color:#fff
    style E fill:#161b22,stroke:#00f0ff,color:#fff
    style G fill:#161b22,stroke:#00ff00,color:#fff
```

---

## 🧠 Component Mind Map

```mermaid
mindmap
  root((☁️ BlueSkies))
    🔐 Security Layer
      Tailscale WireGuard VPN
      End-to-End Encryption
      Zero Public Exposure
      NTFS Access Control
      Windows Lock Screen
    💾 Storage Engine
      2TB SSD - D: Drive
      SMB3 File Sharing
      NTFS Filesystem
      Folder Taxonomy
        01 Daily Archive
        02 Trips and Travel
        03 Events and Festivals
        04 Family and Friends
        05 Projects and Work
        06 Favorites and Highlights
    📱 iOS Automation
      Apple Shortcuts App
      Nightly Cron at 10 PM
      Native SMB Client
      Original Quality HEIC/JPEG
    🎬 Media Stack
      Prowlarr - Indexer
      Radarr - Movie Manager
      qBittorrent - Downloader
      FileBrowser - Web GUI
    📊 Telemetry
      Python psutil Daemon
      CPU and RAM Monitoring
      Disk Space Tracking
      Service Health Checks
      GitHub Gist Cloud Sync
    🌐 Frontend
      GitHub Pages Deployment
      GSAP ScrollTrigger
      Globe.gl 3D Visualization
      Glassmorphic UI
      Plasma Cursor FX
```

---

## ✨ Feature Breakdown

### 1. 📷 Zero-Cost Original Quality Photo Backup

| Attribute | Detail |
|:---|:---|
| **Trigger** | iOS Shortcuts — Every night at 10:00 PM |
| **Protocol** | SMB3 over encrypted Tailscale tunnel |
| **Quality** | Original, uncompressed (HEIC / JPEG) |
| **Destination** | `D:\BlueSkies Cloud\originals\01_Daily_Archive` |
| **Cost** | **$0.00** — No subscription, no app purchase |

> **Why this matters:** Third-party auto-sync apps like PhotoSync require a paid "Pro" subscription ($4.99) to upload at original quality over SMB. This architecture replaces that entirely with native Apple Shortcuts — for free.

### 2. 🔐 Zero-Trust Mesh VPN (Tailscale)

```mermaid
flowchart TB
    subgraph TRADITIONAL["❌ Traditional Port Forwarding"]
        R1["Router"] -->|"Port 443 Open<br/>to the ENTIRE internet"| S1["Server"]
        ATTACKER["🏴‍☠️ Attacker"] -->|"Can reach<br/>open port"| R1
    end

    subgraph TAILSCALE["✅ BlueSkies + Tailscale"]
        R2["Router"] -->|"All ports CLOSED<br/>No inbound rules"| S2["Server"]
        PHONE["📱 iPhone"] <-->|"Encrypted<br/>WireGuard Tunnel"| S2
        ATTACKER2["🏴‍☠️ Attacker"] -.-x|"❌ BLOCKED<br/>Invisible"| R2
    end

    style TRADITIONAL fill:#2d1117,stroke:#ff4444,color:#fff
    style TAILSCALE fill:#0d1117,stroke:#00ff00,color:#fff
```

### 3. 🎬 Automated Media Stack (MovieBots)

One-click deployment via Windows Package Manager:
```cmd
.\Install-MovieBots.bat
```
This batch script installs via `winget`:
- **qBittorrent** — P2P download client  
- **Radarr** — Automated movie library management  
- **Prowlarr** — Universal indexer/tracker manager  

### 4. 📊 Hardware Telemetry Daemon

A persistent Python process that collects and pushes live server metrics:

```python
# Metrics collected every 30 seconds
{
    "cpu_temp":  "12.5% LOAD",
    "ram_usage": "6.2 / 16.0 GB",
    "disk_free": "1482.3 GB FREE",
    "uptime":    "72h 14m",
    "services": {
        "filebrowser": true,
        "radarr":      true,
        "prowlarr":    true,
        "qbittorrent": false
    }
}
```

### 5. 🌐 WebShare File Browser

A portable web-based file manager for remote browsing and sharing:
- **Launch:** `.\Start-WebShare-App.bat`
- **Access:** `http://<tailscale-ip>:8080`
- **Features:** Upload, download, share links, user management

### 6. 🧠 AI Rate Limit Monitor (Blueprint)

An architectural blueprint for a **Manifest V3 Chrome Extension** designed to:
- **Passively intercept** ChatGPT web request counts via DOM/XHR monitoring  
- **Micro-ping** developer API keys (Anthropic, OpenAI, Gemini) using a 1-token request costing **$0.000000375** per check  
- Display usage in a **dark glassmorphic dropdown** popup

---

## 🔒 Security Architecture

```mermaid
graph TB
    subgraph LAYER1["Layer 1: Network Perimeter"]
        A["Tailscale WireGuard VPN<br/>All ports closed to public internet"]
    end

    subgraph LAYER2["Layer 2: Authentication"]
        B["Tailscale Device Auth<br/>Only registered devices can join"]
    end

    subgraph LAYER3["Layer 3: Transport"]
        C["End-to-End Encryption<br/>AES-256 via WireGuard"]
    end

    subgraph LAYER4["Layer 4: File System"]
        D["NTFS Permissions<br/>Read/Write scoped to Tailnet only"]
    end

    subgraph LAYER5["Layer 5: Physical"]
        E["Windows Lock Screen<br/>Hidden root folder in Explorer"]
    end

    subgraph LAYER6["Layer 6: Secrets"]
        F["config.json gitignored<br/>Tokens never committed to Git"]
    end

    LAYER1 --> LAYER2 --> LAYER3 --> LAYER4 --> LAYER5 --> LAYER6

    style LAYER1 fill:#0d1117,stroke:#00ff00,color:#fff
    style LAYER2 fill:#0d1117,stroke:#00cc00,color:#fff
    style LAYER3 fill:#0d1117,stroke:#009900,color:#fff
    style LAYER4 fill:#0d1117,stroke:#007700,color:#fff
    style LAYER5 fill:#0d1117,stroke:#005500,color:#fff
    style LAYER6 fill:#0d1117,stroke:#003300,color:#fff
```

| Threat Vector | Mitigation |
|:---|:---|
| Public internet scanning | Server is invisible — zero open ports |
| Man-in-the-middle attack | WireGuard E2E encryption (AES-256) |
| Unauthorized device access | Tailscale requires authenticated device registration |
| API token leakage | Tokens stored in `config.json` (gitignored), loaded at runtime |
| Physical laptop access | Windows Lock Screen + hidden root folder |
| Telemetry data leakage | JSON contains only system metrics — no PII, no filenames |

---

## 🛠️ Tech Stack

| Layer | Technology | Version / Detail |
|:---|:---|:---|
| **OS** | Windows 10/11 | Storage host with 2TB NTFS SSD |
| **VPN** | Tailscale | WireGuard-based mesh network |
| **File Protocol** | SMB3 | Native Windows file sharing |
| **Client OS** | iOS 17+ | Files App + Shortcuts App |
| **Telemetry** | Python 3.x | `psutil`, `urllib`, `json` |
| **Media - Movies** | Radarr | Port 7878 |
| **Media - Indexer** | Prowlarr | Port 9696 |
| **Media - Downloader** | qBittorrent | Installed via `winget` |
| **Web File Manager** | FileBrowser | Portable `.exe`, Port 8080 |
| **Frontend Framework** | Vanilla JS | No build step |
| **Animation** | GSAP 3.12.5 | ScrollTrigger plugin |
| **3D Globe** | Globe.gl | Three.js wrapper |
| **3D Cards** | Vanilla Tilt 1.8.1 | Glassmorphic parallax |
| **Smooth Scroll** | Lenis 1.0.39 | Studio Freight |
| **Typography** | Google Fonts | Outfit + JetBrains Mono |
| **Hosting** | GitHub Pages | Static deployment from `main` branch |
| **Telemetry Sync** | GitHub Gist API | HTTPS PATCH requests |

---

## 📂 Directory Structure

```
BlueSkies/
│
├── 🌐 FRONTEND (GitHub Pages)
│   ├── index.html              # Main scrollytelling web experience
│   ├── script.js               # GSAP animations, Globe.gl, telemetry simulation
│   ├── style.css               # Glassmorphic design system, plasma cursor
│   └── assets/
│       ├── server_rack.png     # Hero parallax background
│       └── cyber_data.png      # Horizontal scroll panel image
│
├── ⚙️ BACKEND INFRASTRUCTURE
│   ├── telemetry_daemon.py     # Hardware monitoring + GitHub Gist sync
│   ├── Install-MovieBots.bat   # One-click media stack installer (winget)
│   ├── Start-WebShare-App.bat  # FileBrowser web UI launcher
│   └── FileBrowser/            # Portable web-based file manager
│
├── 📝 DOCUMENTATION
│   ├── README.md               # ← You are here
│   ├── BlueSkies_Project_Report.md  # Detailed engineering report
│   └── AI_Monitor_Blueprint.md      # Chrome extension architecture
│
├── 📁 PRIVATE (gitignored)
│   ├── originals/              # Automated iOS photo backups
│   ├── Downloads/              # qBittorrent download target
│   ├── Movies/                 # Radarr movie library
│   ├── TV Shows/               # Television library
│   ├── config.json             # API tokens (never committed)
│   └── telemetry_backup.json   # Local telemetry cache
│
└── .gitignore                  # Protects all private data from Git
```

---

## 🚀 Deployment Guide

### Prerequisites
- Windows 10/11 with a secondary storage drive (D:)
- Python 3.8+ installed
- iPhone with iOS 16+ (for Shortcuts automation)

### Phase 1 — Network Foundation
```
1. Install Tailscale on Windows  →  https://tailscale.com/download
2. Install Tailscale on iPhone   →  App Store
3. Sign in with the same account on both devices
4. Note the Windows machine's Tailscale IP (e.g., 100.88.3.74)
```

### Phase 2 — Storage Configuration
```
1. Create  D:\BlueSkies Cloud\
2. Right-click → Properties → Sharing → Share this folder
3. NTFS Security → Add "Everyone" with Read/Write
4. Create subdirectories under originals/:
   ├── 01_Daily_Archive
   ├── 02_Trips_and_Travel
   ├── 03_Events_and_Festivals
   ├── 04_Family_and_Friends
   ├── 05_Projects_and_Work
   └── 06_Favorites_and_Highlights
```

### Phase 3 — iOS Automation
```
1. Open Shortcuts app on iPhone
2. Create new Automation → Time of Day → 10:00 PM
3. Action 1: Find Photos Where → Date Taken is Today
4. Action 2: Save File → SMB → smb://<tailscale-ip>/BlueSkies Cloud/originals/01_Daily_Archive
5. Enable "Run Without Asking"
```

### Phase 4 — Media Stack
```cmd
.\Install-MovieBots.bat
```

### Phase 5 — Telemetry
```cmd
pip install psutil
python telemetry_daemon.py
```

### Phase 6 — WebShare
```cmd
.\Start-WebShare-App.bat
```

---

## 📊 Telemetry Pipeline

```mermaid
stateDiagram-v2
    [*] --> Boot: python telemetry_daemon.py

    state "Collection Loop (every 30s)" as Loop {
        Boot --> ReadCPU: psutil.cpu_percent()
        ReadCPU --> ReadRAM: psutil.virtual_memory()
        ReadRAM --> ReadDisk: psutil.disk_usage('D:\\')
        ReadDisk --> ReadUptime: psutil.boot_time()
        ReadUptime --> CheckServices: Process scan
        CheckServices --> FormatJSON: Build payload
    }

    FormatJSON --> PushGist: HTTPS PATCH → GitHub Gist API
    FormatJSON --> SaveLocal: Write telemetry_backup.json
    PushGist --> Loop: Sleep 30s
    SaveLocal --> Loop: Sleep 30s
```

---

## 📅 Implementation Timeline

```mermaid
gantt
    title BlueSkies Development Timeline
    dateFormat  YYYY-MM-DD
    axisFormat  %b %d

    section Research & Planning
    Architecture Design           :done, 2026-04-01, 2026-04-10
    Docker Investigation & Pivot  :done, 2026-04-05, 2026-04-12

    section Core Infrastructure
    Tailscale VPN Setup           :done, 2026-04-12, 2026-04-13
    SMB3 Share Configuration      :done, 2026-04-13, 2026-04-14
    NTFS Permissions Tuning       :done, 2026-04-14, 2026-04-14
    iOS Shortcuts Automation      :done, 2026-04-14, 2026-04-15

    section Frontend
    Scrollytelling MVP            :done, 2026-04-14, 2026-04-14
    GSAP Features & Globe.gl      :done, 2026-04-21, 2026-04-21
    Lenis Scroll Polish           :done, 2026-04-21, 2026-04-21

    section Media Stack
    MovieBots Installation        :done, 2026-04-16, 2026-04-18
    Radarr + Prowlarr Config      :done, 2026-04-18, 2026-04-20

    section Telemetry & Monitoring
    Python Daemon Development     :done, 2026-05-01, 2026-05-10
    GitHub Gist Integration       :done, 2026-05-10, 2026-05-15
    FileBrowser WebShare           :done, 2026-05-15, 2026-05-20

    section Documentation
    Industrial README             :done, 2026-05-28, 2026-05-29
```

---

## 🔧 Troubleshooting

| Issue | Cause | Fix |
|:---|:---|:---|
| iPhone shows "Content Unavailable" on SMB | NTFS permission mismatch | Grant "Everyone" Read/Write on folder properties |
| Cannot connect via SMB | Tailscale not running on one device | Verify both devices show as "Connected" in Tailscale admin |
| Telemetry daemon crashes | Missing `psutil` module | `pip install psutil` |
| `telemetry_daemon.py` shows "SECURITY HALT" | Token placeholder not replaced | Create `config.json` with your GitHub token |
| FileBrowser blocked by Windows Defender | Firewall rule not set | Click "Allow Access" when prompted, or add manual rule |
| GitHub push rejected (secret scanning) | Token committed to Git | Ensure `config.json` is in `.gitignore` — never hardcode tokens |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <strong>Engineered & Maintained by Sai Siddharth B S</strong><br/>
  <em>BlueSkies — Because your data belongs to you.</em>
</p>
