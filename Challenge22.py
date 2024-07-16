import random 
 

num = random.randint(1, 100)
tries = 0

print("Guess the right number or you're stuck in this loop forever!")
print("Think of a number which lies between 1 and 100.")

while True:
    try:
        guess = int(input("Your guess: "))
        tries += 1

        if guess < num:
            print("Perhaps, go for a higher number.")
        elif guess > num:
            print("Well, try for a lower number instead.")
        else:
            print(f"Luck was on your side this time! You've successfully guessed the number in {tries} tries.")
            break
    except ValueError:
        print("OOPS!! Please enter a number between 1 and 100.")

print("Managed to escape? Bravo! If not, keep playing.")
