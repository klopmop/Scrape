from joke_api import get_random_joke
from file_manager import save_joke_to_file
from database import init_db, save_to_db

def main():
    #init_db()
    random_joke = get_random_joke()
    save_joke_to_file(random_joke)
    #save_to_db(random_joke)


if __name__ == '__main__':
    main()