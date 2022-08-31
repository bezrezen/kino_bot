import sqlite3
import json

db = sqlite3.connect("movies_list.db")
cursor = db.cursor()
cursor.execute("""UPDATE movies_list SET kp_rating = 0, imdb_rating = 0;""")
db.commit()
with open('films.json','r',encoding='utf-8') as js:
    reader_json = json.load(js)
    for line in reader_json:
        cursor.execute("""UPDATE movies_list SET kp_rating = (?), imdb_rating = (?) WHERE name = (?) AND year = (?);""",(str(line['kp_rating']).lstrip(' '),str(line['imdb_rating']).lstrip(' '),str(line['film_name']).lstrip(' '),str(line['year']).lstrip(' '),))
        db.commit()

    db.close()

