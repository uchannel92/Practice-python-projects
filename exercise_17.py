from random import choice
import requests
url = 'http://norvig.com/ngrams/sowpods.txt'
response = requests.get(url)
r_html = response.text

filename = 'words.txt'
words = r_html.split()


def write_to_file(filename):
  
    with open(filename, 'w') as f:
        for word in words:
            f.write(f'{word}\n')


def read_file(filename):

    words = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            words.append(line)    
    
    random_word = choice(words)
    return random_word.lower()


randomly_picked_word = read_file(filename)
print(randomly_picked_word)
