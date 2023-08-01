#!/usr/bin/env python3
'''module for flask babel'''


from flask_babel import Babel


app = Flask(__name__)


babel = Babel(app)


class Config(object):
    '''defining class for babel configurations'''
    LANGUAGES = ["en", "fr"]
