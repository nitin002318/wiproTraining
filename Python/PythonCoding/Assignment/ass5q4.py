text= input("Enter the content that you want to add")
f=open("log.txt","a")
f.write(text+"\n")

file=open("log.txt","r")
content=file.read()
print(content)