import socket
import pickle
import time

class Packet():

    def __init__(self, sequence, message):
        self.sequence = sequence
        self.message = message

    def set_message(self, new_message):
        self.message = new_messsage

    def get_sequence(self):
        return self.sequence

    def get_message(self):
        return this.message

def main():

    packet_list = []
    for i in range(3):
        ob = Packet(i+1, "Hi " + str(i))
        packet_list.append(ob)
    
    packet_list.append(Packet(4, "FIN"))

    port = 6001
    host = socket.gethostname()

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect( (host, port) )

    for each_packet in packet_list:
        data = pickle.dumps(each_packet)
        clientSocket.send(data)
        print("Sending",each_packet.get_sequence())
        time.sleep(1)
    
    print("Client done")

if __name__ == "__main__":
    main()