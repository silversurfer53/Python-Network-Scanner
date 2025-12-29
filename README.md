# Multi-Threaded Network Port Scanner (Python)

## 📌 Project Overview
This project is a high-performance network reconnaissance tool developed in Python. It identifies open TCP ports on a target IP address and attempts to perform **banner grabbing** to identify the services/versions running on those ports.

To solve the bottleneck of sequential scanning, I implemented **multi-threading**, allowing the script to scan multiple ports simultaneously, significantly reducing the time required for network discovery.



## 🛠 Features
* **TCP Port Scanning:** Checks for open ports using the `socket` library.
* **Multi-threading:** Utilizes the `threading` module to handle 100+ ports at once.
* **Banner Grabbing:** Attempts to capture service information (e.g., SSH, HTTP, FTP versions).
* **Customizable Range:** Easily adjustable port ranges and target IPs.

## 🚀 How It Works
1.  **Socket Connection:** The script initiates a TCP 3-way handshake (`SYN`, `SYN-ACK`, `ACK`).
2.  **Concurrency:** Instead of waiting for Port 1 to finish before checking Port 2, the script spawns a new thread for every port in the range.
3.  **Result Handling:** If a connection is successful (result code `0`), the port is flagged as OPEN.

## 💻 Installation & Usage
### Prerequisites
* Python 3.x installed
* Git

### Setup
```bash
# Clone the repository
git clone [https://github.com/silversurfer53/Python-Network-Scanner.git](https://github.com/silversurfer53/Python-Network-Scanner.git)

# Enter the directory
cd Python-Network-Scanner

# Run the scanner
python scanner.py
