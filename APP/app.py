###########################
#   Importing Libraries   #
###########################

from customtkinter import *
from tkinter import messagebox
from PIL import Image

###########################
#   SetUp of the window   #
###########################

root = CTk() #Set the tkinter to "app" variable
root.title("Password") #Set the title of the window

screen_width = root.winfo_screenwidth() #Get the width of the screen
screen_height = root.winfo_screenheight() #Get the height of the screen

#####      Sizes      #####
root.geometry(f"{int(screen_width/2)}x{int(screen_height/2)}+{int(screen_width/4)}+{int(screen_height/4)}") #Set window size to half the size of the screen and center it
root.minsize(250, 350) #Set minimum size of the Window
root.resizable(True, True) #Set the window to resizable


###########################
#        Main Page        #
###########################

#####    Main Frame   #####
main_frame = CTkFrame(root)

#####   Build Frames  #####
main_left_frame = CTkFrame(main_frame)

#####   Pages Frames  #####
passwords_frame = CTkFrame(main_frame)
configuration_frame = CTkFrame(main_frame)



###########################
#    LogIn/SignUp page    #
###########################

#####    Main Frame   #####
login_frame = CTkFrame(root) #Creates a frame for the login
login_frame.pack(padx=20, pady=40,fill="both",expand="True") #Give padding and size

#####   Build Frames  #####
login_label_frame = CTkFrame(login_frame)
login_label_frame.pack(expand="true")
login_entry_frame = CTkFrame(login_frame)
login_entry_frame.pack(expand="true")
login_button_frame = CTkFrame(login_frame)
login_button_frame.pack(expand="true")


#####    Functions    #####
def login():
    username = "admin"
    password = "admin"
    if login_username_entry.get() == username and login_password_entry.get() == password:
        messagebox.showinfo(title="Login Success", message="Logged in succesfully")
        login_frame.pack_forget()
    else:
        ErrorNotShown = True
        while (ErrorNotShown):
            if login_username_entry.get() != username:
                messagebox.showerror(title="Error", message="Invalid Username")
                ErrorNotShown = False
                break
            if login_password_entry.get() != password:
                messagebox.showerror(title="Error", message="Invalid Password")
                ErrorNotShown = False
                break

#####  Create Widgets #####
login_label = CTkLabel(login_label_frame, text="Login Form") #Label for the menu
login_username_label = CTkLabel(login_entry_frame, text="Username") #Label for the username entry
login_username_entry = CTkEntry(login_entry_frame) #Entry for the username
login_password_label = CTkLabel(login_entry_frame, text="Password") #Label for the password entry
login_password_entry = CTkEntry(login_entry_frame, show="*") #Entry for the passwrd
login_button = CTkButton(login_button_frame, text="Login", command=login) #Login button

#####  Place Widgets  #####
login_label.pack(pady=5, padx=5)
login_username_label.grid(row=1, column=0)
login_username_entry.grid(row=1, column=1, pady=6, padx=5)
login_password_label.grid(row=2, column=0)
login_password_entry.grid(row=2, column=1, pady=6, padx=5)
login_button.pack(pady=6, padx=5)

root.mainloop()