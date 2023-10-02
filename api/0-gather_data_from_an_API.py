import requests
import sys

def get_employee_info(employee_id):
    # Endpoint to get employee details
    employee_endpoint = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_endpoint)
    employee_data = response.json()
    return employee_data

def get_employee_todos(employee_id):
    # Endpoint to get employee TODO list
    todos_endpoint = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todos_endpoint)
    todos_data = response.json()
    return todos_data

def display_employee_progress(employee_id):
    employee_info = get_employee_info(employee_id)
    todos = get_employee_todos(employee_id)

    employee_name = employee_info['name']
    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo['completed'])

    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    for todo in todos:
        if todo['completed']:
            print(f"\t{todo['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    display_employee_progress(employee_id)
