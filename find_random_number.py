# Camputer chose a random number and person try to find number
import os
import random

for i in range(10):
    print('!!!', end='')
print('GUESS NUMBER FASTER', end='')
for i in range(10):
    print('!!!', end='')
print()

list_of_scores = []
if os.path.isfile('data_score.txt'):
    data_score = open('data_score.txt', 'r')
    old_score = data_score.read()
    list_of_scores = old_score.split('$')
    list_of_scores = [int(x) for x in list_of_scores]
    data_score.close()

while True:
    print('''
    1. Start a game
    2. Show my score
    3. Save and Exit
    ''')
    choice = input('Enter your short key :')
    if choice == '1':
        count = 0
        random_number = random.randint(0, 1000)
        print(random_number)
        while True:
            geuss = int(input('Enter your guess : '))
            count = count + 1
            if random_number > geuss:
                print(f'{geuss} is lower than answer, guess higher')
            elif random_number < geuss:
                print(f'{geuss} is higher than answer, guess lower')
            else:
                print(f'we have a winner the answer is {geuss} ')
                list_of_scores.append(count)
                break
    if choice == '2':
        sum = 0
        print(list_of_scores)
        for i in list_of_scores:
            sum = sum + i
        average = sum / len(list_of_scores)
        print(average)
    if choice == '3':
        print('***GOODBYE***')
        list_of_scores = [str(x) for x in list_of_scores]
        data_score = open('data_score.txt' ,'w')
        save = '$'.join(list_of_scores)
        data_score.write(save)
        data_score.close()
        break
