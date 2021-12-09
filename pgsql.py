import psycopg2
from config import pgsql_config


def query(query_string, values=None):
    # Connect to your postgres DB
    cursor = connect()

    # Execute a query
    if values:
        cursor.execute(query_string, values)
    else:
        cursor.execute(query_string)


def query_create(query_string):
    cursor = connect()
    cursor.execute(query_string)
    return cursor.fetchall


def connect():
    connection = psycopg2.connect(f"""
        host='{pgsql_config['host']}'
        dbname='{pgsql_config['dbname']}'
        user='{pgsql_config['user']}'
        password='{pgsql_config['password']}'
    """)

    # Configure connection
    connection.autocommit = True

    # Return connection cursor to perform database operations
    return connection.cursor()