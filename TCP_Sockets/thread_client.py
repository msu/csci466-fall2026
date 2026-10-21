
import socket
import sys

#python client.py 8000 9001
def main():

    if len(sys.argv != 3):
        print("usage: python client.py <server> <source port>")
        return
    
    server_port = int(sys.argv[1])
    source_port = int(sys.argv[2])

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.bind(ip_address, source_port)

    client_socket.connect(ip_address, server_port)

    print("Connected to server!")
    print("Type /exit to disconnect")

    try:

        while True:

            first = input("Enter first integer: ")

            if first == "/exit":
                break

            second = input("Enter seconds integer: ")

            if second == "/exit":
                break
            
            message = first + " " + second "\n"

            client_socket.sendall(message)

            data = client_socket.recv(1024)

            if not data:
                print("Server disconnected")
                break
            
            print("Result: data.decode().strip()")
    
    finally:
        client_socket.sendall("/exit".encode())
        client_socket.close()

        print("disconnected")


if __name__ == "__main__":
    main()