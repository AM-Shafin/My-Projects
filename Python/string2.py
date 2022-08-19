a = 'New string'
print(a.find('w', 1, 3))
print(a.find('i', 1, 3)) 

sen = input("Enter sentence: ")
find = input("What word would you like to find: ")
replaceword = input("What is the new word?")

newsen = sen.replace(find, replaceword)

print(newsen)