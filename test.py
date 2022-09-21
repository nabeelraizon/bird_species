from tkinter import *
from PIL import ImageTk, Image

root = Tk()

c = Canvas(root, width=224, height=224)
c.pack()

img = ImageTk.PhotoImage(Image.open(r"imagepath\imagename.extension"))
c.create_image(x=290, y=100, image=img, anchor=NW)