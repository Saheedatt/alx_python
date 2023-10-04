import requests
import sys

if len(sys.argv) != 2:
    print("First line formatting: Incorrect")
    print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]
url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

response = requests.get(url)

if response.status_code != 200:
    print("First line formatting: Incorrect")
    print(f"No employee found with ID {employee_id}")
    sys.exit(1)

employee_data = response.json()
employee_name = employee_data.get("name")

if not employee_name:
    print("First line formatting: Incorrect")
    print(f"No employee found with ID {employee_id}")
    sys.exit(1)

url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
response = requests.get(url)
todos = response.json()

total_tasks = len(todos)
done_tasks = sum(1 for todo in todos if todo.get("completed"))

print(f"First line formatting: OK")
print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
for todo in todos:
    if todo.get("completed"):
        print(f"\t{todo.get('title')}")
