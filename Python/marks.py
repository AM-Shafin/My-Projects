marks = [77, 76, 65, 78, 62, 64, 60, 77, 75, 79]
while True:
    roll = input('Please enter your roll number: ')
    if int(roll) > len(marks) or int(roll) < 0:
        print('Roll Number not found.')
        quit()
    else:
        print('Your mark is', marks[int(roll)-1])
