from pathlib import Path

def save_joke_to_file(joke_file):

    f_exists = Path("random_joke.txt")

    if not f_exists.exists():
        Path("random_joke.txt").touch()
    else:
        file = "random_joke.txt"
        with open(file, "r") as f:
            lines = f.readlines()

        number = len(lines) + 1

        with open("random_joke.txt", "a") as file_joke:
            file_joke.write(f"{number}. {joke_file} \n")