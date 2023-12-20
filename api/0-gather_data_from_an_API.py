#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her todo list progress.
"""
import requests
from sys import argv


def display_info():
    '''
    This is the function to serch for a user info and tasks.
    '''

    employee_id = str(argv[1])

    users_url = "https://jsonplaceholder.typicode.com/users/" + employee_id

    users_response = requests.get(users_url)

    if users_response.status_code == 200:
        users_data = users_response.json()
        user_name = users_data.get("name")  # Name of the user

    todos_url = "https://jsonplaceholder.typicode.com/todos/"

    todos_response = requests.get(todos_url)

    if todos_response.status_code == 200:
        todos_data = todos_response.json()
        list_complete_task = []
        num_of_task = 0
        num_of_complete_task = 0
        for dict in todos_data:
            if dict.get("userId") == int(employee_id)\
               and dict.get("completed"):
                list_complete_task.append(dict.get("title"))
                num_of_complete_task += 1
            if dict.get("userId") == int(employee_id):
                num_of_task += 1
    # print(f"Employee {user_name} is done
    # with tasks({num_of_complete_task}/{num_of_task}):")
    all_text = f"Employee {user_name} is done with tasks"
    print(f"{all_text}({num_of_complete_task}/{num_of_task}):")
    for task in list_complete_task:
        print(f"\t {task}")


if __name__ == "__main__":

    display_info()
