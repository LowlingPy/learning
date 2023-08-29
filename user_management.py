# user password and data

import json


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

username = input('Enter your username: ')
password = input('Enter your password: ')
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
        login_username = login_user['username']
        print(f'''
                    ***     Welcome {login_username}     ***
                    ###     ADMIN PANEL     ###
        ''')
        print('''
        1. Show users
        2. Add a new user
        3. Delete user
        4. Show user's data
        5. Save and exit
        ''')
        choice = input('Enter your short key : ')

# show users
        if choice == '1':
            for user in users:
                print(user['username'].capitalize())

# add user
        elif choice == '2':
            if login_user['role'] == 'admin':
                new_user = {}
                new_username = input('Enter new username: ').lower()
                new_password = input('Enter new user password: ')
                while True:
                    new_role = input('Role (User/Admin): ').lower()
                    if new_role == 'admin':
                        new_user.update({'username': new_username,'password': new_password, 'data': None, 'role': 'admin', 'name': None, 'lastname': None})
                        users.append(new_user)
                        break
                    elif new_role == 'user':
                        new_user.update({'username': new_username,'password': new_password, 'data': None, 'role': 'user', 'name': None, 'lastname': None})
                        users.append(new_user)
                        break
                    else:
                        print('Role not valid, Try again')
            else:
                print('You have no permission for add new user, Sorry')

# delete user
        elif choice == '3':
            delete_user = input('Enter username you want delete: ').lower()
            for user in users:
                if ('username', delete_user) in user.items():
                    users.remove(user)
                    print(f'User {user["username"]} deleted')

# show user's data
        elif choice == '4':
            for user in users:
                username = user['username']
                data = []
                if user['data'] is not None:
                    data = user['data'].split('$')

                print(f'data of {username} : {data}')

# save and exit
        elif choice =='5':
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
        1. Show your data
        2. Edit your profile
        ''')
        choice = input('Enter your short key : ')
        if choice == '1':
            if login_user['data'] is not None:
                data = login_user['data'].split('$')
                print(f'Your data : {data}')
            else:
                print('You have no data')
        elif choice == '2':
            while True:
                print(f'''
                1. Edit Username({login_user["username"]})
                2. Edit Name({login_user["name"]})
                3. Edit Lastname({login_user["lastname"]})
                4. Edit your password
                5. Back to Main menu
                ''')
                choice_edit = input('Enter your short key : ')
                if choice_edit == '1':
                    new_username = input('Enter your new username : ').lower()
                    login_user['username'] = new_username
                elif choice_edit == '2':
                    new_name = input('Enter your new name : ').lower()
                    login_user['name'] = new_name
                elif choice_edit == '3':
                    new_lastname = input('Enter your new lastname : ').lower()
                    login_user['lastname'] = new_lastname
                elif choice_edit == '4':
                    password_check = input('Enter your password please : ')
                    if password_check == login_user['password']:
                        new_password = input('Enter you new password : ')
                        login_user['password'] = new_password
                elif choice_edit == '5':
                    edited_data = open('users_data.txt', 'w')
                    save = json.dumps(users)
                    edited_data.write(save)
                    edited_data.close()
                    break


