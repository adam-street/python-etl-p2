insert_movie = ('''
    INSERT INTO p2_etl.movie_list
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
''')

create_schema = ('''
    CREATE SCHEMA IF NOT EXISTS p2_etl;
    
    DROP TABLE IF EXISTS p2_etl.movie_list;
    
    CREATE TABLE IF NOT EXISTS p2_etl.movie_list (
        title TEXT,
        rated TEXT,
        released DATE,
        runtime INT,
        genre TEXT[],
        director TEXT,
        writers TEXT[],
        actors TEXT[],
        plot TEXT,
        awards TEXT,
        poster TEXT
        );

''')
