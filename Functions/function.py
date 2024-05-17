import tkinter as tk
from tkinter import messagebox

def add():
    username = entryName.get()
    password = entryPassword.get()
    if username and password:
        with open ("passwords.txt", 'a') as f:
            f.write(f"{username} {password}\n")
        messagebox.showinfo("Success", "Password added successfully")
    else:
        messagebox.showerror("Error", "Please enter username and password")

def get():
    username = entryName.get()
    passwords = {}
    try:
        with open("passwords.txt") as f:
            for k in f: 
                i = k.split(' ')
                passwords[i[0]] = i[1]
    except:
        print("Error")
    if passwords:
        mess = "Your passwords are:\n"
        for i in passwords:
            if i == username:
                mess += f"Password for {username} is {passwords[i]}\n"
        else:
            mess += "No such user exists"
        messagebox.showinfo("Passwords", mess)
    else:
        messagebox.showerror("Error", "No passwords found")

def getlist():
    passwords = {}
    try:
        with open("passwords.txt") as f:
            for k in f: 
                i = k.split(' ')
                passwords[i[0]] = i[1]
    except:
        print("No passwords found")
    if passwords:
        mess = "List of passwords:\n"
        for name, password in passwords.items():
            mess += f"Password for {name} is {password}\n"
        messagebox.showinfo("Passwords", mess)
    else:
        messagebox.showinfo("Passwords", "No passwords found")

def delete():
    username = entryName.get()
    temp_passwords = []
    try:
        with open("passwords.txt") as f:
            for k in f:
                i = k.split(' ')
                if i[0] != username:
                    temp_passwords.append(f"{i[0]} {i[1]}")
        with open("passwords.txt", 'w') as f:
            for line in temp_passwords:
                f.write(line)

        messagebox.showinfo(
            "Success", f"User {username} deleted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error deleting user {username}: {e}")

if __name__ == "__main__":
    app = tk.Tk()
    app.geometry("560x270")
    app.title("GeeksForGeeks Password Manager")

    # Username block
    labelName = tk.Label(app, text="USERNAME:")
    labelName.grid(row=0, column=0, padx=15, pady=15)
    entryName = tk.Entry(app)
    entryName.grid(row=0, column=1, padx=15, pady=15)

    # Password block
    labelPassword = tk.Label(app, text="PASSWORD:")
    labelPassword.grid(row=1, column=0, padx=10, pady=5)
    entryPassword = tk.Entry(app)
    entryPassword.grid(row=1, column=1, padx=10, pady=5)

    # Add button
    buttonAdd = tk.Button(app, text="Add", command=add)
    buttonAdd.grid(row=2, column=0, padx=15, pady=8, sticky="we")

    # Get button
    buttonGet = tk.Button(app, text="Get", command=get)
    buttonGet.grid(row=2, column=1, padx=15, pady=8, sticky="we")

    # List Button
    buttonList = tk.Button(app, text="List", command=getlist)
    buttonList.grid(row=3, column=0, padx=15, pady=8, sticky="we")

    # Delete button
    buttonDelete = tk.Button(app, text="Delete", command=delete)
    buttonDelete.grid(row=3, column=1, padx=15, pady=8, sticky="we")

    app.mainloop()