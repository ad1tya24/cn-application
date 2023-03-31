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
        print("Files and directories in '" + str(folder) + "' :")

        for file in dir_list :
            print(file)

        user_filename=input("Enter the file name: ")
        
        def find_file(filename, search_path):
            for root, dir, files in os.walk(search_path):
                for file in files:
                    if file.startswith(filename):
                        return os.path.join(root, file)
            return None
        result = find_file(user_filename, os.getcwd() + "/" + folder)
        if result:
            print(f"Found {result}")
        else:
            print(f"{user_filename} not found")

        nope, file_extension = os.path.splitext(result)
        
        # file_exist = does_file_exist()
        # print(folder)
        # print(user_filename)
        # print(file_extension)

        dest_folder=input("Enter the file destination folder: ")

        if (user_filename != "") :
            send_file(folder, user_filename, file_extension, dest_folder)
            print("File sent to", dest_folder)
        else :
            quit()


