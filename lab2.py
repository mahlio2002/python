#Вариант 16.
#Написать программу, которая читая текст  из файла, выводит на экран используемые буквы и их количество.

from numpy import flexible
import time
import re 
from collections import Counter
try:
    d = Counter()
    filePath = input('Путь к файлу: ')
    with open(filePath, 'r', encoding='utf8') as file:
        for line in file:
          d.update(line.strip(',.\n'))
        file.close()
        print(d)
        print("Время: " + str(time.process_time()))
except FileNotFoundError:
    print('Файл не обнаружен.')
    print("Время: " + str(time.process_time()))
except ValueError:
    print('Некорректное значение.')
    print("Время выполнения: " + str(time.process_time()))