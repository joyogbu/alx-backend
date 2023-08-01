#!/usr/bin/env python3
'''basic flask app'''


# from 1-app import config
from flask import Flask, render_template


app = Flask(__name__)
# app.config.from_object(config)
# app.config['BABEL_DEFAULT_LOCALE'] = "en"
# app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


"""@babel.localeselector
def get_locale():
    '''defining the function'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])
"""

@app.route('/', strict_slashes=False)
def index():
    '''defining the index page'''
    return render_template('0-index.html')


'''running the flask app'''
if __name__ == "__main__":
    app.run(host="0.0.0.0")
