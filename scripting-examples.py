# Use of String Formatting - Ex1
float1 = 563.78453
print(format(float1, ".3f"))

# f-strings - Ex2
x = 4
n = 3
power = x ** n
print(f"{x} to the power of {n} is equal to {power}")


# User input - Ex3
math_marks = float(input("Enter the Math marks: "))
theory_marks = float(input("Enter the Theory marks: "))

if (math_marks >= 40 and theory_marks >= 30) or (math_marks + theory_marks) >=70:
    print("\nYou have passed")
else:
    print("\nYou have failed")


# Import another python script - Ex4
print("\nNew exercise")
import supporting as sp

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
for month in months:
    if month in ["June", "July"]:
            print(f"{month} is a month for {sp.vacation1}")
    elif month == "December":
            print(f"{month} is a month for {sp.vacation2}")
    else:
        print("The current month is",month)


from datetime import date

# Dates - Ex5
print("\nNew exercise")
current_date = date.today()

# Print the formatted date
print("Today is :%d-%d-%d" % (current_date.day,current_date.month,current_date.year))

custom_date = date(2022, 4, 8)
print("The date yesterday was:",custom_date)


# List Comprehension - Ex6
print("\nNew exercise")

# Create a list of characters using list comprehension
char_list = [char.upper() if not char.isspace() else "+" for char in "I love MacOS" ]
print(char_list)


# Replace List elements - Ex7
print("\nNew exercise")
char_list1 = [" " if char == "+" else char for char in char_list ]
print(char_list1)


# List Comprehension - sum first element of tuple Ex8
print("\nNew exercise")

pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
print(f"Pairs: {pairs}")
print(f"Sum of first elements is: {sum(x[0] for x in pairs)}" )


# Count items in a list - Ex9
print("\nNew exercise")
# Define a string/phrase
phrase = 'I love MacOS. MacOS is by far the best operating system.'
search = 'MacOS'
count = phrase.count(search)
print(f"{search} search word, appears {count} times in the given phrase. ")


# Lambda functions, Filter - Ex10
print("\nNew exercise")
import random
random_list = random.sample(range(0, 1000), 10)
random_list.sort()
print( f"Original list {random_list}")
new_list = list(filter(lambda x: (x%2 == 0 or x <=100) , random_list))
print(f"The resulting list {new_list} is produced after applying the filters x%2 == 0 or x <=100")


# Lambda functions, Apply - Ex11
print("\nNew exercise")
double = lambda x: x * 2
new_list1 = list(map(lambda x: x-1000, random_list))
print(f"The resulting list {new_list1} is produced after applying the condition x-1000")
new_list2 = list(map(double, random_list))










