# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.user import UserMixin

db = SQLAlchemy()


class SubscriberAssociation(db.Model):
    __tablename__ = 'subscriber_association'
    id = db.Column(db.Integer, primary_key=True)
    subscriber_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    subscriber = db.relationship('User', foreign_keys=subscriber_id, backref='subscriptions')
    author = db.relationship('User', foreign_keys=author_id, backref='subscribed_users')


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean(), nullable=False, default=False)
    password = db.Column(db.String(255), nullable=False, default='')
    email = db.Column(db.String(255), nullable=False, unique=True)
    confirmed_at = db.Column(db.DateTime())
    reset_password_token = db.Column(db.String(100), nullable=False, default='')
    channel_title = db.Column(db.String(50), nullable=True)


User.subscribers = db.relationship(
    SubscriberAssociation,
    primaryjoin=db.or_(
        User.id == SubscriberAssociation.author_id,
        User.id == SubscriberAssociation.subscriber_id),
    viewonly=True)
