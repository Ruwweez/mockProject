#login.py
import sqlite3
import gui
import main_menu

def open_main_menu_from_login(Username, userType):
    main_menu.open_main_menu(Username, userType)

def login_and_open_menu(Username, Password):
    # Connect to the database
    conn = sqlite3.connect('userAccounts.db')
    cursor = conn.cursor()

    # Check if the Username and Password match
    cursor.execute("SELECT * FROM Users WHERE Username=? AND Password=?", (Username, Password))
    user = cursor.fetchone()

    if user:
        userType = user[2]  # Assuming the user type is stored in the third column
        gui.destroy_gui()  # Close the login window
        open_main_menu(Username, userType)  # Open the main menu
    else:
        print("Invalid Username or Password")

    conn.close()

if __name__ == "__main__":
    gui.create_gui(login_and_open_menu)
