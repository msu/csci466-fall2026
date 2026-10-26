import socket
import threading
import sys


def handle_client(client_socket, client_address):
    """
    Each connected client gets its own thread.
    This thread receives two numbers, adds them,
    and sends the result back to the client.
    """

    print(f"Client {client_address} connected.")

    try:
        while True:

            # Wait for data from this client
            data = client_socket.recv(1024)

            # An empty response means the client disconnected
            if not data:
                break

            message = data.decode().strip()

            # Client wants to disconnect
            if message == "/exit":
                break

            # Expect two integers separated by a space
            try:
                numbers = message.split()

                num1 = int(numbers[0])
                num2 = int(numbers[1])

                result = num1 + num2

                print(f"{client_address}: {num1} + {num2} = {result}")

                # Send the result back to this client
                client_socket.sendall(
                    (str(result) + "\n").encode()
                )

            except (ValueError, IndexError):
                client_socket.sendall(
                    b"ERROR: Please send two integers.\n"
                )

    except ConnectionResetError:
        print(f"Client {client_address} reset the connection.")

    finally:
        client_socket.close()
        print(f"Client {client_address} disconnected.")


def main():

    if len(sys.argv) != 2:
        print("Usage: python server.py <port>")
        return

    port = int(sys.argv[1])

    # Get the server's hostname and IP address
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    # Create TCP socket
    server_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server_socket.bind((ip_address, port))

    server_socket.listen()

    print(f"Server listening on {ip_address}:{port}")

    # Main thread continuously accepts new clients
    while True:

        client_socket, client_address = server_socket.accept()

        # Create a separate thread for this client
        thread = threading.Thread(
            target=handle_client,
            args=(client_socket, client_address)
        )

        thread.start()


if __name__ == "__main__":
    main()