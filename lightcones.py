import os

import flask
import markdown
import yaml


app = flask.Flask(__name__)


navlinks = (
    { 'name': 'admirations', 'href': '/admirations' },
    { 'name': 'collaborations', 'href': '/collaborations' },
    { 'name': 'fabrications', 'href': '/fabrications' },
    { 'name': 'index', 'href': '/' },
)


def render_newslist(datafile, tagline):
    with open('data/' + datafile) as f:
        newsitems = yaml.load(f)
    for ni in newsitems:
        ni['body'] = markdown.markdown(ni['body'])
    return flask.render_template(
            'newslist.html', newsitems=newsitems, tagline=tagline,
            title=datafile.split('.')[0], navlinks=navlinks)


def render_piclist(datafile, tagline):
    with open('data/' + datafile) as f:
        newsitems = yaml.load(f)
    return flask.render_template(
            'piclist.html', newsitems=newsitems, tagline=tagline,
            title=datafile.split('.')[0], navlinks=navlinks)


@app.errorhandler(404)
def error404(error):
    return flask.render_template(
            'newslist.html', title='http 404', navlinks=navlinks,
            tagline='there is actually no content here.'), 404


@app.errorhandler(500)
def error500(error):
    return flask.render_template(
            'newslist.html', title='http 500', navlinks=navlinks,
            tagline='because i am a bad programmer. please inform me.'), 500


@app.route('/')
def index():
    return flask.render_template(
            'index.html', title='index', navlinks=navlinks)


@app.route('/fabrications')
def fabrications():
    return render_newslist('fabrications.yaml', 'look on my works, ye mighty:')


@app.route('/collaborations')
def collaborations():
    return render_newslist('collaborations.yaml',
                           'i am merely a pawn in these games:')


@app.route('/admirations')
def admirations():
    return render_newslist('admirations.yaml', 'externalities to examine:')


@app.route('/portraits')
def portraits():
    return render_piclist('portraits.yaml', 'portraits of botbr personas:')


# generate URLs for static files
with app.test_request_context():
    for dirpath, dirnames, filenames in os.walk('static'):
        for filename in filenames:
            flask.url_for('static', filename=dirpath+filename)


if __name__ == '__main__':
    app.run()
