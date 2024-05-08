import tkinter as tk
from tkinter import ttk

def open_student_menu(username):
    create_main_menu(username, "student")

def open_faculty_menu(username):
    create_main_menu(username, "faculty")

def create_main_menu(username, user_type):
    root = tk.Tk()
    root.title(f"{user_type.capitalize()} Menu")

    tab_control = ttk.Notebook(root)

    courses_tab = ttk.Frame(tab_control)
    tab_control.add(courses_tab, text='Courses')
    ttk.Button(courses_tab, text='Show Courses').pack(padx=20, pady=20)

    grades_tab = ttk.Frame(tab_control)
    tab_control.add(grades_tab, text='Grades')
    ttk.Button(grades_tab, text='Show Grades').pack(padx=20, pady=20)

    account_settings_tab = ttk.Frame(tab_control)
    tab_control.add(account_settings_tab, text='Account Settings')
    ttk.Button(account_settings_tab, text='Show Account Settings').pack(padx=20, pady=20)

    tab_control.pack(expand=1, fill='both')
    root.mainloop()
