from flask import render_template

__author__ = 'Laim'

from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
