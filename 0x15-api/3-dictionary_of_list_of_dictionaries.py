#!/usr/bin/python3
import json
import requests

# Fetch user and tasks data
user_data = requests.get("https://jsonplaceholder.typicode.com/users").json()
tasks_data = requests.get("https://jsonplaceholder.typicode.com/todos").json()

# Create a dictionary to store the tasks assigned to each user
user_tasks_dict = {user["id"]: [] for user in user_data}

# Populate the dictionary with tasks
for task in tasks_data:
    user_id = task["userId"]
    user_username = next((user["username"] for user in user_data
                         if user["id"] == user_id), "")
    user_tasks_dict[user_id].append({"username": user_username,
                                    "task": task["title"],
                                     "completed": task["completed"]})

# Ensure all users exist in the output
for user in user_data:
    user_id = user["id"]
    if user_id not in user_tasks_dict:
        user_tasks_dict[user_id] = []

# Sort user IDs in ascending order
sorted_user_ids = sorted(user_tasks_dict.keys())

# Create a final dictionary with sorted user IDs
sorted_user_tasks_dict = {user_id: user_tasks_dict[user_id]
                          for user_id in sorted_user_ids}

# Export data to JSON
output_file = "todo_all_employees.json"
with open(output_file, "w") as file:
    json.dump(sorted_user_tasks_dict, file, indent=2)

print(f"Data has been exported to {output_file}")
