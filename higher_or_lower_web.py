from flask import Flask
import random

horl = Flask(__name__)
ai = random.randint(0,9)
@horl.route('/')
def guess():
    return "<h1>Guess the Number from 0 to 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"
@horl.route('/<num>')
def check(num):
    if int(num) == ai:
        return '<h1>Yay!, You\'ve found it.</h1>' \
               '<img src="https://media.giphy.com/media/v7xG9f3ybYDDy/giphy.gif">'
    elif int(num) > ai:
        return '<h1>Too High!</h1>' \
               '<img src="https://media.giphy.com/media/yXBqba0Zx8S4/giphy.gif">'
    else:
        return '<h1>Too Low!</h1>' \
               '<img src="https://media.giphy.com/media/12bpEjD05ac2IM/giphy.gif">'

if __name__ == "__main__":
    horl.run(debug=True)
