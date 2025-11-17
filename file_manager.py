import pathlib
from joke_api import get_random_joke


def save_joke_to_file(joke_file):

    f_exists = pathlib.Path("random_joke.txt")

    if f_exists.exists():
        file = "random_joke.txt"
        with open(file, "r") as f:
            lines = f.readlines()
        number = len(lines) +1

        with open("random_joke.txt", "a") as file_joke:
            file_joke.write(f"{number}. {joke_file} \n")
    else:
        pathlib.Path("random_joke.txt").touch()

        file = "random_joke.txt"
        with open(file, "r") as f:
            lines = f.readlines()
        number = len(lines) + 1

        with open("random_joke.txt", "a") as file_joke:
            file_joke.write(f"{number}. {joke_file} \n")



rand_joke = get_random_joke()
save_joke_to_file(rand_joke)