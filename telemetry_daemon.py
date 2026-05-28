import psutil
import json
import time
import datetime
import urllib.request
import urllib.error
import os

# --- SECURE CLOUD CONFIGURATION ---
CONFIG_FILE = 'config.json'
GITHUB_TOKEN = "YOUR_GITHUB_TOKEN_HERE"
GIST_ID = "f5dc683afb7eeee5a8196df225f29ad6"

if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, 'r') as f:
        _config = json.load(f)
        GITHUB_TOKEN = _config.get("GITHUB_TOKEN", GITHUB_TOKEN)
        GIST_ID = _config.get("GIST_ID", GIST_ID)
# ----------------------------------

# Services to monitor (process name → display name)
SERVICES = {
    "filebrowser": "FileBrowser",
    "radarr": "Radarr",
    "prowlarr": "Prowlarr",
    "qbittorrent": "qBittorrent",
}

def push_to_gist(data):
    if "YOUR_GITHUB" in GITHUB_TOKEN:
        print("[!] SECURITY HALT: Missing GitHub Personal Access Token. Please add it to code.")
        return
        
    url = f"https://api.github.com/gists/{GIST_ID}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json"
    }
    
    payload = {
        "files": {
            "blueskies_telemetry.json": {
                "content": json.dumps(data)
            }
        }
    }
    
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='PATCH')
    try:
        with urllib.request.urlopen(req) as response:
            print(f"[+] Successfully pushed Live Hardware Stats to Cloud API.")
    except Exception as e:
        print(f"[-] FATAL: Failed to push to GitHub Gist: {e}")

def check_services():
    """Check which real services are currently running on this machine."""
    running = {}
    try:
        process_names = [p.info['name'].lower() for p in psutil.process_iter(['name'])]
        for key, display_name in SERVICES.items():
            running[key] = any(key in name for name in process_names)
    except Exception:
        for key in SERVICES:
            running[key] = False
    return running

def get_uptime():
    """Get machine uptime since last boot."""
    boot = datetime.datetime.fromtimestamp(psutil.boot_time())
    delta = datetime.datetime.now() - boot
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, _ = divmod(remainder, 60)
    return f"{hours}h {minutes}m"

def get_telemetry():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    
    # OS Agnostic Disk Check: Drives 'D:\' on Windows, or root '/' on macOS.
    try:
        disk = psutil.disk_usage('D:\\')
    except:
        disk = psutil.disk_usage('/')

    services = check_services()
    uptime = get_uptime()

    # Format the data exactly so the Website HUD displays it natively
    data = {
        "cpu_temp": f"{cpu}% LOAD",
        "ram_usage": f"{ram.used / (1024**3):.1f} / {ram.total / (1024**3):.1f} GB",
        "disk_free": f"{disk.free / (1024**3):.1f} GB FREE",
        "uptime": uptime,
        "services": services
    }

    # Save locally for debugging reference
    with open('telemetry_backup.json', 'w') as f:
        json.dump(data, f)
        
    print(f"[*] Hardware: CPU={cpu}% | Uptime={uptime} | Services={services}")
    push_to_gist(data)

if __name__ == "__main__":
    print("==================================================")
    print(" BLUE-SKIES HARDWARE TELEMETRY BRIDGE (OS-AGNOSTIC) ")
    print("==================================================")
    while True:
        try:
            get_telemetry()
        except Exception as e:
            print(f"[CRITICAL ERROR]: {e}")
        time.sleep(30)
