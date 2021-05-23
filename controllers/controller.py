from flask import render_template, request, redirect
from app import app
from models.game import Game
from models.player import Player


@app.route('/')
def home():
    return render_template('base.html', title='Home')


@app.route('/rules')
def rules():
    return render_template('home.html', title='Rules')


@app.route('/<player1_choice>/<player2_choice>')
def rock_paper_scissors(player1_choice, player2_choice):
    player1 = Player("Saad", player1_choice)
    player2 = Player("Lukas", player2_choice)
    winner = Game().game_winner(player1, player2)
    # if winner:
    #     result = f"{winner} wins by playing {winner}"
    # else:
    #     result = "its a draw"
    return render_template('result.html', player1=player1, player2=player2, winner=winner)


@app.route('/play')
def lets_play():
    return render_template('play_game.html', title="play game")


@app.route("/play", methods=["POST"])
def get_player1_name():
    title = "Play Game"
    player1 = Player(request.form["player1_name"],
                     request.form["player1_selection"])

    random_choice = Game().computer_random_choice()
    player2 = Player("Computer", random_choice)

    winner = Game().game_winner(player1, player2)

    return render_template("play_game.html", title=title, player1_name=player1.name, player1_choice=player1.choice, player2_name=player2.name, player2_choice=player2.choice, winner=winner)
