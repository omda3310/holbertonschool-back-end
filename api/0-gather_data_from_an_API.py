#!/usr/bin/python3
"""
    For a given employee ID, returns information
    about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "___main()__":
    api_url = "https://jsonplaceholder.typicode.com"
    param = sys.argv[1]
    us = requests.get(api_url + "users/{}".format(param)).json()
    todo = requests.get(api_url + "todos", params={"userId": param}).json()

    if us.status_code == 200 and todo.status_code == 200:
        us_ok = us.json()
        todo_ok = todo.json()
        if not us_ok or not todo_ok:
            print("error")
        done_list = []
        for line in todo:
            if line.get("completed") is True:
                done_list.append(line.get("title"))
                print("Employee {} is done with tasks({}/{}):".format(
                    us.get("name"), len(done_list), len(todo)))
        for done in done_list:
            print("\t {}: OK".format(done))
