# user password and data

import json
import random
import bcrypt


def init():
    # admin info
    users = [
        {
            'username': 'milad',
            'password': "b'$2b$12$QiD3DeYmnd4SEAs8go7zIenUO2lbPslY13FEWvurMiQvXuel1uwkq'",
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
    return users


def password_hasher(password):
    pwd = password.encode()
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pwd, salt)
    return hashed


def get_role(user):
    if user['role'] == 'admin':
        return 'admin'
    elif user['role'] == 'user':
        return 'user'
    else:
        return None


def menu(user_role, name):
    if user_role == 'admin':
        print(f'''
                    ***     Welcome {name}     ***
                    ###     ADMIN PANEL     ###
        ''')
        return [
            'Show users',
            'Add a new user',
            'Delete user',
            'Show user\'s data',
            'Start a game',
            'Edit your profile',
            'Save and exit'
        ]
    elif user_role == 'user':
        print(f'         ***    Welcome {name}    ***')
        return [
            'Start a game',
            'Show your score',
            'Edit your profile',
            'Save and exit'
        ]


def game(login_user):
    count = 0
    random_number = random.randint(0, 1000)
    # #cheat
    # print(random_number)
    while True:
        guess = int(input('     Enter your guess(0,1000): '))
        count = count + 1
        if random_number > guess:
            print(f'{guess} is lower than answer, guess higher')
        elif random_number < guess:
            print(f'{guess} is higher than answer, guess lower')
        else:
            print(f'we have a winner the answer is {guess} ')
            list_of_score = []
            if login_user['data'] is not None:
                list_of_score = login_user['data'].split('$')
            count = str(count)
            list_of_score.append(count)
            str_of_score = '$'.join(list_of_score)
            login_user['data'] = str_of_score
            break


def get_clean_users(users):
    list_clean_users = []
    for user in users:
        username = user['username'].capitalize()
        user_role = user['role'].capitalize()
        clean_users_data = f'{username} is {user_role}'
        list_clean_users.append(clean_users_data)
    return list_clean_users


def add_user(username, password, users, role_new):
    new_user = {}
    new_user.update(
        {'username': username, 'password': password, 'data': None, 'role': role_new, 'name': None, 'lastname': None}
    )
    users.append(new_user)
    return f'New {role_new} ({username.capitalize()}) added '


def delete_users(users, user_will_be_deleted):
    for user in users:
        if user['username'] == user_will_be_deleted:
            users.remove(user)
    return f'{user_will_be_deleted.capitalize()} is deleted '


def show_users_data(users):
    for user in users:
        username = user['username']
        list_of_score = user['data'].split('$')
        sum_ = 0
        for i in list_of_score:
            sum_ = sum_ + int(i)
        score = sum_ / len(list_of_score)
        return f'{username} : {score}'


def edit_profile_menu(login_user):
    return [
        f'Edit Username ({login_user["username"]})',
        f'Edit Name ({login_user["name"]})',
        f'Edit Lastname({login_user["lastname"]})',
        'Edit your password',
        'Back to Main menu'
    ]


def change_username(login_user, new_username_def):
    return login_user['username'] == new_username_def


def change_name(login_user, new_name_def):
    return login_user['name'] == new_name_def


def change_lastname(login_user, new_lastname_def):
    return login_user['lastname'] == new_lastname_def


def change_password(login_user, new_password_def, check_password_def):
    if check_password_def == login_user['password']:
        return login_user['password'] == new_password_def


def edit_profile_save(users):
    edited_data = open('users_data.txt', 'w')
    save = json.dumps(users)
    edited_data.write(save)
    edited_data.close()


def save_and_exit(users):
    data = open('users_data.txt', 'w')
    save_users = json.dumps(users)
    data.write(save_users)
    data.close()
    print('         ***GoodBye***')


def show_score(login_user):
    if login_user['data'] is not None:
        list_of_score = login_user['data'].split('$')
        sum_ = 0
        for i in list_of_score:
            sum_ = sum_ + int(i)
        score = sum_ / len(list_of_score)
        return f'Your score : {score}'
    else:
        return 'You have no data'


def login(username, password, users):
    for user in users:
        if username.lower() == user['username'].lower():
            if password == user['password']:
                return True, user
            else:
                return False, 'Wrong password'

    else:
        return False, 'User not found'


all_user = init()
enter_username = input('  Enter your username: ')
enter_password = input('  Enter your password: ')
enter_password_hashed = password_hasher(enter_password)
status, result = login(enter_username, enter_password_hashed, all_user)
if status is False:
    print(result)
    exit()
user_in_app = result
role = get_role(user_in_app)
if role is None:
    print('Invalid role user ')
    exit()

while True:
    # admin panel
    show_menu = menu(role, user_in_app['username'].capitalize())
    for index, item in enumerate(show_menu):
        print(f'{index + 1}. {item}')

    if role == 'admin':
        choice = input('    Enter your short key: ')
        # show users
        if choice == '1':
            for item in get_clean_users(all_user):
                print(item)
        # add user
        elif choice == '2':
            new_username = input('  Enter new username: ').lower()
            new_password = input('  Enter new user password: ')
            new_password_hashed = password_hasher(new_password)
            while True:
                new_role = input('  Role (User/Admin): ').lower()
                if new_role == 'admin' or new_role == 'user':
                    print(add_user(new_username, new_password_hashed, all_user, new_role))
                    break
                print('Role not valid, Try again')

        # delete user
        elif choice == '3':
            delete_user = input('   Enter username you want delete: ').lower()
            for exist_user in all_user:
                if exist_user['username'] == delete_user:
                    print(delete_users(all_user, delete_user))
                    break
            else:
                print('user not found')
        # show user's data
        elif choice == '4':
            print(show_users_data(all_user))

        # start a game
        elif choice == '5':
            game(user_in_app)

        # edit profile
        elif choice == '6':
            while True:
                show_edit_menu = edit_profile_menu(user_in_app)
                for index, item in enumerate(show_edit_menu):
                    print(f'{index + 1}. {item}')
                choice_edit = input('   Enter your short key : ')
                if choice_edit == '1':
                    new_username = input('  Enter your new username : ').lower()
                    change_username(user_in_app, new_username)

                elif choice_edit == '2':
                    new_name = input('  Enter your new name : ').lower()
                    change_name(user_in_app, new_name)

                elif choice_edit == '3':
                    new_lastname = input('  Enter your new lastname : ').lower()
                    change_lastname(user_in_app, new_lastname)

                elif choice_edit == '4':
                    password_check = input('  Enter your password : ')
                    password_check_hashed = password_hasher(password_check)
                    new_password = input('  Enter you new password : ')
                    new_password_hashed = password_hasher(new_password)
                    change_password(user_in_app, new_password_hashed, password_check_hashed)

                elif choice_edit == '5':
                    edit_profile_save(all_user)
                    break

        # save and exit
        elif choice == '7':
            save_and_exit(all_user)
            break

    # user panel
    elif role == 'user':
        choice = input('    Enter your short key : ')

        # start a game
        if choice == '1':
            game(user_in_app)

        # show score
        elif choice == '2':
            print(show_users_data(user_in_app))

        # edite profile
        elif choice == '3':
            while True:
                show_edit_menu = edit_profile_menu(user_in_app)
                for index, item in enumerate(show_edit_menu):
                    print(f'{index + 1}. {item}')
                choice_edit = input('   Enter your short key : ')
                if choice_edit == '1':
                    new_username = input('  Enter your new username : ').lower()
                    change_username(user_in_app, new_username)

                elif choice_edit == '2':
                    new_name = input('  Enter your new name : ').lower()
                    change_name(user_in_app, new_name)

                elif choice_edit == '3':
                    new_lastname = input('  Enter your new lastname : ').lower()
                    change_lastname(user_in_app, new_lastname)

                elif choice_edit == '4':
                    password_check = input('  Enter your password : ')
                    password_check_hashed = password_hasher(password_check)
                    new_password = input('  Enter you new password : ')
                    new_password_hashed = password_hasher(new_password)
                    change_password(user_in_app, new_password_hashed, password_check_hashed)

                elif choice_edit == '5':
                    edit_profile_save(all_user)
                    break

        # save and exit
        elif choice == '4':
            save_and_exit(all_user)
            break
