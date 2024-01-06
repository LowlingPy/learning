# mahdi mohammadi khah 982011056

import re


def a_and_e_finder(text):
    words_starting_with_a_and_e = re.findall(r'\b[ae]\w*', text)
    return words_starting_with_a_and_e


text = input()
words_found = a_and_e_finder(text)
print(words_found)