from main import application

if __name__ == "__main__":
    application.secret_key = 'resdust'
    application.config['SESSION_TYPE'] = 'filesystem'
    application.run()