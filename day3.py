#wowieee broski got into day 3 dayum and you didn't stop crazy grind frfr(conditional statements,logical operators,code blocks, scope)
#conditional statements in python
day = 'friday'
if day == 'friday':
    print("weekend")
else:
    print('work')
    
#logical operators in python = ( >,<,>=,<=,=,==,!= ) ik what this means os need to be descriptive

#is the number odd or even program
user_input = int(input("What's your selected number to check?\n"))
if user_input % 2 == 0:
    print(f"{user_input} is an even number.")
else:
    print(f"{user_input} is an odd number.")

#nested if/else statement using an amusement part roller coaster ticket entry
print("Welcome to the rollercoaster, please elaborate with the questions to buy tickets")
height = int(input("What's your height in cm?\n"))
age = int(input("What's your age?\n"))
if height >= 120:
    if age <= 12:
        print("The ticket price is 7$")
    elif age >= 18:
        print("The ticket price is 10$")
    else:
        print("The ticket price is 14$")
else:
    print("You're not tall enough to enter the rollercoaster sorry!")
    
#bmi 2.0
print("Welcome to the upgraded bmi calculator")
weight = float(input("What's your weight in kg?\n"))
height = float(input("What's your height in meters?\n"))
bmi = weight / (height ** 2)
if bmi <= 18.5:
    print(f"{bmi}, Underweight")
elif bmi <= 25:
    print(f"{bmi}, Normal weight")
elif bmi <= 30:
    print(f"{bmi}, Lil bulky")
else:
    print(f"{bmi}, Obese, Stop eating start gyming")
    
#stupid ahh leap year program
year = int(input("What's the year?\n"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")