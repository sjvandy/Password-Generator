# Passowrd Generator
import random
from tkinter import *
import sys
import os

interests = []
symbols = []

if getattr(sys, 'frozen', False):
    interests_file = os.path.join(sys._MEIPASS, 'interests.txt')
else:
    interests_file = 'interests.txt'

# Grab Interests from file
with open(interests_file) as interests_doc:
    interests = interests_doc.readlines()
    for i in range(len(interests)-1):
        interests[i] = interests[i][:-1]        

def generate_password():
    length = len_entry.get()
    rand_interest = random.choice(interests)
    rand_symbol = random.choice(symbol_entry.get())
    password_length = len(rand_interest) + 1
    if password_length > int(length): digit_len = 2
    else: digit_len = pow(10,(int(length) - password_length))
    random_numbers = random.randint(digit_len,digit_len*9)
    generated_password = f"{rand_interest}{rand_symbol}{random_numbers}"
    new_password.config(text=generated_password, borderwidth=5, relief="flat", bg='grey')
    
def copy_to_clipboard(event):
    root.clipboard_clear()
    root.clipboard_append(new_password.cget("text"))
    copy_lbl.grid(row=6, column=0, columnspan=2)
    root.after(1000, copy_lbl.grid_forget)

root = Tk()
root.title('Password Generator')
root.geometry("400x400")
root.resizable(False, False)

center_frame = Frame(root)
center_frame.pack(expand=True, side='top', anchor='n')
scrollbar = Scrollbar(center_frame)

# Frame Widgets
title_label = Label(center_frame, text="Password Generator", font=("Helvetica", 16))
len_entry = Entry(center_frame)
len_label = Label(center_frame, text="Enter Password Length", font=("Helvetica", 12), justify='right')
symbol_lbl = Label(center_frame, text="Enter Symbols", font=("Helvetica", 12), justify='right')
symbol_entry = Entry(center_frame)
generate_button = Button(center_frame, text="Generate", command=generate_password)
new_password = Label(center_frame, text="", font=("Courier New", 12), justify='center', wraplength=root.winfo_screenwidth())
new_password.bind("<Button-1>", copy_to_clipboard)
copy_lbl = Label(center_frame, text="Copied to Clipboard!", font=("Helvetica", 8), justify='center', fg='lightgrey')


# Grid Layout
title_label.grid(row=0, column=0, columnspan=2, pady=10)  # spans two columns
len_label.grid(row=1, column=0, pady=10)  # placed at row 1, column 0
len_entry.grid(row=1, column=1)  # placed at row 1, column 1
symbol_lbl.grid(row=2, column=0, pady=10)  # placed at row 1, column 0
symbol_entry.grid(row=2, column=1)  # placed at row 1, column 1
generate_button.grid(row=4, column=0, columnspan=2, pady=20)  # placed at row 1, column 1)
new_password.grid(row=5, column=0, columnspan=2)  

root.mainloop()