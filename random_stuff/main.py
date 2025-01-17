def var():
    one = input("?:")
    display()
    return one

def display():
    one = var()
    print(one)

while True:
    var()

