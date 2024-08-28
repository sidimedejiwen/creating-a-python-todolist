# 1-add tasks to a list
# 2-mark task as complete
# 3-view tasks
# 4-Quit
tasks=[]
def function():
  message =""""1-add tasks to a list
  2-mark task as complete
  3-view tasks
  4-Quit"""

  while True: 
    print(message)
    choice = input("enter your choice :")
    if choice == "1":
      add_task()
    elif choice == "2":
      mark_task_complete()
    elif choice == "3":
      views_tasks(tasks)
    elif choice == "4":
      break
    else:
      print("invalid choise, please enter a number between 1 and 4")


def add_task():
  #get task from user
   task = input("Enter task :")
  #define task status
   task_info = {"task": task, "completed":False}
  #add task to the list of tasks
   tasks.append(task_info)
   print("Task added to the liste successfuly")
   
def mark_task_complete():
  #get list of incomplete tasks
  incomplete_tasks = [task for task in tasks if  
  task["completed"] == False]
  if not incomplete_tasks:
    print("no incomplete tasks")
    return 
  #show theme to the user
  for i , task in enumerate(incomplete_tasks):
    print(f" {i+1}- {task['task']}")
    print("***"*10)
  #get the task from the user
  task_number = int(input("choose the task to complete :"))
  #mark the task as complete
  incomplete_tasks[task_number -1]["completed"]= True

  print("task marked completed")
  
def views_tasks(tasks):
  # if there isn't any task,return no task exist
  if not tasks:
    print("no tasks to view")
    return

  for i, task in enumerate(tasks):
    if task["completed"]:
      status = "✅"
    else:
      status="😅"
    print(f"{i+1}.{task['task']}{status}")
  #1.pray at mosque ✅
  #2.read quran ✅
  #3.code with python 😅

function()