#!/usr/bin/env python3
'''module for get locale'''


from flask import request


@babel.localeselector
def get_locale() -> str:
    '''defining the function'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])
