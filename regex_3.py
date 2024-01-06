# mahdi mohammadi khah 982011056

import re


def find_numbers_and_positions(text):
    numbers_with_positions = [(match.group(), match.start()) for match in re.finditer(r'\d+', text)]
    return numbers_with_positions


text = input()
numbers_and_positions = find_numbers_and_positions(text)
for item in numbers_and_positions:
    print(item[0])
    print(f'Index position: {item[1]}')