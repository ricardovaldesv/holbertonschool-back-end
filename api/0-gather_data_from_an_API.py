#!/usr/bin/python3
"""
given employee ID, returns information about his/her todo list progress.
"""
import requests
import sys


def display_employee():
    """
    given employee ID, returns information about his/her todo list progress.
    """
    employee_id = sys.argv[1]
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    users_url = 'https://jsonplaceholder.typicode.com/users'

    todos = requests.get(todos_url)
    users = requests.get(users_url)

    if todos.status_code == 200 and users.status_code == 200:
        todos_data = todos.json()
        users_data = users.json()

        # Create a dictionary for mapping user IDs to names
        user_names = {user['id']: user['name'] for user in users_data}

        completed_tasks = []

        # Get the completed tasks for the specific user
        for task in todos_data:
            user_id = task['userId']
            completed = task['completed']
            title = task['title']

            if user_id == int(employee_id) and completed:
                completed_tasks.append(title)

        # Print the employee's completed tasks
        if int(employee_id) in user_names:
            EMPLOYEE_NAME = user_names[int(employee_id)]
            NUMBER_OF_DONE_TASKS = len(completed_tasks)
            TOTAL_NUMBER_OF_TASKS = len([
                                         task for task in todos_data if task
                                         ['userId'] == int(employee_id)
                                         ])

            print(f"Employee {EMPLOYEE_NAME} is done with tasks"
                  f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

            # Print completed tasks in a list
            for TASK_TITLE in completed_tasks:
                print(f"\t {TASK_TITLE}")
        else:
            print("No employee was found with that ID.")

    else:
        print("The information could not be obtained from the server.")


if __name__ == "__main__":

    display_employee()
