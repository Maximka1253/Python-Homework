import tkinter as tk
from tkinter import messagebox

def save_answers():
    name = entry_name.get()
    genre = favorite_genre.get()
    platform = favorite_platform.get()

    with open("survey_results.txt", "a", encoding="utf-8") as file:
        file.write(f"Имя: {name}\n")
        file.write(f"Любимый жанр игр: {genre}\n")
        file.write(f"Любимая платформа: {platform}\n")
        file.write("-" * 40 + "\n")

    messagebox.showinfo("Готово", "Ответы успешно сохранены!")
    entry_name.delete(0, tk.END)

root = tk.Tk()
root.title("Анкета: игровые предпочтения")
root.geometry('800x675')

tk.Label(root, text="Ваше имя:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Ваш любимый жанр игр:").pack()
favorite_genre = tk.StringVar(value="RPG")
tk.OptionMenu(root, favorite_genre, "RPG", "Шутеры", "Стратегии", "Гонки", "Казуальные").pack()

tk.Label(root, text="Любимая игровая платформа:").pack()
favorite_platform = tk.StringVar(value="ПК")
tk.OptionMenu(root, favorite_platform, "ПК", "PlayStation", "Xbox", "Nintendo", "Мобильные","Другое").pack()

tk.Button(root, text="Сохранить", command=save_answers).pack(pady=10)

root.mainloop()
