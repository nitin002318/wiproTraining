#biggest of 2 number
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

if num1 == num2:
    print("both are equal")
elif num1 > num2 :
    print(num1 ,"is big")
else:
    print(num2," is big")



# biggest from 3
num1 = int(input("Enter 1st number "))
num2 = int(input("Enter 2nd number"))
num3 = int(input("Enter 3rd number"))
if num1==num2 and num2==num3:
    print(("All equals"))
elif num2 >num1 and num2>num3:
    print(num2)
elif num1>num2 and num1>num3:
    print(num1)
elif num3>num1 and num3>num2:
    print(num3)

# Area of square
#
# side=input("Enter side")
# print(side*side)