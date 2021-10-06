#WRITE YOUR CODE IN THIS FILE
def howLong(w):
    total = 0

    for i in range(0, len(w)):
        total = total + i
    return total

print(howLong("Pig"))