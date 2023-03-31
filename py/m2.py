'''
while True:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        result = numerator / denominator
        print("The result is:", result)
        break
    except ZeroDivisionError:
        print("Error: Cannot divide by zero. Please enter a non-zero denominator.")
'''
'''
while True:
    try:
        filename = input("Enter the name of the file: ")
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
        break
    except FileNotFoundError:
        print("Error: File not found. Please enter a valid filename.")
'''


'''
class BankAccount:
    
    def __init__(self):
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
        print("Deposit of", amount, "completed.")
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal of", amount, "completed.")
        else:
            print("Insufficient balance.")
    
    def print_balance(self):
        print("Current balance:", self.balance)
# create an instance of BankAccount
account = BankAccount()

# deposit some money
a=int(input("money: "))

account.deposit(a)

# withdraw some money
account.withdraw(500)

# try to withdraw more money than the balance
account.withdraw(1000)

# print the balance
account.print_balance()
'''


#1 Write a program that takes a list of numbers and returns the sum of all even numbers in the list.
'''
def sum_of_evens(lst):
    even_sum = 0
    for num in lst:
        if num % 2 == 0:
            even_sum += num
    return even_sum
lst =[1, 2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]
print(sum_of_evens(lst))
'''

#2 Write a program that takes a string and returns a new string with all the vowels removed.
'''
def remove_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_string = ""
    for char in string:
        if char.lower() not in vowels:
            new_string += char
    return new_string
string=input("enter string: ")
print(remove_vowels(string))
'''

#3 Write a program that takes a list of strings and returns a new list with all the strings sorted in alphabetical order.
'''
def sort_strings(lst):
    return sorted(lst)
lst=[]
for i in range(3):
 a=input("enter string: ")
 lst.append(a)
print(sort_strings(lst))
'''

#4 Write a program that takes a list of numbers and returns the median value.
'''
def median(lst):
    lst_sorted = sorted(lst)
    length = len(lst_sorted)
    if length % 2 == 0:
        return (lst_sorted[length//2] + lst_sorted[length//2 - 1])/2
    else:
        return lst_sorted[length//2]
lst=[]    
for i in range(5):
 a=int(input("enter number: "))
 lst.append(a)
print(median(lst))
'''

#5 Write a program that takes two lists of numbers and returns a new list with the elements that appear in both lists.
'''
def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))
lst1 = list(map(int, input("Enter lst1: ").split()))
lst2 = list(map(int, input("Enter lst2: ").split()))
print(common_elements(lst1,lst2))
'''

#6 Write a program that takes a list of words and returns the longest word in the list.
'''
lst=[]
for i in range(5):
    a=input("enter string: ")
    lst.append(a)
longest = ""
for word in lst:
    if len(word) > len(longest):
        longest = word
print(longest)
'''
#7 Write a program that takes a list of numbers and returns a new list with only the prime numbers.
'''
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def prime_numbers(lst):
    return [num for num in lst if is_prime(num)]
lst = list(map(int, input("Enter lst: ").split()))
print(prime_numbers(lst))
'''

#8 Write a program that takes a string and returns the number of times each letter appears in the string.
'''
string=input("enter string: ")
letter_count = {}
for char in string:
    if char.isalpha():
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
print(letter_count)
'''

#9 Write a program that takes a list of numbers and returns a new list with the elements squared.
'''
def square_elements(lst):
    return [num**2 for num in lst]
lst = list(map(int, input("Enter lst: ").split()))
print(square_elements(lst))
'''

#10 Write a program that takes a list of strings and returns a new list with only the strings that are palindromes.
'''
words_str = input("Enter a list of words, separated by spaces: ")
words = words_str.split()
def is_palindrome(word):
    return word == word[::-1]
palindromes = [word for word in words if is_palindrome(word)]
print(palindromes)
'''

'''
# create a new list of squares of numbers from 1 to 10
squares = [i**2 for i in range(1, 11)]
print(squares) 


# create a new list of even numbers from an existing list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 69, 10]
evens = [i for i in numbers if i % 2 == 0]
print(evens)

# create a new list of strings, where each string is the original string capitalized
words = ['apple', 'banana', 'cherry', 'date']
capitalized = [word.capitalize() for word in words]
print(capitalized) 
'''

'''
def my_decorator(func):
    def wrapper():
        print("Before function is called.")
        func()
        print("After function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hell!")

# calling the decorated function
say_hello()

'''

'''
# Take user input for list of numbers
num_list = input("Enter a list of numbers, separated by commas: ").split(",")

# Use lambda function and list comprehension to filter out even numbers and double odd numbers
result_list = [(lambda x: x*2)(int(num)) for num in num_list if int(num)%2!=0]

# Print the resulting list
print(result_list)
'''

import time

# Define decorator function to measure time taken by a function to execute
def time_taken_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()   # Get start time
        result = func(*args, **kwargs)   # Call the function
        end_time = time.time()     # Get end time
        print(f"Time taken by {func.__name__}: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

# Example function to add two numbers
@time_taken_decorator
def add_numbers(a, b):
    return a + b

# Call the function and measure its execution time using the decorator
result = add_numbers(5, 7)
print(result)














