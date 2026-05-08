class NegativeNumberError(Exception):
     pass
try:
    num=int(input("Enter the number "))
    if num<0:
        raise NegativeNumberError("Negative number is not allowed")
    print("Number is ", num)
except NegativeNumberError:
    print("You entered the negative number ")