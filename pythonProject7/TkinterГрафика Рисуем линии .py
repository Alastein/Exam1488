import tkinter as tk

# Создаем главное окно
root = tk.Tk()
root.title("Рисование линий и треугольников")

# Создаем холст для рисования
canvas = tk.Canvas(root, width=400, height=400, bg='white')
canvas.pack()

# Рисуем линии
canvas.create_line(50, 50, 150, 150, fill='blue', width=2)

# Рисуем треугольники
canvas.create_polygon(200, 200, 300, 200, 250, 100, outline='black', fill='', width=2)

# Запускаем главный цикл
root.mainloop()

