# importing only those functions 
# which are needed 
from tkinter import *
from tkinter.ttk import *
import os

from pathlib import Path
print(Path.cwd())

# creating tkinter window 
root = Tk() 

# Adding widgets to the root window 
Label(root, text = 'Image Btn', font =( 
'Verdana', 15)).pack(side = TOP, pady = 10) 

print(os.path.join (Path.cwd(),"image.jpg"))

# Creating a photoimage object to use image 
#photo = PhotoImage(file = os.path.join (Path.cwd(),"image.jpg")) 

# here, image option is used to 
# set image on button 
#Button(root, text = 'Click Me !', image = photo).pack(side = TOP) 

mainloop() 

photo = PhotoImage(file = "path_of_file")
