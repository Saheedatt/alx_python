import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]
url_employee = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
url_todos = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

# Get employee details
response_employee = requests.get(url_employee)
employee_data = response_employee.json()
employee_name = employee_data.get("name")

if not employee_name:
    print(f"No employee found with ID {employee_id}")
    sys.exit(1)

# Get employee's TODO list
response_todos = requests.get(url_todos)
todos = response_todos.json()

total_tasks = len(todos)
done_tasks = sum(1 for todo in todos if todo.get("completed"))

print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
for todo in todos:
    if todo.get("completed"):
        print(f"\t{todo.get('title')}")
