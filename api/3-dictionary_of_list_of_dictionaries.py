#!/usr/bin/python3
"""
Exports information about
his/her todo list progress to a JSON format.
"""

import json
import requests


def export_all_to_json():
    """
    Exports information about
    his/her todo list progress to a JSON format.
    """
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    users = requests.get(users_url)
    todos = requests.get(todos_url)

    if users.status_code == 200 and todos.status_code == 200:
        users_data = users.json()
        todos_data = todos.json()

        all_employees_data = {}

        for user in users_data:
            user_id = user['id']
            username = user['username']
            user_tasks = []

            for task in todos_data:
                if task['userId'] == user_id:
                    task_info = {
                        "username": username,
                        "task": task['title'],
                        "completed": task['completed']
                    }
                    user_tasks.append(task_info)

            all_employees_data[user_id] = user_tasks

        filename = "todo_all_employees.json"
        with open(filename, 'w') as file:
            json.dump(all_employees_data, file)
        print(f"Data exported to {filename}")
    else:
        print("Failed to fetch data from the server.")


if __name__ == "__main__":
    export_all_to_json()
