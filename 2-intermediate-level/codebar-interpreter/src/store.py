from os import path
from json import dump, load

# Storage Module
class Controler:
    def set_data(db, data):
        FILE_FOLDER = "data"
        FILE_NAME = f"{db}.json" 
        FILE_PATH = path.join(FILE_FOLDER, FILE_NAME)

        with open(FILE_PATH, "w", encoding="utf-8") as database:
            dump(data, database, indent=4,)

    def get_data(db):
        FILE_FOLDER = "data"
        FILE_NAME = f"{db}.json" 
        FILE_PATH = path.join(FILE_FOLDER, FILE_NAME)

        with open(FILE_PATH, "r") as database:
            content = load(database)
        return content
