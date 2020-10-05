import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def translate(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        rec_word = get_close_matches(word, data.keys())[0]
        yes_no = input(f"Did you mean {rec_word}? y/n: ").lower()
        if yes_no == "y":
            return data[rec_word]
        elif yes_no == 'n':
            return "That word does not exist"
        else:
            return "Sorry, did not understand your entry."
    else:
        return "That word does not exist."


word = (input("Enter word: ")).lower()
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
