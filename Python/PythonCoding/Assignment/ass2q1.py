fruit=["Apple","Banana","Orange","Mongo"]
print("Orignal",fruit)

# add 2 fruit
fruit.append("Grapes")
fruit.append("Kiwi")

# remove fruit
fruit.remove("Banana")
print(fruit)

#Access 2nd and 4th fruit

print(fruit[1])
print(fruit[3])

#Print 3 fruit
print(fruit[:3])

#length
print(len(fruit))