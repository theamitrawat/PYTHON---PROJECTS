# The To_Do_List class is used to create and manage a list of tasks.
class To_Do_List:

  """
  The above function is the initialization method for a class that initializes an empty list called "user_tasks".
  """
  def __init__(self):
    self.user_tasks = []

  """
  The function `add_user_task` allows the user to input a task and adds it to a list of user tasks.
  """
  def add_user_task(self):
    task = input("\n\tEnter your task: ")
    self.user_tasks.append({"task": task, "completed": False})
    print("\n\t~ {Your task added successfully} ~")
    print("\n--------------------------------------------------------")

  """
    The function "view_user_tasks" prints a list of user tasks, including their completion status.:return: nothing.
  """
  def view_user_tasks(self):
    if not self.user_tasks:
      print("\n\t~ No user_tasks in the list. ~")
      print("\n--------------------------------------------------------")
      return
    print("\n\tYour list of user_tasks:\n")
    for task_id, task in enumerate(self.user_tasks, start=1):
      completed_mark = "✔" if task["completed"] else " "
      print(f"\t[{completed_mark}] {task_id}. {task['task'].capitalize()}")
    print("\n--------------------------------------------------------")

  """
  The function "mark_task_completed" allows the user to mark a task as completed by entering the task ID.
  """
  def mark_task_completed(self):
    task_ID = int(
          input("\n\tEnter task I to mark as completed: "))
    if 1 <= task_ID <= len(self.user_tasks):
      self.user_tasks[task_ID - 1]["completed"] = True
      print(f"\n\t~ Task {task_ID} marked as completed. ~")
    else:
      print("\n\t~ Invalid Task ID. ~")

    print("\n--------------------------------------------------------")
  """
  The function allows the user to mark a task as incomplete by providing the task ID.
  """
  def mark_task_incomplete(self):
    task_ID = int(
          input("\n\tEnter Task ID to mark as incomplete: "))
    if 1 <= task_ID <= len(self.user_tasks):
      self.user_tasks[task_ID - 1]["completed"] = False
      print(f"\n\t~ Task {task_ID} marked as incompleted. ~")
    else:
      print("\n\t~ Invalid Task ID. ~")

    print("\n--------------------------------------------------------")

  """
  The function `remove_user_task` removes a task from a list of user tasks based on the task ID provided by the user.
  """
  def remove_user_task(self):
    task_ID = int(input("\n\tEnter Task ID to remove: "))
    if 1 <= task_ID <= len(self.user_tasks):
      removed_task = self.user_tasks.pop(task_ID - 1)
      print(f"\n\t~ Task '{removed_task['task']}' removed. ~")
    else:
      print("\n\t~ Invalid Task ID. ~")

    print("\n--------------------------------------------------------")

  """
  The function `update_task` allows the user to update the description of a task based on its ID.
  """
  def update_task(self):
    task_ID = int(input("\n\tEnter Task ID to update: "))
    if 1 <= task_ID <= len(self.user_tasks):
      new_task_description = input("\n\tEnter new task description: ")
      self.user_tasks[task_ID - 1]["task"] = new_task_description.capitalize()
      print(f"\n\t~ Task {task_ID} updated. ~")
    else:
      print("\n\t~ Invalid Task ID. ~")

    print("\n--------------------------------------------------------")

"""
The main function provides a menu for managing a to-do list.
"""
def main():
  todo_list = To_Do_List()

  # The `while True:` loop is an infinite loop that keeps running until a break statement is encountered. In this case, it is used to continuously display the menu options and prompt the user for their choice until they choose to quit the program (option 7).
  while True:
    print("\n1. Add task.")
    print("2. View tasks")
    print("3. Mark Completed")
    print("4. Mark Incomplete")
    print("5. Remove task")
    print("6. Update task")
    print("7. Quit")

    user_choice = input("\n---> Enter your choice: ")

    choice_list = ['1','2','3','4','5','6','7']
    if user_choice in choice_list:

      # The `match` statement is a new feature introduced in Python 3.10. It is used for pattern matching, similar to a switch statement in other programming languages. In this case, it is used to match the value of `user_choice` and execute the corresponding code block.
      match user_choice:
        case '1':
          todo_list.add_user_task()
        case '2':
          todo_list.view_user_tasks()
        case '3':
          todo_list.mark_task_completed()
        case '4':
          todo_list.mark_task_incomplete()
        case '5':
          todo_list.remove_user_task()
        case '6':
          todo_list.update_task()
        case '7':
          print("\n~ Thanks to using to do list.Please use it again soon! ~")
          print("\n--------------------------------------------------------")
          break
    else:
      print("\n\tInvalid option. Please choose correct option.")
      print("\n--------------------------------------------------------")

# The `if __name__ == "__main__"` condition is used to check if the current script is being run as the main module. This condition is true when the script is executed directly, but false when the script is imported as a module into another script.
if __name__ == "__main__":
  main()
