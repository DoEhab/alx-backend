#!/usr/bin/env python3
"""
flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel


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


@babel.localeselector
def get_locale() -> str:
    """
    determine the best match with our supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def basic_app() -> str:
    """
    :return: html page
    """
    return render_template("3-index.html")


if __name__ == '__main__':
    app.run()
