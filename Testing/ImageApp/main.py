from tkinter import *
from PIL import ImageTk, Image

# Make an image viewer - as a carousel

root = Tk()
root.title("Image Viewer")
root.iconbitmap('icon.ico')

theImage1 = ImageTk.PhotoImage(Image.open('images/test1.jpeg'))
theImage2 = ImageTk.PhotoImage(Image.open('images/test2.jpeg'))
theImage3= ImageTk.PhotoImage(Image.open('images/test3.jpeg'))
theImage4 = ImageTk.PhotoImage(Image.open('images/test4.jpeg'))
theImage5 = ImageTk.PhotoImage(Image.open('images/test5.jpeg'))

# To iterate through the images
imageList = [theImage1, theImage2, theImage3, theImage4, theImage5]

theLabel = Label(image = theImage1)
theLabel.grid(row=0, column=0, columnspan=3)

def next():
    global theLabel
    global nextButton
    global backButton
    theLabel.grid_forget() # get rid of something, to delete thigns from the screen
    # To erase the previous image
    # Now will show next image
    theLabel = Label(image = imageList[num-1])
    button


    theLabel.grid(row=0, column=0, columnspan=3)
    
def back():
    return


exitButton = Button(root, text = "Exit", command=root.quit)
exitButton.grid(row = 1, column=1)

nextButton = Button(root, text = "Next", command=lambda: next())
nextButton.grid(row=1, column=2)

backButton = Button(root, text = "Previous", command=lambda: back())
backButton.grid(row=1, column=0)



root.mainloop()