from app import app, db
from models import User

with app.app_context():
    db.create_all()


def init_db():
    with app.app_context():
        db.session.add(User(
            email='sk@yt.ru', password='sk', confirmed_at='2014-08-18',
            channel_title=u'My dogs'))
        db.session.add(User(
            email='ad@min.ru', password='admin', confirmed_at='2014-08-18',
            channel_title=u'My servers'))
        db.session.add(User(
            email='dummy@ru.ua', password='dummy', confirmed_at='2014-08-18',
            channel_title=u'My cats'))
        db.session.commit()

if __name__ == '__main__':
    import sys
    if '--init_db' in sys.argv:
        init_db()
