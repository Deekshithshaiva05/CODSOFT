import datetime

def main():
    
    def task():
        tasks = []
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        print(f"------WELCOME TO THE TO-DO LIST------\nToday's Date: {today}")
        
        while True:
            try:
                choice = int(input("1. ADD\n2. UPDATE\n3. DELETE\n4. VIEW\n5. MARK AS DONE\n6. EXIT/STOP\nEnter your choice: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            
            if choice == 1:
                total_task = int(input("Enter how many tasks you want to add: "))
                for i in range(1, total_task + 1):
                    task_name = input(f"Enter task {i}: ")
                    priority = input("Enter priority (High, Medium, Low): ")
                    due_date = input("Enter due date (YYYY-MM-DD): ")
                    tasks.append({"task_name": task_name, "priority": priority, "due_date": due_date, "done": False})
                print(f"{total_task} task(s) have been successfully added.")
                
            elif choice == 2:
                update_value = input("Enter the task name you want to update: ")
                for task in tasks:
                    if task["task_name"] == update_value:
                        new_uv = input("Enter the new task: ")
                        task["task_name"] = new_uv
                        task["priority"] = input("Enter new priority (High, Medium, Low): ")
                        task["due_date"] = input("Enter new due date (YYYY-MM-DD): ")
                        print(f"Updated task to: {new_uv}")
                        break
                else:
                    print("Task not found.")
                    
            elif choice == 3:
                del_value = input("Enter the task you want to delete: ")
                for task in tasks:
                    if task["task_name"] == del_value:
                        tasks.remove(task)
                        print(f"The task '{del_value}' is deleted.")
                        break
                else:
                    print("Task not found.")
                    
            elif choice == 4:
                if not tasks:
                    print("No tasks found.")
                else:
                    print("The total tasks are:")
                    for index, task in enumerate(tasks):
                        status = "Done" if task["done"] else "Not Done"
                        print(f"{index + 1}. {task['task_name']} - Priority: {task['priority']} - Due Date: {task['due_date']} - {status}")

            elif choice == 5:
                try:
                    task_index = int(input("Enter task number to mark as done: ")) - 1
                    if 0 <= task_index < len(tasks):
                        tasks[task_index]["done"] = True
                        print("The task marked as done.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
                      
            elif choice == 6:
                print("The TO-DO LIST is closing.")   
                print("THANK YOU")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 6.")
                
    task()
main()