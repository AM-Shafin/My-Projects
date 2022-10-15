import random
from tkinter import *

# Dictionary and vars
schema = {
    "rock" : {"rock" : 1, "paper" : 0, "scissors" : 2},
    "paper" : {"rock" : 2, "paper" : 1, "scissors" : 0},
    "scissors" : {"rock" : 0, "paper" : 2, "scissors" : 1}
}
bot_score = 0
player_score = 0

# AfterButton pressed action handler function
def outcome_handler(user_choice):
    global bot_score
    global player_score
    outcomes = ['rock', 'paper', 'scissors']
    random_num = random.randint(0, 2)
    bot_choice = outcomes[random_num]
    result = schema[user_choice][bot_choice]

    player_choice_label.config(fg = "red", text = "Player Choice : "+str(user_choice))
    bot_choice_label.config(fg = "green", text = "Computer Choice : "+str(bot_choice))

    if result == 2:
        player_score += 2
        player_score_label.config(text = "Player : "+str(player_score))
        outcome_label.config(fg = "red", text = "Outcome : Player won")
    elif result == 1:
        player_score += 1
        bot_score += 1

        player_score_label.config(text = "Player : "+str(player_score))
        bot_score_label.config(text = "Bot : "+str(bot_score))
        outcome_label.config(fg = "blue", text = "Outcome : Draw")
    elif result == 0:
        bot_score += 2
        bot_score_label.config(text = "Bot : "+str(bot_score))
        outcome_label.config(fg = "green", text = "Outcome : Bot won!")



# Main screen
master = Tk()
master.title("Rock Paper Scissor")

# Labels
Label(master, text = "Rock, Paper, Scissors", font = ("Calibri", 14)).grid(row = 0, sticky = N, pady = 10, padx = 200)
Label(master, text = "Please select an option", font = ("Calibri", 12)).grid(row = 1, sticky = N)

# Player score on screen
player_score_label = Label(master, text = "Player  : 0", font = ("Calibri", 12))
player_score_label.grid(row = 2, sticky = W)
# AI score on screen
bot_score_label = Label(master, text = "Bot  : 0", font = ("Calibri", 12))
bot_score_label.grid(row = 2, sticky = E)

player_choice_label = Label(master, font = ("Calibri", 12))
player_choice_label.grid(row = 3, sticky = W)

bot_choice_label = Label(master, font = ("Calibri", 12))
bot_choice_label.grid(row = 3, sticky = E)

outcome_label = Label(master, font = ("Calibri", 12))
outcome_label.grid(row = 3, sticky = N)

# Buttons
Button(master, text = "Rock", width = 15, command = lambda: outcome_handler("rock")).grid(row = 4, sticky = W, padx = 5, pady = 5)
Button(master, text = "Paper", width = 15, command = lambda: outcome_handler("paper")).grid(row = 4, sticky = N, pady = 5)
Button(master, text = "Scissors", width = 15, command = lambda: outcome_handler("scissors")).grid(row = 4, sticky = E, padx = 5, pady = 5)

# Dummy label
Label(master).grid(row=5)


master.mainloop()