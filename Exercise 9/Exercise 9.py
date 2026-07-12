'''
# Exercise 1
import random

original_list = ["Nada", "Anas", "Omar", "Maria"]
choice = random.choice(original_list)

print("The picked name is:", choice)
'''
'''
#Exercise 2 
from datetime import datetime

today = datetime.now()

print(today.strftime("%Y-%m-%d"))   
print(today.strftime("%d/%m/%Y"))   
print(today.strftime("%B %d, %Y"))  
'''
'''
#Exercise 3
from pathlib import Path

filename = input("Please enter a filename to check: ").strip()

file_path = Path(filename)

if file_path.exists():
    print(f"The file '{filename}' exists.")
else:
    print(f"The file '{filename}' does not exist.")
'''
'''
#Exercise 4

from grade_utils import calculate_percentage, get_grade_report

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 50},
    {"name": "Charlie", "score": 75}
]

total_score = 0
for student in students:
    total_score += student["score"]

max_possible_score = len(students) * 100

final_percentage = calculate_percentage(total_score, max_possible_score)
grade, message = get_grade_report(final_percentage)

print("=" * 45)
print("       FINAL PERFORMANCE REPORT")
print("=" * 45)
print(f"  Total Score : {total_score} / {max_possible_score}")
print(f"  Percentage  : {final_percentage:.1f}%")
print(f"  Final Grade : {grade}")
print("-" * 45)
print(f"  {message}")
print("=" * 45)
'''
#Exercise 5
#I will pick requests library
import requests

response = requests.get("https://github.com")
print(response.text)

'''
import requests: Imports the library to enable internet communication tools.
requests.get(...): Sends a request to the GitHub server to fetch data from that specific web address.
response = : Stores the complete server answer inside a variable.
print(response.text): Extracts and prints the actual text data returned by the server onto the screen.
'''