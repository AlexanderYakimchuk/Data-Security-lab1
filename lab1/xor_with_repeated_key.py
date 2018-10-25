from lab1.caesar import caesar_decipher

with open('static/xor_input.txt', 'r') as file:
    bytes = file.read()
text = []
for i in range(0, len(bytes), 2):
    text.append(chr(int(bytes[i:i + 2], 16)))


def xor_encrypt(text, key):
    new_text = ''
    for i in range(len(text)):
        new_text += chr(ord(text[i]) ^ ord(key[i % len(key)]))
    return new_text


def get_match_index(text, alphabet):
    index = 0
    for i in range(len(alphabet)):
        count_i = float(text.count(alphabet[i]))
        index += (count_i * (count_i - 1)) / (len(text) * (len(text) - 1))
    return index


def get_correlation_index(text, new_text):
    num = 0
    for i in range(len(text)):
        if text[i] == new_text[i]:
            num += 1
    return num / len(text)


def correlation(text):
    new_text = text[1:] + text[0]
    indexes = {}
    for i in range(2, len(new_text)):
        new_text = new_text[1:] + new_text[0]
        indexes[i] = get_correlation_index(text, new_text)
    return indexes


def match_index(text):
    alphabet = list(set(text))
    indexes = {}
    for i in range(2, len(text)):
        indexes[i] = get_match_index(text[::i], alphabet)
    return indexes


# indexes = correlation(text)
# for k, v in indexes.items():
#     print(k, v)

length = 3
rows = []
for i in range(length):
    rows.append(caesar_decipher(text[i::length]))

decrypted_text = ''
for i in range(len(rows[0])):
    for j in range(length):
        decrypted_text += rows[j][i]

# print(decrypted_text)
