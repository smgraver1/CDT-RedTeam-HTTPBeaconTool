# CDT Red Team HTTP Beacon Tool
# Stephen Graver
# Event 3
# 1/3/2026

**Category:** Beacon or Callback Tool   
**Target Environment:** Python 3

## 1. Overview
This is a custom Red Team command-and-control (C2) beacon designed to bypass basic network security monitoring. It utilizes standard HTTP/1.1 traffic to check in with a listener, retrieve commands, and exfiltrate data. 

Unlike standard "noisy" reverse shells, Phantasm focuses on **stealth and persistence** by mimicking legitimate web traffic and utilizing randomized check-in intervals to defeat timing-based anomaly detection.

### Key Features
* **Time Jitter:** Implements a randomized sleep interval to break the "heartbeat" signature.
* **Traffic Obfuscation:** All command-and-control communication is Base64 encoded to evade string-matching IDS/IPS rules.
* **Modular Command Execution:** Supports any shell command supported by the target OS.
* **Stateless C2:** The server-side is built on Flask, providing a lightweight, scalable listener.

## 2. Requirements & Dependencies
### Server (C2)
* **OS:** Linux recommended
* **Language:** Python 3
* **Dependencies:** `Flask`
* **Installation:** `pip install flask`

### Target (Beacon)
* **OS:** Windows or Linux
* **Language:** Python 3
* **Dependencies:** `requests`
* **Installation:** `pip install requests`

## 3. Installation Instructions

### Step 1: Deploy the C2 Server
1. Clone the repository to your Red Team infrastructure.
2. Install Flask: `pip install flask`
3. Launch the listener:
   ```bash
   python3 server.py