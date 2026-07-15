def add_task(task):
    with open("tasks.txt","a") as file:
        file.write(task + "\n") 
    
add_task("Go to gym")
add_task("Go to office")
add_task("Go to store")
add_task("Go to dokan")



def view_tasks():
    try:
        with open("tasks.txt","r") as file:
            for i,line in enumerate(file,1):
                print(f"{i}. {line.strip()}")
    
    except FileNotFoundError:
        print("No tasks yet")


view_tasks()


def remove_task(task_number):
    with open("tasks.txt","r") as file:
        tasks = file.readlines()
    

    if task_number < 1 or task_number > len(tasks):
         print("Invalid task number")
         return
    
    tasks.pop(task_number - 1 )

    with open("tasks.txt","w") as file:
        file.writelines(tasks)
    
remove_task(2)
view_tasks() 









def task_count():
    count = 0
    with open("tasks.txt","r") as file:
        for line in file:
            count += 1
    return count






result = task_count()
print(result)