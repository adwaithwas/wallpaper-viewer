from tkinter import *
from PIL import ImageTk, Image
import os

counter = 1
root = Tk()
root.title("wallpaper viewer")
root.geometry("1280x720")
root.configure(bg="black")

def rotate_img():
    global counter
    img_label.config(image=img_array[counter%len(img_array)])
    counter += 1

heading_text = Label(root,text="wallpapers", fg="white", bg="black")
heading_text.pack()
heading_text.config(font=("Times", 35))

files = os.listdir("wallpapers")

img_array = []
for file in files:
    img = Image.open(os.path.join("wallpapers", file))
    resized_img = img.resize((800,480))
    
    img_array.append(ImageTk.PhotoImage(resized_img))

img_label = Label(root, image=img_array[0])
img_label.pack(pady=(50,10))

next_btn = Button(root, text="Next", bg="white", fg="black", width=20, height=2, command=rotate_img)
next_btn.pack()
next_btn.config(font=("times", 14))

root.mainloop()