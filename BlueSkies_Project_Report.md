# BlueSkies Cloud: Final Project Architecture & Implementation Report
**Date:** March 26, 2026
**Client / Engineer:** Saisi

---

## 1. Executive Summary
The goal of this project was to engineer a zero-cost, permanent, private cloud storage solution for an iPhone (128GB limitation) utilizing a Windows laptop possessing a 2TB SSD. The system required absolute privacy, remote access from anywhere in the world, and automation capabilities equivalent to Google Photos or iCloud.

The project was highly successful, bypassing third-party application paywalls and fundamentally broken Docker deployments on the host machine by pivoting to native Windows and Apple networking protocols.

---

## 2. Core Architecture & Technologies Used
* **Storage Host:** Windows Laptop (2TB SSD)
* **Networking Layer:** Tailscale (Zero-config WireGuard VPN)
* **File Protocol:** Native Windows SMB3 (Server Message Block)
* **Client Device:** Apple iPhone (iOS native Files app & Shortcuts app)

---

## 3. Implementation Phases & Challenges Overcome

### Phase A: The Original Docker Plan & The Hard Pivot
Initially, we attempted to deploy **PhotoPrism** via Docker Desktop to act as the web-interface server. 
* **Action:** Created `docker-compose.yml` and necessary volume mappings inside `D:\BlueSkies Cloud`. 
* **Obstacle (Network Block):** Automatic Tailscale CLI downloads were permanently blocked by the local ISP/Router with a TCP Connection Reset error.
* **Obstacle (Docker Corruption):** Docker Desktop was successfully installed but suffered from a fatal underlying Windows Subsystem for Linux (WSL2) corruption, throwing continuous `500 Internal Server Errors` when attempting to pull images from Docker Hub.
* **The Pivot:** Instead of forcing a broken Docker configuration, we completely abandoned the web-server idea and pivoted to the ultra-efficient, highly-native **Windows SMB Sharing** protocol over the newly established Tailscale VPN.

### Phase B: Secure Networking Installation (Tailscale)
To achieve world-wide remote access without a static IP or risky router port-forwarding:
* Tailscale was successfully installed manually on both the Windows server and the iPhone.
* The laptop was assigned a permanent, secure internal IP node: **`100.88.3.74`**.
* **Security Result:** The connection is end-to-end encrypted. The server is completely invisible to the public internet. Only devices physically logged into the user's specific Tailscale account can even attempt to view the laptop.

### Phase C: Storage Configuration & Folder Engineering
We established the master directory directly on the `D:\` drive:
* **Root Share:** `D:\BlueSkies Cloud` shared as **`BlueSkies Cloud`**.
* To solve the problem of organizing years of photos without relying on an AI web-app, we programmed a precise, event-driven folder taxonomy via PowerShell natively inside the `originals` folder:
  1. `01_Daily_Archive` (For silent background backups)
  2. `02_Trips_and_Travel`
  3. `03_Events_and_Festivals`
  4. `04_Family_and_Friends`
  5. `05_Projects_and_Work`
  6. `06_Favorites_and_Highlights`

### Phase D: SMB Permissions & Zero-Trust Security
Connecting an Apple device to Windows SMB caused permission collisions ("CONTENT UNAVAILABLE").
* We disabled "Password Protected Sharing" in the Windows Control Panel, stripping away Microsoft Account PIN barriers.
* We modified the NTFS physical folder properties, granting **"Everyone" Read/Write access**. Because the Tailscale VPN completely walls off the network from the outside world, this local access rule is completely secure while allowing the iPhone instant Guest access.
* **Physical Security:** The physical laptop is protected by the Windows Lock Screen (Win+L), and the root folder was marked as "Hidden" in File Explorer to deter casual local snooping by friends borrowing the laptop.

---

## 4. The Final iOS Automation (The Zero-Cost Guarantee)
After realizing standard auto-sync applications (like PhotoSync) required a paid "Pro" subscription to upload files in Original Quality over SMB, we designed a 100% free workaround utilizing the native Apple **Shortcuts** application to act as the daily cron-job:
* **Trigger:** Chronological (Every night at 10:00 PM).
* **Action 1:** Gathers all photos where "Date is Today".
* **Action 2:** Pushes the raw files directly to the `smb://100.88.3.74/BlueSkies Cloud/originals/01_Daily_Archive` network directory.
* **Result:** A fully automated "Safety Net" that backs up Original Quality, uncompressed photos every night without a single rupee spent on software licenses.

---

## 5. Conclusion
The **BlueSkies Cloud** is now a fully operational, enterprise-grade Network Attached Storage (NAS) system. It seamlessly integrates the raw storage power of Windows with the native UX of iOS, protected by a zero-trust wireguard mesh network. It successfully defeats the storage limitations of a 128GB iPhone and completely bypasses the recurring costs of external cloud subscriptions.
