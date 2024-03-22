from tkinter.simpledialog import askinteger, askfloat, askstring
from tkinter import *
from tkinter.messagebox import askquestion
top = Tk()

top.geometry("1000x1000")
def show():
   num = askinteger("Input", "Input an Integer")
   print(num)
   
print(askquestion("What", "Virus"))
   
B = Button(top, text ="Click", command = show)
B.place(x=50,y=50)

top.mainloop()