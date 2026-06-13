#EXCERCISE1
'''
month=int(input("Please enter a valid month number to give you its season \n"))
if month in (12,1,2):
    print("It's summer")
elif month in (3,4,5):
    print ("It's Autamn")
elif month in (6,7,8):
    print ("It's winter")
elif month in (9,10,11):
    print("It's spring")
else:
    print("Invalid number")
    
    '''
'''
#Excercise2
weight = float(input("Please enter your weight in kg \n"))
height = float(input("please enter your height in m \n"))
if height>2.5:
    height=height/100
BMI = weight / (height**2)
if BMI <18.5:
    print ("Underweight")
elif 18.5<=BMI<24.9:
    print ("Normal")
elif 24.9<= BMI <30:
    print ("Overweight")
else:
    print ("Obese")
 '''   
'''
# Excercise 3
kwh = float(input("Enter the number of kWh consumed: "))

total_bill = 0.0

if kwh <= 100:
    total_bill = kwh * 0.40
elif kwh <= 300:
    total_bill = (100 * 0.40) + ((kwh - 100) * 0.65)
else:
    total_bill = (100 * 0.40) + (200 * 0.65) + ((kwh - 300) * 0.95)

print (" The bill total is : ", total_bill)       
'''
# Excercise 4
print("You will play 'Paper, Rock, Scissors' against the computer")
choice = input("Please enter your choice \n").lower().strip()
computer_choice = "rock"

# Check if the choice is valid by looking inside a list
if choice not in ["paper", "scissors", "rock"]:
    print("Your choice is out of game")
elif choice == computer_choice:
    print("We are equal!! , it's the same to computer's choice")
elif choice == "paper":
    print("Congratulations! Paper covers rock. You win!")
elif choice == "scissors":
    print("Unfortunately, you lose. Rock smashes scissors.")
