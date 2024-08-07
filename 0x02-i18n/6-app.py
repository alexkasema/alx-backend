#!/usr/bin/env python3
""" Use user locale """

from flask_babel import Babel
from flask import Flask, g, render_template, request
from typing import Dict, Union


class Config:
    """ A configuration class to set up options """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """ gets a user based on their id """
    login_id = request.args.get('login_as', '')
    if login_id:
        return users.get(int(login_id), None)
    return None


@app.before_request
def before_request() -> None:
    """ get user before any other function is executed """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """ gets the language from the user accept header the browser transmits"""
    locale = request.args.get('locale', '')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    req_header_locale = request.headers.get('locale', '')
    if req_header_locale in app.config['LANGUAGES']:
        return req_header_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """The default route """
    return render_template('6-index.html',)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
