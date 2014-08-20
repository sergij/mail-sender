# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from flask import Flask, url_for, redirect, render_template, request
from flask.ext.babel import Babel
from flask.ext.mail import Mail
from flask.ext.user import UserManager, SQLAlchemyAdapter
from flask.ext.user import current_user, login_required


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    babel = Babel(app)
    mail = Mail(app)
    from models import db, User, SubscriberAssociation

    db.init_app(app)
    db_adapter = SQLAlchemyAdapter(db, User)
    UserManager(db_adapter, app)

    @app.route('/subscriptions')
    @login_required
    def subscriptions_page():
        my_subscriptions = current_user.subscriptions
        return render_template('subscriptions.html')

    @app.route('/subscribe/<channel_id>', methods=['POST', 'DELETE'])
    @login_required
    def sub_unsub_action(channel_id):
        if request.method == 'DELETE':
            SubscriberAssociation.query.filter_by(
                author_id=channel_id, subscriber_id=current_user.id).delete()
            return {'success': True}
        if not db.session.query(db.exists().where(User.id == channel_id)).scalar():
            return {'success': False}
        new_subscribe = SubscriberAssociation(author_id=channel_id, subscriber_id=current_user.id)
        db.session.add(new_subscribe)
        db.session.commit()
        return {'success': True}

    @app.route('/')
    def home_page():
        if current_user.is_authenticated():
            return redirect(url_for('subscriptions_page'))
        else:
            return redirect(url_for('user.login'))

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
