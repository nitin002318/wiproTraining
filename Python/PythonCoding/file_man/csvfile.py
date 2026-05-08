import csv
import os

'''
empid,enam
101,AAA
102,BBB
'''

def wirte_csv(filename):
    data={
        {"name":"Karan","age":23},
        {"name": "Raman", "age": 33}
    }
    columnname=["name","age"]
    with open(filename,"w", newline ="\n") as file:
        writer = csv.DictWriter(file,filename=columnname)
        writer.writeheader()
        writer.writerows(data)
def write_csv(filename):
    with open(filename,"r",newline ="\n") as file:
        reader=csv.DictReader(file)
        for row in reader 
filename = "myfile.csv"
wirte_csv(filename)