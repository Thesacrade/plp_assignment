with open("my file.txt", "r") as f:
    content = f.read()
    
with open("my file.txt","a") as f1:
    f1.write("\n Python is a general purpose programming language")

file_name = input("Enter the name of the file to be opened ")
try:
    with open(file_name, "r") as f2:
        f2.read()
except FileNotFoundError:
    print("The specified file can not be found")