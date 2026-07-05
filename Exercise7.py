'''
# Exercise 1
product = {
    "name": "Phone",
    "price": 1000,
    "quantity": 8
}

discount = product.get("discount", 0)
print("Discount amount:", discount)
'''
'''
#Exercise 2
sentence = input("Please input a sentence: ").strip().lower()
words = sentence.split()
word_counts = {}

for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

print("\nWord Counts:")
for word, count in word_counts.items():
    print(f"  '{word}': {count}")
'''
'''
# Exercise 3
visitor_emails = [
    "alice@example.com",
    "bob@example.com",
    "alice@example.com",  # مكرر
    "charlie@example.com",
    "bob@example.com"     # مكرر
]

unique_visitors_set = set(visitor_emails)
unique_visitors_count = len(unique_visitors_set)

print("Number of unique visitors is:", unique_visitors_count)
'''
'''
# Exercise 4
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 50},
    {"name": "Charlie", "score": 75},
    {"name": "David", "score": 58}
]

passed_students = []
for student in students:
    if student["score"] >= 60:
        passed_students.append(student)

print("Passed students are:", passed_students)
'''

#Exercise 5
person1_interests = {"Python", "Gaming", "Photography", "Football"}
person2_interests = {"Cooking", "Photography", "Music", "Python"}

common_interests = person1_interests & person2_interests

print("Common interests:", common_interests)