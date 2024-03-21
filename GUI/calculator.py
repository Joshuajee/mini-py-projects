from tkinter import *


root = Tk()

root.geometry("400x300")

root.maxsize(400, 300)

root.minsize(300, 250)

currentValue =  StringVar()

stored_val = None
operation_val = None

def number(val):
    currentValue.set(currentValue.get() + val)
    
def store(operation):
    global stored_val
    global operation_val
    operation_val = operation
    stored_val =  int(currentValue.get())
    currentValue.set("")

def equal():
    value = int(currentValue.get())
    
    if (operation_val) == "add":
        currentValue.set(str(stored_val + value))
    elif (operation_val) == "sub":
        currentValue.set(str(stored_val - value))
    elif (operation_val) == "mul":
        currentValue.set(str(stored_val * value))
    elif (operation_val) == "div":
        currentValue.set(str(stored_val / value))
         



Entry(root, textvariable=currentValue, width=50).grid(column=0, row=0, columnspan=5)

Button(root, text="7", command=lambda: number("7")).grid(column=0, row=1)
Button(root, text="8", command=lambda: number("8")).grid(column=1, row=1)
Button(root, text="9", command=lambda: number("9")).grid(column=2, row=1)
Button(root, text="x", command=lambda: store("mul")).grid(column=3, row=1)
Button(root, text="/", command=lambda: store("div")).grid(column=4, row=1)


Button(root, text="4", command=lambda: number("4")).grid(column=0, row=2)
Button(root, text="5", command=lambda: number("5")).grid(column=1, row=2)
Button(root, text="6", command=lambda: number("6")).grid(column=2, row=2)
Button(root, text="+", command=lambda: store("add")).grid(column=3, row=2)
Button(root, text="-", command=lambda: store("sub")).grid(column=4, row=2)

Button(root, text="1", command=lambda: number("1")).grid(column=0, row=3)
Button(root, text="2", command=lambda: number("2")).grid(column=1, row=3)
Button(root, text="3", command=lambda: number("3")).grid(column=2, row=3)
Button(root, text="0", command=lambda: number("0")).grid(column=3, row=3)
Button(root, text="=", command=equal).grid(column=4, row=3)








mainloop()