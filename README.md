## Setup
   1. To run the program you must create a new file in the project's root folder called ```config.py``` with the following format.
   This is what the program reads to know what datbase to connect to and with what credentials.
      ```
       pgsql_config = {
           'host': '********',
           'dbname': '******',
           'user': '********',
           'password': '****'
       }
       ```
    
      - ```host``` is the hostname or url of the database, it will look like ```abcdefg.abcdefg.us-east-2.rds.amazonaws.com```

      - ```dbname``` is the datbase name of the host you want to connect to, you can use ```aaatest``` to test with.

      - ```user``` is the username

      - ```password``` is the password
   
   2. Create the ```venv``` from the pycharm project config screen and install the ```psycopg2-binary``` package
   3. Make sure your run configuration is pointed to you projects ```venv```
         - It should say ```Project Default```
   
## Project
   1. Create a fork of this repo with the following naming convention ```[first-name]-[last-name]-python-etl-p2```
   2. Create a schema called ```petl2```
         - ___use this schema for any tables created for this projecet___
   4. Create a table called ```movie_list``` with the following structure
         | Col Name          | Col Type       |
         | ------------- |:-------------:|
         | title      | text |
         | rated      | text |
         | released      | date |
         | runtime      | integer |
         | genre      | text[] |
         | director      | text |
         | writers      | text[] |
         | actors      | text[] |
         | plot      | text |
         | awards      | text |
         | poster      | text |
         
   4. Update the program so that when ```main.py``` is run it...
      
      Inserts a row into the ```movie_list``` table for each item in the ```datasets/json/movies.json``` JSON file that passes the following requirements
      
         a. ```The movie was made in or after 2018```
         
         b. ```The movie has a english version```
         
         c. ```The movie is not already in the table```

   ### Hints
   - https://www.geeksforgeeks.org/read-json-file-using-python/
   - All the data required is ```NOT``` inside the ```movies.json``` file, you will need to use the ```API``` provided. Look at the ```get_movie_data()``` function in the ```main.py``` file.
   - You WILL need to do some data conversion to be able to insert into the table.
      - Look up ```datetime.strptime```
         - this should help once you do a little digging... ```%d %b %Y```
      - When converting data you may also want to look up the following python functions ```split``` and ```replace```
   - if a movies is not foundy by title in the API ```OR``` any required data is returned as ```N/A``` from the API you can ignore that movie.
   - ```API``` calls are not free, you should do as much filtering as possible before you request the extra data to keep costs down.
      
