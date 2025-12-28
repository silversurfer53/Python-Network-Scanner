import socket
import threading # This allows us to do many things at once

def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        s.close()
    except:
        pass

target = "8.8.8.8"
# We are going to scan the top 100 ports instead of just a few
ports = range(1, 101) 

print(f"Scanning {target} with Multi-threading...")

# This loop starts a new 'thread' for every port
for port in ports:
    thread = threading.Thread(target=scan_port, args=(target, port))
    thread.start()