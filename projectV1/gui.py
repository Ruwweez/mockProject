# gui.py

import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import main

conn = sqlite3.connect('userAccounts.db')  # Define conn globally

def destroy_gui():
    root.withdraw()

def login(username_entry, password_entry, after_login_function, conn):  # Pass conn as an argument
    username = username_entry.get()
    password = password_entry.get()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE UserName=? AND Password=?", (username, password))
    user = cursor.fetchone()
    user_type = None  # Initialize user_type
    if user:
        if user[2] == 'Student':
            messagebox.showinfo("Login Successful", "Welcome Student!")
            user_type = 'Student'
        elif user[2] == 'Faculty':
            messagebox.showinfo("Login Successful", "Welcome Faculty!")
            user_type = 'Faculty'
        after_login_function(username, user_type)  # Execute the after login function
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def create_gui(login_function, after_login_function, conn):  # Pass conn as an argument
    global root
    root = tk.Tk()
    root.title("Login")

    tab_control = ttk.Notebook(root)

    login_tab = ttk.Frame(tab_control)
    tab_control.add(login_tab, text='Login')

    ttk.Label(login_tab, text="Username:").pack(pady=5)
    username_entry = ttk.Entry(login_tab)
    username_entry.pack(pady=5)

    ttk.Label(login_tab, text="Password:").pack(pady=5)
    password_entry = ttk.Entry(login_tab, show="*")
    password_entry.pack(pady=5)

    def login_and_execute_after_login():
        login_function(username_entry, password_entry, after_login_function, conn)  # Pass conn

    login_button = ttk.Button(login_tab, text="Login", command=login_and_execute_after_login)
    login_button.pack(pady=10)

    tab_control.pack(expand=1, fill='both')
    root.mainloop()
