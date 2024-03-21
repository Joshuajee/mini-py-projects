from tkinter import *
from tkinter.ttk import *

root  = Tk()

root.geometry("400x400")


value = IntVar()

entry = Entry(root, width=40, textvariable=value)

entry.grid(row=0, column=0, columnspan=5)


def number(num): 
    current_val = str(value.get())
    value.set(int(current_val+num))
    
    print(value.get())


Button(root, text="7", command=lambda: number("7")).grid(row=1, column=0)
Button(root, text="8", command=lambda: number("8")).grid(row=1, column=1)
Button(root, text="9", command=lambda: number("9")).grid(row=1, column=2)
Button(root, text="x").grid(row=1, column=3)
Button(root, text="/").grid(row=1, column=4)

Button(root, text="4", command=lambda: number("4")).grid(row=2, column=0)
Button(root, text="5", command=lambda: number("5")).grid(row=2, column=1)
Button(root, text="6", command=lambda: number("6")).grid(row=2, column=2)
Button(root, text="+").grid(row=2, column=3)
Button(root, text="-").grid(row=2, column=4)

Button(root, text="1", command=lambda: number("1")).grid(row=3, column=0)
Button(root, text="2", command=lambda: number("2")).grid(row=3, column=1)
Button(root, text="3", command=lambda: number("3")).grid(row=3, column=2)
Button(root, text="0").grid(row=3, column=3)
Button(root, text="=").grid(row=3, column=4)



mainloop()