'''
# Exercise 1
with open("notes.txt", "w") as file:
    file.write("My name is Nada\n")
    file.write("My age is 29\n")
    file.write("Its the third line\n")

with open("notes.txt", "r") as file:    
    for row in file:
        print(row.strip())

'''
'''
# Exercise 2
user_action = input("Please enter an action: ").strip()

with open("activity_log.txt", "a") as file:
    file.write(user_action + "\n")

print("Action added successfully!")

'''
'''
# Exercise 3
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number, please enter another one!")


age = get_number("Please enter your age: ")
print("Your age is:", age)
'''
'''
# Exercise 4
import csv

students = []
total = 0

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["score"] = int(row["score"])
        students.append(row)
        total += row["score"]

average = total / len(students)
print("The average of the students is:", average)
'''
# Exercise 5

# FileNotFoundError
with open("missing_file.txt", "r") as file:
    content = file.read()
    
# ValueError
age = int("Nada")

# KeyError
product = {"name": "Phone", "price": 1000}
print(product["discount"])
