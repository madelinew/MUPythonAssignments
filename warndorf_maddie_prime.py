userX = input("What number to you want to test if it is prime?")

def prime(x):
    x = int(userX)
    tf = True
    for i in range(2, x):
        if x % i == 0:
            tf = False
            break
    if tf:
        print("prime")
    else:
        print("not prime")

prime(userX)