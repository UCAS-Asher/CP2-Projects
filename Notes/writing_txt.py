#Asher Wangia, Writing to Text Notes
import csv


"""
r = read the file
w = write on the file(replace old file)
w+ = read and write
a = append(adds to the file, doesn't delete them)
x = create file
a+ = append and read the file
"""


with open("Notes/test.txt", "a", newline="") as file:
    fieldnames = [""]
    
    
    
    while True:   
       file.write("I have changed the file")

data = [

]


with open("Notes/user_info.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([["silly_username","Black"],["silly_username","Black"],["","teal"],["basic_name","white"]])
    
with open("Notes/user_info.csv", "r") as file:  
    reader= csv.reader(file)
    for row in reader:
        print(f"username: {row[0]} color: {row[1]}")