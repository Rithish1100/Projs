from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters=[random.choice(letters) for _ in range(nr_letters) ]
    password_symbols=[random.choice(symbols)for _ in range(nr_symbols) ]
    password_numbers=[random.choice(numbers) for _ in range(nr_numbers) ]

    password_list=password_letters+password_symbols+password_numbers
    shuffle(password_list)
    password="".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def to_store():
    website=website_entry.get()
    email=email_username_entry.get()
    password=password_entry.get()
    website_len=len(website_entry.get())
    password_len=len(password_entry.get())
    if website_len==0 or password_len==0:
        messagebox.showinfo(title="Warning",message="Please don't leave any fields empty")

    if website_len>0 and password_len>0:
        is_ok=messagebox.askyesno(title=website,message=f"These are the details entered:\nEmail:{email}\n Password:{password}\n Is it ok to save?")

    if is_ok:
        with open("data.txt","a")as holder:
            holder.write(f"{website}|{email}|{password}\n")
            website_entry.delete(0,END)
            password_entry.delete(0,END)
    
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=100,pady=100)

canvas=Canvas(width=200,height=200)
pass_image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=pass_image)
canvas.grid(row=0,column=1,columnspan=2)

website_label=Label(text="Website:",fg="black")
website_label.grid(row=1,column=0,pady=5,sticky="e",padx=(0,10))

website_entry=Entry(width=40)
website_entry.grid(row=1,column=1,columnspan=2,pady=5,sticky="w")
website_entry.focus()

email_username_label=Label(text="Email/Username:",fg="black")
email_username_label.grid(row=2,column=0,pady=5,sticky="e",padx=(0,10))

email_username_entry=Entry(width=40)
email_username_entry.grid(row=2,column=1,columnspan=2,pady=5,sticky="w")
email_username_entry.insert(0,"rithishcgouda@gmail.com")

password_label=Label(text="Password:",fg="black")
password_label.grid(row=3,column=0,pady=5,sticky="e",padx=(0,10))

password_entry=Entry(width=21)
password_entry.grid(row=3,column=1,pady=5,sticky="w",padx=(0,10))

password_generator_button=Button(text="Generate Password",fg="black",command=generate_password)
password_generator_button.grid(row=3,column=2,pady=5,sticky="w")

add_button=Button(width=35,text="Add",fg="black",command=to_store)
add_button.grid(row=4,column=1,columnspan=2,pady=5,sticky="w")

window.mainloop()