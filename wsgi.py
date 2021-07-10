from main import application

if __name__ == "__main__":
    
    application.config['SESSION_TYPE'] = 'filesystem'
    application.run()