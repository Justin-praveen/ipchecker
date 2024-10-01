import ipaddress
import argparse




# ANSI escape code for red
RED = "\033[91m"
RESET = "\033[0m"

def show_banner():
    banner = f"""
    {RED}==================================
          IP Checker CLI Tool
           by Your Name Here
    ==================================
      Find out if an IP is public or private!
    {RESET}
    """
    print(banner)


def check_ip_type(ip):
    try:
        # Parse the IP address
        ip_obj = ipaddress.ip_address(ip)
        
        # Check if the IP is private
        if ip_obj.is_private:
            return f"{ip} is a **private** IP address."
        else:
            return f"{ip} is a **public** IP address."
    
    except ValueError:
        return f"{ip} is not a valid IP address."

def main():

    show_banner()
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Check if an IP address is private or public.")
    
    # Add IP address argument
    parser.add_argument("ip", help="The IP address to check.")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Check if the IP is private or public
    result = check_ip_type(args.ip)
    print(result)

if __name__ == "__main__":
    main()
