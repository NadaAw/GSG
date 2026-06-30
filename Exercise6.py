'''
# Exercise 1
def first_last(items):
    if not items:
        return None
    return (items[0], items[-1])
'''
'''
# Exercise 2
def passing_grades (grades):
    success_students = []
    
    for grade in grades:
        if grade >= 60:
            success_students.append(grade)
    
    return success_students
    

grades = [45, 60, 72, 58, 90, 33, 67]
result = passing_grades(grades)
print(result)
'''
'''
# Exercise 3
def reversed_sentence(sentence):
    
    splitted_sentence = sentence.split(" ")
    reversed_words = splitted_sentence[::-1]
    
    return " ".join(reversed_words)
    
    
sentence = input("Please enter a sentence to revers: ")
print("The reversed sentence is: " , reversed_sentence(sentence))
'''
'''
# Exercise 4

scores = [45, 88, 92, 67, 74, 100, 85, 92]
scores.sort(reverse=True)
top_three = scores[:3]
print("Top three scores:", top_three)
'''

# Exercise 5
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
total = 0

for list1 in nested_list:
    for number in list1:
        total += number
        
print("The total is:", total)