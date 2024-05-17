from tkinter import messagebox
import os

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

