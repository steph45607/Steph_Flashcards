from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Framing')

# Frame - to spearate windows, as a partition
frame = LabelFrame(root, text="this is frame 1", padx = 50, pady=50) # pad here to add space inside the frame, act as padding in css
frame.pack(padx=10, pady = 10) # pad here to add space outside the frame, act as margin in css

button = Button(frame, text = "Button 1")
button.grid(row=0, column=0)

button2 = Button(frame, text = "Button 2")
button2.grid(row = 0, column=1)


root.mainloop()