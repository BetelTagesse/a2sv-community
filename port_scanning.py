
import nmap
import re

ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

port_min = 0
port_max = 65535

open_ports = []

while True:
	ip_add_entered = input("\nplease enter the ip adress that you want to scan:")
	if ip_add_pattern.search(ip_add_entered):
		print(f"{ip_add_entered} is a valid ip address")
		break
	
while True:
	print("Please enter the range of ports you want to scan in format: <int>-<int>")
 		port_range = input("Enter port range:")
		port_range_valid = port_range_pattern.search(port_range.replace("",""))
		if port_range_valid:
		    port_min =  int(port_range_valid.group(1))
		    port_max = int(port_range_valid.group(2))
		    break

 nm = nmap.PortScanner()

    for port in range(port_min, port_max + 1):
        try:
            result = nm.scan(ip_add_entered, str(port))
            port_status = result['scan'][ip_add_entered]['tcp'][port]['state']
            
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

  


# In this modified code:
# - The `scan_ports` function now categorizes each port as "open," "closed," or "filtered" based on the obtained port status from the `nmap` scan.
# - The results are printed accordingly.
# - The open ports are collected in the `open_ports` list and displayed at the end.

# This should provide you with a clear indication of the status of each scanned port.

        
