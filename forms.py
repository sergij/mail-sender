from __future__ import unicode_literals

from wtforms import Form, TextAreaField, SubmitField, validators, TextField
from flask.ext.security.forms import RegisterForm


class ExtendedRegisterForm(RegisterForm):
    chanel_title = TextField('Channel title', [validators.Required()])


class ContactForm(Form):
    message = TextAreaField('Message', [validators.Required('Please enter a message.')])
    submit = SubmitField('Send')
