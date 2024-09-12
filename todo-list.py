todo_list = []
while True:
  if len(todo_list) == 0:
    print("Your ToDo list is empty")
  else:
    print("ToDo list:")
    index = 1
    for task in todo_list:
      print(f"{index}. {task}")
      index += 1
  
  print("Options: ")
  print("1) Add Task")
  print("2) Remove Task")
  print("3) Quit")

  choice = input("Choose: ")

  if choice == "1":
    new_task = input("Input a task: ")
    todo_list.append(new_task)
    print("Your task has been added")
  elif choice == "2":
    if todo_list == 0:
      print("Your ToDo list is empty")
    else:
      todo_list.pop()
  elif choice == "3":
    print("Quitting")
    break