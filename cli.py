import os
import sys
import json
import datetime

#function to read Json file if exists
def load_tasks(json_path):
    if os.path.exists(json_path):
        with open(json_path, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []
    



def main():
    args = sys.argv[1:]  # Read all the arguments except the script name
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current file directory
    json_path = os.path.join(current_dir, "tasks.json")  # JSON file in this directory

    if not args:
        print("Please, deposit a command.")
        return

    command = args[0]
    params = args[1:]

    if command == "add":
        if params:
            taskList = load_tasks(json_path)
            if taskList:
                new_id = max(task["id"] for task in taskList) + 1
            else:
                new_id = 1

            # create new task
            now = datetime.datetime.now().isoformat()
            task = {
                "id": new_id,
                "description": params[0],
                "status": "to-do",
                "createdAt": now,
                "updatedAt": now
            }

            taskList.append(task)

            # Save in the Json file
            with open(json_path, "w") as f:
                json.dump(taskList, f, indent=4)

            print(f'Task added successfully (ID: {task["id"]})')
        else:
            print("There is no task description")
            
    if command == "update":
        task_id = args[1]
        #The command update is attached to an identifier (ID), that's why task id is declared as the word after update
        if task_id:
            params = args[2:]
            taskList = load_tasks(json_path)
            
            new_description = params[0]
            updateDate = datetime.datetime.now().isoformat()
            updated = False #updated is an boolean variable that determines the actions

            for task in taskList: #run on the dictionaries in the JSON file
                if task_id == str(task["id"]):
                    task["description"] = new_description 
                    task["updatedAt"] = updateDate
                    updated = True
                    #updated is True with the modification of the keys "description" and "updatedAt" in the dictionary task
                    break  # no need to still looking for

            if updated:
                with open(json_path, "w") as f:
                    json.dump(taskList, f, indent=4) #Json file modification
                print(f'Task updated successfully (ID: {task_id})')
            else:
                print(f"No task found with ID: {task_id}")
        else:
            print("Task ID missing")
    
    if command == "delete":
        task_id = args[1]
        #The command delete is attached to an identifier (ID), that's why task id is declared as the word after the command
        if task_id:
            taskList = load_tasks(json_path)
            deleted = False #Another boolean variable, in this case to determinate if the task is deleted
        
            for i, task in enumerate(taskList): #the run is made by the function enumerate to add a counter to each task
                if task_id == str(task["id"]):
                    del taskList[i]
                    deleted = True
                    #deleted is true when the [i] element in task list was deleted
                    break
            if deleted:
                with open(json_path, "w") as f:
                    json.dump(taskList, f, indent=4)
                print(f'Task deleted successfully (ID: {task_id})') #modification in json-file
            else:
                print(f"No task found with ID: {task_id}")
        else:
            print("Task ID missing")
            
    if command == "mark-in-progress":
        task_id = args[1]
        #The command mark-in-progress is attached to an identifier (ID), that's why task id is declared as the command
        if task_id:
            taskList = load_tasks(json_path)
            updateDate = datetime.datetime.now().isoformat()
            markInProgress = False
        
            for task in taskList:
                if task_id == str(task["id"]):
                    task["status"] = "in-progress"
                    task["updatedAt"] = updateDate
                    markInProgress = True
                    break
            if markInProgress:
                with open(json_path, "w") as f:
                    json.dump(taskList, f, indent = 4)
                    print(f'Task marked in-progress successfully (ID: {task_id})')
            else:
                print(f'No task found with ID: {task_id}')
        else:
            print('Task ID missing')
    
    if command == "mark-done":
        task_id = args[1]
        #The command mark-done is attached to an identifier (ID), that's why task id is declared as the command
        if task_id:
            taskList = load_tasks(json_path)
            updateDate = datetime.datetime.now().isoformat()
            markDone = False
        
            for task in taskList:
                if task_id == str(task["id"]):
                    task["status"] = "done"
                    task["updatedAt"] = updateDate
                    markDone = True
                    break
            if markDone:
                with open(json_path, "w") as f:
                    json.dump(taskList, f, indent = 4)
                    print(f'Task marked done successfully (ID: {task_id})')
            else:
                print(f'No task found with ID: {task_id}')
        else:
            print('Task ID missing')
    
    if command == "list":
        #The command list is attached to four cases that why are all included in this lines
        if len(args) > 1:
            status = args[1]
            taskList = load_tasks(json_path)
            
            if status == "done":
                doneList = []
                for task in taskList:
                    if task["status"] == "done":
                        doneList.append(task)
                if len(doneList) >= 1:
                    print(doneList)
                else:
                    print("'done' task list is empty")
                    
            if status == "to-do":
                todoList = []
                for task in taskList:
                    if task["status"] == "to-do":
                        todoList.append(task)
                if len(todoList) >= 1:
                    print(todoList)
                else:
                    print("'To-do' task list is empty")
                    
            if status == "in-progress":
                progressList = []
                for task in taskList:
                    if task["status"] == "in-progress":
                        progressList.append(task)
                if len(progressList) >= 1:
                    print(progressList)
                else:
                    print("'in-progress' task list is empty")
            else:
                print(f'Command list {status} not found')
            
        else:
            taskList = load_tasks(json_path)
            print(taskList)
        
    
if __name__ == "__main__":
    main()

