# This a applition for your TODO list and manage your tasks
import json

todo_lists = [
    {
        'listname': None,
        'done_task': None,
        'undone_task': None,
    }
]
file = open('todo_list.txt', 'r')
data = file.read()

if data:
    todo_lists = json.loads(data)
file.close()

while True:
    print('****     Do all of them now, not tomorrow     ****')
    print('''
    1. Creat a new TODO list
    2. Open a TODO list
    3. Delete a TODO list
    4. Save and Exit
    ''')
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
            print('''
            1. Show your tasks
            2. Change status
            3. Edit tasks
            4. Save and back to Main Menu
            5. Save and Exit
            ''')
            choice = input('Enter of them number ->')

            if choice == '1':
                print('''
                1. All
                2. Done
                3. Undone
                ''')
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
                print('''
                1. Make done
                2. Make undone
                ''')
                choice = input('Enter of them number ->')

                if choice == '1':

                elif choice == '2':

            elif choice == '3':
                print('''
                1. Remove a task
                2. Add a task
                ''')
                choice = input('Enter of them number ->')

                if choice == '1':

                elif choice == '2':

            elif choice == '4':

                break
            elif choice == '5':

                exit()

    elif choice == '3':

    elif choice == '4':

        exit()
