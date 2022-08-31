import sqlite3
import csv

def create_db():
  db=sqlite3.connect("movies_list.db")
  cursor = db.cursor()
  cursor.execute("""CREATE TABLE IF NOT EXISTS movies_list(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    name_lower TEXT,
    genre TEXT,
    actor TEXT,
    director TEXT,
    country TEXT,
    year TEXT,
    kp_rating INTEGER,
    imdb_rating INTEGER,
    poster_url TEXT);
    """)
  db.commit()

def add_film():

  db = sqlite3.connect("movies_list.db")
  cursor = db.cursor()
  with open('movies.csv','r',encoding='utf-8') as file:
    dr = csv.DictReader(file)
    to_db = [(i['name'], i['name_lower'], i['genre'],i['actor'],i['director'],i['country'],i['year'], 0, 0, i['link']) for i in dr]

  cursor.executemany("""
    INSERT INTO movies_list 
    (name, name_lower, genre, actor, director, country, 
    year,kp_rating,imdb_rating,poster_url) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, to_db)
  db.commit()
  db.close()
  
create_db()
add_film()

