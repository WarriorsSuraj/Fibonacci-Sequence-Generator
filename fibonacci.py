# WarriorsSuraj
# March 2nd, 2024
# This is a simple program that will print out the fibonacci sequence to n terms

# defining fibonacci sequence function
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)
    
# taking user input and ensuring that the number of terms is greater than or equal to one
terms = int(input("How many terms of the fibonnaci sequence would you like to print? "))
try:    
    if terms <= 0:
        print("Invalid number of terms inputted.")
    else:
        for x in range(terms):
            print(fibonacci(x))
except ValueError:
    print("Please enter a valid integer for the number of terms.")
