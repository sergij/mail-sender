# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from flask.ext.script import Manager
from flask.ext.user import UserManager, SQLAlchemyAdapter
from wtforms import validators, TextField
from flask.ext.security import Security
from flask.ext.security.forms import RegisterForm


class ExtendedRegisterForm(RegisterForm):
    chanel_title = TextField('Название канала', [validators.Required()])


from app import app, db
app.config.from_object(os.environ['APP_SETTINGS'])

from models import User

db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter, app)
security = Security(app, user_manager, register_form=ExtendedRegisterForm)

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
