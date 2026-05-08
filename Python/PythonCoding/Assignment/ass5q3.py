source=open("new.txt","r")

destination = open("destination.txt","w")
data = source.read()

destination.write(data)
source.close()
destination.close()