text=input("Enter the content of the file ")
f=open("new.txt","w")
f.write(text)
print("Text added to the file")

f=open("new.txt","r")
print(f.read())
