import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import main_menu

def login(username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()
    conn = sqlite3.connect('userAccounts.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    if user:
        if user[2] == 'student':
            messagebox.showinfo("Login Successful", "Welcome Student!")
            main_menu.open_student_menu(username)
        elif user[2] == 'faculty':
            messagebox.showinfo("Login Successful", "Welcome Faculty!")
            main_menu.open_faculty_menu(username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
    conn.close()

def create_gui():
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

    login_button = ttk.Button(login_tab, text="Login", command=lambda: login(username_entry, password_entry))
    login_button.pack(pady=10)

    tab_control.pack(expand=1, fill='both')
    root.mainloop()

create_gui()
