import re
import json


def is_type_and_duration(text):
    return bool(text.endswith('ore') or text.endswith('.'))


def separate_type_from_duration(text):
    match = re.match(r'^(.*\D|PG-13)(\d\s*(?:h|ore)\s*\d*\s*min\.|\d+\s*(?:h|ore)\s*\d*)$', text)
    if match:
        genre = match.group(1)
        duration = match.group(2).replace('\xa0', ' ').replace('.', '').replace('ore', 'h')
        return genre.strip(), duration.strip()
    else:
        return None, None


def transform_from_ro_to_en_chars(text):
    ro_to_en = {
        'ă': 'a',
        'â': 'a',
        'î': 'i',
        'ș': 's',
        'ş': 's', 
        'ț': 't',
        'ţ': 't',
        'Ă': 'A', 
        'Â': 'A',
        'Î': 'I',
        'Ș': 'S',
        'Ț': 'T'
    }
    for ro_char, en_char in ro_to_en.items():
        text = text.replace(ro_char, en_char)
    return text


def transform_sublists_from_ro_to_en_chars(sublists):
    return [[transform_from_ro_to_en_chars(item) if item else '' for item in sublist] for sublist in sublists]


def arrange_each_movie_in_sublist(movies_list):
    movies_sublists = []
    i = 0
    while i < len(movies_list):
        sublist = []
        name_items = []
        genre_items = []
        type_items = []
        duration_items = []
        # Gather items (name-like items) until a duration-like item is found
        while i < len(movies_list) and not is_type_and_duration(movies_list[i]):
            name_items.append(movies_list[i])
            i += 1

        if i < len(movies_list) and is_type_and_duration(movies_list[i]):
            sublist.append(' '.join(name_items))
            type_items, duration_items = separate_type_from_duration(movies_list[i])
            sublist.append(type_items)
            sublist.append(duration_items)
            i += 1
            if i < len(movies_list):
                genre_items.append(movies_list[i])
                sublist.extend(genre_items)
                i += 1
            else:
                sublist.append('')
        
        movies_sublists.append(sublist)
        movies_sublists = transform_sublists_from_ro_to_en_chars(movies_sublists)
    return movies_sublists


def arrage_movie_data_in_json_structure(movies_sublists_list):
    movies = []
    for movie_list in movies_sublists_list:
        name = movie_list[0]
        type = movie_list[1]
        duration = movie_list[2]
        genre = movie_list[3]
        movies.append(
            {
                'name': name,
                'type': type,
                'duration': duration,
                'genre': genre
            }
        )

    return movies


# Save the movie data to JSON file
def save_movies(movies):
    with open('data_storage/movies.json', 'w') as file:
        json.dump(movies, file, indent=4)


# Load the movie data from JSON file
def load_movies():
    try:
        with open('data_storage/movies.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
