todo_list = []

def show_tasks():
    if not todo_list:
        print("No tasks found.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
    print()

def add_task():
    task = input("Enter your task to add : ")
    todo_list.append(task)
    print(f"Task '{task}' added to your To-Do list!\n")

def delete_task():
    show_tasks()
    if todo_list:
        try:
            task_num = int(input("Enter the  Serial number of the task to delete : "))
            deleted_task = todo_list.pop(task_num - 1)
            print(f"Task '{deleted_task}' deleted from your list!\n")
        except (ValueError, IndexError):
            print("Invalid task number!\n")

def show_menu():
    print("To-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Delete a Task")
    print("4. Exit")

def todo_app():
    while True:
        show_menu()
        choice = input("Please enter your choice 1 to 4 : ")
        
        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
           delete_task()
        elif choice == '4':
            print("Exiting the to-do list program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

todo_app()
