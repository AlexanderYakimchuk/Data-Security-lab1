letter_frequency = {'E': 12.0,
                    'T': 9.10,
                    'A': 8.12,
                    'O': 7.68,
                    'I': 7.31,
                    'N': 6.95,
                    'S': 6.28,
                    'R': 6.02,
                    'H': 5.92,
                    'D': 4.32,
                    'L': 3.98,
                    'U': 2.88,
                    'C': 2.71,
                    'M': 2.61,
                    'F': 2.30,
                    'Y': 2.11,
                    'W': 2.09,
                    'G': 2.03,
                    'P': 1.82,
                    'B': 1.49,
                    'V': 1.11,
                    'K': 0.69,
                    'X': 0.17,
                    'Q': 0.11,
                    'J': 0.10,
                    'Z': 0.07}
ordered_letters = ['e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'd', 'l', 'u',
                   'c', 'm', 'f', 'y', 'w', 'g', 'p', 'b', 'v', 'k', 'x', 'q',
                   'j', 'z']

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

dict_letters = {'e': 0, 't': 1, 'a': 2, 'o': 3, 'i': 4, 'n': 5, 's': 6, 'r': 7,
                'h': 8, 'd': 9, 'l': 10, 'u': 11, 'c': 12, 'm': 13, 'f': 14,
                'y': 15, 'w': 16, 'g': 17, 'p': 18, 'b': 19, 'v': 20, 'k': 21,
                'x': 22, 'q': 23, 'j': 24, 'z': 25}


def get_frequency(text):
    symbols = {}
    for symbol in text:
        symbols[symbol] = symbols.get(symbol, 0) + 1

    return symbols


def list_assessment(arr):
    dif = 0
    for i in range(len(arr)):
        dif += abs(i - dict_letters.get(arr[i].lower(), 26))
    return dif
