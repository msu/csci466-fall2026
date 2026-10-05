import socket   
import pickle
class Packet():

    def __init__(self, sequence, message):
        self.sequence = sequence
        self.message = message

    def set_message(self, new_message):
        self.message = new_messsage

    def get_sequence(self):
        return self.sequence

    def get_message(self):
        return self.message

def main():

    port = 6001
    host = socket.gethostname()
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind( (host, port) )
    print("Server is listening")

    serverSocket.listen(1)

    connection, addr = serverSocket.accept();

    while(True):
        data = connection.recv(1024)

        ob = pickle.loads(data)

        print(ob.get_sequence())

        if ob.get_message() == "FIN":
            break

if __name__ == "__main__":
    main()