file = open("new.txt","r")
lines=0
words=0
char=0
for line in file:
    lines = lines+1
    words= words+len(line.split())
    char=char+len(line)

print("Lines",lines)
print("Words" ,words)
print("Characters", char)

file.close()