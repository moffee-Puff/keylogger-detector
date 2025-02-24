# Keylogger Detector

A Python-based tool to detect potential keyloggers on your system by monitoring suspicious processes and activities. Built for Kali Linux, this tool helps identify unauthorized programs that may be capturing keystrokes.

---

## How It Works

The Keylogger Detector works by analyzing running processes and system activities to identify potential keyloggers. Here's how it functions:

1. **Process Monitoring**:
   - The tool scans all running processes on the system.
   - It checks for known keylogger signatures or suspicious behavior (e.g., processes with "keylogger" in their name).

2. **Network Activity Monitoring**:
   - The tool monitors network connections to detect processes sending data to external servers (a common behavior of keyloggers).

3. **File System Monitoring**:
   - The tool scans for suspicious files or directories commonly associated with keyloggers.

4. **Alert System**:
   - If a potential keylogger is detected, the tool alerts the user with details about the suspicious process or activity.

---

## How to Use

### Prerequisites
- Kali Linux (or any Linux distribution with Python 3).
- Python 3.x.
- The `psutil` library (install using `pip`).

### Installation

1. **Install Required Libraries**:
   ```bash
   sudo apt update
   sudo apt install python3-pip
   pip3 install psutil

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/keylogger-detector.git
  cd keylogger-detector

3. **Run the Script**:
   ```bash
   sudo python3 keylogger_detector.py

4. **Usage**:
  Run the script:
   ```bash
   sudo python3 keylogger_detector.py

The tool will start scanning your system for potential keyloggers.
If a suspicious process or activity is detected, the tool will display an alert with details.

Example Output:
```bash
$ sudo python3 keylogger_detector.py
[*] Starting keylogger detection...

[!] Potential keylogger detected:
    Process Name: evil_keylogger
    PID: 1234
    Network Connection: 192.168.1.100:8080

[!] Suspicious file detected:
    File Path: /usr/local/bin/keylogger.sh
    File Size: 1024 KB

[*] Scan complete. Check the results above.




