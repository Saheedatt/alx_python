import json
import urllib.request

def get_employee_data(employee_id):
    # Endpoint URLs for employee details and todo list
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetch employee details
    with urllib.request.urlopen(employee_url) as response:
        employee_data = json.loads(response.read().decode())
        employee_name = employee_data.get('name', 'Unknown Employee')

    # Fetch todo list
    with urllib.request.urlopen(todo_url) as response:
        todo_data = json.loads(response.read().decode())

    # Display employee TODO list progress
    print(f"Employee {employee_name} is done with tasks({sum(1 for task in todo_data if task['completed'])}/{len(todo_data)}):")
    for i, task in enumerate(todo_data, start=1):
        print(f"Task {i} Formatting: {'OK' if task['completed'] else 'Incorrect'}")

if __name__ == "__main__":
    try:
        employee_id = int(input("Enter the employee ID: "))
        get_employee_data(employee_id)
    except ValueError:
        print("Employee ID should be an integer.")
