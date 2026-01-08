n = float(input("Enter the number:"))
guess = n/2
while(guess != (guess +n/guess)/2):
    guess = (guess + n / guess) / 2 
    print("guess:",guess)

print(guess)