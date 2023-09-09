# This a applition for your todo list and manage your tasks
import json


def inti():
    todo_lists = [
        {
            'listname': 'test1',
            'done_task': [
                {
                    'id': 1,
                 'task': 'Test task'
                }
            ],
            'undone_task': [
                {
                    'id' : 2,
                    'task': 'Test task'
                }
            ],
        }

    ]
    file = open('todo_list.txt', 'r')
    data = file.read()

    if data:
        todo_lists = json.loads(data)
    file.close()
    return todo_lists


def main_menu():
    main_menu_list = [
        'Create a new TODO list',
        'Open a TODO list',
        'Delete a TODO list',
        'Save and Exit'
    ]
    return main_menu_list


def create_list():
    pass


def list_menu():
    sub_menu_list = [
         'Show your tasks',
         'Change status',
         'Edit tasks',
         'Save and back to Main Menu',
         'Save and Exit'
    ]
    return sub_menu_list


def show_tasks():
    task_list = [
        'All',
        'Done',
        'Undone',
    ]
    return task_list


def change_status():
    status_list = [
        'Make done',
        'Make undone'
    ]
    return status_list


def edit_task():
    edit_list = [
        'Remove a task',
         'Add a task'
    ]
    return edit_list

def save_and_back():
    pass


def save_and_exit():
    pass


def delete_list():
    pass


while True:
    print('****     Do all of them now, not tomorrow     ****')

    choice = input('Enter of them number ->')

    if choice == '1':
        new_list = {
            'listname': None,
            'done_task': [],
            'undone_task': [],
        }
        new_list['listname'] = input('New TODO list name: ').lower()
        new_task_list = []
        while True:
            answer = input('Add a task?(Yes/No) ').lower()
            if answer in ['yes', 'y', '\n']:
                new_task = input('Write your task: ')
                new_task_list.append(new_task)
            elif answer in ['no', 'n', 'nope']:
                break

        new_list['undone_task'] = new_task_list

    elif choice == '2':
        list_sel = input('Enter your TODO lis name: ')
        for list in todo_lists:
            if list['listname'] == list_sel.lower():
                list_sel = list
                break
            else:
                print('List not found')
        while True:

            choice = input('Enter of them number ->')

            if choice == '1':

                choice = input('Enter of them number ->')
                done = '\n'.join(list_sel['done_task'])
                undone = '\n'.join(list_sel['undone_task'])
                if choice == '1':
                    print(f'Done:\n{done}\n Undone:\n{undone}')
                elif choice == '2':
                    print(f'Done:\n{done}')
                elif choice == '3':
                    print(f'Undone:\n{undone}')
            elif choice == '2':

                choice = input('Enter of them number ->')
                if choice == '1':

                elif choice == '2':

            elif choice == '3':

                choice = input('Enter of them number ->')
                if choice == '1':

                elif choice == '2':

            elif choice == '4':
                break

            elif choice == '5':

    elif choice == '3':

    elif choice == '4':


