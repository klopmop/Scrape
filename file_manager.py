def save_joke_to_file(joke_file):

    file = "random_joke.txt"
    with open(file, "r") as f:
        lines = f.readlines()
    number = len(lines) +1

    with open("random_joke.txt", "a") as file_joke:
        file_joke.write(f"{number}. {joke_file} \n")