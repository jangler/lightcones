import os

import flask


app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html', title='lightcones')


# generate URLs for static files
with app.test_request_context():
    for dirpath, dirnames, filenames in os.walk('static'):
        for filename in filenames:
            flask.url_for('static', filename=dirpath+filename)


if __name__ == '__main__':
    app.run()
