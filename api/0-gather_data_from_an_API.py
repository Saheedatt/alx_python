import requests
import sys

def get_employee_data(employee_id):
    # Endpoint URLs for employee details and todo list
    employee_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

    # Fetch employee details
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # Fetch todo list
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Display employee TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(employee_name, sum(1 for task in todo_data if task['completed']), len(todo_data)))
    for i, task in enumerate(todo_data, start=1):
        print("Task {} Formatting: {}".format(i, 'OK' if task['completed'] else 'Incorrect'))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_data(employee_id)
