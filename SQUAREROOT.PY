n = int(input("Enter the number:"))
root = 0 
while n > 0:
    n = n - (2 * root + 1)
    root =root + 1
print(f"The root of the number is {root}")
