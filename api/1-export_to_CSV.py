import csv
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]
url_user = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
response_user = requests.get(url_user)
user_data = response_user.json()
employee_name = user_data.get("name")

if not employee_name:
    print(f"No employee found with ID {employee_id}")
    sys.exit(1)

url_todos = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
response_todos = requests.get(url_todos)
todos = response_todos.json()

total_tasks = len(todos)
done_tasks = sum(1 for todo in todos if todo.get("completed"))

csv_file_name = f"{employee_id}.csv"

# Write data to CSV
with open(csv_file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
    for todo in todos:
        task_completed_status = "Completed" if todo.get("completed") else "Not Completed"
        writer.writerow([employee_id, employee_name, task_completed_status, todo.get("title")])

print(f"Data exported to {csv_file_name}.")
