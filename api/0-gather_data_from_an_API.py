import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]

# Get employee details
employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
employee_response = requests.get(employee_url)

if employee_response.status_code != 200:
    print(f"No employee found with ID {employee_id}")
    sys.exit(1)

employee_data = employee_response.json()
employee_name = employee_data.get("name", "Unknown Employee")

# Get employee's TODO list
todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
todos_response = requests.get(todos_url)

if todos_response.status_code != 200:
    print("Unable to fetch TODO data.")
    sys.exit(1)

todos = todos_response.json()

total_tasks = len(todos)
done_tasks = sum(1 for todo in todos if todo["completed"])

print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
for todo in todos:
    if todo["completed"]:
        print(f"\t{todo['title']}")
