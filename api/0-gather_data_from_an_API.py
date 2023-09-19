#!/usr/bin/python3
"""
Checks student output for returning info from REST API
"""

import requests
import sys

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    us_ok = requests.get(api_url + "users/{}".format(
        sys.argv[1])).json()
    todo_ok = requests.get(
        api_url + "todos", params={"userId": sys.argv[1]}).json()

    done_list = []
    for t in todo_ok:
        if t.get("completed") is True:
            done_list.append(t.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        us_ok.get("name"), len(done_list), len(todo_ok)))

    for done in done_list:
        print("\t {}:".format(done))
