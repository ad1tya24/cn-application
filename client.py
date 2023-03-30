# Client Main Program
from client_side import send_file
import os

if __name__ == "__main__" :
    # client_main()
    print("File Transfer System")
    print("Move files from one location to the next")

    print("Please add your files to the Client_Data folder")
    print("Press Enter to exit file transfer")

    while True :
        folder=input("Enter the folder name: ")
        dir_list = os.listdir(os.getcwd() + "/" + folder)
        print("Files and directories in '", folder, "' :")
        print(dir_list)

        user_filename=input("Enter the file name: ")
        file_name, file_extension = os.path.splitext(user_filename)
        
        # file_exist = does_file_exist()
        print(folder)
        print(file_name)
        print(file_extension)

        dest_folder=input("Enter the file destination folder: ")
        print(dest_folder)

        if (file_name != "") :
            send_file(folder, file_name, file_extension, dest_folder)
        else :
            quit()


