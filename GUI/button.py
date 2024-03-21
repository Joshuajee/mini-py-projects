import tkinter as tk 

app = tk.Tk() 

app.title('Counter App') 

counter = 0

text = tk.Label(app, text=counter)

def decrease():
    global counter
    counter -= 1
    print(counter)
    text.config(text=counter)

def increase():
    global counter
    counter += 1
    print(counter)
    text.config(text=counter)
    

# label = tk.Label(app, text=)


increaseBtn = tk.Button(app, text='Increase', width=25, background="#00ff00", command=increase) 

decreaseBtn = tk.Button(app, text='Decrease', width=25,  background="#ff0000", command=decrease) 

text.place(x=100, y=100)

increaseBtn.pack()

decreaseBtn.pack() 

app.mainloop()