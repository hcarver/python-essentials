import csv
import os
from collections import defaultdict

dir_path = os.path.dirname(os.path.abspath(__file__))

CURRICULUM_PATH = os.path.dirname(dir_path)
DATA_PATH = os.path.join(CURRICULUM_PATH, 'data')
FEMALE_FILE = os.path.join(DATA_PATH, 'popular_female_names_by_decade.csv')
MALE_FILE = os.path.join(DATA_PATH, 'popular_male_names_by_decade.csv')


def _read_csv(path):
    with open(path) as f:
        reader = csv.DictReader(f)
        return list(reader)


def _read_name_popularity_by_year(path):
    name_data = _read_csv(path)
    names = defaultdict(dict)
    for item in name_data:
        names[int(item['Year'])][item['Name'].lower()] = int(item['Count'])
    return dict(names)


girls_popularity_by_decade = _read_name_popularity_by_year(FEMALE_FILE)
boys_popularity_by_decade = _read_name_popularity_by_year(MALE_FILE)

girls_names_2010 = girls_popularity_by_decade[2010].copy()
boys_names_2010 = boys_popularity_by_decade[2010].copy()

girls_names_1960 = girls_popularity_by_decade[1960].copy()
boys_names_1960 = boys_popularity_by_decade[1960].copy()
