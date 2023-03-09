import sys

print("You have 5 attempts. See if you can guess it. Good luck!")

for i in range (5, 0, -1):
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
    
    
    
   
        
