import nmap
import sqlite3
import tkinter as tk
from tkinter import messagebox, scrolledtext
import socket
import netifaces

# 🔹 Detects the current IP range
def get_network_range():
    try:
        iface = netifaces.gateways()['default'][netifaces.AF_INET][1]
        ip = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']
        subnet = "24"  # Assuming default subnet /24
        network_range = f"{ip.rsplit('.', 1)[0]}.0/{subnet}"
        return network_range
    except Exception as e:
        return "192.168.1.0/24"  # Default fallback

# 🔹 Initialize SQLite Database
def init_db():
    conn = sqlite3.connect("trusted_devices.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS trusted_devices (
            mac TEXT PRIMARY KEY,
            name TEXT
        )
    """)
    conn.commit()
    conn.close()

# 🔹 Get trusted devices from database
def get_trusted_devices():
    conn = sqlite3.connect("trusted_devices.db")
    cursor = conn.cursor()
    cursor.execute("SELECT mac, name FROM trusted_devices")
    devices = {row[0]: row[1] for row in cursor.fetchall()}
    conn.close()
    return devices

# 🔹 Add a trusted device to the database
def add_trusted_device():
    mac = mac_entry.get().strip().upper()
    name = name_entry.get().strip()

    if not mac or not name:
        messagebox.showerror("Error", "Both MAC Address and Name are required!")
        return

    conn = sqlite3.connect("trusted_devices.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO trusted_devices (mac, name) VALUES (?, ?)", (mac, name))
        conn.commit()
        messagebox.showinfo("Success", f"Added {name} ({mac}) to trusted devices.")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "This MAC address is already trusted!")
    conn.close()

# 🔹 Scan network and check for unknown devices
def scan_network():
    network = network_label.cget("text").split(": ")[1]  # Get detected network
    scanner = nmap.PortScanner()
    try:
        scanner.scan(hosts=network, arguments="-sn")
        results_text.delete("1.0", tk.END)
        unknown_devices = []
        trusted_devices = get_trusted_devices()

        for host in scanner.all_hosts():
            mac = scanner[host]['addresses'].get('mac', 'Unknown MAC').upper()
            device_name = trusted_devices.get(mac, "Unknown Device")
            results_text.insert(tk.END, f"Device: {host} - {device_name} ({mac})\n")

            if device_name == "Unknown Device":
                unknown_devices.append(f"{host} ({mac})")

        if unknown_devices:
            alert_message = "⚠️ Unknown Devices Found:\n" + "\n".join(unknown_devices)
            messagebox.showwarning("Alert!", alert_message)

    except Exception as e:
        messagebox.showerror("Error", f"Scan failed: {e}")

# 🔹 GUI Setup
root = tk.Tk()
root.title("Advanced Network Scanner")
root.geometry("600x500")  # Set window size

# Main Frame
main_frame = tk.Frame(root, padx=10, pady=10)
main_frame.pack(padx=20, pady=20)

# Network Range
network_label = tk.Label(main_frame, text=f"Detected Network: {get_network_range()}", font=("Arial", 12))
network_label.grid(row=0, column=0, pady=5)

# Scan Button
scan_button = tk.Button(main_frame, text="Scan Network", command=scan_network, font=("Arial", 12), bg="blue", fg="white")
scan_button.grid(row=1, column=0, pady=5)

# Results Display
results_text = scrolledtext.ScrolledText(main_frame, width=50, height=15, font=("Arial", 10))
results_text.grid(row=2, column=0, pady=10)

# Trusted Device Section
trusted_device_frame = tk.LabelFrame(main_frame, text="Add Trusted Device", font=("Arial", 12), padx=10, pady=10)
trusted_device_frame.grid(row=3, column=0, pady=10, sticky="w")

# MAC Address
mac_label = tk.Label(trusted_device_frame, text="MAC Address:", font=("Arial", 10))
mac_label.grid(row=0, column=0, padx=5, pady=5)
mac_entry = tk.Entry(trusted_device_frame, width=30, font=("Arial", 10))
mac_entry.grid(row=0, column=1, padx=5, pady=5)

# Device Name
name_label = tk.Label(trusted_device_frame, text="Device Name:", font=("Arial", 10))
name_label.grid(row=1, column=0, padx=5, pady=5)
name_entry = tk.Entry(trusted_device_frame, width=30, font=("Arial", 10))
name_entry.grid(row=1, column=1, padx=5, pady=5)

# Add Trusted Device Button
add_button = tk.Button(trusted_device_frame, text="Add Trusted Device", command=add_trusted_device, font=("Arial", 12), bg="green", fg="white")
add_button.grid(row=2, column=0, columnspan=2, pady=10)

# Status Bar
status_label = tk.Label(root, text="Ready", font=("Arial", 10), relief="sunken", anchor="w", padx=5)
status_label.pack(fill=tk.X, side=tk.BOTTOM)

# Initialize database
init_db()

root.mainloop()
