# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from flask import Flask, redirect, render_template, url_for
from flask.ext.babel import Babel
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.user import current_user, login_required

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)

babel = Babel(app)
mail = Mail(app)


@app.route('/')
def home_page():
    if current_user.is_authenticated():
        return redirect(url_for('subscriptions_page'))
    else:
        return redirect(url_for('user.login'))


@app.route('/subscriptions')
@login_required
def subscriptions_page():
    return render_template("subscriptions.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
