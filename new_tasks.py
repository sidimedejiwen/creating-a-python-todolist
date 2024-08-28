


tasks = [{"task":"Quran", "completed":True},
 {"task":"pray","completed":True },
 {"task":"study","completed":False},
 {"task":"sleep","completed":False},
 {"task":"CODE_WITH_PYTHON", "completed":True}]
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
  views_tasks(tasks) 
  
    

    

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
  views_tasks(tasks)