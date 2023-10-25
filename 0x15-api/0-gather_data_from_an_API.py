#!/usr/bin/python3
'''This script  returns information about his/her
TODO list progress using RestApi'''
import requests
import sys


if __name__ == '__main__':
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        exit()

    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = '{api}/users/{id}'.format(api=base_url, id=employee_id)
    todo_url = '{user_url}/todos'.format(user_url=user_url)

    '''get the user's response'''
    res = requests.get(user_url).json()
    '''get the employee name'''
    name = res.get('name')
    '''Get the todo response'''
    res = requests.get(todo_url).json()
    '''get total number of tasks'''
    total_tasks = len(res)
    '''get the incompleted tasks'''
    non_completed = sum([elem['completed'] is False for elem in res])
    '''get completed tasks'''
    completed_tasks = total_tasks - non_completed
    str = ("Employee {emp_name} is done with tasks" +
           "({completed_tasks}/{total_tasks}): ")
    print(str.format(emp_name=name, completed_tasks=completed_tasks,
                     total_tasks=total_tasks))
    '''print the the complete tasks'''
    for elem in res:
        if elem.get('completed') is True:
            print('\t', elem.get('title'))
