"""
# Excercise 1
num1= int(input("Enter the first number "))
num2= int(input("Enter the second number "))
print (" The result of adding the two numbers is: ", num1+num2)
print (" The result of subtracting the two numbers is: ", num1-num2)
print (" The result of dividing the two numbers is: ", num1/num2)
print (" The result of multiplying the two numbers is: ", num1*num2)
print (" The result of floor divide the two numbers is: ", num1//num2)
print (" The modulo after dividing the two numbers is: ", num1%num2)
print (" The result of num1 ** num2: ", num1**num2)
"""
"""
# Exercise 2
word_from_user = input(" Please enter a sentence: ")
#1
print(" The sentence in upper case is: ", word_from_user.upper())
#2
print (" The number of charachters in the sentence is: ", len(word_from_user))
#3 
print (" The number of words in the sentence is: ", len(word_from_user.split( )))
#4 
print("Python" in word_from_user)
#5 
print (word_from_user[::-1])
"""
'''
# Excercise 3
num3= "3.7"
print("Lets start with string ", num3)
num3= float(num3)
print ("The float of string 3.7 is", num3 , " and its type is ", type(num3))
num3 = num3*4
print ("The multiplication 3.7 with is", num3 , " and its type is ", type(num3))
num3= int(num3)
print ("The int of the last result is", num3 , " and its type is ", type(num3))
num3 = str(num3)
print ("The string of the last result is", num3 , " and its type is ", type(num3))
'''

# Exercise 4
password= input("Please enter the password beginning with a letter   ")
#1
print("Is the password longer than 8 char.? ",len(password)>8 ) 
#2
print("Does it contain an uppercase letter? ",password != password.lower() ) 
#3
print("Does it start with a letter? ",password[0].isalpha() ) 