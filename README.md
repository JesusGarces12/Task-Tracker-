# Task Tracker CLI

Original project in: https://roadmap.sh/projects/task-tracker

A simple command-line task manager written in Python.  
It allows you to add, update, delete, and list tasks using a local JSON file as the database.

Tested and executed on **Ubuntu 24.04 LTS** using the terminal.

---

## Features

- Add tasks with descriptions
- Update task descriptions
- Mark tasks as `to-do`, `in-progress`, or `done`
- Delete tasks by ID
- List all tasks or filter by status

---

## Requirements

- Python 3.10+ (pre-installed on Ubuntu 24.04)

---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/JesusGarces12/Task-Tracker-
cd Task-Tracker
```

2. Run the script using Python:
```
python3 cli.py [command] [arguments]
```

## Command and usage

# Add a task 
Adds a new task with a default status of to-do.
``` python3 cli.py add "Buy groceries" ```

# Update a task description
Updates the description of a task by its ID.
 ```
python3 cli.py update [id] "New description"
# Example:
python3 cli.py update 2 "Buy groceries and cook dinner"
```

# Delete a task
Deletes a task by its ID.
 ```
python3 cli.py delete [id]
# Example:
python3 cli.py delete 2
 ```

# Mark task as in progress
Changes the status of a task to "in-progress".
 ```
python3 cli.py mark-in-progress [id]
# Example:
python3 cli.py mark-in-progress 2
 ```

# Mark task as done
Changes the status of a task to "done".
 ```
python3 cli.py mark-done [id]
# Example:
python3 cli.py mark-done 2
 ```

# List all tasks
Prints all tasks from the JSON file.
 ```
python3 cli.py list
 ```

# List tasks by status
Filters tasks by their status.
 ```
python3 cli.py list to-do
python3 cli.py list in-progress
python3 cli.py list done
 ```

# File structure
Task-Tracker/
├── cli.py          # Main Python script
├── tasks.json      # JSON file where tasks are stored (auto-generated)
└── README.md       # Project documentation

# Author
Developed by Jesús Garcés

License
This project is licensed under the MIT License.
