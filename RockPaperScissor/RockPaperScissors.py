import random

def play():
    user = input("Your choice?\t'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'
    
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost!'

def is_win(p, o): # p represent Player and o represent Opponent
    #return true if the player wins
    if (p == 'r' and o == 's') or (p == 's' and o == 'p') or (p == 'p' and o == 'r'):
        return True
    return False

print(play())