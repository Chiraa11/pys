import tkinter as tk 
from tkinter import messagebox
root = tk.Tk()

def onClickSubmit():
    name = name_textbox.get()
    email = email_textbox.get()
    phone = phone_textbox.get()
    
    if name and email and phone:
        messagebox.showinfo("status", "Data submitted")
    else:
        messagebox.warning("warning", "Please fill all the fields")




root.geometry("400x400")
root.configure(bg = "#FD9FA2")

name_label = tk.Label(root, text = "Enter name ")
name_label.pack(anchor = tk.W, padx = 20)
name_textbox = tk.Entry(root)
name_textbox.pack(anchor = tk.W, padx = 20)  #E for right side

email_label = tk.Label(root, text = "Enter email ")
email_label.pack(anchor =tk.W, padx = 20)
email_textbox = tk.Entry(root)
email_textbox.pack(anchor = tk.W, padx = 20)

phone_label = tk.Label(root, text = "Enter Phone ")
phone_label.pack(anchor = tk.W, padx = 20)
phone_textbox = tk.Entry(root)
phone_textbox.pack(anchor = tk.W, padx = 20)
 
submit_button = tk.Button(root, text = "Submit ", command=onClickSubmit)
submit_button.pack(anchor = tk.W, padx = 20)

root.mainloop()