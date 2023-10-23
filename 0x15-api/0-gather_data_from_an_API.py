#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee
"""

from requests import get
from sys import argv

if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = argv[1]
        main_url = 'https://jsonplaceholder.typicode.com'
        todo_url = main_url + "/todos?userId={}".format(employee_id)
        user_url = main_url + "/users/{}".format(employee_id)

        try:
            todo_response = get(todo_url)
            user_response = get(user_url)

            if todo_response.status_code == 200 and user_response.status_code == 200:
                todo_data = todo_response.json()
                user_data = user_response.json()

                employee_name = user_data.get("name")
                total_tasks = len(todo_data)
                completed_tasks = sum(1 for task in todo_data if task["completed"])

                print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_tasks, total_tasks))
                for task in todo_data:
                    if task["completed"]:
                        print("\t{}".format(task["title"]))
            else:
                print("Error: Unable to fetch data. Please check the employee ID.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    """main_url = 'https://jsonplaceholder.typicode.com'
    todo_url = main_url + "/user/{}/todos".format(argv[1])
    name_url = main_url + "/users/{}".format(argv[1])
    todo_result = get(todo_url).json()
    name_result = get(name_url).json()

    todo_num = len(todo_result)
    todo_complete = len([todo for todo in todo_result
                         if todo.get("completed")])
    name = name_result.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(name, todo_complete, todo_num))
    for todo in todo_result:
        if (todo.get("completed")):
            print("\t {}".format(todo.get("title")))"""
