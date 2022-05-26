

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
    print('Файл *.txt не обнаружен.')
    print("Время: " + str(time.process_time()))
except ValueError:
    print('Некорректное значение.')
    print("Время: " + str(time.process_time()))