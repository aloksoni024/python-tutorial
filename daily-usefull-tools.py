# tuple = (1, 2, 3,5,6,2,67,2,5,3,65,43,6,7,8,8,9,10,11,12,13,14,15,16,17,18,19,20)
# print(tuple)

# list = [1, 2, 3,5,6,2,67,2,5,3,65,43,6,7,8,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(list)

# dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10}
# print(dict)

# set = {1, 2, 3, 3, 4,1,2,3,5,7,8,4,6,9}
# print(set)

import numpy as np


def calculator():
    print("=====Welcome to the calculator=======")
    while True:
        
        operation = input("Enter the operation: add, subtract, multiply, divide or enter 'exit' to exit:")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("Calculating...")
        if operation == "add":
            print(f"The sum of {a} and {b} is {a + b}\n")
        elif operation == "subtract":
            print(f"The difference of {a} and {b} is {a - b}\n")
        elif operation == "multiply":
            print(f"The product of {a} and {b} is {a * b}\n")
        elif operation == "divide":
            print(f"The quotient of {a} and {b} is {a / b}\n")
        elif operation == "exit":
            print("Thank you for using the calculator")
            break
        else:
            print("Invalid operation\n")

def guess_the_number():
    print("Please enter the range")
    start_number = int(input("Enter the start number of range: "))
    end_number = int(input("Enter the end number of range: "))

    random_number = np.random.randint(start_number, end_number)

    print("You have 10 attempt to guess the number\n")
    for i in range(10):
        print(f"======You have {10-i} attempts left======")
        guess_number = int(input("Enter the number you want to guess: "))
        if guess_number == random_number:
            print(f"You guessed the number correctly with {i+1} attempts\n")
            break
        elif guess_number > random_number:
            print(f"Number is less than {guess_number}\n")
        elif guess_number < random_number:
            print(f"Number is greater than {guess_number}\n")

    print(f"Game over!!!!!The number was {random_number}\n")


tasks = []
done_tasks = []


def to_do_list():
    print("=====To Do List=====")
    print("1. Add a task")
    print("2. Show all Pending tasks")
    print("3. Mark task as Done")
    print("4. Show all Done tasks")
    print("5. Exit")

    while True:
        choice = input("Enter the choice: ")
        if choice == "1":
            task = input("Please enter the task you want to add: ")
            tasks.append(task)
            print("Task added successfully!!!!")
        elif choice == "2":
            print("All Pending tasks: ")
            for task in tasks:
                print(task)
        elif choice == "3":
            task = input("Please enter the task you want to mark as Done: ")
            done_tasks.append(task)
            tasks.remove(task)
            print("Task marked as Done!!!!")
        elif choice == "4":
            print("All Done tasks: \n")
            for task in done_tasks:
                print(task)
        elif choice == "5":
            print("Thank you for using the To Do List")
            break
        else:
            print("Invalid choice\n")

if __name__ == "__main__":
    while True:
        print("======Welcome to the basics of Python=======")
        print("Please choose the option\n")
        print("1. Calculator")
        print("2. Guess the number")
        print("3. To Do List")
        print("4. Exit")
        choice = input("Enter the choice: ")
        if choice == "1":
            calculator()
        elif choice == "2":
            guess_the_number()
        elif choice == "3":
            to_do_list()
        elif choice == "4":
            print("Thank you for using the basics of Python")
            break
        else:
            print("Invalid choice\n")
