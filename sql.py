create_schema = ('''
    create schema if not exists petl2;
''')

create_table = ('''
    create table if not exists petl2.movies_list(
        Title Text,
        Rated text,
        Released date,
        Runtime int,
        Genre text[],
        Director text,
        Writers text[],
        Actors text[],
        Plot text,
        Awards text[],
        Poster text
    );
''')

insert_table = ('''
    insert into petl2.movies_list (Title,Rated,Released,Runtime,Genre,Director,Writers,Actors,Plot,Awards,Poster)
        values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
''')