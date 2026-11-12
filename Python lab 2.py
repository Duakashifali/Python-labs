#TASK 1 

sap = input("Enter your SAP ID: ")
name = input("Enter your name: ")

print("Hey", name, "your SAP is", sap)

#task 2

a = 10
b = 20

print("Before swapping:")
print("a =", a)
print("b =", b)

temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)

# Task 3

Message = "Programming language"

print("Character r:", Message.count('r'))
print("Character a:", Message.count('a'))
print("Character m:", Message.count('m'))
print("Character n:", Message.count('n'))
print("Character u:", Message.count('u'))

print("Occurrences of r:", [i for i in range(len(Message)) if Message[i] == 'r'])
print("Occurrences of a:", [i for i in range(len(Message)) if Message[i] == 'a'])
print("Occurrences of m:", [i for i in range(len(Message)) if Message[i] == 'm'])
print("Occurrences of n:", [i for i in range(len(Message)) if Message[i] == 'n'])
print("Occurrences of u:", [i for i in range(len(Message)) if Message[i] == 'u'])

# Task 4

salary = 50000

print("Original Salary:", salary)

bonus = 10000
salary += bonus

print("Bonus:", bonus)

deduction = 5000
salary -= deduction

print("Deduction:", deduction)
print("Final Salary:", salary)

# T ask 5 

roll_numbers = [101, 102, 103, 104, 105]

roll = int(input("Enter your roll number: "))

if roll in roll_numbers:
    print("Student is enrolled.")
else:
    print("Student is not enrolled.")

second_list = roll_numbers

if roll_numbers is second_list:
    print("Both variables refer to the same list.")
else:
    print("Both variables refer to different lists.")
