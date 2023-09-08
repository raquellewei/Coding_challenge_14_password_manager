from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_box.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
file = 'data.txt'
def save_password():
    password = password_box.get()
    website = website_box.get()
    username = email_box.get()

    if len(password) < 1 or len(website) < 1 or len(username) < 1:
        messagebox.showinfo(title='Oops!', message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nUsername: {username}"
                                                            f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open(file, 'a') as f:
                f.write(f"{website} | {username} | {password}\n")
            password_box.delete(0, END)
            website_box.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
window.config(bg='white')

website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)
website_box = Entry(width=36, bg="white", highlightthickness=0)
website_box.grid(row=1, column=1, columnspan=2, sticky="EW")
website_box.focus()

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0)
email_box = Entry(width=36, bg="white", highlightthickness=0)
email_box.grid(row=2, column=1, columnspan=2, sticky="EW")
email_box.insert(0, 'weimaomao_3@hotmail.com')

password_label = Label(text="Password:", bg="white", highlightthickness=0)
password_label.grid(row=3, column=0)
password_box = Entry(width=21, highlightthickness=0)
password_box.grid(row=3, column=1, sticky="EW")

generate_button = Button(text="Generate Password", highlightbackground='white', borderwidth=0.5,
                         command=generate_password)
generate_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", highlightbackground="white", borderwidth=0.5, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


window.mainloop()
