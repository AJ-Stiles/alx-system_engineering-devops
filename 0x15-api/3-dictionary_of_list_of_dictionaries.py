#!/usr/bin/python3
import requests
import json

base_url = "https://jsonplaceholder.typicode.com/users"
todo_url = "https://jsonplaceholder.typicode.com/todos"

user_data = requests.get(base_url).json()
tasks_data = requests.get(todo_url).json()

task_dict = {}

for user in user_data:
    user_id = user["id"]
    username = user["username"]
    user_tasks = []

    for task in tasks_data:
        if task["userId"] == user_id:
            user_tasks.append({"username": username, "task": task["title"],
                               "completed": task["completed"]})

    task_dict[user_id] = user_tasks

with open("todo_all_employees.json", "w") as file:
    json.dump(task_dict, file)

print("Data has been exported to todo_all_employees.json")
