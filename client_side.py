# Client Side
from socket import *
from constants import *

def read_file (filepath) :
    file = open(filepath, "r")
    data = file.read()

    file.close()

    return data

def send_file (filename) :
    IP = gethostbyname(gethostname())
    PORT = get_server_port()
    FORMAT = get_format()
    SIZE = get_size()

    # Eastablish TCP Connection
    client = socket(AF_INET, SOCK_STREAM)

    ADDR = get_server_addr(IP, PORT)
    client.connect(ADDR)

    print("Connection Eastablished")

    # Todo: The folder names should be changed based on the folder that the user wants
    absolute_filepath = "Client_Data/" + filename + ".txt"
    relative_filepath =  filename + ".txt"

    data = read_file(absolute_filepath)
    client.send(filename.encode(FORMAT))
    
    recv_file_msg = client.recv(SIZE).decode(FORMAT)
    print("From SERVER: ", recv_file_msg)

    client.send(data.encode(FORMAT))

    recv_data_msg = client.recv(SIZE).decode(FORMAT)
    print("From SERVER: ", recv_data_msg)

    print("Closing connection")
    print("Ending Communication")
    client.close()