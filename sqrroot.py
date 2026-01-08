n = float(input("Enter the number:"))
guess = n/2
while(guess*guess >n):
    guess = guess - 0.0001

print("square root:",guess)

