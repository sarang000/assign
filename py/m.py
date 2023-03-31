'''
# Ask user for their name and age
name = input("What is your name? ")
age = int(input("How old are you? "))

# Calculate age after 10 years
age_in_10_years = age + 10

# Print out message with calculated age
print("Hi {}, in 10 years you will be {} years old.".format(name, age_in_10_years))
'''

'''
# Ask user for temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Print out converted temperature
print("{:.1f} degrees Celsius is equivalent to {:.1f} degrees Fahrenheit.".format(celsius, fahrenheit))
'''


'''
# Import the math module to access the value of pi
import math

# Ask user for radius
radius = float(input("Enter the radius of the circle: "))

# Calculate area and circumference
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

# Print out calculated values
print("The area of the circle is {:.2f} square units.".format(area))
print("The circumference of the circle is {:.2f} units.".format(circumference))
'''


'''
# Ask user for a string
string = input("Enter a string: ")

# Calculate length of string
length = len(string)

# Get first and last characters of string
first_char = string[0]
last_char = string[-1]

# Reverse the string
reverse_string = string[::-1]

# Print out various information about the string
print("The length of the string is:", length)
print("The first character of the string is:", first_char)
print("The last character of the string is:", last_char)
print("The string in reverse order is:", reverse_string)
'''


'''
# Ask user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# Print out results
print("The result of adding the two numbers is:", addition)
print("The result of subtracting the second number from the first number is:", subtraction)
print("The result of multiplying the two numbers is:", multiplication)
print("The result of dividing the first number by the second number is:", division)
'''


'''
# Ask user for a list of numbers
numbers = input("Enter a list of numbers, separated by spaces: ").split()

# Convert the list of strings to a list of floats
numbers = [float(num) for num in numbers]

# Find the largest and smallest numbers in the list
largest = max(numbers)
smallest = min(numbers)

# Print out the results
print("The largest number in the list is:", largest)
print("The smallest number in the list is:", smallest)
'''



'''
# Ask user for a number
num = int(input("Enter a number: "))

# Check if the number is even or odd
if num % 2 == 0:
   print(num, "is even")
else:
    print(num, "is odd")'''



# Ask user for a list of names
names = input("Enter a list of names, separated by spaces: ").split()

# Sort the list of names
names.sort()

# Print out the sorted list of names
print("The sorted list of names is:", names)


