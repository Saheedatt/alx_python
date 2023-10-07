#!/usr/bin/python3
import json
import requests

def get_employee_data(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    return user_data, todos_data


def get_all_employee_data():
    all_employees_data = {}

    for employee_id in range(1, 11):
        user_data, todos_data = get_all_employee_data(employee_id)
        username = user_data['username']
        complete_task =[{"username": username, "tasks": task['title'], "completed": task['completed']} for task in todos_data]
        all_employees_data[employee_id] = complete_task

    return all_employees_data


def export_to_json(data):
    filename = "todo_all_employees.json"
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

if __name__ == "__main__":
    all_employees_data = get_all_employee_data()
    export_to_json(all_employees_data)
