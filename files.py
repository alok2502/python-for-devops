import os

folders = input("Enter name of folder saparated by a space : ").split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Folder " + folder + " not found")
        continue
    print("-----------Listing files for folder " +folder+ "---------------")
    for i in files:
        print(i)
