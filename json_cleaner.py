import json

with open ("films.json", "w", encoding="utf-8") as file:
    reader_json = json.load(file)
    for row in reader_json:
        if row['kp_rating'] == "-" or row['kp_rating'] == "–" or row['kp_rating'] == "None":
            row['kp_rating'] = 0
        if row['imdb_rating'] == "-" or row['imdb_rating'] == "–" or row['imdb_rating'] == "None":
            row['imdb_rating'] = 0