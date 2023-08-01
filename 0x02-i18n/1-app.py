#!/usr/bin/env python3
'''module for flask babel'''


from flask_babel import Babel


app = Flask(__name__)
# app.config.from_object(Config)


babel = Babel(app)


class Config(object):
    '''defining class for babel configurations'''
    LANGUAGES = ["en", "fr"]

    @babel.localeselector
    def get_locale():
        '''defining the function'''
        return request.accept_languages.best_match(app.config['LANGUAGES']) 
