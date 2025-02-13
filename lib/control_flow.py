#!/usr/bin/env python3

def admin_login(username, password):
    # Check if the username is "admin" or "ADMIN" and the password is "12345"
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    # Return a message based on the temperature
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

def fizzbuzz(num):
    # Check for FizzBuzz conditions
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

def calculator(operation, num1, num2):
    # Perform the given arithmetic operation
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2 if num2 != 0 else "Cannot divide by zero!"
    else:
        print("Invalid operation!")
        return None

# Testing the functions
print(admin_login("sudo", "12345"))  # "Access denied"
print(admin_login("admin", "12345"))  # "Access granted"
print(admin_login("ADMIN", "12345"))  # "Access granted"
print(admin_login("admin", "54321"))  # "Access denied"

print(hows_the_weather(30))  # "It's brisk out there!"
print(hows_the_weather(50))  # "It's a little chilly out there!"
print(hows_the_weather(90))  # "It's too dang hot out there!"
print(hows_the_weather(70))  # "It's perfect out there!"

print(fizzbuzz(3))   # "Fizz"
print(fizzbuzz(5))   # "Buzz"
print(fizzbuzz(15))  # "FizzBuzz"
print(fizzbuzz(7))   # 7

print(calculator("+", 3, 4))  # 7
print(calculator("-", 10, 5)) # 5
print(calculator("*", 6, 3))  # 18
print(calculator("/", 8, 2))  # 4.0
print(calculator("/", 8, 0))  # "Cannot divide by zero!"
print(calculator("%", 10, 3)) # "Invalid operation!"
