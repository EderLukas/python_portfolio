from flask import Flask
import random
app = Flask(__name__)

rnd = random.randint(0, 9)


@app.route('/')
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/l378khQxt68syiWJy/giphy.gif" >'


@app.route("/<int:guess>")
def guess_the_number(guess):

    if guess > rnd:
        return "<h1 style='color: blue'> Too hight, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' >"
    elif guess < rnd:
        return "<h1 style='color: red'> Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' >"
    elif guess == rnd:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' >"


if __name__ == '__main__':
    app.run(port=8000, debug=True)
