import os

def list_files_in_folders(folders):
    for folder in folders:
        try:
            files = os.listdir(folder)
        except FileNotFoundError:
            print("Folder " + folder + " not found")
            continue
        print("-----------Listing files for folder " +folder+ "---------------")
        for i in files:
            print(i)
            
if __name__ == "__main__":
    folders = input("Enter name of folder saparated by a space : ").split()
    list_files_in_folders(folders)
