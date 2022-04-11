import socket


def netcat(hostname, port, content):
    """
    Send a message to a server and receive its response.

    Args:
        hostname (str): The hostname or IP address of the server to connect to.
        port (int): The port number to connect to.
        content (str): The message to send to the server.

    Returns:
        str: The server's response.

    Raises:
        ConnectionError: If there is an issue with the network connection.
        Exception: If an unexpected error occurs.
    """
    response = []
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
            conn.connect((hostname, port))
            conn.sendall(content.encode())
            conn.shutdown(socket.SHUT_WR)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                response.append(data.decode())
    except socket.error as e:
        raise ConnectionError(f"Socket error: {e}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")

    full_response = "".join(response)
    print("Server response:")
    print(full_response)
    print("Connection closed.")
    return full_response


if __name__ == "__main__":
    netcat()
