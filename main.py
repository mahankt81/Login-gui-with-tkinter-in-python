from tkinter import *
from tkinter import messagebox
import re
import os

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
    register_screen.resizable(width = False , height = False)

    global email_entry
    global username_entry
    global password_entry
    global username
    global password
    global email
    username = StringVar()
    password = StringVar()
    email = StringVar()

    Label(register_screen , text = "Fill below form" , bg = "green" , font = ("Calibri" , 15)).pack()
    Label(register_screen , text = "").pack()

    Label(register_screen , text = "Username *").pack()
    #Label(register_screen , text = "").pack()
    username_entry = Entry(register_screen , textvariable=username)
    username_entry.pack()
    #Label(register_screen , text = "").pack()
    Label(register_screen , text = "Email *").pack()
    #Label(register_screen , text = "").pack()
    email_entry = Entry(register_screen , textvariable=email)
    email_entry.pack()
    #Label(register_screen , text="").pack()
    Label(register_screen , text = "Password *").pack()
    #Label(register_screen , text = "").pack()
    password_entry = Entry(register_screen , textvariable=password , show = '*')
    password_entry.pack()
    Label(register_screen , text="").pack()
    Button(register_screen , text = "Register" , width = '10' , height = '1' , command = user_register).pack()


def login():
    global login_screen
    global username_verify
    global password_verify
    global username_login
    global password_login

    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry('300x250')
    login_screen.resizable(width = False , height = False)

    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_screen , text = "Enter your info for login" , bg = "blue" , font = ("Calibri" , 15)).pack()
    Label(login_screen , text = "").pack()

    Label(login_screen , text = "Username *").pack()
    username_login = Entry(login_screen , textvariable=username_verify)
    username_login.pack()
    Label(login_screen , text = "Password *").pack()
    password_login = Entry(login_screen , textvariable=password_verify , show = '*')
    password_login.pack()
    Label(login_screen, text="").pack()
    Button(login_screen , text = "Login" , width = '10' , height = '1' , command=user_login).pack()



def user_register():

    username_info = username.get()
    password_info = password.get()
    email_info = email.get()

    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex , email_info):
        file = open(username_info , "w")
        file.write(username_info + '\n')
        file.write(password_info + '\n')
        file.write(email_info + '\n')
        file.close()
        messagebox.showinfo("Success" , "Your registration is successful!")
        email_entry.delete(0 , END)
        password_entry.delete(0 , END)
        username_entry.delete(0, END)
    else:
        messagebox.showwarning("Email", "Email not valid")
        email_entry.delete(0 , END)
        password_entry.delete(0 , END)

def user_login():
    username1 = username_verify.get()
    password1 = password_verify.get()


    file_list = os.listdir()

    if username1 in file_list:
        file1 = open(username1 , "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            messagebox.showinfo("Success" , f"Login is successful!Your email is: {verify[2]}")

        else:
            messagebox.showerror('Password' , "Password is not valid!")
    else:
        messagebox.showwarning("Not found" , "User not found!")

    username_login.delete(0 , END)
    password_login.delete(0 , END)

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry('300x250')
    main_screen.title("Account Login")

    Label(text = "chose Login or Register" , width = '300' , height = '2' , font =('Calibri' , 13)).pack()
    Label(text = "").pack()

    Button(text = "Login" , height = '2' , width = '30' , command = login).pack()
    Label(text="").pack()

    Button(text = "Register" , height = '2' , width = '30' , command = register).pack()

    main_screen.mainloop()

main_account_screen()
