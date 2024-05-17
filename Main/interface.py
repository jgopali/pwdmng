import logicpwd
import tkinter as tk

def add():
    username = entryName.get()
    password = entryPassword.get()
    function.add(username, password)

def get():
    username = entryName.get()
    function.get(username)

def get_list():
    function.get_list()

def delete():
    username = entryName.get()
    function.delete(username)

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

    # List button
    buttonList = tk.Button(app, text="List", command=get_list)
    buttonList.grid(row=3, column=0, padx=15, pady=8, sticky="we")

    # Delete button
    buttonDelete = tk.Button(app, text="Delete", command=delete)
    buttonDelete.grid(row=3, column=1, padx=15, pady=8, sticky="we")

    app.mainloop()