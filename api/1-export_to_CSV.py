import csv
import requests
import sys


def export_to_csv(employee_id):
    todos = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    users_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

    todos = requests.get(todos)
    user = requests.get(users_url)

    if todos.status_code == 200 and user.status_code == 200:
        todos_data = todos.json()
        user_data = user.json()

        if isinstance(user_data, list) and len(user_data) > 0:
            user_name = user_data[0]['username']
        elif isinstance(user_data, dict):
            user_name = user_data.get('username', '')
        else:
            user_name = ''

        filename = f"{employee_id}.csv"

        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

            rows = [
                ['UserID', 'username', 'Completed', 'Title']
            ]

            for task in todos_data:
                rows.append([
                    str(task['userId']),
                    user_name,
                    str(task['completed']),
                    task['title']
                ])

            csv_writer.writerows(rows[1:])
    else:
        print("Failed to fetch data from the server.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the employee ID as an argument.")
    else:
        employee_id = sys.argv[1]
        export_to_csv(employee_id)
