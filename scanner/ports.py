"""
80

1-1000

22, 80, 443
"""


def parse_ports(port_spec: str) -> list[int]:

    # Remove spaces from the beginning and end of the input.
    port_spec = port_spec.strip()

    # CASE 1: The user entered a range, such as "1-1000".
    if "-" in port_spec:
        
        # Separate the starting port and ending port.
        start_str, end_str = port_spec.split("-", 1)

        # Convert them from strings into integers.
        start = int(start_str)
        end = int(end_str)

        # Make sure the port range is valid.
        if start < 1 or end > 65535 or start > end:
            raise ValueError(f"Invalid port range: {port_spec}")

        # Create an empty list for the ports.
        ports = []

        # Go through every number in the range.
        for port in range(start, end + 1):
            ports.append(port)

        # Return the completed list.
        return ports

    # CASE 2: The user entered multiple ports, such as "22, 80, 443".
    if "," in port_spec:

        # Split the string wherever there is a comma.
        port_strings = port_spec.split(",")

        # Create an empty list for the ports.
        ports = []

        # Go through each port one at a time.
        for p in port_strings:

            # Remove extra spaces.
            p = p.strip()

            # Convert the port from a string into an integer.
            port = int(p)

            # Add the integer to the list.
            ports.append(port)

        # Return the completed list.
        return ports

    # CASE 3: The user entered one port, such as "80".
    port = int(port_spec)

    # Return the single port inside a list.
    return [port]