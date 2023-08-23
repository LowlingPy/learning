# Camputer chose a random number and person try to find number

for i in range(10):
    print('!!!', end='')
print('GUESS NUMBER FASTER', end='')
for i in range(10):
    print('!!!', end='')
print()

import random

random_number = random.randint(0, 1000)

geuss = int(input('Enter your guess : '))

while random_number > geuss:
    print(f'{geuss} is lower than answer, guess higher')
    geuss = int(input('Try again : '))
    while random_number < geuss:
        print(f'{geuss} is higher than answer, guess lower')
        geuss = int(input('Try again : '))
if random_number == geuss:
    print(f'we have a winner the answer is {geuss} ')
