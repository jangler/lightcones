import pathlib

import flask


app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html', title='news')


# generate URLs for static files
with app.test_request_context():
    for p in pathlib.Path('static').iterdir():
        flask.url_for('static', filename=str(p))


if __name__ == '__main__':
    app.run()
