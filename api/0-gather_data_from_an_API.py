#!/usr/bin/python3
"""Gather data about completed tasks for specific user"""

import requests
import sys

if __name__ == "__main__":

    if sys.argv[1].isdigit():

        user_id = sys.argv[1]
        employee = requests.get('https://jsonplaceholder.typicode.com/users',
                                params={'id':  user_id})
        tasks = requests.get('https://jsonplaceholder.typicode.com/todos',
                             params={'userId':  user_id})

        user_name = employee.json()[0].get('name')
        total_tasks = len(tasks.json())
        done_tasks = 0

        # count done tasks
        for task in tasks.json():
            if task.get('completed'):
                done_tasks += 1

        print("Employee {} is done with tasks({}/{}):\
    ".format(user_name, done_tasks, total_tasks))
        for task in tasks.json():
            if task.get('completed'):
                print("\t {}".format(task.get('title')))
