# user password and data

users = [
     {
        'username': 'Milad',
        'password': 'M123456',
        'data': '2$5$4'
    },
     {
        'username': 'Masood',
        'password': 'M123456',
        'data': '3$5$4'
    },
     {
        'username': 'AmIr',
        'password': 'M123456',
        'data': '4$5$4'
    }
]
username = input('Enter your username: ')
password = input('Enter your password: ')

for user in users:
    if username.lower() == user['username'].lower():
        if password == user['password']:
            break
        else:
            print('incorrect password')
            exit()
else:
    print('user not found')
    exit()

print('''
1. Show users
2. Add a new user
3. Delete user
4. Save and exit
''')
choice = input('Enter your short key :')
if choice == '1':
    print(users)