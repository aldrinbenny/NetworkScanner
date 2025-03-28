# Network Scanner and Trusted Device Manager

## Description

**Network Scanner and Trusted Device Manager** is a Python-based tool that helps users scan their local network and detect all connected devices. It provides an easy-to-use GUI interface and displays the devices' IP addresses and hostnames. Additionally, users can mark certain devices as "trusted," and the tool will remember them for future scans. This is particularly useful for users who want to monitor their home or office network for unauthorized devices.

The tool uses the powerful `nmap` for network scanning and stores trusted devices in a lightweight **SQLite database**.

## Features

- Scan your local network and display connected devices.
- Automatically detect your local IP range.
- Identify devices by their IP address and hostname.
- Mark devices as **trusted** and store them in a local database.
- Simple GUI interface, designed for both technical and non-technical users.
- Export and manage your trusted devices list.
  
## Installation

To get started with **Network Scanner and Trusted Device Manager**, follow these steps to install the necessary dependencies and run the program.

### Prerequisites

Make sure you have the following installed on your system:

- Python (version 3.6 or higher) - [Download Python](https://www.python.org/downloads/)
- [Nmap](https://nmap.org/) - A powerful network scanning tool.
  - For Windows, make sure to add Nmap to your system `PATH`.

### Install Dependencies

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/NetworkScanner.git
    cd NetworkScanner
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # For Windows
    source venv/bin/activate # For macOS/Linux
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

   The `requirements.txt` includes all the necessary libraries for this project. It includes:

   - `nmap`: To scan the local network.
   - `netifaces`: To detect the local network interfaces and IP address range.
   - `tkinter`: For the GUI interface.
   - `sqlite3`: For managing the trusted device database.

### Usage

1. Once you have installed the dependencies, run the application:

    ```bash
    python network_gui.py
    ```

2. The program will open the graphical user interface. You will be prompted to input your network range (e.g., `192.168.1.0/24`). This will start the network scanning process.

3. The program will list all the devices connected to your network. You can click on "Mark as Trusted" for devices you recognize and want to store for future reference.

4. All trusted devices are stored locally in an SQLite database, so the program will remember them during future scans.

### How It Works

- The program uses **nmap** to scan the local network for all connected devices. It detects devices using IP addresses and hostnames.
- **SQLite** is used to store trusted devices locally on your computer.
- The user interacts with the program using a simple **Tkinter GUI**.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

We welcome contributions to this project. If you'd like to help improve the tool, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -am 'Add your feature'`).
4. Push to your branch (`git push origin feature/your-feature`).
5. Open a pull request on GitHub.

### Issues

If you encounter any bugs or have any questions, please open an issue on the repository.

---

## Example of Scanning

After launching the program, you can enter your network range (e.g., `192.168.1.0/24`), and the program will scan all devices connected to that range. Here's a simple output:


