from models.player import *
import random


class Game:

    choices = ["rock", "paper", "scissors"]
    # computer = choices[randint(0, 2)]

    def game_winner(self, player1, player2):

        if player1.choice not in self.choices or player2.choice not in self.choices:
            return "Invalid Entry, Please try again"
        if player1.choice == player2.choice:
            return "its a draw"
        winner = player1.name

        if player1.choice == "rock" and player2.choice == "paper":
            winner = player2.name
        elif player1.choice == "paper" and player2.choice == "scissors":
            winner = player2.name
        elif player1.choice == "scissors" and player2.choice == "rock":
            winner = player2.name
        return winner

    def computer_random_choice(self):
        return random.choice(self.choices)
