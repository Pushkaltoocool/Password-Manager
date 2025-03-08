from tkinter import*
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!#$%&()*+"

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    pyperclip.copy(password)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    password_doc = open("data.txt", "a")
    website = website_entry.get()
    password = password_entry.get()
    email = user_entry.get()
    final_text = f"{website}|{email}|{password}\n"
    if not website or not password or not email:
        messagebox.showerror("Error", "Please don't leave any fields empty!")
        password_doc.close()
        return
    is_ok = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nProceed to save?"
    )
    if not is_ok:
        password_doc.close()
        return
    else:
        password_doc.write(final_text)
        password_doc.close()
        website_entry.delete(0, END)
        password_entry.delete(0, END)





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(height=200, width=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:")
label_website.grid(row=1, column=0)

label_user = Label(text="Email/Username:")
label_user.grid(row=2, column=0)

label_password = Label(text="Password:")
label_password.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

user_entry = Entry(width=35)
user_entry.insert(0, "example@gmail.com")
user_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate = Button(text="Generate Password", command=generate_password)
generate.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=add_password)
add_btn.grid(row=4, column=1, columnspan=2)
















window.mainloop()
