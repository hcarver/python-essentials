import os

dir_path = os.path.dirname(os.path.abspath(__file__))

CURRICULUM_PATH = os.path.dirname(dir_path)
DATA_PATH = os.path.join(CURRICULUM_PATH, 'data')


with open(os.path.join(DATA_PATH, 'words_list.txt')) as f:
    word_list = sorted([word.strip().lower() for word in f.readlines()])
