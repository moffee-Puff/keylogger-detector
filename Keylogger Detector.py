import psutil
import os

# Function to detect potential keyloggers
def detect_keyloggers():
    print("[*] Starting keylogger detection...\n")

    # Check running processes
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            process_name = proc.info['name'].lower()
            if "keylogger" in process_name:
                print(f"[!] Potential keylogger detected:\n"
                      f"    Process Name: {proc.info['name']}\n"
                      f"    PID: {proc.info['pid']}\n")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # Check network connections
    for conn in psutil.net_connections():
        if conn.status == 'ESTABLISHED' and conn.raddr:
            print(f"[!] Suspicious network connection detected:\n"
                  f"    Process Name: {psutil.Process(conn.pid).name()}\n"
                  f"    PID: {conn.pid}\n"
                  f"    Remote Address: {conn.raddr.ip}:{conn.raddr.port}\n")

    # Check for suspicious files
    suspicious_dirs = ["/usr/local/bin", "/tmp", "/var/tmp"]
    for dir_path in suspicious_dirs:
        for root, _, files in os.walk(dir_path):
            for file in files:
                if "keylogger" in file.lower():
                    file_path = os.path.join(root, file)
                    file_size = os.path.getsize(file_path) / 1024  # Size in KB
                    print(f"[!] Suspicious file detected:\n"
                          f"    File Path: {file_path}\n"
                          f"    File Size: {file_size:.2f} KB\n")

    print("[*] Scan complete. Check the results above.")

# Main function
def main():
    detect_keyloggers()

if __name__ == "__main__":
    main()
