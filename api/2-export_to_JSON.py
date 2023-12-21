#!/usr/bin/python3
"""
Given employee ID, exports information about
his/her todo list progress to a JSON format.
"""

import json
import requests
import sys


def export_to_json(employee_id):
    """
    Given employee ID, exports information about
    his/her todo list progress to a JSON format.
    """
    todos = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

    todos = requests.get(todos)
    user = requests.get(user_url)

    if todos.status_code == 200 and user.status_code == 200:
        todos_data = todos.json()
        user_data = user.json()

        user_name = user_data['username']
        tasks = []

        for task in todos_data:
            task_info = {
                "task": task['title'],
                "completed": task['completed'],
                "username": user_name
            }
            tasks.append(task_info)

        filename = f"{employee_id}.json"
        with open(filename, 'w') as file:
            json.dump({f"{employee_id}": tasks}, file)
    else:
        print("Failed to fetch data from the server.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the employee ID as an argument.")
    else:
        employee_id = sys.argv[1]
        export_to_json(employee_id)
