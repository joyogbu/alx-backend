#!/usr/bin/env python3
'''mockimg user log in'''


from flask import Flask, render_template, g
from flask_babel import Babel
from flask import request


app = Flask(__name__)
babel = Babel(app)


# @app.route('/<login_as>')
def get_user(login_as):
    '''defining the function'''
    users = {
            1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
            2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
            3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
            4: {"name": "Teletubby", "locale": None,
                "timezone": "Europe/London"},
            }
    user_dict = {}
    if login_as is None:
        return None
    # for k, v in users.items():
    if login_as not in users:
        return None
    for k, v in users.items():
        if k == login_as:
            user_dict[login_as] = users.get(v)
    return (user_dict)
    # return render_template('5-html', user = user_dict)


@app.before_request
def before_request(login_as):
    '''defining the function'''
    user = get_user(login_as)
    g.user = user


@app.route('/<login_as>')
def index():
    '''defining the function'''
    if g.user is not None:
        return render_template('5-index.html', user=g.user)


'''runnng the app'''
if __name__ == "__main__":
    app.run(host='0.0.0.0')
