# Day 12 - Python Logic and Functions


# Exercise 1: Grade Calculator

def calculate_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"


# Exercise 2: Multiplication Table

def multiplication_table():
    again = "yes"

    while again == "yes":
        try:
            number = int(input("Enter a whole number: "))
            for i in range(1, 13):
                print(number, "x", i, "=", number * i)
        except ValueError:
            print("Error: please enter a whole number, not text.")

        again = input("Do you want another table? (yes/no): ").lower()


# Exercise 3: Temperature Converter

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


# Exercise 5: Utility Menu

running = True

while running:
    print("\n--- Python Utility Menu ---")
    print("a. Grade Calculator")
    print("b. Multiplication Table")
    print("c. Temperature Converter")
    print("d. Exit")

    choice = input("Choose an option (a-d): ")

    if choice == "a":
        try:
            score = float(input("Enter your score (0-100): "))
            print("Grade:", calculate_grade(score))
        except ValueError:
            print("Error: please enter a number, not text.")
    elif choice == "b":
        multiplication_table()
    elif choice == "c":
        try:
            temp_c = float(input("Enter temperature in Celsius: "))
            print("Temperature in Fahrenheit:", celsius_to_fahrenheit(temp_c))
        except ValueError:
            print("Error: please enter a number, not text.")
    elif choice == "d":
        print("Goodbye!")
        running = False
    else:
        print("Invalid choice. Please enter a, b, c or d.")