import nmap

def scan_network(network_range):
    scanner = nmap.PortScanner()
    print(f"Scanning network: {network_range}...")
    
    scanner.scan(hosts=network_range, arguments="-sn")  # -sn means ping scan (no port scanning)

    devices = []
    for host in scanner.all_hosts():
        device_info = {
            "IP": host,
            "MAC": scanner[host]["addresses"].get("mac", "Unknown"),
            "Status": scanner[host].state()
        }
        devices.append(device_info)
    
    return devices

if __name__ == "__main__":
    network = input("Enter your network range (e.g., 192.168.1.0/24): ")
    results = scan_network(network)

    print("\nDevices found:")
    for device in results:
        print(f"IP: {device['IP']}, MAC: {device['MAC']}, Status: {device['Status']}")
