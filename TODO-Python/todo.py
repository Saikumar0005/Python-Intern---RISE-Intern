import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
from datetime import datetime

DATA_FILE = "todo_data.json"

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks():
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def update_listbox():
    task_listbox.delete(0, tk.END)
    for idx, task in enumerate(tasks):
        status = "✅" if task["done"] else "❌"
        display = f"{status} {task['task']} (Priority: {task['priority']}, Due: {task['due']})"
        task_listbox.insert(tk.END, display)

def add_task():
    task_name = task_entry.get().strip()
    if not task_name:
        messagebox.showwarning("Input Error", "Task name cannot be empty.")
        return
    priority = priority_var.get()
    due_date = due_date_entry.get().strip() or "None"
    task = {"task": task_name, "done": False, "priority": priority, "due": due_date}
    tasks.append(task)
    save_tasks()
    update_listbox()
    task_entry.delete(0, tk.END)
    due_date_entry.delete(0, tk.END)

def delete_task():
    selected = task_listbox.curselection()
    if not selected:
        return
    tasks.pop(selected[0])
    save_tasks()
    update_listbox()

def toggle_done():
    selected = task_listbox.curselection()
    if not selected:
        return
    idx = selected[0]
    tasks[idx]["done"] = not tasks[idx]["done"]
    save_tasks()
    update_listbox()

def edit_task():
    selected = task_listbox.curselection()
    if not selected:
        return
    idx = selected[0]
    new_text = simpledialog.askstring("Edit Task", "Update task name:", initialvalue=tasks[idx]["task"])
    if new_text:
        tasks[idx]["task"] = new_text.strip()
        save_tasks()
        update_listbox()

tasks = load_tasks()
window = tk.Tk()
window.title("To-Do List App")
window.geometry("500x400")

tk.Label(window, text="Task:").pack()
task_entry = tk.Entry(window, width=40)
task_entry.pack(pady=2)

tk.Label(window, text="Priority (High/Medium/Low):").pack()
priority_var = tk.StringVar(value="Medium")
priority_menu = tk.OptionMenu(window, priority_var, "High", "Medium", "Low")
priority_menu.pack(pady=2)

tk.Label(window, text="Due Date (optional - YYYY-MM-DD):").pack()
due_date_entry = tk.Entry(window, width=30)
due_date_entry.pack(pady=2)

tk.Button(window, text="Add Task", command=add_task).pack(pady=5)

task_listbox = tk.Listbox(window, width=60, height=12)
task_listbox.pack(pady=10)

button_frame = tk.Frame(window)
button_frame.pack()

tk.Button(button_frame, text="Mark Done/Undone", command=toggle_done).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Edit", command=edit_task).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Delete", command=delete_task).grid(row=0, column=2, padx=5)

update_listbox()
window.mainloop()
