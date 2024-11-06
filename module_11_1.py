'''
Задание
pillow - обработать изображение, например, изменить его размер,
применить эффекты и сохранить в другой формат.
'''

from PIL import Image

image = Image.open("1.jpg")  # Открываем изображение

new_size = (1200, 800)  # Новый размер изображения
res = image.resize(new_size)
res.save('C:/Users/User/PycharmProjects/pythonProject1/11.jpg')

cropped = image.crop((430, 530, 725, 740)) # Обрезка изображения
cropped.save('C:/Users/User/PycharmProjects/pythonProject1/111.png') # и сохранение в новом формате

'''
Задание
pandas - считать данные из файла, 
выполнить простой анализ данных (на своё усмотрение) и вывести результаты в консоль.
'''
import pandas as pd

df = pd.read_excel('test.xlsx') # Считываем данные из xlsx файла
mean_values = df.mean() # вычислим среднее значение для числовых колонок

print("Средние значение по каждой колонке:") # Выводим результат в консоль
print(mean_values)