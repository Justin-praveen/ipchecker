import ipaddress
import argparse

# ANSI escape code for red
RED = "\033[91m"
RESET = "\033[0m"

def show_banner():
    banner = f"""
    {RED}==================================
          IP Checker CLI Tool
           by Justin-Praveen
    ==================================
      Find out if an IP is public or private!
      Also identifies the IP class (A, B, C, D, E).
    {RESET}
    """
    print(banner)

def get_ip_class(ip_obj):
    """Determine the IP class based on the first octet."""
    first_octet = int(str(ip_obj).split('.')[0])

    if 1 <= first_octet <= 126:
        return "Class A"
    elif 128 <= first_octet <= 191:
        return "Class B"
    elif 192 <= first_octet <= 223:
        return "Class C"
    elif 224 <= first_octet <= 239:
        return "Class D (Multicast)"
    elif 240 <= first_octet <= 255:
        return "Class E (Experimental)"
    else:
        return "Unknown Class"

def check_ip_type(ip):
    try:
        # Parse the IP address
        ip_obj = ipaddress.ip_address(ip)
        
        # Determine if it's private or public
        if ip_obj.is_private:
            ip_type = f"{ip} is a **private** IP address."
        else:
            ip_type = f"{ip} is a **public** IP address."
        
        # Get the class of the IP address
        ip_class = get_ip_class(ip_obj)
        
        return f"{ip_type} It belongs to {ip_class}."
    
    except ValueError:
        return f"{ip} is not a valid IP address."

def main():

    show_banner()
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Check if an IP address is private or public and determine its class.")
    
    # Add IP address argument
    parser.add_argument("ip", help="The IP address to check.")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Check if the IP is private or public and find its class
    result = check_ip_type(args.ip)
    print(result)

if __name__ == "__main__":
    main()
