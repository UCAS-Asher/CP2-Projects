import csv
import time


with open("Notes/test.txt", "a") as file: 
    while True:
        time.sleep(1)
        file.write("\nI have changed the file")