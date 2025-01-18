#damn bro is grinding through the night frfr, so proud of bro(python loops - for loops,ranges and code blocks)
#a simple for loop(takes a var called fruit and uses it to iterate all of the items in the list)
fruits = ['peach','cherry','apple']
for fruit in fruits:
    print('Big ' + fruit + ' pie')
#height average exercise
student_heights = input("Enter student heights separated by spaces: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# Calculate the average
total_height = 0
length = 0
for height in student_heights:
    total_height += height
    length += 1
average_height = total_height / length
print(average_height)