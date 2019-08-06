assign_number=50
guess_number=input("enter the number you guess")
guess_number=int(guess_number)

if assign_number==guess_number:
    print("the number you enter is 50")
else:
    if guess_number < assign_number:
        print("Too low")
    else:
        print("too high")

    
