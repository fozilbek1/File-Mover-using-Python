import os

source = "test.txt"
destination = "/home/fozil/Programming/Python Projects/test.txt"

try:
    if os.path.exists(destination):
        print("there is already a file there!")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")