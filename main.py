import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Petrovich News")
root.geometry("350x350")

background = Image.open("images/background.jpg")
background_image = ImageTk.PhotoImage(background)

text = tk.Label(root, text="Введите ссылку на новость:")
text.pack()

entry_url = tk.Entry(root)
entry_url.pack()

button_get = tk.Button(root, text="Подтвердить")
button_get.pack()

background_label = tk.Label(root, image=background_image)
background_label.pack()



root.mainloop()