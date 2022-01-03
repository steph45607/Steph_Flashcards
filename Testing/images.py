# To change the icon on the tab

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Steph')
root.iconbitmap('test.png')


# Using images
theImage = ImageTk.PhotoImage(Image.open("test.png")) # To open the image file
theLabel = Label(image = theImage) # Assign the image variable to as a label with image keyword
theLabel.pack() # So they can print it as a label with pack


# Button to quit the app
quit_button = Button(root, text = "Exit Program", command=root.quit) # quit keyword = to quit the program, in this case quit the 
quit_button.pack()

root.mainloop()