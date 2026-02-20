"""
Task Tracker - A simple CLI task manager.
This is the base application we'll build on using stacked PRs.
"""


def main():
    print("Welcome to Task Tracker!")
    print("Commands: add, list, quit")

    tasks = []

    while True:
        command = input("> ").strip().lower()

        if command == "quit":
            print("Goodbye!")
            break
        elif command == "list":
            if not tasks:
                print("No tasks yet.")
            for i, task in enumerate(tasks, 1):
                print(f"  {i}. {task}")
        elif command == "add":
            task = input("Task: ").strip()
            if task:
                tasks.append(task)
                print(f"Added: {task}")
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
