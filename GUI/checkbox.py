from tkinter import *

root = Tk() 
root.geometry("300x200") 

w = Label(root, text ='Checkbox', font = "50") 
w.pack() 

Checkbutton1 = BooleanVar() 
Checkbutton2 = IntVar() 
Checkbutton3 = IntVar() 

def printOut():
    print(Checkbutton1.get())
    

Button1 = Checkbutton(root, text = "A", 
					variable = Checkbutton1, 
					onvalue = True, 
					offvalue = False, 
					height = 2, 
                    command=printOut,
					width = 10) 

Button2 = Checkbutton(root, text = "B", 
					variable = Checkbutton2, 
					onvalue = 1, 
					offvalue = 0, 
					height = 2, 
					width = 10) 

Button3 = Checkbutton(root, text = "C", 
					variable = Checkbutton3, 
					onvalue = 1, 
					offvalue = 0, 
					height = 2, 
					width = 10) 
	
Button1.pack() 
Button2.pack() 
Button3.pack() 

mainloop() 
