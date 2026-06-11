tasks = []
while True:
    print("\n====TO DO LIST====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task Status")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("\nEnter your choice : ")

    if choice == "1":
        print("Add Task")
        task_name = input("Enter Task Name : ")
        dead_line = input("Enter deadline : ")
        status = "Pending"
        task = {
            "task_name" : task_name, 
            "dead_line" : dead_line,
            "status" : status
        }
        tasks.append(task)
        print(task)
    elif choice == "2":
        print("View Tasks")
        if len(tasks)>0:
            count = 1
            for task in tasks:
                print(task)
                count += 1
        else:
            print("List is empty / No tasks available")
    elif choice == "3":
        print("Update Task Status")
        if len(tasks)>0:
            count = 1
            for task in tasks:
                print(count, task)
                count += 1
            task_number = int(input("Enter task number to update status : ")) 
            index = task_number - 1
            new_status = input("Enter new status : ")
            tasks[index]["status"] = new_status
            print("Task updated successfully!")
        else:
            print("List is empty / No tasks available")
    elif choice == "4":
        print("Delete Task")
        if len(tasks)>0:
            count = 1
            for task in tasks:
                print(count, task)
                count += 1
            task_number = int(input("Enter task number to delete task : "))
            index = task_number - 1
            tasks.pop(index)
            print("Task deleted successfully")
        else:
            print("List is empty / No tasks available")
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("invalid choice!")