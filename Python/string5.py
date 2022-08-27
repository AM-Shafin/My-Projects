#input: Bangladesh
#Output: aBgnaledhs
#Makes a new string with swapped positions of elements that are side by side from original string
sen = input('Insert string: ')
char = []

for i in range(0, len(sen)-1, 2):
    char.append(sen[i+1])
    char.append(sen[i])
char.append(sen[-1])
print("".join(char))