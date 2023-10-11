import random
from IPython.display import clear_output

#create a dictionary of choices, key beats 1st value & loses to 2nd value in list
choices = {"rock": ["scissors", "paper"],
          "paper": ["rock", "scissors"],
        "scissors": ["paper", "rock"]}


class Game():
    def __init__(self):
        pass

    def game(self):
        while True:

            #cpu makes choice, alert player cpu has choosen
            cpu_choice = list(choices.keys())[random.randint(0, len(list(choices.keys())) -1)] #using randint for cpu to make choice
            #random.choice(list(choices.keys()))    #more precise way for cpu to make choice
            print("CPU has choosen!\n")

            #ask usr for an action
            action = str(input("Choose rock, paper or scissors!\n\nPress R for rock\nPress P for Paper\nPress S for scissors\nOr press q to quit\n"))

            #decision tree based on action taken
            if action.lower() == "q":
                clear_output()
                print("Thank you for playing!")
                break
            if action.lower() == "p":
                user_choice = "paper"
            if action.lower() == "r":
                user_choice = "rock"
            if action.lower() == "s":
                user_choice = "scissors"

            #elavuate usr choice vs cpu to determine winner
            if user_choice ==  cpu_choice:
                print("Game Tied!")
                print("Please choose again!\n")
            if cpu_choice == choices.get(user_choice)[0]:
                clear_output()
                print(f'CPU choose {cpu_choice}!')
                print(f'And you choose {user_choice}!\n')
                print("Congratulations you've won!!\n")
            if cpu_choice == choices.get(user_choice)[1]:
                clear_output()
                print(f'CPU choose {cpu_choice}!')
                print(f'And you choose {user_choice}!\n')
                print("You lose!\n")

game = Game()
game.game()