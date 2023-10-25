#!/usr/bin/python3
'''
This script returns information about an employee's TODO list progress using a REST API.
Usage: python script_name.py employee_id
'''
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Invalid employee ID. Please provide a valid integer ID.")
        sys.exit(1)

    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todo_url = f'{user_url}/todos'

    user_response = requests.get(user_url).json()
    employee_name = user_response.get('name')

    todo_response = requests.get(todo_url).json()
    total_tasks = len(todo_response)
    non_completed = sum(1 for task in todo_response if not task['completed'])
    completed_tasks = total_tasks - non_completed

    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    for task in todo_response:
        if task['completed']:
            print(f"\t{task['title']}")
