import pandas as pd
import math

from fifa_player_recommendation_system.modules import db, utils
from scipy.spatial import distance
from numpy import dot
from numpy.linalg import norm

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

def calculate_similarity(player_1: list, player_2: list):
    """Calculate the similarity between 2 players using cosine similarity

    Args:
        player_1: First player's information
        player_2: Second player's information

    Returns: Similarity between two players as a numeric score (higher is better)
    """

    # TODO: most important attributes per position

    if player_1['Position'] == 'GK':
        player_1_stats = player_1[['GK Diving', 'GK Handling', 'GK Kicking', 'GK Positioning', 'GK Reflexes']]
    else:
        player_1_stats = player_1[['Weak Foot', 'Skill Moves', 'Attacking Work Rate',
            'Defensive Work Rate', 'Crossing', 'Finishing', 'Heading Accuracy', 'Short Passing',
            'Volleys', 'Dribbling', 'Curve', 'Free Kick Accuracy', 'Long Passing', 'Ball Control',
            'Acceleration', 'Sprint Speed', 'Agility', 'Reactions', 'Balance', 'Shot Power',
            'Jumping', 'Stamina', 'Strength', 'Long Shots', 'Aggression', 'Interceptions',
            'Positioning', 'Vision', 'Penalties', 'Composure', 'Marking', 'Standing Tackle',
            'Sliding Tackle']]

    if player_2['Position'] == 'GK':
        player_2_stats = player_2[['GK Diving', 'GK Handling', 'GK Kicking', 'GK Positioning', 'GK Reflexes']]
    else:
        player_2_stats = player_2[['Weak Foot', 'Skill Moves', 'Attacking Work Rate',
            'Defensive Work Rate', 'Crossing', 'Finishing', 'Heading Accuracy', 'Short Passing',
            'Volleys', 'Dribbling', 'Curve', 'Free Kick Accuracy', 'Long Passing', 'Ball Control',
            'Acceleration', 'Sprint Speed', 'Agility', 'Reactions', 'Balance', 'Shot Power',
            'Jumping', 'Stamina', 'Strength', 'Long Shots', 'Aggression', 'Interceptions',
            'Positioning', 'Vision', 'Penalties', 'Composure', 'Marking', 'Standing Tackle',
            'Sliding Tackle']]

    return 1 - float(distance.cosine(player_1_stats.values, player_2_stats.values))

def train():
    global player_columns, work_rates

    players = db.get_players()
    players_df = pd.DataFrame(players)
    players_df.columns = player_columns

    # convert work rates to a numeric value
    players_df['Attacking Work Rate'] = players_df['Attacking Work Rate'].map(work_rates)
    players_df['Defensive Work Rate'] = players_df['Defensive Work Rate'].map(work_rates)

    player_1 = players_df.iloc[0]
    player_2 = players_df.iloc[13]

    print('Similarity between {name1} and {name2}: {score}'.format(name1=player_1['Short Name'], name2=player_2['Short Name'], score=calculate_similarity(player_1, player_2)))