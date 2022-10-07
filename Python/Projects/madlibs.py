# string concatenation (aka how to put string together)
# suppose we want to create a string that says "Good morning, _____ "
from msilib.schema import Verb


guest = 'Shafin' # some string variable

# a few wasy to do this
# print("Good morning, "+guest)
# print("Good morning, {}".format(guest))
# print(f"Good morning, {guest}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)