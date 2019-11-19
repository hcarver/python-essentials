import os
import json

dir_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(dir_path, 'data')


with open(os.path.join(data_path, 'words_list.txt')) as f:
    words = {word.strip().lower() for word in f.readlines()}


with open(os.path.join(data_path, 'films_by_genre.json')) as f:
    _films_by_genre_raw = json.load(f)


films_by_genre = {
    category: set(films) for category, films in _films_by_genre_raw.items()
}
