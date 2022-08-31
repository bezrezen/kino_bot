import sqlite3

with sqlite3.connect("movies_list.db") as db:
    cursor = db.cursor()

    actors_str = 'джек николсон, морган фримен, джон траволта, вертинская '
    directors_str = 'майк николс, Гэри Фледер, птушко'
    country_str = 'США, Франция, Великобритания, СССР'
    genre_str = 'Драма, Боевик, Комедия, фильм ужасов'
    year_start = 1961
    year_finish = 1997
    not_want_str = 'ревность, состояние'

    actors_list = actors_str.title().split(',')
    directors_list = directors_str.title().split(',')
    countries_list = country_str.title().split(',')
    genres_list = genre_str.lower().split(',')
    movies_not_want = not_want_str.title().split(',')
  

    list_movies_actor = list()
    list_movies_director = list()
    list_movies_countries = []
    list_movies_genres = []
    list_movies_year = []

    for actor in actors_list:    
        actor = actor.strip()
        cursor.execute("SELECT * FROM movies_list WHERE actor LIKE '%'||?||'%'", (actor,))
        list_movies_actor = list_movies_actor + cursor.fetchall()

    for director in directors_list:
        director = director.strip()
        cursor.execute("SELECT * FROM movies_list WHERE director LIKE '%'||?||'%'", (director,))
        list_movies_director = list_movies_director + cursor.fetchall()

    for country in countries_list:
        country = country.strip()
        if country.lower() == 'сша':
            country = 'США'
        elif country.lower() == 'ссср':
            country = 'СССР'
        cursor.execute("SELECT * FROM movies_list WHERE country LIKE '%'||?||'%'", (country,))
        list_movies_countries = list_movies_countries + cursor.fetchall()

    for genre in genres_list:
        genre = genre.strip()
        cursor.execute("SELECT * FROM movies_list WHERE genre LIKE '%'||?||'%'", (genre,))
        list_movies_genres = list_movies_genres + cursor.fetchall()

    cursor.execute("SELECT * FROM movies_list WHERE year <= ? and year >= ?", (year_finish, year_start))
    list_movies_year = list_movies_year + cursor.fetchall()

    prefinal_movies_list = list(
        set(list_movies_actor) & set(list_movies_director) 
        & set(list_movies_countries) & set(list_movies_genres) & set(list_movies_year)
    )
    
    id = 0
    for mov1 in prefinal_movies_list:
        id +=1
        print(F"id: {id}, название: {mov1[0]}, год: {mov1[5]}, оценка: {mov1[7]}, страна: {mov1[4]}")

    for mov in movies_not_want:
        mov = mov.strip()
        for mov2 in prefinal_movies_list:
            if mov == mov2[0]:
                prefinal_movies_list.remove(mov2)
    print(' ')
    id_ = 0
    for mov1 in prefinal_movies_list:
        id_ +=1
        print(F"id: {id_}, название: {mov1[0]}, год: {mov1[5]}, оценка: {mov1[7]}, страна: {mov1[4]}")
    
    


