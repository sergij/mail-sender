
from __future__ import unicode_literals

from flask import url_for, redirect, render_template, request
from flask.ext.mail import Message
from flask.ext.user import current_user, login_required

from app import app, mail
from forms import ContactForm
from models import db, User, SubscriberAssociation


@app.route('/subscriptions')
@login_required
def subscriptions_page():
    subscriptions = User.query.filter(User.id.in_(
        [o.author_id for o in current_user.subscriptions])).all()
    show_all = request.args.get('subscriptions', '') != '1'
    other_channels = (
        User.query.filter(db.not_(User.id.in_(
            [o.author_id for o in current_user.subscriptions]))).all()
        if show_all else [])
    return render_template(
        'subscriptions.html',
        subscriptions=subscriptions,
        other_channels=other_channels)


@app.route('/')
def home_page():
    if current_user.is_authenticated():
        return redirect(url_for('subscriptions_page'))
    else:
        return redirect(url_for('user.login'))


@app.route('/subscribe/<channel_id>', methods=['GET'])
@login_required
def subscribe(channel_id):
    if not db.session.query(db.exists().where(User.id == channel_id)).scalar():
        return redirect(request.referrer)
    new_subscribe = SubscriberAssociation(author_id=channel_id, subscriber_id=current_user.id)
    db.session.add(new_subscribe)
    db.session.commit()
    return redirect(request.referrer)


@app.route('/unsubscribe/<channel_id>', methods=['GET'])
@login_required
def unsubscribe(channel_id):
    SubscriberAssociation.query.filter_by(
        author_id=channel_id, subscriber_id=current_user.id).delete()
    db.session.commit()
    return redirect(request.referrer)


def send_mails(message, recipients):
    subject = 'Notification from postman'
    with mail.connect() as conn:
        for user in recipients:
            msg = Message(
                recipients=[user.email],
                body=message,
                subject=subject)
            conn.send(msg)


@app.route('/send-notifications', methods=['POST', 'GET'])
@login_required
def send_notifications():
    form = ContactForm()
    if form.validate_on_submit():
        recipients = [o.subscriber for o in current_user.subscribers]
        send_mails(form.message.data, recipients)
    return render_template('send-notifications.html', form=form)
