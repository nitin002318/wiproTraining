grade= input("Enter the grade").upper()
match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case "D":
        print("Bad")
    case "E":
        print("Very Bad")
    case _:
        print("Invaid input")

