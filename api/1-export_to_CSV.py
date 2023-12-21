#!/usr/bin/python3
"""
Given employee ID, exports information about
his/her todo list progress to a CSV file.
"""
import csv
import requests
import sys


def export_to_csv(employee_id):
    """
    Given employee ID, exports information about his/her
    todo list progress to a CSV file.
    """
    todos = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    users_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

    todos = requests.get(todos)
    user = requests.get(users_url)

    if todos.status_code == 200 and user.status_code == 200:
        todos_data = todos.json()
        user_data = user.json()

        user_name = user_data['username']

        filename = f"{employee_id}.csv"

        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            csv_writer.writerow(['UserID', 'username', 'Completed', 'Title'])

            for task in todos_data:
                csv_writer.writerow([
                    str(task['userId']),
                    user_name,
                    str(task['completed']),
                    task['title']
                ])
    else:
        print("Failed to fetch data from the server.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the employee ID as an argument.")
    else:
        employee_id = sys.argv[1]
        export_to_csv(employee_id)
