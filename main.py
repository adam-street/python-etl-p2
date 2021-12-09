import pgsql
import sql
import json
import requests
from datetime import datetime

def get_movie_data(title):
    headers = {"Authorization": "9855f49b"}
    request_url = f"https://www.omdbapi.com/?t={title}&apikey=686eed26"
    return requests.get(request_url, headers=headers).json()

if __name__ == '__main__':

    # get some movie data from the API
    pgsql.query(sql.create_schema, ["My Insert!"])
    # print(get_movie_data('WarGames'))

h = open('datasets/json/movies.json')
data = json.load(h)
h.close()
movie = []
for row in data:
    if row['year'] >= 2018:
        dataset = get_movie_data(row['title'])
        if dataset['Response'] != 'False' and 'English' in dataset['Language'] and dataset['Title'] != 'N/A' and \
                dataset['Rated'] != 'N/A' and dataset['Released'] != 'N/A' and dataset['Runtime'] != 'N/A' and \
                dataset['Genre'] != 'N/A' and dataset['Director'] != 'N/A' and dataset['Writer'] != 'N/A' and \
                dataset['Actors'] != 'N/A' and dataset['Plot'] != 'N/A' and dataset['Awards'] != 'N/A' and \
                dataset['Poster'] != 'N/A' and datetime.strptime(dataset['Released'], "%d %b %Y").year > 2017:
            movie_no_dup = list(set(movie))
            if dataset['Title'] not in movie_no_dup:
                info = []
                info.append(dataset['Title'])
                info.append(dataset['Rated'])
                info.append(dataset['Released'])
                cleaner = dataset['Runtime']
                cleaner = cleaner.strip(' min')  # Change from hard code to fluid
                info.append(int(cleaner))
                cleaner2 = dataset['Genre'].split(', ')
                info.append(list(cleaner2))
                info.append(dataset['Director'])
                cleaner3 = dataset['Writer'].split(', ')
                info.append(list(cleaner3))
                cleaner4 = dataset['Actors'].split(', ')
                info.append(list(cleaner4))
                info.append(dataset['Plot'])
                info.append(dataset['Awards'])
                info.append(dataset['Poster'])
                pgsql.query(sql.insert_movie, info)
                movie.append(dataset['Title'])
