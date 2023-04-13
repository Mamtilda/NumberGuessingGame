import sys

print("You have 5 attempts. See if you can guess it. Good luck!")
invalid_attempts = 0
for i in range (5, 0, -1):
<<<<<<< HEAD
    try:
        user_input = int(input("Enter a number here: "))
        if user_input == 25:
            print("Congratulations!!! That is the correct answer.")
            sys.exit()
        elif user_input > 25:
            print("Too high. Try again!")
        else:
            print("Too low. Try again!")
    except ValueError:
        print("Invalid input. Please enter a number.")
        invalid_attempts += 1

    if i == 1:
        print("You are all out of moves. The correct answer was 25.")
        print("Better luck next time!")
        break

    if invalid_attempts == 3:
        print("Too many invalid attempts. Exiting...")
        break
=======
    user_input = int(input("Enter a number here: "))
    if user_input == 25:
        print("Congratulations!!! That is the correct answer.")
        sys.exit()
        
    elif user_input > 25:
        print("Too high. Try again!")
        
    else:
        print("Too low. Try again!")
        
    if i == 1:
        print("You are all out of moves. The correct answer was 25.")
        print("Better luck next time!")
    
    
    
   
        
>>>>>>> 58fcb63aa1f6d373def000ea2827b09a9d062add
