import tkinter as tk
from tkinter import ttk
import main_menu
import gui
import sqlite3

conn = sqlite3.connect('userAccounts.db')

def after_login(UserName, UserType, conn):  # Add conn as an argument
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE UserName=?", (UserName,))
    users = cursor.fetchone()
    if UserType == 'Student':
        main_menu.login_and_open_menu(UserName, UserType, gui.root)
    elif UserType == 'Faculty':
        main_menu.login_and_open_menu(UserName, UserType, gui.root)

if __name__ == "__main__":
    gui.create_gui(gui.login, lambda username, user_type: after_login(username, user_type, conn), conn)
