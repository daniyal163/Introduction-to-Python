import random
secret_number = random.randint(1,100)
guess = int(input("your guess: "))
attempts = 0
while attempts<2:
    guess = int(input("your guess: "))
    attempts += 1
    if guess==secret_number:
       print(f"Bravo! found in {attempts} attempts", secret_number)
       break
    elif guess<secret_number:
        print("Too low")
    else:   
        print("Too high")
if guess!=secret_number:
    print("you lost! it was : ,", secret_number)