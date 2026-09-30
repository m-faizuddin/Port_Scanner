
import argparse  # Lets the user provide the target, ports, and timeout through the terminal.
import sys # Used to stop the program when an error occurs.


from colorama import Fore, Style, init as colorama_init  # Used to make the output colorful.

from scanner.core import scan_ports #Imports our function that scans multiple ports. 
from scanner.ports import parse_ports #Converts the user's port input into a list of integers. 


# Initialize colorama to enable colored output in the terminal.
colorama_init(autoreset=True)  


# Creates and configures the command-line argument parser
def build_parser():
    parser = argparse.ArgumentParser(
        prog = "mini-nmap",
        description = "A lightweight educational port scanner."
    )

    parser.add_argument(
        "--target",
        required = True,
        help="IP address or hostname to scan (e.g. 192.168.1.10)"
    )

    parser.add_argument(
        "--ports",
        required = True,
        help="Ports to scan: single (80), range (1-1000), or list (80, 443, 22)"
    )

    parser.add_argument(
        "--timeout",
        type = float,
        default = 0.5,
        help="Seconds to wait per port before marking it closed (default: 0.5)" 
    )


    #Give the finished parser back
    return parser



# #Temporary Test 
# my_parser = build_parser()
# print(my_parser)

# Main function that controls the overall flow of the program.
def main():

    # Build the command-line parser with the arguments we defined above.
    parser = build_parser() 

    # Read the user's command-line input and organize it into args.
    args = parser.parse_args() 

    # # Temporary test to see what parse_args() gives us.
    # print(args)

    # Try to convert the user's port input into a list of integers.
    try:
        ports = parse_ports(args.ports)

    # If the port input is invalid, show the error and stop the program.
    except ValueError as e:
        print(f"Error parsing --ports: {e}", file=sys.stderr)
        sys.exit(1)

    # Show what target is being scanned and how many ports will be checked.
    print(f"\nScanning {args.target} ({len(ports)} port(s))...")
    print("-" * 34)

    # Try to scan the target using the ports and timeout provided.
    try:
        results = scan_ports(args.target, ports, timeout=args.timeout)
    # If the target cannot be resolved, show the error and stop the program.
    except ValueError as e: 
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    #Create an empty list to store only the open ports.
    open_ports = []

    #Go through each port and its True/False scan result. 
    for port, is_open in results.items():

        #If the port is open, add it to the open_ports list. 
        if is_open:
            open_ports.append(port)

    #Go through each port that the user asked to scan. 
    for port in ports: 

        #Check the result for the current port
        if results[port]:
            status = f"{Fore.GREEN}OPEN{Style.RESET_ALL}"
        else:
            status = f"{Fore.RED}closed{Style.RESET_ALL}"

        # Display the port number and its status.
        print(f"Port {port:<6} -> {status}")

    # Print a line after all port results.
    print("-" * 34)

    #Show how many open ports were found.
    print(f"Scan complete. {len(open_ports)} open port(s) found.\n")


#Run main() only when this file is executed directly. 
if __name__ == "__main__":
    main() 