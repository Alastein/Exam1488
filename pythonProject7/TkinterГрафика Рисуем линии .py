import tkinter as tk
# Создаем главное окно
root = tk.Tk()
root.title("Рисование текста и треугольников")
# Создаем холст для рисования
canvas = tk.Canvas(root, width=400, height=400, bg='white')
canvas.pack()
# Рисование треугольника
points = [(100, 100), (250, 200), (50, 200)]
canvas.create_polygon(points, fill="red")
# Рисование текста
text = "Ну типа текст"
canvas.create_text(200, 250, text=text, font=("Arial", 24), fill="blue")
# Запускаем главный цикл
root.mainloop()

