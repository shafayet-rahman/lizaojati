#WOWWWW bro's doing the work frfr(wifey effect) day4(randomisation and lists in python)
#you must first import the random module
import random
#you must thn use the random module and use the methods given with it(the code below outputs a random number 1 - 10)
random_int = random.randint(1,10)
print(random_int)
#random float 
random_float = random.random() * 5 #outputs a floating number between 0 - 1 multiplied by five
#you import other python files from the same folder 
"""import day3
print(day3.day) #will import the day variable from day 3 and output the value"""
#coin toss
toss = random.random()
if toss > 0.5:
    print("Heads")
else:
    print("Tails")

#Wowie we now have lists in python aka arrays in js
dhaka = ['uttara','Gulshan','banani','purandhaka']
#we can access lists by using square after the var name and using the index we want as arg,+1 = counting from the start,-1 = counting from the finish
print(dhaka[1]) #Gulshan
print(dhaka[-1]) #purandhaka
# we can also assign the items within the lists
dhaka[2] = 'mirpur' #replaces banani with mirpur