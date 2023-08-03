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
    loc = request.args.get('locale')
    if loc is not None:
        return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/<locale>')
def index():
    '''defining the function'''
    return render_template('4-index.html')


'''runnng the app'''
if __name__ == "__main__":
    app.run(host='0.0.0.0')
