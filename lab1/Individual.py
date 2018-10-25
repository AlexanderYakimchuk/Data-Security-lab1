import random

from lab1.substitution_cipher import decrypt

with open('static/2_grans.txt', 'r') as file:
    list_2_grans = file.read().split()

with open('static/3_grans.txt', 'r') as file:
    list_3_grans = file.read().split()


class Individual:
    def __init__(self, chromosome):
        self.chromosome = chromosome

    @property
    def fitness(self):
        decrypted_text = decrypt(self.chromosome)
        number_2_grans = self.get_2_grans_number(decrypted_text)
        number_3_grans = self.get_3_grans_number(decrypted_text)
        return number_3_grans * 0.7 + number_2_grans * 0.3

    def mutate(self):
        index = random.randint(0, 24)
        lst = list(self.chromosome)
        lst[index], lst[index + 1] = lst[index + 1], lst[index]
        self.chromosome = ''.join(lst)

    def give_offspring(self, parent2):
        new_chromosome = ''
        for i in range(len(self.chromosome)):
            if self.chromosome[i] == parent2.chromosome[i]:
                new_chromosome += self.chromosome[i]
            elif self.chromosome[i] not in new_chromosome:
                if parent2.chromosome[i] not in new_chromosome:
                    parent = random.choice([self, parent2])
                    new_chromosome += parent.chromosome[i]
                else:
                    new_chromosome += self.chromosome[i]
            else:
                new_chromosome += parent2.chromosome[i]
        return Individual(new_chromosome)


    def get_2_grans_number(self, decrypted_text):
        number = 0
        for gran in list_2_grans:
            number += decrypted_text.count(gran.upper())
        return number

    def get_3_grans_number(self, decrypted_text):
        number = 0
        for gran in list_3_grans:
            number += decrypted_text.count(gran.upper())
        return number
