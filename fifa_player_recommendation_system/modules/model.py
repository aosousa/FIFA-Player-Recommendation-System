import pandas as pd

from fifa_player_recommendation_system.modules import db

player_columns = ['ID', 'Short Name', 'Full Name', 'Overall', 'Potential', 'Value', 
        'Position', 'Nationality', 'Picture URL', 'Age', 'Height (cm)', 'Weight (kg)', 
        'Club', 'League', 'Wage (€)', 'Release Clause (€)', 'Preferred Foot', 'Player Stats ID',
        'Player ID', 'Game Version', 'Weak Foot', 'Skill Moves', 'Attacking Work Rate',
        'Defensive Work Rate', 'Crossing', 'Finishing', 'Heading Accuracy', 'Short Passing',
        'Volleys', 'Dribbling', 'Curve', 'Free Kick Accuracy', 'Long Passing', 'Ball Control',
        'Acceleration', 'Sprint Speed', 'Agility', 'Reactions', 'Balance', 'Shot Power',
        'Jumping', 'Stamina', 'Strength', 'Long Shots', 'Aggression', 'Interceptions',
        'Positioning', 'Vision', 'Penalties', 'Composure', 'Marking', 'Standing Tackle',
        'Sliding Tackle', 'GK Diving', 'GK Handling', 'GK Kicking', 'GK Positioning', 
        'GK Reflexes', 'Pace Total', 'Shooting Total', 'Passing Total', 'Dribbling Total',
        'Defending Total', 'Physicality Total', 'ST Rating', 'LW Rating', 'LF Rating',
        'CF Rating', 'RF Rating', 'RW Rating', 'CAM Rating', 'LM Rating', 'CM Rating',
        'RM Rating', 'LWB Rating', 'CDM Rating', 'RWB Rating', 'LB Rating', 'CB Rating',
        'RB Rating', 'GK Rating']

# def preprocess_training_data():

def train():
    global player_columns 

    players = db.get_players()
    players_df = pd.DataFrame(players)
    players_df.columns = player_columns

    # drop unnecessary columns before training
    players_df = players_df.drop(columns=['ID', 'Short Name', 'Full Name', 'Nationality', 'Picture URL',
    'Club', 'League', 'Wage (€)', 'Release Clause (€)', 'Player Stats ID', 'Player ID', 'Pace Total',
    'Shooting Total', 'Passing Total', 'Dribbling Total', 'Defending Total', 'Physicality Total', 
    'ST Rating', 'LW Rating', 'LF Rating', 'CF Rating', 'RF Rating', 'RW Rating', 'CAM Rating', 
    'LM Rating', 'CM Rating', 'RM Rating', 'LWB Rating', 'CDM Rating', 'RWB Rating', 'LB Rating', 
    'CB Rating', 'RB Rating', 'GK Rating'])

    print(players_df)

# def get_evaluation_metrics(clf, x, y)