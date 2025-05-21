def get_number_of_words(text):
    words = text.split()
    return len(words)


def get_number_of_times_each_character_appears(text):
    character_count: dict[str, int] = {}
    for character in text:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1

    return character_count


def sort_dict_by_value(d: dict[str, int]) -> dict[str, int]:
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
