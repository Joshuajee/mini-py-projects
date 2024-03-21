# Program to make a simple 
# login screen 


import tkinter as tk

root=tk.Tk()

root.title("BMI Calculator")

# setting the windows size
root.geometry("600x400")


num1 =tk.IntVar()
num2  = tk.IntVar()

disp_answer=tk.StringVar()

def calculate():
    disp_answer.set(str(num1.get() + num2.get()))
	
	
# creating a label for 
# name using widget Label
name_label = tk.Label(root, text = 'Number 1', font=('calibre',10, 'bold'))

# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(root,textvariable = num1, font=('calibre',10,'normal'))

# creating a label for password
passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))

# creating a entry for password
passw_entry=tk.Entry(root, textvariable = num2, font = ('calibre',10,'normal'))

# creating a button using the widget 
# Button that will call the submit function 
sub_btn=tk.Button(root,text = 'Calculate', command = calculate)

# Text Widget

display = tk.Label(root, textvariable=disp_answer)


name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)

display.grid(row=3, column=1)


# performing an infinite loop 
# for the window to display
root.mainloop()
