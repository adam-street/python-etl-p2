import pgsql
import sql
import requests
import json
from datetime import datetime

def get_movie_data(title):
    headers = {"Authorization": "9855f49b"}
    request_url = f"https://www.omdbapi.com/?t={title}&apikey=686eed26"
    return requests.get(request_url, headers=headers).json()

if __name__ == '__main__':

    # get some movie data from the API
    # print(get_movie_data('WarGames'))
    # pgsql.query(sql.create_schema)
    pgsql.query(sql.create_table, [""])

    titles = []
    movieDict = {}
    f = open('datasets/json/movies.json')
    reader = json.loads(f.read())
    for i in reader:
        if i ["year"] >= 2018:
            titles.append(i["title"])
            # query(sql.create_insert, i)
    titleset = set(titles)
    titles = list(titleset)
    moviedict = {}
    for a in titles:
        moviedict[a] = get_movie_data(a)
    print(titles)
    f.close()

    # written the new json file/no dups & >=2018
    # f_write = open('datasets/json/filteredmovies.json', 'w')
    # json.dump(moviedict, f_write, indent=4)
    # f_write.close

    # get count for how many items are in the filteredmovies
    # count = 0
    # for i in moviedict:
        # count +=1
    # print(count)

    with open('datasets/json/filteredmovies.json', 'r') as f2:
       filtered_movies = json.loads(f2.read())

    value = "English"
    english_list = []
    for k, v in filtered_movies.items():
        for k1, v1 in v.items():
            if k1 == "Language":
                if value in v1:
                    english_list.append(v)
    # print(english_list, len(english_list))

    eleven_columns = []
    keys_extracted = ["Title", "Rated", "Released", "Runtime", "Genre", "Director", "Writer", "Actors", "Plot",
                      "Awards", "Poster"]

    for i in english_list:
        a_subset = {key: i[key] for key in keys_extracted}
        eleven_columns.append(a_subset)
    # print(eleven_columns, len(eleven_columns))

    not_NA_movies = []
    for i in eleven_columns:
        if "N/A" not in i.values():
            not_NA_movies.append(i)
    # print(len(not_NA_movies))

    newtitles = []
    for i in not_NA_movies:
        if (datetime.strptime(i["Released"], '%d %b %Y').year >= 2018):
            newtitles.append(i)
    # print(len(newtitles))

    # converting columns into the right conversions
    for item in newtitles:
       data_conversions = []
       data_conversions.append(item["Title"])
       data_conversions.append(item["Rated"])
       date_obj = datetime.strptime(item["Released"], "%d %b %Y")
       data_conversions.append(date_obj)
       info = item["Runtime"]
       data_conversions.append(info.strip(' min'))
       data_conversions.append(item["Genre"].split(","))
       data_conversions.append(item["Director"])
       data_conversions.append(item["Writer"].split(","))
       data_conversions.append(item["Actors"].split(","))
       data_conversions.append(item["Plot"].strip(','))
       data_conversions.append(item["Awards"].split(","))
       data_conversions.append(item["Poster"])

       pgsql.query(sql.create_insert, data_conversions)





















