class TaskManager:
    def __init__(self):
        self.tasks = []
        self.top = -1

    def add_task(self):
        title = input("Task Title: ")
        description = input("Task Description: ")
        self.tasks.append({"title": title, "description": description, "completed": False})
        print("Task added")

    def mark_task_completed(self):
        self.display_tasks()
        task_index = int(input("Enter the task Number to be marked as completed: ")) - 1
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task index. Task not found.")

    def display_tasks(self):
        for index, task in enumerate(self.tasks):
            status = "Task Completed" if task["completed"] else "Pending"
            print(f"Task {index + 1}: {task['title']} - Description: {task['description']} - Status: {status}")

    def run(self):
        while True:
            print("\nTask Manager Menu:")
            print("1. Add Task\n2. Mark Completed\n3. Display Tasks\n4. Exit")
            choice = input("Enter your choice (1/2/3/4): ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.mark_task_completed()
            elif choice == "3":
                self.display_tasks()
            elif choice == "4":
                print("Exiting Task Manager.")
                break
            else:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    TaskManager().run()
