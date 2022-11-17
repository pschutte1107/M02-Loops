secret = 6
guess = 3
if guess > secret:
    print("too high")
elif guess < secret:
    print("too low")
elif guess == secret:
    print("Just right")

small = False
green = True
if small:
    if green:
        print("its a pea")
    else:
        print("its a cherry")
else:
    if green:
        print("its a watermelon")
    else:
        print("its a pumpkin")
