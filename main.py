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
    
    """Reading the movies.json file into the dataset"""
    
    f = open(".//datasets/json/movies.json", 'r')
    dataset = f.read()
    datadict = json.loads(dataset)

    # Filtering the dataset to contain only the rows where the year is on or after 2018
    
    search_value = [2018, 2019, 2020, 2021] 
    movie_2018_list = []
    for i in range(len(datadict)):
        for k, v in datadict[i].items():
            for j in search_value:
                if j in datadict[i].values():
                    movie_2018_list.append(datadict[i])   
    
    # Creating new list to hold just the titles of the movies which has year on or after 2018.
                    
    title_list = []
    title_set = {}
    
    for item in movie_2018_list:
        title_list.append(item["title"])
    
    # Conversion from list to set removes the duplicate values.
    title_set = list(set(title_list))
    
    # Now connecting with API and getting the information for the filtered titles and writing it in the Finalmovies.json
    
    movies_API = {}
    """f_write = open("FinalMovies.json",'w')
    for item in title_set:
        movies_API[item]=get_movie_data(item)
    json.dump(movies_list,f_write,indent=4)"""

    with open("FinalMovies.json", 'r')as f1:
        final_movies_json = json.loads(f1.read())

    # Retaining all the movies that has the language constraint of English.
    value = "English"
    all_english_movies = []
    for k, v in final_movies_json.items():
        for k1, v1 in v.items():
            if k1 == "Language":
                if value in v1:
                    all_english_movies.append(v)

    # Filtering the data just to have the 11 required columns
    eleven_columns_alone = []
    keys_to_extract = ["Title", "Rated", "Released", "Runtime", "Genre", "Director", "Writer", "Actors", "Plot",
                       "Awards", "Poster"]
    
    for i in all_english_movies:
        a_subset = {key: i[key] for key in keys_to_extract}
        eleven_columns_alone.append(a_subset)

    # Filtering the dataset to have the film that had all the valid response. Removing N/A responses from the list.
    not_NA_movies = []
    for i in eleven_columns_alone:
        if "N/A" not in i.values():
            not_NA_movies.append(i)

    # calling the query function in pgsql to create a new schema called 'petl1'

    pgsql.query(sql.create_schema)

    # calling the query_create table function in the pgsql to create the table in Postgres.

    pgsql.query_create(sql.create_table)

    """Converting the Released column from string to date, Slicing and striping the extra space from runtime and casting 
    it to int. using split function on the delimiter commas on the list string values to have the list format"""

    for item in not_NA_movies:
        to_add_table = []
        to_add_table.append(item["Title"])
        to_add_table.append(item["Rated"])
        date_obj = datetime.strptime(item["Released"], "%d %b %Y")
        to_add_table.append(date_obj)
        to_add_table.append(int(item["Runtime"][0:3].strip()))
        to_add_table.append(item["Genre"].split(","))
        to_add_table.append(item["Director"])
        to_add_table.append(item["Writer"].split(","))
        to_add_table.append(item["Actors"].split(","))
        to_add_table.append(item["Plot"].strip(','))
        to_add_table.append(item["Awards"].split(","))
        to_add_table.append(item["Poster"])
        pgsql.query(sql.insert_table, to_add_table)
