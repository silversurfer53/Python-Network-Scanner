import socket # The library used for network connections

def scan_port(ip, port):
    try:
        # Create a socket object (AF_INET = IPv4, SOCK_STREAM = TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout so it doesn't wait forever on closed ports
        s.settimeout(1)
        
        # Attempt to connect to the IP and Port
        result = s.connect_ex((ip, port)) # returns 0 if port is open
        
        if result == 0:
            print(f"[+] Port {port} is OPEN")
            # Try to "grab the banner" (get the software version)
            try:
                banner = s.recv(1024).decode().strip()
                print(f"    --> Banner: {banner}")
            except:
                print("    --> Banner: Could not retrieve")
        
        s.close()
    except Exception as e:
        pass

# Target configuration
target_ip = "127.0.0.1" # Start by scanning your own machine (localhost)
ports_to_scan = [21, 22, 80, 443, 3389]

print(f"Starting scan on {target_ip}...")
for port in ports_to_scan:
    scan_port(target_ip, port)
print("Scan complete.")