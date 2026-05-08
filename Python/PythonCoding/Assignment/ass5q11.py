file =input("ENTER THE FILE Name")
try:
    f=open(file,"r")
    content=f.read()
    print("this is inside the file","\n",content)
except FileNotFoundError:
    print("THis file is not exist")
finally:
    print("Program completed")
