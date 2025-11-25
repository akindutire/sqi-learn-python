print("_____Welcome to Todo List_______\n")


def view_tasks():
    print(f"Here are your task so far")
    for x, item in enumerate(todos, start=1):
        print(f"{x}. {item['name']} @ {item['time']} - {'Completed' if item.get('completed', False) else 'Not Completed'}")

todos = []
i = 0;
while True:
    if i == 0:
        task = {'name': str(input("Add a task: ")), 'time': str(input("Enter time for task: ")), 'completed': False}
        todos.append(task)
    else:
        print('''
              1. Add more task
              2. Delete task
              3. Edit task
              4. Mark task as completed
              5. Exit app
              ''')
        choice = int(input("Enter choice: "))
        if choice == 1:
            task = {'name': str(input("Add a task: ")), 'time': str(input("Enter time for task: "))}
            todos.append(task)
        elif choice == 2:
            view_tasks()
            _taskToRemoveIndex = int(input("Enter the index to delete: "))
            if _taskToRemoveIndex > len(todos) or _taskToRemoveIndex == 0:
                print("Error, activity index out of range")
                continue
            # _taskToRemove = todos[_taskToRemoveIndex-1]
            # todos.remove(_taskToRemove)
            # OR pop fn can remove at the beginning or at a certain index
            todos.pop(_taskToRemoveIndex-1) 
        elif choice == 3:
            view_tasks()
            _taskToRemoveIndex = int(input("Enter the index to replace: "))
            if _taskToRemoveIndex > len(todos) or _taskToRemoveIndex == 0:
                print("Error, activity index out of range")
                continue
            todos[_taskToRemoveIndex-1] = {'name': str(input("Add a task: ")), 'time': str(input("Enter time for task: "))}
            task = None
        elif choice == 4:
            view_tasks()
            _taskIndex = int(input("Enter the index to mark as completed: "))
            todos[_taskIndex-1]['completed'] = True
        elif choice == 5:
            break
        else:
            print("Invalid choice\n")
 
        
    i += 1


   

# if not todos:  # todos is empty or False
if len(todos) > 0 or not todos:
    print('\n______My Tasks______\n')
    for x, item in enumerate(todos, start=1):
        print(f"{x}. {item['name']} @ {item['time']}")