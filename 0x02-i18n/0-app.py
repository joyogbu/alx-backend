#!/usr/bin/env python3
'''basic flask app'''


from flask import Flask


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    '''defining the index page'''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0")
