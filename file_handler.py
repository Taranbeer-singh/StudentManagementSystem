# File handling functions

import json


FILE_NAME = "students.json"


def save_students(students):

    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def load_students():

    try:

        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:

        return []
    