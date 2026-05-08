while True:
    try:
        num1=float(input("Enter the First number"))
        num2=float(input("Enter the second number"))
        res=num1/num2
    except ZeroDivisionError:
        print("You can not enter the zero")
    except ValueError:
        print("Please enter the correct data type")

    else:
        print(res)
        break