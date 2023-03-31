'''
#1 A simple calculator program in Python

def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

print("Select operation.")
print("1-Add")
print("2-Sub")
print("3-Mul")
print("4-Div")

select = input("Enter choice: ")

num1 = int(input("Enter first num: "))
num2 = int(input("Enter second num: "))

if select == '1':
    print(num1,"+",num2,"=", add(num1,num2))

elif select == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))

elif select == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))

elif select == '4':
    print(num1,"/",num2,"=", divide(num1,num2))
else:
    print("Invalid input")
'''


'''
#2todo list using python
task = []
completed = []
def add(i):
    task.append(i)

def delete(i):
    print(i + " is deleted from the list")
    task.remove(i)

def view():
    n = 1
    print("nunber of Tasks in list")
    for t in task:
        print(str(n)+" : "+t)
        n = n + 1
    n = 1 
    if(completed != []):
        print("Tasks Completed")
        for t in completed:
            print(str(n)+" : "+t)
            n = n + 1
    else:
        print("No task completed yetn")


def done(i):
    print("n"+ i + " is donen")
    task.remove(i)
    completed.append(i)

while True:
    print("select: 1-add task, 2-delete task , 3-view task")
    select=int(input("enter choice: "))
    if select==1:
               string=input("enter task: ")
               add(string)
    elif select==2:
               string=input("delete task: ")
               delete(string)
    elif select==3:
                view()
'''

'''
#3 weather using python
import requests, json


api_key = "5169e593a2e4ff0915d2c0f4d795563f"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("city name : ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)
x = response.json()
if x["cod"] != "404":
	y = x["main"]
	current_temperature = y["temp"]-273.15
	current_pressure = y["pressure"]
	current_humidity = y["humidity"]
	z = x["weather"]
	weather_description = z[0]["description"]
	print(" Temperature (C)  = " +
					str(current_temperature) +
		"\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n humidity (in percentage) = " +
					str(current_humidity) +
		"\n description = " +
					str(weather_description))

else:
	print(" City Not Found ")
'''



#4tic tac toe
def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], "|", end=" ")
        print()
        print("-------------")

def check_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

def check_tie(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
player = "X"
while True:
    print_board(board)
    row = int(input("Player " + player + ", enter row number (1-3): "))
    col = int(input("Player " + player + ", enter column number (1-3): "))
    if board[row-1][col-1] != " ":
        print("That position is already taken. Try again.")
        continue
    board[row-1][col-1] = player
    if check_win(board):
            print_board(board)
            print("Player " + player + " wins!")
            break
    if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break
    if player == "X":
            player = "O"
    else:
            player = "X"


'''
#5 hangman
import time
import random
name = input("What is your name? ")
print ("Hello, " + name, "Time to play hangman!")
time.sleep(1)
print ("Start guessing...\n")
time.sleep(0.5)
## A List Of Secret Words
words = ['python','programming','html','css','javascript','nodejs']
word = random.choice(words)
guesses = ''
turns = 5
while turns > 0:         
    failed = 0             
    for char in word:      
        if char in guesses:    
            print (char,end="")    
        else:
            print ("_",end=""),     
            failed += 1    
    if failed == 0:        
        print ("\nYou won") 
        break              
    guess = input("\nguess a character:") 
    guesses += guess                    
    if guess not in word:  
        turns -= 1        
        print("\nWrong")    
        print("\nYou have", + turns, 'more guesses') 
        if turns == 0:           
            print ("\nYou Lose")
'''



'''
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Banglore", "Chennai", "Mumbai", "Delhi"],
        "answer": "Delhi"
    }
]

def ask_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    answer = input("Enter your answer (1-4): ")
    return question["options"][int(answer)-1] == question["answer"]

def play_quiz():
    score = 0
    for question in questions:
        if ask_question(question):
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {question['answer']}")
    print(f"Your final score is {score}/{len(questions)}")

play_quiz()

'''
