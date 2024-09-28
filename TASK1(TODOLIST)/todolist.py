import tkinter as tk
from tkinter import messagebox

# Initialize the window
root = tk.Tk()
root.title("Colorful To-Do List")
root.geometry("400x600")
root.configure(bg="#333333")  # Dark gray background

# Initialize list to store tasks
tasks = []

# Define fonts and colors
task_font = ("Arial", 12, "bold")
button_color = "#76D7C4"  # Light green
task_color = "#F9E79F"    # Light yellow
bg_color = "#333333"      # Background color dark gray
input_bg_color = "#555555"  # Darker gray for input
input_font = ("Arial", 12)

# Function to add a new task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append({'task': task, 'completed': False})
        task_entry.delete(0, tk.END)
        update_task_list()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to update the task display
def update_task_list():
    # Clear the current list
    task_listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        status = "✔" if task['completed'] else "✘"
        task_listbox.insert(tk.END, f"{i + 1}. {task['task']} [{status}]")

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks.pop(selected_task_index)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to mark a task as completed
def complete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks[selected_task_index]['completed'] = True
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

# Function to update a selected task
def update_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task != "":
            tasks[selected_task_index]['task'] = new_task
            task_entry.delete(0, tk.END)
            update_task_list()
        else:
            messagebox.showwarning("Input Error", "Please enter a task to update.")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to update.")

# GUI Elements

# Task input
task_entry = tk.Entry(root, font=input_font, bg=input_bg_color, width=30)
task_entry.pack(pady=10)

# Add Task button
add_button = tk.Button(root, text="Add Task", width=20, font=task_font, bg=button_color, command=add_task)
add_button.pack(pady=5)

# Listbox to display tasks
task_listbox = tk.Listbox(root, height=10, font=task_font, bg=task_color)
task_listbox.pack(pady=10, padx=20)

# Buttons to manage tasks
complete_button = tk.Button(root, text="Mark Task as Completed", width=20, font=task_font, bg=button_color, command=complete_task)
complete_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=20, font=task_font, bg=button_color, command=delete_task)
delete_button.pack(pady=5)

update_button = tk.Button(root, text="Update Task", width=20, font=task_font, bg=button_color, command=update_task)
update_button.pack(pady=5)

# Main loop
root.mainloop()
