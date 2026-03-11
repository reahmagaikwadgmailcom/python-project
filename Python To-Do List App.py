# To-Do List Application

tasks = []

while True:
    print("\n---- TO DO LIST MENU ----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == '2':
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task)

    elif choice == '3':
        task_no = int(input("Enter task number to delete: "))
        if 0 < task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            print("Task removed:", removed)
        else:
            print("Invalid task number")

    elif choice == '4':
        print("Exiting To-Do List App")
        break

    else:
        print("Invalid choice")
