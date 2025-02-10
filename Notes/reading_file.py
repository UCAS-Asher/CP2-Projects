# Asher Wangia, Reading Notes Python
import csv


with open("Notes/test.txt","r") as file:
    content = file.read()
    print(content)

users = {}

with open("Notes/user_info.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        users.update({row[0]:row[1]})