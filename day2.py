# wowie we made it to day 2
#integers-----------------
#we can select a character of a string by using [] and putting in the index of the char we want as arg, this is also called subscripting
print("hello"[4])

#anything inside a string is a string even numbers so the code below will just concatenate the two strings
print("123" + "345")

#numbers outside a string is deemed as interger,below is a normal sum print 
print(3999+670)

#when writing large numbers we use commas such as 345,679,978 but in python we can just use underscored instead of commas
print(123_456_789)

#floooooats in py(anything with a decimal)
print(3.14)

#the key to conditionals the damn booleans
print(True)

#checking previous day1 error
error = 7
solved_error = str(error)
print(solved_error + ' ' + "Days")

#type conversion exercise
user_input = input("what's your input?\n")
digit_one = int(user_input[0])
digit_two = int(user_input[1])
user_input_added = digit_one + digit_two
output = str(user_input_added)
print("Your two digits added: " + output)

#Mathematics in python
print(1+1)
print(1-1)
print(1*2)
print(9/3) #when doing division the result will be float
print(5**5)

#BMI calculator 
#weight = int(input("What's your weight in kgs?\n"))
#height = float(input("What's your height in meters?\n"))
#Bmi = weight / height ** 2
#Bmi_output = int(Bmi)
#print(Bmi_output)

#rounding in python 
print(round(8/3)) #3
print(round(8/3,2)) #rounds up to two decimals = 2.67
print(8//3) #no bs direct 2 = how many times you can divide it by 3
 #assignment shorcuts
x = 5
x += 1 #x = x + 1
x -= 1 #x = x - 1
x *= 2 #x = x * 2 
x /= 2 #x = x / 2
x %= 2 #x = x % 2