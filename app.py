from flask import Flask , session
from flask.globals import request
from flask.json import jsonify
from flask.templating import render_template
from boggle import Boggle

app = Flask(__name__)
boggle_game = Boggle()
app.config["SECRET_KEY"] = "this_is_a_secret_key_that_has_to_be_used_to_access_the_session"


@app.route("/")
def home():
    board = boggle_game.make_board()
    session["board"] = board
    return render_template("home.html",board = board)



@app.route("/check-valid-word")
def check_valid_word():
    board = session["board"]
    word = request.args["word"]
    session["word"] = word
    valid_word = boggle_game.check_valid_word(board,word)
    print(valid_word)
    return jsonify({'result': valid_word})
