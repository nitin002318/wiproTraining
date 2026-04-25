word=input("Enter")
count=0
for char in word:
    if char.lower() in ("aeiou"):
        count += 1
print(count)