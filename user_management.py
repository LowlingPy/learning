# user password and data

import json
import random

# from getpass import getpass


# admin info
users = [
    {
        'username': 'milad',
        'password': '123',
        'data': '2$5$4',
        'role': 'admin',
        'name': None,
        'lastname': None
     }
]

file = open('users_data.txt', 'r')
data = file.read()
if data:
    users = json.loads(data)

file.close()

username = input('  Enter your username: ')
password = input('  Enter your password: ')
for user in users:
    if username.lower() == user['username'].lower():
        if password == user['password']:
            login_user = user
            break
        else:
            print('incorrect password')
            exit()
else:
    print('user not found')
    exit()

while True:
# admin panel
    if login_user['role'] == 'admin':
        login_username = login_user['username'].capitalize()
        print(f'''
                    ***     Welcome {login_username}     ***
                    ###     ADMIN PANEL     ###
        ''')
        print('''
        1. Show users
        2. Add a new user
        3. Delete user
        4. Show user's data
        5. Start a game
        6. Edit your profile
        7. Save and exit
        ''')
        choice = input('    Enter your short key: ')

# show users
        if choice == '1':
            for user in users:
                username = user['username'].capitalize()
                user_role = user['role'].capitalize()
                print(f'{username} is {user_role}')

# add user
        elif choice == '2':
            if login_user['role'] == 'admin':
                new_user = {}
                new_username = input('  Enter new username: ').lower()
                new_password = input('  Enter new user password: ')
                while True:
                    new_role = input('  Role (User/Admin): ').lower()
                    if new_role == 'admin':
                        new_user.update(
                            {'username': new_username, 'password': new_password, 'data': None, 'role': 'admin',
                             'name': None, 'lastname': None})
                        users.append(new_user)
                        print(f'New admin ({new_username}) added ')
                        break
                    elif new_role == 'user':
                        new_user.update(
                            {'username': new_username, 'password': new_password, 'data': None, 'role': 'user',
                             'name': None, 'lastname': None})
                        users.append(new_user)
                        print(f'New user ({new_username}) added ')
                        break
                    else:
                        print('Role not valid, Try again')
            else:
                print('You have no permission for add new user, Sorry')

# delete user
        elif choice == '3':
            delete_user = input('   Enter username you want delete: ').lower()
            for user in users:
                if ('username', delete_user) in user.items():
                    users.remove(user)
                    print(f'{user["username"]} deleted')

# show user's data
        elif choice == '4':
            for user in users:
                username = user['username']
                list_of_score = []
                if user['data'] is not None:
                    list_of_score = user['data'].split('$')
                    print(f'Data of {username} : {list_of_score}')
                    list_of_score = login_user['data'].split('$')
                    sum = 0
                    for i in list_of_score:
                        sum = sum + int(i)
                    score = sum / len(list_of_score)
                    print(f'{username} : {score}')
                else:
                    print(f'{username} has no score')
        # start a game
        elif choice == '5':
            count = 0
            random_number = random.randint(0, 1000)

            # #cheat
            # print(random_number)
            while True:
                geuss = int(input('     Enter your guess(0,1000): '))
                count = count + 1
                if random_number > geuss:
                    print(f'{geuss} is lower than answer, guess higher')
                elif random_number < geuss:
                    print(f'{geuss} is higher than answer, guess lower')
                else:
                    print(f'we have a winner the answer is {geuss} ')
                    list_of_score = []
                    if login_user['data'] is not None:
                        list_of_score = login_user['data'].split('$')
                    count = str(count)
                    list_of_score.append(count)
                    str_of_score = '$'.join(list_of_score)
                    login_user['data'] = str_of_score
                    break

        # edit profile
        elif choice == '6':
            while True:
                print(f'''
                1. Edit Username({login_user['username']})
                2. Edit Name({login_user['name']})
                3. Edit Lastname({login_user['lastname']})
                4. Edit your password
                5. Back to Main menu
                ''')
                choice_edit = input('   Enter your short key : ')
                if choice_edit == '1':
                    new_username = input('  Enter your new username : ').lower()
                    login_user['username'] = new_username
                elif choice_edit == '2':
                    new_name = input('  Enter your new name : ').lower()
                    login_user['name'] = new_name
                elif choice_edit == '3':
                    new_lastname = input('  Enter your new lastname : ').lower()
                    login_user['lastname'] = new_lastname
                elif choice_edit == '4':
                    password_check = input('  Enter your password: ')
                    if password_check == login_user['password']:
                        new_password = input('  Enter you new password : ')
                        login_user['password'] = new_password
                elif choice_edit == '5':
                    edited_data = open('users_data.txt', 'w')
                    save = json.dumps(users)
                    edited_data.write(save)
                    edited_data.close()
                    break

        # save and exit
        elif choice == '7':
            data = open('users_data.txt', 'w')
            save_users = json.dumps(users)
            data.write(save_users)
            data.close()
            print('         ***GoodBye***')
            break

# user panel
    elif login_user['role'] == 'user':
        print(f'         ***    Welcome {login_user["username"]}    ***')
        print('''
        1. Start a game
        2. Show your score
        3. Edit your profile
        4. Save and exit
        ''')
        choice = input('    Enter your short key : ')

        # start a game
        if choice == '1':
            count = 0
            random_number = random.randint(0, 1000)

            # #cheat
            # print(random_number)
            while True:
                geuss = int(input('     Enter your guess(0,1000): '))
                count = count + 1
                if random_number > geuss:
                    print(f'{geuss} is lower than answer, guess higher')
                elif random_number < geuss:
                    print(f'{geuss} is higher than answer, guess lower')
                else:
                    print(f'we have a winner the answer is {geuss} ')
                    list_of_score = []
                    if login_user['data'] is not None:
                        list_of_score = login_user['data'].split('$')
                    count = str(count)
                    list_of_score.append(count)
                    str_of_score = '$'.join(list_of_score)
                    login_user['data'] = str_of_score
                    break

        # show score
        elif choice == '2':
            list_of_score = []
            if login_user['data'] is not None:
                list_of_score = login_user['data'].split('$')
                sum = 0
                for i in list_of_score:
                    sum = sum + int(i)
                score = sum / len(list_of_score)
                print(f'Your score : {score}')
            else:
                print('You have no data')

        # edite profile
        elif choice == '3':
            while True:
                print(f'''
                1. Edit Username({login_user['username']})
                2. Edit Name({login_user['name']})
                3. Edit Lastname({login_user['lastname']})
                4. Edit your password
                5. Back to Main menu
                ''')
                choice_edit = input('   Enter your short key : ')
                if choice_edit == '1':
                    new_username = input('  Enter your new username : ').lower()
                    login_user['username'] = new_username
                elif choice_edit == '2':
                    new_name = input('  Enter your new name : ').lower()
                    login_user['name'] = new_name
                elif choice_edit == '3':
                    new_lastname = input('  Enter your new lastname : ').lower()
                    login_user['lastname'] = new_lastname
                elif choice_edit == '4':
                    password_check = input('    Enter your password please : ')
                    if password_check == login_user['password']:
                        new_password = input('  Enter you new password : ')
                        login_user['password'] = new_password
                elif choice_edit == '5':
                    edited_data = open('users_data.txt', 'w')
                    save = json.dumps(users)
                    edited_data.write(save)
                    edited_data.close()
                    break

        # save and exit
        elif choice == '4':
            data = open('users_data.txt', 'w')
            save_users = json.dumps(users)
            data.write(save_users)
            data.close()
            print('         ***GoodBye***')
            break
