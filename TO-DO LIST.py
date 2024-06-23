class ToDo:
    #intialize the object with a list using constructor
    def _init_(self):
        self.tasks = []

   #to add task to the to do list by adding description of the task
    def add_task(self, task_description):
        self.tasks.append({"description": task_description, "completed": False})
        print(f"Task '{task_description}' added.")
    
    #to view all the tasks that are added to the todo list
    def view_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
        else:
            for index, task in enumerate(self.tasks):
                status = "Done" if task["completed"] else "Pending"
                print(f"{index + 1}. {task['description']} - {status}")

    #to mark the task completed to change their status to completed;
    def mark_task_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")

    #to delete the task from the to do list
    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            task = self.tasks.pop(task_number - 1)
            print(f"Task '{task['description']}' deleted.")
        else:
            print("Invalid task number.")

todo_list = ToDo()  #to create a instance of class ToDo 


#while loop to loop run the program until user exits 
while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
        
    choice = input("Enter your choice: ").strip()
        
    if choice == '1': #1 too add task
        task_description = input("Enter task description: ").strip()
        todo_list.add_task(task_description)
    elif choice == '2': #2 to view all the task
        todo_list.view_tasks()
    elif choice == '3': #3 to mark tasks completed
        task_number_str = input("Enter the task number to mark as completed: ").strip()
        if task_number_str.isdigit():
            task_number = int(task_number_str)
            todo_list.mark_task_completed(task_number)
        else:
            print("Invalid input. Please enter a valid number.")
    elif choice == '4': #4 to delete the tasks from todolist
        task_number_str = input("Enter the task number to delete: ").strip()
        if task_number_str.isdigit():
            task_number = int(task_number_str)
            todo_list.delete_task(task_number)
        else:
            print("Invalid input. Please enter a valid number.")
    elif choice == '5': #5 to exit 
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
