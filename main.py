# #!/usr/bin/env python3
# #Use these commands in Kali to install required software:
# #  sudo apt install python3-pip
# #  pip install python-nmap

# # Import nmap so we can use it for the scan
# import nmap
# # We need to create regular expressions to ensure that the input is correctly formatted.
# import re

# # Regular Expression Pattern to recognise IPv4 addresses.
# ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
# # Regular Expression Pattern to extract the number of ports you want to scan. 
# # You have to specify <lowest_port_number>-<highest_port_number> (ex 10-100)
# port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
# # Initialising the port numbers, will be using the variables later on.
# port_min = 0
# port_max = 65535

# # This port scanner uses the Python nmap module.
# # You'll need to install the following to get it work on Linux:
# # Step 1: sudo apt install python3-pip
# # Step 2: pip install python-nmap



# open_ports = []
# # Ask user to input the ip address they want to scan.
# while True:
#     ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
#     if ip_add_pattern.search(ip_add_entered):
#         print(f"{ip_add_entered} is a valid ip address.")
#         break

# while True:
#     # You can scan 0-65535 ports. This scanner is basic and doesn't use multithreading so scanning 
#     # all the ports is not advised.
#     print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
#     port_range = input("Enter port range: ")
#     port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
#     if port_range_valid:
#         port_min = int(port_range_valid.group(1))
#         port_max = int(port_range_valid.group(2))
#         break

# nm = nmap.PortScanner()
# # We're looping over all of the ports in the specified range.
# for port in range(port_min, port_max + 1):
#     try:
#         # The result is quite interesting to look at. You may want to inspect the dictionary it returns. 
#         # It contains what was sent to the command line in addition to the port status we're after. 
#         # For in nmap for port 80 and ip 10.0.0.2 you'd run: nmap -oX - -p 89 -sV 10.0.0.2
#         result = nm.scan(ip_add_entered, str(port))
#         # Uncomment following line and look at dictionary
#         # print(result)
#         # We extract the port status from the returned object
#         port_status = (result['scan'][ip_add_entered]['tcp'][port]['state'])
#         print(f"Port {port} is {port_status}")
#     except:
#         # We cannot scan some ports and this ensures the program doesn't crash when we try to scan them.
#         print(f"Cannot scan port {port}.")
        



import nmap
import re

ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

port_min = 0
port_max = 65535

def get_ip_address():
    while True:
        ip_add_entered = input("\nPlease enter the IP address that you want to scan: ")
        if ip_add_pattern.search(ip_add_entered):
            print(f"{ip_add_entered} is a valid IP address.")
            return ip_add_entered

def get_port_range():
    while True:
        print("Please enter the range of ports you want to scan in the format: <int>-<int> (e.g., 60-120)")
        port_range = input("Enter port range: ")
        port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
        if port_range_valid:
            return int(port_range_valid.group(1)), int(port_range_valid.group(2))

def scan_ports(ip_address, port_range):
    nm = nmap.PortScanner()
    open_ports = []

    for port in range(port_range[0], port_range[1] + 1):
        try:
            result = nm.scan(ip_address, str(port))
            port_status = result['scan'][ip_address]['tcp'][port]['state']
            
            # Update output based on port status
            if port_status == 'open':
                print(f"Port {port} is open.")
                open_ports.append(port)
            elif port_status == 'closed':
                print(f"Port {port} is closed.")
            else:
                print(f"Port {port} is filtered.")

        except Exception as e:
            print(f"Cannot scan port {port}. Exception: {e}")

    return open_ports

if __name__ == "__main__":
    ip_address = get_ip_address()
    port_range = get_port_range()

    open_ports = scan_ports(ip_address, port_range)

    if open_ports:
        print(f"\nOpen ports: {open_ports}")
    else:
        print("\nNo open ports found.")


# In this modified code:
# - The `scan_ports` function now categorizes each port as "open," "closed," or "filtered" based on the obtained port status from the `nmap` scan.
# - The results are printed accordingly.
# - The open ports are collected in the `open_ports` list and displayed at the end.

# This should provide you with a clear indication of the status of each scanned port.
