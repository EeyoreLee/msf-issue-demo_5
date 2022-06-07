import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HOST = os.environ.get('HOST', '0.0.0.0')
PORT = os.environ.get('PORT', 41000)
DICT_FILE_PATH = os.environ.get("DICT_FILE_PATH", os.path.join(BASE_DIR, "weights", "keyword_example_100.txt"))