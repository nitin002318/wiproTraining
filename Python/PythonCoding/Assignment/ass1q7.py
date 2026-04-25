color= input("Enter a traffic light colour").lower()
match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Ready")
    case "green":
        print("Go")
    case _:
        print("Wrong input")
