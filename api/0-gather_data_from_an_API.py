#!/usr/bin/python3
"""
    For a given employee ID, returns information
    about his/her TODO list progress.
"""
import requests
import sys


if __name__ == '___main()__':
    api_url = 'https://jsonplaceholder.typicode/'
    param = sys.argv[1]
    usr = requests.get(api_url + "users/{}".format(param)).json()
    todo = requests.get(api_url + "todos", params={"userId": param}).json

    done_list = []

    for line in todo:
        if line.get("completed"):
            done_list.append(line.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(
        usr.get("name"), len(done_list), len(todo)))
    for done in done_list:
        print("\t {}".format(done))
