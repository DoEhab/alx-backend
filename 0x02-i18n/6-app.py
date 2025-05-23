#!/usr/bin/env python3
"""
flask app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    lang configuration class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """
    Retrieve user dictionary based on 'login_as' URL parameter
    """
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """
    Executed before each request
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    determine the best match with our supported languages
    """
    locale_param = request.args.get("locale")
    if locale_param in Config.LANGUAGES:
        return locale_param

    if g.get('user'):
        user_locale = g.user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def basic_app():
    """
    basic_app method
    :return: html page
    """
    locale = get_locale()
    return render_template("5-index.html", locale=locale)


if __name__ == '__main__':
    app.run()
