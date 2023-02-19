import pandas as pd

from fifa_player_recommendation_system.modules import db, utils

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)

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

work_rates = {
    'Low': 1,
    'Medium': 2,
    'High': 3
}

def train():
    global player_columns, work_rates

    players = db.get_players()
    players_df = pd.DataFrame(players)
    players_df.columns = player_columns

    # extract only the columns that will be used for similarity comparison
    stats_data_df = players_df.iloc[:, 20:58]
    stats_data_df['Attacking Work Rate'] = stats_data_df['Attacking Work Rate'].map(work_rates)
    stats_data_df['Defensive Work Rate'] = stats_data_df['Defensive Work Rate'].map(work_rates)

    # drop unnecessary columns before training
    # players_train_df = players_df.drop(columns=['ID', 'Short Name', 'Full Name', 'Overall', 'Potential', 'Value', 
    #     'Nationality', 'Picture URL', 'Club', 'Age', 'Height (cm)', 'Weight (kg)', 'League', 'Wage (€)', 'Release Clause (€)', 
    #     'Preferred Foot' 'Player Stats ID', 'Player ID', 'Game Version', 'Pace Total', 'Shooting Total', 'Passing Total', 
    #     'Dribbling Total', 'Defending Total', 'Physicality Total', 'ST Rating', 'LW Rating', 'LF Rating', 'CF Rating', 'RF Rating', 
    #     'RW Rating', 'CAM Rating', 'LM Rating', 'CM Rating', 'RM Rating', 'LWB Rating', 'CDM Rating', 'RWB Rating', 'LB Rating', 
    #     'CB Rating', 'RB Rating', 'GK Rating'])