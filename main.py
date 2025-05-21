from stats import (
    get_number_of_times_each_character_appears,
    get_number_of_words,
    sort_dict_by_value,
)

import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file).lower()
    number_of_words = get_number_of_words(text)
    number_of_each_char = get_number_of_times_each_character_appears(text)
    sorted_list = sort_dict_by_value(number_of_each_char)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for character, count in sorted_list.items():
        if character.isalpha():
            print(f"{character}: {count}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
