import requests

def get_employee_todo_list_progress(employee_id):

  # Get employee details
  employee_details_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
  employee_details_response = requests.get(employee_details_url)
  employee_details = employee_details_response.json()

  # Get employee TODO list
  employee_todo_list_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
  employee_todo_list_response = requests.get(employee_todo_list_url)
  employee_todo_list = employee_todo_list_response.json()

  # Calculate TODO list progress
  number_of_done_tasks = 0
  total_number_of_tasks = 0
  for task in employee_todo_list:
    total_number_of_tasks += 1
    if task["completed"]:
      number_of_done_tasks += 1

  # Display TODO list progress
  print(f"Employee {employee_details['name']} is done with tasks {number_of_done_tasks}/{total_number_of_tasks}:")
  for task in employee_todo_list:
    if task["completed"]:
      print(f"\t{task['title']}")

if __name__ == "__main__":

  # Get employee ID from user input
  employee_id = input("Enter employee ID: ")

  # Get employee TODO list progress
  employee_todo_list_progress = get_employee_todo_list_progress(employee_id)

  # Display TODO list progress
  print(employee_todo_list_progress)
