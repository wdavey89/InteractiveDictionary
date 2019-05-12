import json
from difflib import get_close_matches
from termcolor import colored
from colorama import init

def main():
    data = json.load(open('data.json'))
    word = input("Enter word: ")
    translate(data, word)

def translate(data, word):
    init()
    if word in data:
        print(colored(data[word], 'green'))
    elif len(get_close_matches(word, data.keys())) > 0:
        alternatives = input("Did you mean {} instead? ".format(get_close_matches(word, data.keys())[0])).lower()
        if alternatives == 'y':
            newword = get_close_matches(word, data.keys())[0]
            print(colored(data.get(newword),'green'))
        else:
            print(colored("No words found, please double check it.", 'red'))
        
    else:
        print('No alternatives found.')


if __name__ == '__main__':
    main()
