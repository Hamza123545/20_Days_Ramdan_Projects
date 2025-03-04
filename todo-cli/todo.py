import click
import json
import os

TODO_FILE = "todo.json"

def load_tasks():
    return json.load(open(TODO_FILE, "r")) if os.path.exists(TODO_FILE) else []

def save_tasks(tasks):
    json.dump(tasks, open(TODO_FILE, "w"), indent=4)

@click.group()
def cli():
    pass

@click.command()
@click.argument("task")
def add(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    click.echo(f"Added: {task}")

@click.command()
def list():
    tasks = load_tasks()
    if not tasks:
        return click.echo("No tasks available.")
    for i, task in enumerate(tasks, 1):
        click.echo(f"{i}. {task['task']} [{'✓' if task['done'] else '✗'}]")

@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        click.echo(f"Completed: {tasks[task_number - 1]['task']}")
    else:
        click.echo("Invalid task number.")

@click.command()
@click.argument("task_number", type=int)
def remove(task_number):
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        click.echo(f"Removed: {tasks.pop(task_number - 1)['task']}")
        save_tasks(tasks)
    else:
        click.echo("Invalid task number.")

cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(remove)

if __name__ == "__main__":
    cli()
