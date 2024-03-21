import tkinter as tk

root = tk.Tk()

root.geometry("500x500")


# root.maxsize(200, 200)

# root.minsize(150, 100)

root.title("Simple app")


#root.minsize(250, 300)


def button_clicked():
    print("Clicking Button")


button = tk.Button(
    root, 
    text="Click Me!", 
    bg="blue", 
    fg="white",
    activebackground="#00FF00",
    activeforeground="yellow",
    command=button_clicked
)
checkbutton = tk.Checkbutton(root, text="Hello")

button_2 = tk.Button(root, text="Exit", command=root.destroy)
checkbutton_2 = tk.Checkbutton(root,text="Hello 2")

button.grid(row=0, column=0)
checkbutton.grid(row=0, column=1)

button_2.grid(row=0, column=2)

checkbutton_2.place(x=300, y=200)

my_entry = tk.StringVar()

entry = tk.Entry(root, textvariable=my_entry)

entry.grid(row=2, column=1)


root.mainloop()