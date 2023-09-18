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
    todo = requests.get(api_url + "todos", params={"userId": param}).json

    done_list = []

    for line in todo:
        if line["completed"] is True:
            done_list.append(line["title"])
    print("Employee {} is done with tasks({}/{}):".format(
        us["name"], len(done_list), len(todo)))
    for done in done_list:
        print("\t {}".format(done))
