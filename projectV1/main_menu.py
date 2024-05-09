#main_menu.py
import tkinter as tk
from tkinter import ttk
import sqlite3

def open_main_menu(username, userType, root, conn):
    root.title(f"{userType.capitalize()} Menu")

    tab_control = ttk.Notebook(root)

    courses_tab = ttk.Frame(tab_control)
    tab_control.add(courses_tab, text='Courses')

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Courses")
        courses = cursor.fetchall()

        for course in courses:
            ttk.Label(courses_tab, text=f"Course ID: {course[0]}").pack()
            ttk.Label(courses_tab, text=f"Course Name: {course[1]}").pack()
            ttk.Label(courses_tab, text=f"Course Code: {course[2]}").pack()
            ttk.Separator(courses_tab, orient='horizontal').pack(fill='x', pady=5)
    except sqlite3.Error as e:
        print(f"Error retrieving courses: {e}")

    tab_control.pack(expand=1, fill='both')


    grades_tab = ttk.Frame(tab_control)
    tab_control.add(grades_tab, text='Grades')
    ttk.Button(grades_tab, text='Show Grades').pack(padx=20, pady=20)

    account_settings_tab = ttk.Frame(tab_control)
    tab_control.add(account_settings_tab, text='Account Settings')
    ttk.Button(account_settings_tab, text='Show Account Settings').pack(padx=20, pady=20)

    tab_control.pack(expand=1, fill='both')
