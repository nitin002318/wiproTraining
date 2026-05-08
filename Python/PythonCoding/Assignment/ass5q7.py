try:
    num1=int(input("Enter the first number"))
    num2=int(input("Enter the Second number"))
    ans=num1/num2
except ZeroDivisionError:
    print("Can not devide by Zero")
except ValueError:
    print("Enter the correct value")
else:
    print(ans)