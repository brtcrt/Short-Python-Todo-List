import tkinter as tk  # Import the modules for interfaces.
from tkinter import messagebox  # Fucking pop-up windows. It works brilliantly though. Also super easy to use.
import json  # Standard json library. Using this for data storage. Unstable but works.
from tkinter import ttk  # For quick access to parts like the Button.
from tkcalendar import Calendar  # Used for the date picking.
from datetime import date  # Used for setting starting date.

with open('tasks.json') as json_file:
    try:
        tasks_loaded = json.load(json_file)  # Getting the saved info from the json file.
    except KeyError:
        print("Some random key error from start up or the json file was changed.")  # Problems with using .json as a db.
task = {
    "tasks": [

    ]
}  # Using a dictionary to store data whilst the program is running. This also makes converting to json easy.
try:
    tasks_list = tasks_loaded["tasks"]
    print(tasks_list)
    task["tasks"] = tasks_list  # Current data is set to saved data on start up. Basically how the save-load system works.
except KeyError:
    print("Some random key error from start up or the json file was changed.")  # Problems with using .json as a db.
addedTask = ""  # To put all the info received in to order.
def PickDate():  # To pick a date for the task.
    def print_sel():
        global addedTask
        global tasks_list
        global task
        if addedTask == "":  # Solves a problem where the program would die if the user enters an empty string. Idk who'd do that, but yeah. Just in case.
            messagebox.showinfo("Something bad happened :(", "Please enter your task first!")  # Also to keep everything in order. (Task first, date second)
        else:
            task["tasks"].append(str(addedTask) + " --- Task Date: " + str(cal.selection_get()))  # Combines the task & date into a single string so it is easier to display.
            messagebox.showinfo("Success!", "Set the date for the task! Don't forget to submit the task to your list!")  # Just to give some feedback to the user.
    top = tk.Toplevel(root)
    cal = Calendar(top,font="Arial 14", selectmode='day',cursor="hand1", year=date.today().year, month=date.today().month, day=date.today().day)  # The date-picker system.
    cal.pack(fill="both", expand=True)  # Packing it.
    ttk.Button(top, text="Choose", command=print_sel).pack()  # The pick date button.
def SaveToJson():  # Saving to the local json database.
    global task
    if addedTask == "":
        messagebox.showinfo("Something bad happened :(", "Please enter your task first!")  # So the user can't add an empty string to the list.
    else:
        with open('tasks.json', 'w') as tasks_dumped:
            json.dump(task, tasks_dumped, indent=3, sort_keys=True)  # This somehow fucking works.
            messagebox.showinfo("Success!", "Saved to your list.")  # Again, giving feedback to the user so they understand they can close the window safely.
def AddTask():  # Get the tasks name from the user.
    global task
    global addedTask
    global entry
    addedTask = (str(entry.get()))  # This should have been the first function that I wrote but it wasn't so it's gonna stay here.
    messagebox.showinfo("Success!", "Added the task! Don't forget to set the date for it!")
def ShowList():  # Showing the list.
    i, last_list = 0, ""  # I hate defining variables like this but it was necessary. Not for any functionality of course.
    global task
    for task in task["tasks"]:  # Putting all the tasks in the list/dictionary in to a neat little string.
        i += 1
        last_list = last_list + "{}) Task name: ".format(str(i)) + task + "\n"
    messagebox.showinfo("Your todo list", last_list)  # Using pop-up windows literally everywhere because they are so easy to use and they just work.
root = tk.Tk()  # The core of the tkinter interface system.
s = ttk.Style(root)  # Some styling.
s.theme_use('clam')  # Some more styling.
entry = ttk.Entry(root)  # Getting the input from the user. This is the thing which adds the little input box.
entry.pack(padx=10, pady=10) # Packing it separately because it wouldn't stop giving errors.
ttk.Button(root, text="Set task", command=AddTask).pack(padx=10, pady=10)  # Button for setting task.
ttk.Button(root, text='Choose date', command=PickDate).pack(padx=10, pady=10)  # Button for choosing a  date.
ttk.Button(root, text='Submit', command=SaveToJson).pack(padx=10, pady=10)  # Button for submitting/saving to json.
ttk.Button(root, text='Show list', command=ShowList).pack(padx=10, pady=10)  # Button for showing the list.
root.mainloop()  # Finally initialize the program. And yes I spent about 10 minutes trying to get it to be exactly 69 lines :)