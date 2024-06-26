import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Button", "Вы нажали на кнопку")

def on_label_click(event):
    messagebox.showinfo("Label", "Вы нажали на метку")

def on_entry_return(event):
    messagebox.showinfo("Entry", f"Вы ввели: {entry.get()}")

# Создаем главное окно
root = tk.Tk()
root.title("Пример Tkinter")
root.geometry("300x200")

# Создаем кнопку
button = tk.Button(root, text="Нажми меня", bg="lightblue", fg="darkblue", command=on_button_click)
button.pack(pady=10)

# Создаем метку
label = tk.Label(root, text="Нажми на меня", bg="lightgreen", fg="darkgreen")
label.pack(pady=10)
label.bind("<Button-1>", on_label_click)  # Обработка клика по метке

# Создаем поле ввода
entry = tk.Entry(root, bg="lightyellow", fg="darkred")
entry.pack(pady=10)
entry.bind("<Return>", on_entry_return)  # Обработка нажатия Enter в поле ввода

# Запускаем главный цикл
root.mainloop()
