import socket
import sys


def main():

    if len(sys.argv) != 3:
        print("Usage: python client.py <server_port> <source_port>")
        return

    server_port = int(sys.argv[1])
    source_port = int(sys.argv[2])

    # Get hostname and IP address
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    # Create TCP socket
    client_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    # Explicitly bind the client's source port
    client_socket.bind((ip_address, source_port))

    # Connect to the server
    client_socket.connect((ip_address, server_port))

    print("Connected to addition server!")
    print("Type /exit to disconnect.")

    try:
        while True:

            first = input("\nEnter first integer: ")

            if first == "/exit":
                break

            second = input("Enter second integer: ")

            if second == "/exit":
                break

            # Send both numbers in one message
            message = first + " " + second + "\n"

            client_socket.sendall(message.encode())

            # Wait for the result
            data = client_socket.recv(1024)

            if not data:
                print("Server disconnected.")
                break

            print("Result:", data.decode().strip())

    finally:
        # Notify server that the client is leaving
        try:
            client_socket.sendall(b"/exit\n")
        except OSError:
            pass

        client_socket.close()

        print("Disconnected from server.")


if __name__ == "__main__":
    main()