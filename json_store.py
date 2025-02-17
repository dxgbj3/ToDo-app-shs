import json
from models import TaskManager


def save_tasks_in_json(tasks):
    with open('tasks.json', 'w', encoding='utf-8') as outfile:
        json.dump(tasks, outfile)


def import_tasks_from_json():
    with open('tasks.json', 'r') as json_file:
        tasks = json.load(json_file)
        return tasks


if __name__ == '__main__':
    created_tasks = import_tasks_from_json()
    task_manager = TaskManager()
    task_manager.set_tasks(created_tasks)

    test_todo = task_manager.add_task("test", "this is a test task")

    save_tasks_in_json(task_manager.get_tasks())
