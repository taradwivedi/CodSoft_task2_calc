# Task 2
# Simple Calculator App
import tkinter as tk
from tkinter import messagebox

# Creation of root window
root = tk.Tk() 

# Window title
root.title("Basic Calculator")

# Creation of different functions for arithmetic operations
def add_func():
    cal_func(1)
def sub_func():
    cal_func(2)
def mult_func():
    cal_func(3)
def div_func():
    cal_func(4)

def cal_func(choice):
    num = num_text1.get()
    if not num:
        messagebox.showinfo("No Entry","Please enter number.")
        num_text1.focus_set()
        return
    num2 = num_text2.get()
    if not num2:
        messagebox.showinfo("No Entry","Please enter number.")
        num_text2.focus_set()
        return

    # Addition operation
    if choice == 1:
        result = int(num_text1.get()) + int(num_text2.get())
        result_lbl.config(text=f"Result: {result}")
    # Subtraction operation
    elif choice == 2:
        result = int(num_text1.get()) - int(num_text2.get())
        result_lbl.config(text=f"Result: {result}")
    # Multiplication Operation
    elif choice == 3:
        result = int(num_text1.get()) * int(num_text2.get())
        result_lbl.config(text=f"Result: {result}")
    # Division Operation
    else:
        if int(num2) > 0:
            result = int(num_text1.get()) / int(num_text2.get())
            result_lbl.config(text=f"Result: {result}")
        else:
            messagebox.showinfo("Invalid","Please enter number greater than 0.")
            num_text2.focus_set()

# Creating frame 1
frame1 = tk.Frame()
frame1.grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S)  

# Adding widgets to frame 1
num_lbl1 = tk.Label(frame1, text="Enter No 1:")
num_lbl1.grid(row=0, column=0, padx=10, pady=10)
num_text1 = tk.Entry(frame1, width=10)
num_text1.grid(row=0, column=1, padx=5, pady=5)

num_lbl2 = tk.Label(frame1, text="Enter No 2:")
num_lbl2.grid(row=0, column=2, padx=10, pady=10)
num_text2 = tk.Entry(frame1, width=10)
num_text2.grid(row=0, column=3, padx=5, pady=5)

# Creating frame 2
frame2 = tk.Frame()
frame2.grid(row=1, column=0, sticky=tk.W+tk.E+tk.N+tk.S)  

# Adding widgets to frame 2
add_btn = tk.Button(frame2, text="Add", command=add_func)
add_btn.grid(row=0, column=0, padx=5, pady=5)
add_btn = tk.Button(frame2, text="Subtract", command=sub_func)
add_btn.grid(row=0, column=1, padx=5, pady=5)
add_btn = tk.Button(frame2, text="Multiply", command=mult_func)
add_btn.grid(row=0, column=2, padx=5, pady=5)
add_btn = tk.Button(frame2, text="Divide", command=div_func)
add_btn.grid(row=0, column=3, padx=5, pady=5)

# Result label
result_lbl = tk.Label(root, text="",fg="red")
result_lbl.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Sets cursor at the number one label
num_text1.focus_set()
root.mainloop()