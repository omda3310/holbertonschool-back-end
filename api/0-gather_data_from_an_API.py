#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee
"""

import json
import requests
import sys


if __name__ == '__main__':
    main_url = 'https://jsonplaceholder.typicode.com'
    todo_url = main_url + "/users/{}/todos".format(sys.argv[1])
    name_url = main_url + "/users/{}".format(sys.argv[1])
    todo_result = requests.get(todo_url).json()
    name_result = requests.get(name_url).json()

    todo_num = len(todo_result)
    todo_complete = len([todo for todo in todo_result
                         if todo.get("completed")])
    name = name_result.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(name, todo_complete, todo_num))
    for todo in todo_result:
        if (todo.get("completed")):
            print("\t {}".format(todo.get("title")))
