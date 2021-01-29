from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
FONT = ("Arial", 12, "normal")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Generates a secure password, fills it into input field and clips it into clipboard"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    ipt_password.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_credentials():
    """Checks input length, asks for conformation, writes credentials
    to file and deletes input fields (website/password)"""

    if len(ipt_website.get()) == 0 or len(ipt_email.get()) == 0 or len(ipt_password.get()) == 0:
        messagebox.showinfo(title="No entries", message="Please make sure you haven't "
                                                        "left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=ipt_website.get(), message=f"These are the details "
                                                                        f"entered: \n"
                                                                f"Email: {ipt_email.get()}\n"
                                                                f"Password: {ipt_password.get()}\n"
                                                                f"Is it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{ipt_website.get()} | {ipt_email.get()} | {ipt_password.get()}\n")

            ipt_website.delete(0, END)
            ipt_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=220, height=220)
window.config(padx=50, pady=50)

# Logo
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Column 0 / Labels
lbl_website = Label(text="Website:", font=FONT)
lbl_website.grid(column=0, row=1)
lbl_mail_name = Label(text="Email/Username:", font=FONT)
lbl_mail_name.grid(column=0, row=2)
lbl_password = Label(text="Password:", font=FONT)
lbl_password.grid(column=0, row=3)

# Column 1 / Input fields
ipt_website = Entry(width=35, font=FONT)
ipt_website.grid(column=1, row=1, columnspan=2)
ipt_website.focus()
ipt_email = Entry(width=35, font=FONT)
ipt_email.insert(0, "eder.lukas@bluewin.ch")
ipt_email.grid(column=1, row=2, columnspan=2)
ipt_password = Entry(width=23, font=FONT)
ipt_password.grid(column=1, row=3)

btn_add = Button(text="Add", command=add_credentials, width=45)
btn_add.grid(column=1, row=4, columnspan=2)

# Column 2 / Generate Password button
btn_generate_pass = Button(text="Generate Password", command=generate_password)
btn_generate_pass.grid(column=2, row=3)

window.mainloop()

