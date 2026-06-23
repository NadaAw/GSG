# Excercise #1
'''
def celsius_to_fahrenheit(c):
    result = (c * 9/5) + 32
    return result

def fahrenheit_to_celsius(f):
    result = (f - 32) * 5/9
    return result

def celsius_to_kelvin(c):
    result = c + 273.15
    return result
    

tempreture_in_celecius = 25
tempreture_in_fahrenhiet = 77

print(f"{tempreture_in_celecius}°C is {celsius_to_fahrenheit(tempreture_in_celecius)}°F")
print(f"{tempreture_in_fahrenhiet}°F is {fahrenheit_to_celsius(tempreture_in_fahrenhiet)}°C")
print(f"{tempreture_in_celecius}°C is {celsius_to_kelvin(tempreture_in_celecius)}K")

'''
'''
# Excercise 2
def is_palindrome(text):
    clean = text.replace(" ", "").lower() 
    
    return clean == clean[:: -1]
    
text = input("Please enter your text to check if it is palindrome or not  ")
result = is_palindrome(text)
print( "the result is", result)
'''

'''

# Excercise 3
  
  
def analyse_grades(grades):
    average = sum(grades)/len(grades)
    highest_grade = max(grades)
    lowest_grade = min(grades)
    count=0
    for grade in grades :
        if grade >=60:
            count+=1
            
    
    print("Average:", average)
    print("Highest grade:", highest_grade)
    print("Lowest grade:", lowest_grade)
    print("Students passed:", count)    

grades = [75, 82, 59, 90, 60, 45]

analyse_grades(grades)

'''

# Excercise 4

def calculate_factorial(number):
    """
    Calculate and return the factorial of a non-negative integer.

    The factorial of n is the product of all integers from 1 to n.
    For example, 5! = 5 × 4 × 3 × 2 × 1 = 120.
    """
    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


def main():
    """Read a number from the user and print its factorial."""
    number = int(input("Number: "))
    factorial = calculate_factorial(number)
    print(factorial)


main()