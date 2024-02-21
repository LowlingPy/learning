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
        'Show all TODO lists',
        'Delete a TODO list',
        'Create a new user',
        'Save and Exit',
    ]
    return main_menu_list


def create_user(cursor, user_name, password):
    password = password_hasher(password)
    cursor.execute(
        f'''
        insert into users(
        username, password_hashed)
        values (
        '{user_name}', '{password}'
        );
        '''
    )
    conn.commit()


def create_list(cursor, connection, user_id, list_name):
    cursor.execute(
        f'''
        insert into list (user_id, name)
        values({user_id}, {list_name});
        '''
    )
    connection.commit()
    print(f'**New list({list_name} created**')


def search_list_by_name(cursor, list_name, user_id):
    cursor.execute(
        f'''
        select * from list where name is {list_name} and user_id is {user_id};
        '''
    )
    list = cursor.fetchone()
    list_id = list[0]
    return list_id


def delete_list(cursor, list_id):
    cursor.execute(
        f'''
        delete from list
        where id = {list_id};
        '''
    )
    print('List deleted')


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


def show_all_list(cursor, user_id):
    cursor.execute(
        f'''
        select * from list where uer_id = {user_id};)
        '''
    )
    list = cursor.fetchall()
    list_name =[]
    for item in list:
        list_name.append(item[2])
    return list_name


def check_table(cursor, connection):
    cursor.execute(
        f'''
        SELECT EXISTS (
        SELECT 1                 
        FROM information_schema.tables
        WHERE table_name = 'users')
        AS table_existence;
        '''
    )
    result = cursor.fetchone()
    print(f'User table exists : {result[0]}')
    if result[0] is False:
        password = password_hasher('admin')
        cursor.execute(
            f'''
            CREATE TABLE users(
            id bigserial primary key,
            username varchar(255),
            password_hashed varchar);
            '''
        )
        connection.commit()
        cursor.execute(
            f'''
            insert into users(username, password_hashed)
            values('admin', '{password}');
            '''
        )
        connection.commit()
        cursor.execute(
            f'''
                SELECT EXISTS (
                SELECT 1                 
                FROM information_schema.tables
                WHERE table_name = 'users')
                AS table_existence;
                '''
        )
        result = cursor.fetchone()
        print(f'User table exists : {result[0]}')

    cursor.execute(
        f'''
        SELECT EXISTS (
        SELECT 1                 
        FROM information_schema.tables
        WHERE table_name = 'list')
        AS table_existence;
        '''
    )
    result = cursor.fetchone()
    print(f'Lists table exists : {result[0]}')
    if result[0] is False:
        cursor.execute(
            f'''
            CREATE TABLE list(
            id int primary key,
            user_id integer NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id),
            name varchar(255));
            '''
        )
        connection.commit()
        cursor.execute(
            f'''
                SELECT EXISTS (
                SELECT 1                 
                FROM information_schema.tables
                WHERE table_name = 'list')
                AS table_existence;
                '''
        )
        result = cursor.fetchone()
        print(f'List table exists : {result[0]}')

    cursor.execute(
        f'''
        SELECT EXISTS (
        SELECT 1                 
        FROM information_schema.tables
        WHERE table_name = 'task')
        AS table_existence;
        '''
    )
    result = cursor.fetchone()
    print(f'Tasks table exists : {result[0]}')
    if result[0] is False:
        cursor.execute(
            f'''
            CREATE TABLE task(
            id bigserial primary key,
            list_id integer NOT NULL,
            FOREIGN KEY (list_id) REFERENCES list (id),
            task varchar(65535),
            task_status BOOLEAN DEFAULT False);
            '''
        )
        connection.commit()
        cursor.execute(
            f'''
                SELECT EXISTS (
                SELECT 1                 
                FROM information_schema.tables
                WHERE table_name = 'task')
                AS table_existence;
                '''
        )
        result = cursor.fetchone()
        print(f'Task table exists : {result[0]}')


conn = copg.connect(
database='todo_list',
user='postgres',
password='postgres',
host='127.0.0.1',
port='5432'
)
cur = conn.cursor()
check_table(cur, conn)

while True:
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    cur.execute(
        f'''
        select * from users where username = '{username}';
        '''
    )
    user = cur.fetchone()
    if user is not None:
        user_id = user[0]
        if user[2] == password_hasher(password):
            break
        else:
            print('User/Password Incorrect')
    elif user is None:
        print('User/Password Incorrect')


# start app
while True:
    print('****     Do all of them now, not tomorrow     ****')
    for index, item in enumerate(main_menu()):
        print(f'{index + 1}. {item}')
    choice = input('Enter of them number ->')

    # create a new todo_list
    if choice == '1':
        list_name = input('New list name? ').lower()
        new_list = create_list(cur, conn,user_id, list_name)
        list = search_list_by_name(cur, list_name, user_id)

        # add or not task to new list
        while True:
            answer = input('Add a task?(Yes/no) ').lower()
            if answer in ['yes', 'y', '']:
                write_task = input('Write your task: ')
                create_task(cur, list_id, write_task)

            elif answer in ['no', 'n', 'nope']:
                break

    # show todo list
    elif choice == '2':
        for index, item in enumerate(show_all_list(cur, user_id)):
            print(f'{index + 1}. {item}')

    # delete a todo list
    elif choice == '3':
        list_name = input('List you want to delete(list name) :').lower()
        list_id = search_list_by_name(cur, list_name, user_id)
        delete_list(cur, list_id)

    elif choice == '4':
        new_username = input('Enter new username :').lower()
        new_password = input('Enter new password :').lower()
        create_user(cur, new_username, new_password)

    elif choice == '5':
        exit()
