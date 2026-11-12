# task 1
num = int(input("Enter an integer: "))

if num >= 0 and num <= 9:
    print("The number is a Single-digit integer.")
elif num >= 10 and num <= 99:
    print("The number is a Double-digit integer.")
elif num >= 100 and num <= 999:
    print("The number is a Triple-digit integer.")
else:
    print("The number has more than three digits.")

# Task 2
num = int(input("Enter an integer: "))

if num % 2 == 0:
    print(num, "is an Even number.")
else:
    print(num, "is an Odd number.")
    
# Task 3
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

if length == breadth:
    print("The given shape is a Square.")
else:
    print("The given shape is a Rectangle.")
    
# Task 4
salary = float(input("Enter employee salary: "))
years = int(input("Enter years of service: "))

if years > 5:
    bonus = salary * 5 / 100
    net_salary = salary + bonus

    print("Employee Bonus: ", bonus)
    print("Net Salary: ", net_salary)
else:
    print("No bonus is given.")
    print("Net Salary: ", salary)

#task 5
year = int(input("Enter a year: "))

if year % 400 == 0:
    print(year, "is a Leap Year.")
elif year % 100 == 0:
    print(year, "is not a Leap Year.")
elif year % 4 == 0:
    print(year, "is a Leap Year.")
else:
    print(year, "is not a Leap Year.")