list=[1,23,1,3,1,5,7,45,65]
try:
    index =int(input("Enter the index value"))
except IndexError:
    print("You enter the wrong index")
else:
    print("Value is ",list[index])