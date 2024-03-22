from tkinter import *
from triva import trivia


root = Tk()
root.geometry("800x600")

question_var = StringVar()
question_index = 0

def next_question():
    global question_index
    question_var.set(trivia[question_index]["Question"])
    question_index +=  1


question_label = Label(root, textvariable=question_var)
question_label.pack()

button = Button(root, text="Next", command=next_question)
button.pack()

next_question()

root.mainloop()


