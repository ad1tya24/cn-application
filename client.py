# Client Main Program
from client_side import send_file

if __name__ == "__main__" :
    # client_main()
    print("File Transfer System")
    print("Move files from one location to the next")

    print("Please add your files to the Client_Data folder")
    print("Press Enter to exit file transfer")

    while True :
        filename = input("Enter the name of the file :")
        # file_exist = does_file_exist()

        if (filename != "") :
            send_file(filename)
        else :
            quit()


