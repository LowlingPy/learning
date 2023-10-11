# This a applition for your todo list and manage your tasks

import json
import os


def init():
    data_lists = []
    if os.path.exists('todo_list.txt'):
        file = open('todo_list.txt', 'r')
        data = file.read()
        if data:
            data_lists = json.loads(data)
    else:
        file = open('todo_list.txt', 'w')
    file.close()
    return data_lists


def main_menu():
    main_menu_list = [
        'Create a new TODO list',
        'Open a TODO list',
        'Delete a TODO list',
        'Save and Exit'
    ]
    return main_menu_list


def create_list(name):
    new_list = {
        'listname': name,
        'done_task': [],
        'undone_task': [],
        'counter': 0
    }
    return new_list


def list_menu():
    sub_menu_list = [
        'Show your tasks',
        'Change status',
        'Manage tasks',
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


def manage_task():
    edit_list = [
        'Remove a task',
        'Add a task'
    ]
    return edit_list


def add_task(task, selected_dic):
    new_task = {}
    new_task['task'] = task
    selected_dic['counter'] += 1
    new_task['id'] = selected_dic['counter']
    selected_dic['undone_task'].append(new_task)


def save(data_list):
    data = open('todo_list.txt', 'w')
    save = json.dumps(data_list)
    data.write(save)
    data.close()


def delete_list(target_list, all_lists):
    for list in all_lists:
        if list['listname'] == target_list:
            all_lists.remove(list)
            break


def task_tup(request, selected_dic):
    done_list = selected_dic['done_task']
    undone_list = selected_dic['undone_task']
    all_task_list = done_list + undone_list
    dic_to_tup = []
    # show all
    if request == 'all':
        for item in all_task_list:
            task = item['task']
            id = item['id']
            x = (task, id)
            dic_to_tup.append(x)

    # show done
    elif request == 'done':
        for item in done_list:
            task = item['task']
            id = item['id']
            x = (task, id)
            dic_to_tup.append(x)

    # show undone
    elif request == 'undone':
        for item in undone_list:
            task = item['task']
            id = item['id']
            x = (task, id)
            dic_to_tup.append(x)

    return  dic_to_tup


todo_lists = init()
while True:
    print('****     Do all of them now, not tomorrow     ****')
    for index, item in enumerate(main_menu()):
        print(f'{index + 1}. {item}')
    choice = input('Enter of them number ->')
    #create a new list
    if choice == '1':
        list_name = input('New list name? ').lower()
        new_list = create_list(list_name)
        # add or not task to new list
        while True:
            answer = input('Add a task?(Yes/no) ').lower()
            if answer in ['yes', 'y', '']:
                write_task = input('Write your task: ')
                add_task(write_task, new_list)

            elif answer in ['no', 'n', 'nope']:
                break

        todo_lists.append(new_list)

    #open list
    elif choice == '2':
        dic_sel = input('Enter your TODO lis name: ').lower()
        for dic in todo_lists:
            if dic['listname'] == dic_sel.lower():
                dic_sel = dic
                break
            else:
                print('List not found')
        #list menu
        while True:
            for index, item in enumerate(list_menu()):
                print(f'{index + 1}. {item}')
            choice = input('Enter number ->')
            #show tasks
            if choice == '1':
                for index, item in enumerate(show_tasks()):
                    print(f'{index + 1}. {item}')
                choice = input('Enter number ->')

                #show all
                if choice == '1':
                    print(task_tup('all',dic_sel))
                #show done
                elif choice == '2':
                    print(task_tup('done', dic_sel))
                #show undone
                elif choice == '3':
                    print(task_tup('undone', dic_sel))
            #change status
            elif choice == '2':
                for index, item in enumerate(change_status()):
                    print(f'{index + 1}. {item}')
                choice = input('Enter number ->')

                #make done
                if choice == '1':
                    print(task_tup('undone', dic_sel))
                    id_for_done = input('Select an id ->')

                #make undone
                elif choice == '2':
                    print(task_tup('done', dic_sel))
                    id_for_done = input('Select an id ->')

            #edit task
            elif choice == '3':
                for index, item in enumerate(manage_task()):
                    print(f'{index + 1}. {item}')
                choice = input('Enter number ->')
                #remove
                if choice == '1':
                    print(task_tup('all', dic_sel))
                    id_for_done = input('Select an id ->')
                #add
                elif choice == '2':
                    new_task = {}
                    new_task['task'] = input('Write your task: ')
                    counter = len(dic_sel['done_task'] + dic_sel['undone_task'])
                    new_task['id'] = counter + 1
                    dic_sel['undone_task'].append(new_task)

            elif choice == '4':
                save(todo_lists)
                break

            elif choice == '5':
                save(todo_lists)
                exit()

    elif choice == '3':
        del_list = input('')
        delete_list()

    elif choice == '4':
        save(todo_lists)
        exit()


