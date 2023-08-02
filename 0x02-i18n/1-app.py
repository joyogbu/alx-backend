#!/usr/bin/env python3
'''module for flask babel'''


from flask import Flask
from flask_babel import Babel


app = Flask(__name__)


babel = Babel(app)


class Config(object):
    '''defining class for babel configurations'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@app.route('/', strict_slashes=False)
def index():
    '''defining the function'''
    return render_template('1-index.html')


app.config.from_object(Config)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
