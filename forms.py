from __future__ import unicode_literals

from flask.ext.wtf import Form
from wtforms import TextAreaField, SubmitField, validators, TextField
from flask.ext.user.forms import RegisterForm


class ExtendedRegisterForm(RegisterForm):
    channel_title = TextField('Channel title', [validators.Required()])


class ContactForm(Form):
    message = TextAreaField('Message', [validators.Required('Please enter a message.')])
    submit = SubmitField('Send')
