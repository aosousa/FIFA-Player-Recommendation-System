import psycopg2

from configparser import ConfigParser

conn = None

def config(filename='database.ini', section='postgresql'):
    """Read database configuration file and return a dictionary
    of configuration key-value pairs.

    Args:
        filename: Name of the file where the configuration is stored.
        section: Which section to read from

    Returns:
        db: Dictionary of configuration key-value pairs.
    """
    parser = ConfigParser()
    parser.read('./config/{}'.format(filename))

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} was not found in {1}'.format(section, filename))
    
    return db

def connect():
    global conn

    try:
        print('Connecting to PSQL...')
        params = config()
        conn = psycopg2.connect(**params)
        print('Connection established')

        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print('Error occurred connecting to PostgreSQL')
        print(error)

def get_players():
    """Get player information by joining the players and player_stats tables

    Returns:
        players: Players list
    """
    global conn

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM players JOIN player_stats ON player_stats.player_id = players.id')
    players = cursor.fetchall()

    cursor.close()

    return players