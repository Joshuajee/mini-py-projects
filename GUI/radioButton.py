# Importing Tkinter module 
from tkinter import *
from tkinter.ttk import *

# Creating master Tkinter window 
master = Tk() 
master.geometry("175x175") 

# Tkinter string variable 
# able to store any string value 
v = StringVar() 

# Dictionary to create multiple buttons 
values = {"RadioButton 1" : "1", 
		"RadioButton 2" : "2", 
		"RadioButton 3" : "300", 
		"RadioButton 4" : "4", 
		"RadioButton 5" : "5"} 

# Loop is used to create multiple Radiobuttons 
# rather than creating each button separately 
for (text, value) in values.items(): 
    print(text, value)
    Radiobutton(master, text = text, variable = v,
		value = value).pack(side = TOP, ipady = 5) 
 
def show(): 
    print(v.get())

Button(master, text="Click Me!", command=show).pack()

# Infinite loop can be terminated by 
# keyboard or mouse interrupt 
# or by any predefined function (destroy()) 
mainloop() 
