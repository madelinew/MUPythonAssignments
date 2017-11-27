userX = input("How many Fibonacci numbers would you like?")

if int(userX) < 3:
    print("ERROR! Please enter a number greater than 3")
    userX = input("How many Fibonacci numbers would you like?")

def fib():
    x = int(userX)-1
    fiblist = [0, 1]
    for i in range(0, x):
        fiblist.append(fiblist[i] + fiblist[i+1])
    return(fiblist)

userfib = fib()


index = 0
for n in userfib:
    print(str(index) + ":" + str(n))
    index+=1

