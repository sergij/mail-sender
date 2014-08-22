# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from flask import Flask
from flask.ext.babel import Babel
from flask.ext.mail import Mail
from flask.ext.user import UserManager, SQLAlchemyAdapter


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
babel = Babel(app)
mail = Mail(app)
from models import db, User
from forms import ExtendedRegisterForm

db.init_app(app)
db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter, app, register_form=ExtendedRegisterForm)
from views import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
