#!/usr/bin/python3
"""test"""
import json
import requests
import sys


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    inp = int(sys.argv[1])
    us_ok = requests.get(api_url + "users/{}".format(inp)).json()
    username = us_ok.get("name")
    todo_oka = requests.get(f'{api_url}todos', params={"userId": inp})
    todo_ok = todo_oka.json()

    done_list = []
    for t in todo_ok:
        if t.get("completed") is True:
            done_list.append(t.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(username,
          len(done_list), len(todo_ok)))

    for done in done_list:
        print("\t {}:".format(done))
