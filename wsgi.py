from main import application
from flask import session

sess = session()

if __name__ == "__main__":
    application.secret_key = 'secret'
    application.config['SESSION_TYPE'] = 'filesystem'
    sess.init_app(application)
    application.run()