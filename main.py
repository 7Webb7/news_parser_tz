import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
from urllib.parse import urlparse
from bs4 import BeautifulSoup

def is_valid_url(url):
    parsed_url = urlparse(url)
    return all([parsed_url.scheme, parsed_url.netloc])

def get_news():
    url = entry_url.get()
    if not is_valid_url(url):
        messagebox.showerror("Ошибка", "Введите корректный URL")
        return

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Ошибка", f"Не удалось получить данные с URL: {e}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    # Извлекаем заголовок страницы
    title = soup.title.string if soup.title else "Без заголовка"

    # Извлекаем текст страницы
    paragraphs = soup.find_all("p", class_="topic-body__content-text")
    if paragraphs:
        body_text = "\n\n".join(p.get_text() for p in paragraphs)
    else:
        body_text = "Текст новости не найден."

    # Сохраняем заголовок и текст в файл
    filename = "news.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Заголовок: {title}\n\n")
        file.write(body_text)

    # Обновляем поле вывода
    text_bottom.config(text="Файл сохранен")


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