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
