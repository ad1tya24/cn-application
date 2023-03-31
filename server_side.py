from socket import *
from constants import *
import os


def store_file (folder, filename, data) :
    absolute_path = os.getcwd() + "/" + folder + "/" + filename 
    file = open(absolute_path, "w")

    file.write(data);

    file.close()


def receive_file () :
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

    print()

    while True :
        connection_socket, client_addr = server.accept()
        print("NEW CONNECTION: " + str(client_addr[0] )+ " CONNECTED")

        # folder = connection_socket.recv(SIZE).decode(FORMAT)

        # filename = connection_socket.recv(SIZE).decode(FORMAT)
        folder_and_filename = connection_socket.recv(SIZE).decode(FORMAT)
        folder, filename = folder_and_filename.split(',')

        print("Folder was RECEIVED: ", folder)
        print("Filename was RECEIVED: ", filename)

        # Error: Crashes when there are multiple files
        print("File was RECEIVED")
        connection_socket.send("File and Folder RECEIVED.".encode(FORMAT))

        data = connection_socket.recv(SIZE).decode(FORMAT)
        print("Content was RECEIVED\n",data)
        connection_socket.send("File Data was RECEIVED.".encode(FORMAT))

        store_file(folder, filename, data)

        connection_socket.close()
        print("CONNECTION: " + str(client_addr[0] )+ " DISCONNECTED")
        print("+==============+==============+")

        