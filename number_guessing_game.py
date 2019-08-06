
import random
wining_number= random.randint(1,100)
guess_number=1

number=int(input("enter a number"))
game_over=False

while not game_over:
    if number==wining_number:
        print(f"you win! and you guess at {guess_number}")
        game_over=True
    else:
        if number < wining_number:
            print("too low") 
        else:
            print("too high")

        guess_number+= 1
        number=int(input("enter a number")) # DRY-Don't repeat your code: follow your principle.

