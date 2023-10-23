#!/usr/bin/python3
import json
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python3 gather_data_and_export_json.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]
user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
tasks_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

user_data = requests.get(user_url).json()
tasks_data = requests.get(tasks_url).json()

tasks_list = [{"task": task['title'], "completed": task['completed'],
              "username": user_data['username']} for task in tasks_data]

output_file = f"{employee_id}.json"
with open(output_file, "w") as f:
    json.dump({user_data['id']: tasks_list}, f)

print(f"Data has been exported to {output_file}")
