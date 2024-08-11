import tkinter as tk
from PIL import Image, ImageTk

def get_news():
    url = entry_url.get()
    text_bottom.config(text=f"Новость по ссылке {url}")

root = tk.Tk()
root.title("Petrovich News")
root.geometry("350x350")

background = Image.open("images/background.jpg")
background_image = ImageTk.PhotoImage(background)

text = tk.Label(root, text="Введите ссылку на новость:")
text.pack()

entry_url = tk.Entry(root)
entry_url.pack()

button_get = tk.Button(root, text="Подтвердить", command=get_news)
button_get.pack()

text_bottom = tk.Label(root, text="Необходимо ввести ссылку")
text_bottom.pack()

background_label = tk.Label(root, image=background_image)
background_label.pack()



root.mainloop()