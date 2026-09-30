import socket


def scan_port(target: str, port: int, timeout: float = 0.5) -> bool:

    # Create an IPv4 TCP socket that we can use to attempt a connection.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Don't wait longer than the specified timeout for the network operation.
    sock.settimeout(timeout)

    # Try to make the connection, and handle any errors that occur.
    try:

        # Try to connect to this port on the target.
        # connect_ex() returns 0 if the connection succeeds.
        # Otherwise, it returns an error code.
        result = sock.connect_ex((target, port))

        # True if the connection succeeded, False otherwise.
        is_open = result == 0

        # Return whether the connection succeeded.
        return is_open

    except socket.gaierror:
        raise ValueError(f"Could not resolve target: {target}")
    except OSError:
        return False 
    finally: 
        sock.close() 


def scan_ports(target:str, ports:list[int], timeout:float = 0.5) -> dict[int, bool]:

    # Create an empty dictionary to store the results.
    results = {}

    # Go through each port one at a time.
    for port in ports:

        # Scan this port and store True or False in the dictionary.
        results[port] = scan_port(target, port, timeout)

    return results


# print(scan_ports("127.0.0.1", [22, 80, 443]))