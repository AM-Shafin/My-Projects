# input: Hello Test! 123 123, good.
# Output: expected
# Enter a string: Hello Test! 123 123, good.
# HT
# elloestgood
# 123123
# !  , .
def separate(str):
    uppercase, lowercase, digit, other = '', '', '', ''
    for char in str:
        if char.isupper():
            uppercase += char
        elif char.islower():
            lowercase += char
        elif char.isdigit():
            digit += char
        else:
            other += char
        
    print(uppercase, '\n', lowercase, '\n', digit, '\n', other)

sentence = input('Input: ').strip()
separate(sentence)


