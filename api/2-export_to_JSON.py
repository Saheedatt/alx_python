import json
import requests
import sys


if len(sys.argv) != 2:
    print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]
url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
response = requests.get(url)
employee_data = response.json()

if "id" not in employee_data:
    print(f"No employee found with ID {employee_id}")
    sys.exit(1)

url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
response = requests.get(url)
todos = response.json()

employee_name = employee_data["username"]

total_tasks = len(todos)
done_tasks = sum(1 for todo in todos if todo.get("completed"))

# Prepare the data in JSON format
data = {
    "USER_ID": [{
        "task": todo["title"],
        "completed": todo["completed"],
        "username": employee_name
    } for todo in todos]
}

# Write the JSON data to a file
filename = f"{employee_id}.json"
with open(filename, "w") as json_file:
    json.dump({employee_id: data}, json_file, indent=4)

print(f"Data exported to {filename}")
