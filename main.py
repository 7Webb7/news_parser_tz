import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Petrovich News")

background = Image.open("images/background.jpg")
background_image = ImageTk.PhotoImage(background)

background_label = tk.Label(root, image = background_image)
background_label.place(relwidth=1, relheigh =1)

text = tk.Label(root, text  = "Введите ссылку на новость:").pack()
runButton = tk.Button(root, text = "Поехали", fg = "red").pack()

root.mainloop()