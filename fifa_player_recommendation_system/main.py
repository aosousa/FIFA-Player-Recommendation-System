from fifa_player_recommendation_system.modules import db, model, server, utils

if __name__ == '__main__':
    # create DB connection
    db.connect()

    # train the model
    model.train()

    # run Flask server
    server.run_server()