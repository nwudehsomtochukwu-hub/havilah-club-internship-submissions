# Day 11 - Introduction to Python


# Exercise 1: Variables and Data Types

name = "Somtochukwu"
age = 22
height = 1.75
is_student = True

print("Name:", name, type(name))
print("Age:", age, type(age))
print("Height:", height, type(height))
print("Is a student:", is_student, type(is_student))


# Exercise 2: Two Numbers Calculator

# input() gives text, so we convert to float to do maths
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

print("Sum:", x + y)
print("Difference:", x - y)
print("Product:", x * y)
print("Quotient:", x / y)
print("Remainder:", x % y)


# Exercise 3: Temperature Converter

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print("Temperature in Fahrenheit:", fahrenheit)

fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
kelvin = (fahrenheit_input - 32) * 5 / 9 + 273.15
print("Temperature in Kelvin:", kelvin)


# Exercise 4: Robot Sensor Monitor

robot_name = input("Enter robot name: ")
robot_id = input("Enter robot ID: ")
sensor_name = input("Enter sensor name: ")
sensor_reading = float(input("Enter sensor reading: "))
operating_limit = float(input("Enter operating limit: "))

difference = operating_limit - sensor_reading

print("----- Robot Sensor Report -----")
print("Robot Name:", robot_name)
print("Robot ID:", robot_id)
print("Sensor Name:", sensor_name)
print("Sensor Reading:", sensor_reading)
print("Operating Limit:", operating_limit)
print("Difference (limit - reading):", difference)