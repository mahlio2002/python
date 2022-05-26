

from numpy import flexible
import time
import re 
from collections import Counter
try:
    d = Counter()
    filePath = input('Введите путь к файлу: ')
    with open(filePath, 'r', encoding='utf8') as file:
        for line in file:
          d.update(line.strip(',.\n'))
        file.close()
        print(d)
        print("Время выполнения: " + str(time.process_time()))
except FileNotFoundError:
    print('Файл *.txt не обнаружен.')
    print("Время выполнения: " + str(time.process_time()))
except ValueError:
    print('Вы ввели некорректное значение.')
    print("Время выполнения: " + str(time.process_time()))