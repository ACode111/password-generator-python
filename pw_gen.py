import tkinter as tk
import tkinter.ttk as ttk
import pyperclip
import random
import string
import sys

try:

    def password_gen():

        pw = ""

        pool = ""

        if status_letter.get():
            pool += string.ascii_letters
        if status_symbol.get():
            pool += string.punctuation
        if status_number.get():
            pool += string.digits
        if password_lenght.get() == "":
            label_pwlenght = tk.Label(root, text="Please enter a password length", font=("Arial", 16))
            label_pwlenght.pack(pady=20)
        if pool == "":
            label_pwlenght = tk.Label(root, text="Please select at least one option", font=("Arial", 16))
            label_pwlenght.pack(pady=20)

        else:
            for i in range(int(password_lenght.get())):
                pw += random.choice(pool)

        password_sonuc.config(text=pw)

    def copy():
        password = password_sonuc.cget("text")
        if password:
            pyperclip.copy(password)

    #window
    root = tk.Tk()
    root.title("Password Generator")
    root.geometry("400x400")

    #variables
    status_letter = tk.BooleanVar()
    status_symbol = tk.BooleanVar()
    status_number = tk.BooleanVar()

    #checkboxes
    label_letter = ttk.Checkbutton(root, text="Letters", variable=status_letter)#letters checkbox
    label_letter.pack()                                                          

    label_symbol = ttk.Checkbutton(root, text="Symbols", variable=status_symbol)#symbols checkbox
    label_symbol.pack()                                                          

    label_number = ttk.Checkbutton(root, text="Numbers", variable=status_number)#numbers checkbox
    label_number.pack()                                                          

    #lenght
    password_lenght = ttk.Entry(root)#-------------------------------------------password length entry
    password_lenght.pack()                                                      

    #label
    label = tk.Label(root, text="Password Generator", font=("Arial", 16))#----------label
    label.pack(pady=20)

    #result
    password_sonuc = tk.Label(root, text="", font=("Arial", 16))#-------------------result
    password_sonuc.pack(pady=20)

    #password generate button
    button = ttk.Button(root, text="Generate Password", command=password_gen)#-----password generate button
    button.pack(pady=10)

    # copy button
    copy_button = ttk.Button(root, text="Copy to Clipboard", command=copy)#---------copy button
    copy_button.pack(pady=5)

    root.mainloop()

except Exception as e:
    print(f"Error: {e}")
    sys.exit()
