#application for todolist with using ddatabase

import psycopg2 as copg
import hashlib


def password_hasher(password):
    h = hashlib.new('sha256')
    bpass = password.encode()
    h.update(bpass)
    hashed = h.hexdigest()
    return hashed


def main_menu():
    main_menu_list = [
        'Create a new TODO list',
        'Open a TODO list',
        'Delete a TODO list',
        'Save and Exit'
    ]
    return main_menu_list


def create_list(cursor, user_id, list_name):
    cursor.execute(
        f'''
        insert into lists (user_id, list_name)
        values({user_id}, {list_name});
        '''
    )
    print(f'**New list({list_name} created**')


def del_list(cursor, list_id):
    cursor.execute(
        f'''
        delete from lists
        where id = {list_id};
        '''
    )


def create_task(cursor, list_id, task):
    cursor.execute(
        f'''
        insert into tasks (list_id, task)
        values({list_id}, {task});
        '''
    )


def del_task(cursor, task_id):
    cursor.execute(
        f'''
        delete from tasks
        where id = {task_id};
        '''
    )

def list_id_selector(cursor, user_id, )



conn = copg.connect(
database='todo_list',
user='postgres',
password='postgres',
host='127.0.0.1',
port='5432'
)
cur = conn.cursor()

username = input('user: ')
password = input('password: ')

cur.execute(
    f'''
    select * from users where user_name = '{username}';
    '''
)
user = cur.fetchone()

if user is None:
    print('User/Password Incorrect')
else:
    if user[2] == password_hasher(password):
        pass
    else:
        print('User/Password Incorrect')

while True:
    print('****     Do all of them now, not tomorrow     ****')
    for index, item in enumerate(main_menu()):
        print(f'{index + 1}. {item}')
    choice = input('Enter of them number ->')
    # create a new todo_list
    if choice == '1':
        list_name = input('New list name? ').lower()
        new_list = create_list(cur, user[0], list_name)

        # add or not task to new list
        while True:
            answer = input('Add a task?(Yes/no) ').lower()
            if answer in ['yes', 'y', '']:
                write_task = input('Write your task: ')
                create_task(cur, list_id, write_task)

            elif answer in ['no', 'n', 'nope']:
                break