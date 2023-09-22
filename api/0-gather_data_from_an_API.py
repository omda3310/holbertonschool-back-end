#!/usr/bin/python3
"""test"""
import json
import requests
import sys

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    inp = int(sys.argv[1])
    user_info = requests.get(api_url + "users/{}".format(inp)).json()

    # Fix the URL formatting for todos
    todos_url = api_url + "users/{}/todos".format(inp)
    todos_info = requests.get(todos_url).json()

    done_list = []
    for t in todos_info:
        if t.get("completed") is True:
            done_list.append(t.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(user_info.get("name"),
          len(done_list), len(todos_info)))

    for done in done_list:
        print("\t {}:".format(done))
