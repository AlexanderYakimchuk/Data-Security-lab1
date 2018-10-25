import random

from lab1.frequency_analysis import alphabet, dict_letters

letters_frequency = {'L': 0, 'P': 1, 'V': 2, 'E': 3, 'Y': 4, 'W': 5, 'S': 6,
                     'U': 7,
                     'Q': 8, 'M': 9, 'C': 10, 'H': 11, 'F': 12, 'A': 13,
                     'T': 14, 'K': 15,
                     'G': 16, 'O': 17, 'D': 18, 'B': 19, 'R': 20, 'N': 21,
                     'I': 22,
                     'X': 23, 'J': 24, 'Z': 25}

frequency_letters = {v: k for k, v in letters_frequency.items()}


def read_text():
    with open('static/substitution_input.txt', 'r') as file:
        s = str(file.read())
    return s


def generate_initial_key():
    key = ''
    for i in range(len(alphabet)):
        key += frequency_letters[dict_letters[alphabet[i]]]
    return key


def mutation(key):
    index = random.randint(0, 24)
    lst = list(key)
    lst[index], lst[index + 1] = lst[index + 1], lst[index]
    return ''.join(lst)


def decrypt(key):
    related_letters = dict()
    for i in range(len(alphabet)):
        related_letters[key[i].upper()] = alphabet[i].upper()
    encrypted_text = read_text()
    decoded_text = ''
    for i in encrypted_text:
        decoded_text += related_letters[i]
    return decoded_text
