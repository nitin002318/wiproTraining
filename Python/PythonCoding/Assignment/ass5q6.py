file=input("Enter the file name ")

try:
    with open(file,"r") as f:
        content=f.read()
        print(content)
except:
    print("There is no file ")