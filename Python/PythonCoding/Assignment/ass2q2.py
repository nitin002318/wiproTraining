cities=("Delhi","Mumbai","Goa")
print("Tuple",cities)

# Access Fist and last
print("First city",cities[0])
print("Last city",cities[-1])

# Create another tuple
more_cities=("Pareis","London")

# Adding
all=cities + more_cities

# Unpacking

c1,c2,c3=cities
print((c1,c2,c3))