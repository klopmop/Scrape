import pathlib
from joke_api import get_random_joke


FILE = "random_joke.txt"

def save_joke_to_file(joke_file):

    f_exists = pathlib.Path(FILE)

    if f_exists.exists():
        with open(FILE, "r") as f:
            lines = f.readlines()
        number = len(lines) +1

        with open(FILE, "a") as file_joke:
            file_joke.write(f"{number}. {joke_file} \n")
    else:
        pathlib.Path(FILE).touch()

        with open(FILE, "r") as f:
            lines = f.readlines()
        number = len(lines) + 1

        with open(FILE, "a") as file_joke:
            file_joke.write(f"{number}. {joke_file} \n")
