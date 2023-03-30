from socket import *
from constants import *
import os
from cryptography.fernet import Fernet


def store_file(folder, filename, data) :
    absolute_path = os.getcwd() + "/" + folder + "/" + filename 
    file = open(absolute_path, "w")
    file.write(data)
    file.close()


def decrypt_data(key, data):
    f = Fernet(key)
    decrypted_data = f.decrypt(data)
    return decrypted_data.decode()


def receive_file() :
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

        folder = connection_socket.recv(SIZE).decode(FORMAT)
        print("Folder was RECEIVED: ", folder)

        filename = connection_socket.recv(SIZE).decode(FORMAT)
        print("Filename was RECEIVED: ", filename)

        # Error: Crashes when there are multiple files
        print("File was RECEIVED")
        connection_socket.send("File was RECEIVED.".encode(FORMAT))

        key = connection_socket.recv(SIZE)
        data = connection_socket.recv(SIZE)

        print("Encrypted Key: ", key)
        print("Encrypted Data: ", data)

        decrypted_data = decrypt_data(key, data)

        print("Content was RECEIVED\n", decrypted_data)

        data = connection_socket.recv(SIZE).decode(FORMAT)

        connection_socket.send("File Data was RECEIVED.".encode(FORMAT))

        store_file(folder, filename, data)

        connection_socket.close()
        print("CONNECTION: " + str(client_addr[0] )+ " DISCONNECTED")
        print("+==============+==============+")

        