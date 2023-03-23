# Server Side
from socket import *
from constants import *


def store_file (filename, data) :
    absolute_path = "Server_Data/" + filename + ".txt"
    file = open(absolute_path, "w")

    file.write(data);

    file.close()


def server_main () :
    IP = gethostbyname(gethostname())
    PORT = get_server_port()
    FORMAT = get_format()
    SIZE = get_size()

    # Eastablish TCP Connection
    server = socket(AF_INET, SOCK_STREAM)

    print("Server is UP and RUNNING")

    ADDR = get_server_addr(IP, PORT)
    server.bind(ADDR)

    # This is the welcoming socket
    server.listen()
    print("Server is LISTENING")


    while True :
        connection_socket, client_addr = server.accept()
        print("NEW CONNECTION: " + str(client_addr[0] )+ " CONNECTED")

        filename = connection_socket.recv(SIZE).decode(FORMAT)

        # Error: Crashes when there are multiple files
        print("File was RECEIVED")
        connection_socket.send("File was RECEIVED.".encode(FORMAT))

        data = connection_socket.recv(SIZE).decode(FORMAT)
        print("Content was RECEIVED\n",data)
        connection_socket.send("File Data was RECEIVED.".encode(FORMAT))

        store_file(filename, data)


        connection_socket.close()
        print("CONNECTION: " + str(client_addr[0] )+ " DISCONNECTED")
        quit()

        