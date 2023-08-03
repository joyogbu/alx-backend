#!/usr/bin/env python3
'''module for get locale'''


from flask import Flask, render_template
from flask_babel import Babel
from flask import request


app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    '''defining the function'''
    if request.args.get(locale):
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    '''defining the function'''
    return render_template('2-index.html')


'''runnng the app'''
if __name__ == "__main__":
    app.run(host='0.0.0.0')
