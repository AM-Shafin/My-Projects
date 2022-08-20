#input: Hello
#output: No
#input: madam
#output: Yes
#A functions that prints yes if input is 
def ispalindrome(s):
    s = s.lower()
    n = int(len(s))
    for i in range(0, n//2):
        if s[i] != s[n-i-1]:
            return False
    return True    

sen = str(input("Insert your word: "))
if(ispalindrome(sen)):
    print('Yes')
else:
    print('No')

