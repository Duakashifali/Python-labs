# TASK 1
import numpy as np

marks = np.array([
    [85, 90, 78],
    [88, 76, 92],
    [95, 89, 84]
])

print("Marks of Three Students:")
print(marks)

# TASK 2
import numpy as np

numbers = np.arange(1, 21)

print("Numbers from 1 to 20:")
print(numbers)

# task 3
import numpy as np

a = np.array([10, 20, 30])
b = np.array([2, 4, 5])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

#Task 4
import numpy as np

marks = np.array([85, 90, 78, 95, 88])

print("Marks:", marks)
print("Sum:", np.sum(marks))
print("Average:", np.mean(marks))
print("Minimum:", np.min(marks))
print("Maximum:", np.max(marks))

# task 5
def check_number(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("Enter a number: "))

print("The number is:", check_number(number))

# task 6
def calculate_marks(marks):
    highest = max(marks)
    lowest = min(marks)
    average = sum(marks) / len(marks)

    return highest, lowest, average

marks = [85, 90, 78, 95, 88]

high, low, avg = calculate_marks(marks)

print("Highest Marks:", high)
print("Lowest Marks:", low)
print("Average Marks:", avg)