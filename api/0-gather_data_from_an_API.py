#!/usr/bin/python3
"""test"""
import json
import requests
import sys


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    inp = int(sys.argv[1])
    us_ok = requests.get(api_url + "users/{}".format(inp)).json()
    todo_ok = requests.get(api_url + "user/{}/todos".format(inp)).json()

    done_list = []
    for t in todo_ok:
        if t.get("completed") is True:
            done_list.append(t.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(us_ok.get("name"),
          len(done_list), len(todo_ok)))

    for done in done_list:
        print("\t {}:".format(done))
