from lab1.frequency_analysis import get_frequency, list_assessment

with open('static/caesar_input.txt', 'r') as caesar_file:
    text = caesar_file.read()


def caesar_xor_encrypt(text, key):
    new_text = ''
    for letter in text:
        new_text += chr(ord(letter) ^ key)
    return new_text


def caesar_decipher(text):
    texts = {}
    for i in range(2 ** 9 - 1):
        new_text = caesar_xor_encrypt(text, i)
        arr = list(dict(
            sorted(get_frequency(new_text).items(),
                   key=lambda x: -x[1])).keys())
        texts[new_text] = list_assessment(arr)
    sorted_texts = list(dict(sorted(texts.items(), key=lambda x: x[1])).keys())
    # texts = dict.txt(sorted(texts.items(), key=lambda x: x[1])[:5])
    return sorted_texts[0]

