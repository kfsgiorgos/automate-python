# exercise to ensure users input is a positive number

print("How many laptops do you have?")
numLaptops = input()

try:
    assert int(numLaptops) > 0, "The number should be a positive integer."
    if int(numLaptops) >=5:
        print("That is too many laptops.")
    else:
        print("That is not too many laptops.")
except ValueError:
    print("You did not enter a number. Please enter a number.")
