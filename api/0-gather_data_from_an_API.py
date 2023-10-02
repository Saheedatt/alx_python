import sys
import requests

def get_employee_data(employee_id):
    # Endpoint URLs for emplyee details and todo list
    employee_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

    #Fetch employee details
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data['name']

    #to fetch todo list
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    #count completed tasks
    completed_tasks = [task for task in todo_data if task['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todo_data)

    # Display employee TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(employee_name, num_completed_tasks, total_tasks))
    for task in completed_tasks:
        print("    {}".format(task['title']))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_data(employee_id)