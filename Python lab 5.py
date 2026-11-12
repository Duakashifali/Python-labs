ai_tools = ["ChatGPT", "Gemini", "Claude", "Copilot", "DeepSeek"]

for tool in ai_tools:
    print(tool)
    
#Task 2
language = input("Enter a programming language: ")

for letter in language:
    print(letter)

# Task 3
courses = ["Python", "Machine Learning", "Artificial Intelligence", "Deep Learning", "Data Science"]

search = input("Enter an item to search: ")

for item in courses:
    if item == search:
        print("Item found!")
        break
else:
    print("Item not found!")
    
# task 4
models = ["ChatGPT", "Gemini", "Claude", "Copilot", "DeepSeek"]

scores = [90, 85, 88, 92, 95]

total = 0

for i in range(len(models)):
    print(models[i], "Score:", scores[i])
    total = total + scores[i]

average = total / len(scores)

print("Total Score:", total)
print("Average Score:", average)