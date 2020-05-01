import os
import csv

dir_path = os.path.dirname(os.path.abspath(__file__))

CURRICULUM_PATH = os.path.dirname(dir_path)
DATA_PATH = os.path.join(CURRICULUM_PATH, 'data')


with open(os.path.join(DATA_PATH, 'english_web_word_frequencies.csv')) as f:
    reader = csv.reader(f)
    next(reader) # skip header line
    words, word_frequencies = zip(*reader)
    words = tuple(word.strip().lower() for word in words)
    word_frequencies = tuple(int(freq) for freq in word_frequencies)
