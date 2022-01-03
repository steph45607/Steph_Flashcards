from tkinter import *
from PIL import ImageTk, Image

# Make an image viewer - as a carousel

root = Tk()
root.title("Image Viewer")
root.iconbitmap('icon.ico')
# root.geometry("400x200")

theImage1 = ImageTk.PhotoImage(Image.open('images/test1.jpeg'))
theImage2 = ImageTk.PhotoImage(Image.open('images/test2.jpeg'))
theImage3 = ImageTk.PhotoImage(Image.open('images/test3.jpeg'))
theImage4 = ImageTk.PhotoImage(Image.open('images/test4.jpeg'))
theImage5 = ImageTk.PhotoImage(Image.open('images/test5.jpeg'))

# To iterate through the images
imageList = [theImage1, theImage2, theImage3, theImage4, theImage5]

# status = Label(text = "Image " + (i+1) + " of " + len(imageList))

i = 0
theLabel = Label(image = imageList[i])
theLabel.grid(row=0, column=0, columnspan=3)
status = Label(text = "Image " + str(i+1) + " of " + str(len(imageList)), bd = 1,relief=SUNKEN, anchor=E).grid(row=2, column=0, columnspan=3, sticky=W+E)

def next():
    global i
    global theLabel
    if i == 4:
        i = 0
    else:
        i += 1
    theLabel.grid_forget()
    theLabel = Label(image = imageList[i])
    theLabel.grid(row=0, column=0, columnspan=3)
    global status
    status = Label(text = "Image " + str(i+1) + " of " + str(len(imageList)), bd = 1, relief=SUNKEN, anchor = E).grid(row=2, column=0, columnspan=3, sticky=W+E)


def back():
    global i
    global theLabel
    if i == 0:
        i = 4
    else:
        i -= 1
    theLabel.grid_forget()
    theLabel = Label(image = imageList[i])
    theLabel.grid(row=0, column=0, columnspan=3)
    global status
    status = Label(text = "Image " + str(i+1) + " of " + str(len(imageList))).grid(row=2, column=0, columnspan=3)


exitButton = Button(root, text = "Exit", command=root.quit)
exitButton.grid(row = 1, column=1)

nextButton = Button(root, text = "Next", command=lambda: next())
nextButton.grid(row=1, column=2)

backButton = Button(root, text = "Previous", command=lambda: back())
backButton.grid(row=1, column=0)



root.mainloop()