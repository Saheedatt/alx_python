import requests
import sys

if len(sys.argv) !=2:
    print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]
employee_name_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
response = requests.get(employee_name_url)
employee_name = response.json().get("name")

if not employee_name:
    print(f"No employee found with ID {employee_id}")
    sys.exit(1)

employee_todo_list_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
response = requests.get(employee_todo_list_url)
todos = response.json()

total_tasks = len(todos)
done_tasks = sum(1 for todo in todos if todo.get("completed"))

print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
for todo in todos:
    if todo.get("completed"):
        print(f"\t {todo.get('title')}")
