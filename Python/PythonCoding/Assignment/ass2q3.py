color={"Pink","Yellow","Blue","Green","Brown"}
print(color)

# Add new color
color.add("White")
print(color)
color.remove("Blue")
print("Updated color",color)

color2={"Green","Pink","Gray"}

# operation
print("Union",color|color2)
print("Intersection",color&color2)
print("Diffrence",color-color2)

color_to_check="Pink"
if color_to_check in color:
    print("The color is in the set ")
else:
    print("Not in the set")