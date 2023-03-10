# number guesser

import random
n = random.randint(1, 101)
guess = int(input("Enter any number: "))
i=0
while i < 4:
    i+=1
    if guess < n:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
        print("Got it!")
        break

if guess != n:
    print("lose")
    print("The number was", n)
