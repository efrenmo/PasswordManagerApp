import customtkinter
from tkinter import *
from tkinter import messagebox
import pandas as pd
from pandastable import Table, TableModel
from PIL import Image
from random import choice, randint, shuffle
import os
import csv
import pyperclip



BLACK = "#000000"
GREY = "#393E46"
BLUE = "#2F89FC"
FONT_NAME = "Courier"

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '@', '%', '&', '(', ')', '*', '+']



# ---------------------------- UI SETUP ------------------------------- #

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("497x300+790+325")
        self.title("My Passwords")
        self.configure(fg_color="black", background="black", bg="black", highlightbackground="black")
        #self.label = customtkinter.CTkLabel(self, text="My Passwords")
        #self.label.grid(padx=20, pady=20)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Password Manager")
        self.geometry("600x512")
        self.configure(#padx=50,
                       pady=50,
                       fg_color="black"
                       )
        #self.grid()
        self.toplevel_window = None

        # load image
        self.logo_image = customtkinter.CTkImage(Image.open("./logo512x512.png"), size=(256, 256))


        ##### Labels #####
        self.home_frame_large_image_label = customtkinter.CTkLabel(self,
                                                                   #self.home_frame,
                                                                   text="",
                                                                   image=self.logo_image,
                                                                   )
        self.home_frame_large_image_label.grid(row=0, column=1,
                                               sticky="e",
                                               # padx=20,
                                               # pady=10
                                               )
        self.website_label = customtkinter.CTkLabel(self,
                                                    #self.home_frame,
                                                    text="Website:",
                                                    justify="right",
                                                    font=customtkinter.CTkFont(size=14, weight="bold"))
        self.website_label.grid(row=1,
                                column=0,
                                sticky="ne",
                                padx=20,
                                #pady=(20, 10)
                                )
        self.email_user_label = customtkinter.CTkLabel(self,
                                                       #self.home_frame,
                                                       width=60,
                                                       text="Email | Username:",
                                                       font=customtkinter.CTkFont(size=14, weight="bold")
                                                       )
        self.email_user_label.grid(row=2, column=0,
                                   sticky="e",
                                   padx=20,
                                   #pady=(20, 10)
                                    )
        self.password_label = customtkinter.CTkLabel(self,
                                                     text="Password:",
                                                     font=customtkinter.CTkFont(size=14, weight="bold"),
                                                     )
        self.password_label.grid(row=3, column=0, sticky="ne", padx=20)

        ##### Entries #####

        self.website_entry = customtkinter.CTkEntry(self, width=300)
        self.website_entry.grid(row=1,
                                column=1,
                                columnspan=2,
                                # padx=(20, 0),
                                # pady=(20, 20),
                                sticky="nw"
                                )
        self.email_user_entry = customtkinter.CTkEntry(self,
                                                       width=300,
                                                       )
        self.email_user_entry.insert(0, "a.efrenmo@gmail.com")
        #self.password_entry.delete(0, END)
        self.email_user_entry.grid(row=2,
                                column=1,
                                # columnspan=2,
                                # padx=(20, 0),
                                # pady=(20, 20),
                                sticky="nw"
                                )
        self.password_entry = customtkinter.CTkEntry(self, width=174)
        self.password_entry.grid(row=3,
                                column=1,
                                # columnspan=2,
                                # padx=(20, 0),
                                # pady=(20, 20),
                                sticky="nw"
                                )
        self.generate_password_button = customtkinter.CTkButton(master=self,
                                                                text="Generate Password",
                                                                width= 21,
                                                                command=self.generate_password,
                                                                )
        self.generate_password_button.grid(column=1,
                                           row=3,
                                           # padx=20,
                                           # pady=10,
                                           sticky="ne",
                                           )
        self.generate_password_button.configure(fg_color="#41B3FF", text_color="black")


        self.add_button = customtkinter.CTkButton(master=self,
                                                  text="Add",
                                                  width= 174,
                                                  command=self.save_to_vault,
                                                  )

        self.add_button.grid(column=1,
                             row=4,
                             # padx=20,
                             # pady=10,
                             sticky="nw",
                             )
        self.add_button.configure(fg_color="#41B3FF", text_color="black")

        self.my_passwords_button = customtkinter.CTkButton(master=self,
                                                           text="My Passwords",
                                                           width=124,
                                                           command=self.open_toplevel,
                                                           )
        self.my_passwords_button.grid(column=1,
                                      row=4,
                                      # padx=20,
                                      # pady=10,
                                      sticky="ne",
                                      )
        self.my_passwords_button.configure(fg_color="#41B3FF", text_color="black")

        self.toplevel_window = None

    # -------------------------- GENERATE PASSWORD ----------------------------- #

    def generate_password(self):
        pass_letters = [choice(LETTERS) for _ in range(randint(8, 10))]
        pass_symbols = [choice(NUMBERS) for _ in range(randint(2, 4))]
        pass_numbers = [choice(SYMBOLS) for _ in range(randint(2, 4))]
        password_list = pass_letters + pass_symbols + pass_numbers

        shuffle(password_list)
        password = "".join(password_list)
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, password)
        # Copies the generated password to the clipboard
        pyperclip.copy(password)

    # ---------------------------- SAVE PASSWORD ------------------------------- #
    def save_to_vault(self):
        site = self.website_entry.get().title()
        email = self.email_user_entry.get()
        password = self.password_entry.get()

        if len(site) == 0 or len(password) == 0:
            messagebox.showwarning(title="Oops!", message="Please don not leave any of the fields empty")

        else:
            is_ok = messagebox.askokcancel(title=site,
                                           message=f"These are the details entered: \nEmail|Username: {email} \nPassword: {password} \nClick OK to save?")

            if is_ok:
                with open('vault.csv', newline='', mode='a', encoding='UTF8') as csv_file:
                    fields = ['site', 'username/email', 'password']
                    writer = csv.DictWriter(csv_file, fieldnames=fields)
                    if os.path.getsize('vault.csv') == 0:
                        writer.writeheader()
                    writer.writerow({fields[0]: site, fields[1]: email, fields[2]: password})
                self.website_entry.delete(0, END)
                self.password_entry.delete(0, END)

    # -------------------------- Open My Passwords ----------------------------- #
    def get_df(self):
        df = pd.read_csv('vault.csv')
        return df
    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
            self.table = Table(self.toplevel_window, dataframe=self.get_df(),showtoolbar=False, showstatusbar=False, editable = True)
            self.table.show()
            #self.toplevel_window.focus()
        else:
            self.toplevel_window.focus()  # if window exists focus it

if __name__ == "__main__":
    app = App()
    app.mainloop()
