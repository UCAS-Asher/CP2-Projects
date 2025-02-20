
import time


while True:
    f = open("Notes/test.txt", "a")
    f.write("\nNow the file has more content!")
    time.sleep(0.1)