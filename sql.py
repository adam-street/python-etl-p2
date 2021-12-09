
create_schema =('''
    CREATE SCHEMA IF NOT EXISTS petl2
''')

create_table =('''
    CREATE TABLE IF NOT EXISTS petl2.movie_list (
        title TEXT NOT NULL,
        rated TEXT NOT NULL,
        released DATE NOT NULL,
        runtime INT NOT NULL,
        genre TEXT[] NOT NULL,
        director TEXT NOT NULL,
        writers TEXT[] NOT NULL,
        actors TEXT[] NOT NULL,
        plot TEXT NOT NULL,
        awards TEXT NOT NULL,
        poster TEXT NOT NULL);
    ''')

create_insert =('''
    INSERT INTO petl2.movie_list
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    ''')