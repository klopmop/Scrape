def main():
    init_db()
    random_joke = get_random_joke()
    save_joke_to_file(random_joke)

    save_to_db(random_joke)

if __name__ == '__main__':
    main()