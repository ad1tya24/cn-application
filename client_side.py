# Client Side
from socket import *
from constants import *
import os
from cryptography.fernet import Fernet



def read_file(filepath) :
    file = open(filepath, "r")
    data = file.read()
    file.close()
    return data


def encrypt_data(key, data) :
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data


def send_file(folder, filename, file_extension, dest_folder) :
    IP = gethostbyname(gethostname())
    PORT = get_server_port()
    FORMAT = get_format()
    SIZE = get_size()

    # Eastablish TCP Connection
    client = socket(AF_INET, SOCK_STREAM)

    ADDR = get_server_addr(IP, PORT)
    client.connect(ADDR)

    print("Connection Established")

    # Todo: The folder names should be changed based on the folder that the user wants
    absolute_filepath =  os.getcwd() + "/" + folder + "/" + filename + file_extension
    relative_filepath =  folder + filename
    print("Absolute Path: ",absolute_filepath)

    data = read_file(absolute_filepath)
    key = Fernet.generate_key()

    # client.send(dest_folder.encode(FORMAT))
    # client.send(filename.encode(FORMAT))
    #client.send(file_extension.encode(FORMAT))

    client.send((dest_folder + ',' + filename + file_extension).encode(FORMAT))

    encrypted_data = encrypt_data(key, data)
    client.send(key + b',' + encrypted_data)

    # client.send(key)
    # client.send(encrypted_data)
    
    recv_file_msg = client.recv(SIZE).decode(FORMAT)
    print("From SERVER: ", recv_file_msg)

    client.send(data.encode(FORMAT))

    recv_data_msg = client.recv(SIZE).decode(FORMAT)
    print("From SERVER: ", recv_data_msg)

    print("Closing connection")
    print("Ending Communication")
    client.close()