import json
import sys
import urllib.request

def get_employee_data(employee_id):
    # Endpoint URLs for employee details and todo list
    employee_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

    # Fetch employee details
    with urllib.request.urlopen(employee_url) as response:
        employee_data = json.loads(response.read().decode())
        employee_name = employee_data.get('name', 'Unknown Employee')

    # Fetch todo list
    with urllib.request.urlopen(todo_url) as response:
        todo_data = json.loads(response.read().decode())

    # Display employee TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(employee_name, sum(task['completed'] for task in todo_data), len(todo_data)))

    # Display each task
    for i, task in enumerate(todo_data, start=1):
        print("Task {} Formatting: {}".format(i, 'OK' if task['completed'] else 'Incorrect'))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_data(employee_id)
