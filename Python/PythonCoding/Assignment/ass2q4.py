person={
    "name":"Karan",
    "age":23,
    "hobby":"Playing"
}
print(person)
print(person["name"])

person["Food"]="Pizza"
person["hobby"]="Singing"

print(person)

print(person.keys())
print(person.values())

person.pop("age")

print(person)