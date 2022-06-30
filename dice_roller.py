import tkinter
from PIL import Image,ImageTk
import random


root = tkinter.Tk()
root.geometry('800x800')
photo = tkinter.PhotoImage(file = "d6.png")
root.iconphoto(False,photo)
root.title('Roll dice')
root.configure(bg='#FFFFFF')

dice = ['d1.png','d2.png','d3.png','d4.png','d5.png','d6.png']

image1 = tkinter.PhotoImage(file = "d6.png")
label1 = tkinter.Label(root, image = image1)
label1.pack(expand = True)


def roll_dice():
    image1 = tkinter.PhotoImage(file = (random.choice(dice)))
    label1.configure(image = image1)
    label1.image = image1

button = tkinter.Button(text='Roll Dice', width = 20, height = 2, command = roll_dice)
button.pack(expand=True)
root.mainloop()



