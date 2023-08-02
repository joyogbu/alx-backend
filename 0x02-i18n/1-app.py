#!/usr/bin/env python3
'''module for flask babel'''


from flask import Flask
from flask_babel import Babel


app = Flask(__name__)
# app.config.from_pyfile('mysettings.cfg')
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


babel = Babel(app)


class Config(object):
    '''defining class for babel configurations'''
    LANGUAGES = ["en", "fr"]

# app.config.from_object(Config)
# app.config['BABEL_DEFAULT_LOCALE'] = 'en'
# app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
