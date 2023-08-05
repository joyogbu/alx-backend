#!/usr/bin/env python3
'''module for parameterize template'''


from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    '''defining class for babel configurations'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    '''defining the function'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    '''defining the gettext function'''
    # home_title = _('Welcome to Holberton')
    # home_header = _('Hello world!')
    return render_template('3-index.html')


if __name__ == "__main__":
    '''runing rhe flask qpp'''
    app.run(host='0.0.0.0')
