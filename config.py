import os


class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = os.environ['MAILER_SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ['MAILER_DATABASE_URL']
    CSRF_ENABLED = True

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ['MAILER_USERNAME']
    MAIL_PASSWORD = os.environ['MAILER_PASSWORD']
    MAIL_DEFAULT_SENDER = '"Mail robot" <{0}>'.format(os.environ['MAILER_SENDER'])

    # USER_ENABLE_USERNAME = True
    USER_ENABLE_CONFIRM_EMAIL = True
    # USER_ENABLE_CHANGE_USERNAME = True
    USER_ENABLE_CHANGE_PASSWORD = True
    USER_ENABLE_FORGOT_PASSWORD = True
    USER_ENABLE_RETYPE_PASSWORD = True
    USER_LOGIN_TEMPLATE = 'flask_user/login_or_register.html'
    USER_REGISTER_TEMPLATE = 'flask_user/login_or_register.html'
