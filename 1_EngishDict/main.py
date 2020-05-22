import json
from difflib import get_close_matches


data = json.load(open("data.json", "r"))


def lookup(key):
    key = key.lower()
    if key in data:
        return data[key]
    elif key.title() in data:
        return data[key.title()]
    elif key.upper() in data:
        return data[key.upper()]
    else:
        best_match = get_close_matches(key, data.keys(), n=1, cutoff=0.8)
        if len(best_match):
            response = input(f"{key} is not in dictionary. Did you mean {best_match[0]}? (y/n): ")
            if response.lower() == 'y':
                return data[best_match[0]]
            else:
                return "Negative response (or one that is not understand). Please enter another word."
        else:
            return "Word is not in dictionary. Please double check it."


while True:
    word = input("Enter word: ")
    defs = lookup(word)
    if isinstance(defs, list):
        for i, definition in enumerate(defs):
            print(f"{i+1}: {definition}")
    else:
        print(defs)
