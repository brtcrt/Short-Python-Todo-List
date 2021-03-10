import tkinter as tk
from tkinter import messagebox
import json
from tkinter import ttk
from tkcalendar import Calendar
from datetime import date
with open('tasks.json') as json_file:
    try:
        tasks_loaded = json.load(json_file)
    except KeyError:
        print("a")
task = {
    "tasks": [

    ]
}
try:
    tasks_list = tasks_loaded["tasks"]
    print(tasks_list)
    task["tasks"] = tasks_list
except KeyError:
    print("b")
Today = date.today()
TodayYear = Today.year
TodayMonth = Today.month
TodayDay = Today.day
addedTask = ""
def example1():
    def print_sel():
        global addedTask
        global tasks_list
        global task
        print(cal.selection_get())
        # tasks_list.append(cal.selection_get())
        if addedTask == "":
            messagebox.showinfo("Something bad happened :(", "Please enter your task first!")
        else:
            task["tasks"].append(str(addedTask) + " --- Task Date: " + str(cal.selection_get()))
        print(task)

    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=TodayYear, month=TodayMonth, day=TodayDay)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="Choose", command=print_sel).pack()
def example2():
    global task
    if addedTask == "":
        messagebox.showinfo("Something bad happened :(", "Please enter your task first!")
    else:
        with open('tasks.json', 'w') as tasks_dumped:
            json.dump(task, tasks_dumped, indent=3, sort_keys=True)
            messagebox.showinfo("Success!", "Saved to your list.")
def example3():
    global task
    global addedTask
    global entry
    print(entry.get())
    addedTask = (str(entry.get()))
def example4():
    i = 0
    global task
    last_list = ""
    for task in task["tasks"]:
        i += 1
        last_list = last_list + "{}) Task name: ".format(str(i)) + task + "\n"
    messagebox.showinfo("Your todo list", last_list)
root = tk.Tk()
s = ttk.Style(root)
s.theme_use('clam')
entry = ttk.Entry(root)
entry.pack(padx=10, pady=10)
ttk.Button(root, text="Set task", command=example3).pack(padx=10, pady=10)
ttk.Button(root, text='Choose date', command=example1).pack(padx=10, pady=10)
ttk.Button(root, text='Submit', command=example2).pack(padx=10, pady=10)
ttk.Button(root, text='Show list', command=example4).pack(padx=10, pady=10)
root.mainloop()