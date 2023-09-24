#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee
"""

from requests import get
from sys import argv

if __name__ == '__main__':
    URL = 'https://jsonplaceholder.typicode.com'
    td_url = URL + "/user/{}/todos".format(argv[1])
    n_url = URL + "/users/{}".format(argv[1])
    td_result = get(td_url).json()
    n_result = get(n_url).json()

    todo_count = len(td_result)
    todo_complete = len([todo for todo in td_result
                         if todo.get("completed")])
    name = n_result.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(name, todo_complete, todo_count))
    for todo in td_result:
        if (todo.get("completed")):
            print("\t {}".format(todo.get("title")))