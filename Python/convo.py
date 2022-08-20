import turtle 

name = turtle.textinput('name', 'What is your name? ')
name = name.lower()
if name.startswith('mr'):
    print('Hello Sir, how are you?')
elif name.startswith('mrs') or name.startswith('ms') or name.startswith('miss'):
    print('Hello Madam, how are you?')
else:
    name = name.capitalize()
    print('Hi', name, '! How are you?')
    print(str)

turtle.exitonclick()