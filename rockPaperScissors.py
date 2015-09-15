import random

__author__ = 'dealen'


class GameFigure:

    def __init__(self, number, name, danger1, danger2, prey1, prey2):
        self.list_of_dangers = [danger1, danger2]
        self.list_of_preys = [prey1, prey2]
        self.name = name
        self.number = number

    number = ""
    list_of_dangers = []
    list_of_preys = []
    name = ""

    def is_in_danger(self, computer_type):
        if self.is_draw(computer_type.name):
            return 1
        if computer_type.name in self.list_of_dangers:
            return 2
        if self.is_won(computer_type.name):
            return 3
        return 2

    def is_won(self, c_name):
        if c_name in self.list_of_preys:
            return True
        return False

    def is_draw(self, c_name):
        if self.name == c_name:
            return True
        return False

listOfGameFigures = [
    GameFigure("1", "Rock", "Paper", "Spock", "Lizard", "Scissors"),
    GameFigure("2", "Paper", "Scissors", "Lizard", "Spock", "Rock"),
    GameFigure("3", "Scissors", "Spock", "Rock", "Lizard", "Paper"),
    GameFigure("4", "Spock", "Lizard", "Paper", "Scissors", "Rock"),
    GameFigure("5", "Lizard", "Rock", "Scissors", "Spock", "Paper")
]

print('Welcome in game Rock Paper Scissors Spock Lizard game!')

gamer_choice = ''

# main game loop
while gamer_choice != '-1':
    gamer_choice = input("Choose your symbol :"
                         "\n1 - Rock\n2 - Paper\n3 - Scissors"
                         "\n4 - Spock\n5 - Lizard\n\nTo close write '-1'\n")

    print('Gamer choice: ', gamer_choice)
    gamer_chosen_item = GameFigure

    if gamer_choice != '-1':
        for i in listOfGameFigures:
            if str(gamer_choice) == str(i.number):
                print(' in for -', i.name, ' ', i.number)
                gamer_chosen_item = i

        print('You have chosen ', gamer_chosen_item.name)
        computer_choice = random.choice(listOfGameFigures)
        print('Computer have chosen ', computer_choice.name)
        result = gamer_chosen_item.is_in_danger(computer_choice)

        if result == 3:
            print('You have lost...')
        elif result == 2:
            print('You have won!')
        elif result == 1:
            print('Draw')
