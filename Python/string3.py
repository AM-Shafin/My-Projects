text = " this is a string. "
print(text)
print(text.lstrip()) #lstrip() remove space from left side of the string
print(text.rstrip()) #rstrip() remove space from right side of the string
print(text.strip()) #strip() remove space from both side of the string

#Converting a string to UPPERCASE or lowercase
s1 = "Programming"
print(s1.upper())
print(s1.lower())
s2 = "hello"
print(s2.capitalize()) #Capitalizes the first word

str = "I  am  a  programmer"
words = str.split()

for word in words:
    print(word)

print(str.count('am')) #count() methode prints how many substrings are there in given string


#Use of startswith() and endswith() methodes 
#>>> s = "Bangladesh"
#>>> s.startswith("Ban")   
#True
#>>> s.startswith("ban")
#False
#>>> s.startswith("an")
#False
#>>> s.endswith("Ban")
#False
#>>> s.endswith("desh")
#True
#>>> s.endswith("h")
#True

name = "Mr. Anderson"
if name.startswith('Mr.'):
    print('Dear Sir')