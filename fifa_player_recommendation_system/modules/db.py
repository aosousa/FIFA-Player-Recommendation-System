import psycopg2

from configparser import ConfigParser

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
    try:
        print('Connecting to PSQL...')
        params = config()
        return psycopg2.connect(**params)
    except (Exception, psycopg2.DatabaseError) as error:
        print('Error occurred connecting to PostgreSQL')
        print(error)