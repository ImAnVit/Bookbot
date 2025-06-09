def count_words(text):
    return len(text.split())

def count_characters(text):
    my_dict = {}
    for char in set(text):
        my_dict[char] = text.count(char)
    return my_dict

def sorted_dict(my_dict):
    sorted_items = sorted(my_dict.items())
    return "\n".join(f"{key}: {value}" for key, value in sorted_items)