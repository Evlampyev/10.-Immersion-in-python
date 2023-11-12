### CSV (Comma-Separated Values)

__CSV__ — текстовый формат, предназначенный для представления
табличных данных. Строка таблицы соответствует строке текста,
которая содержит одно или несколько полей, разделенных запятыми

#### [Чтение](task_5.py) CSV

import csv

* __with open('biostats.csv', 'r', newline='') as f:__
  параметр newline='' для работы с CSV
* __csv_file = csv.reader(f)__
  csv_file позволяет построчно читать csv файл в список list

#### [Запись](task_6.py) CSV

import csv

* __csv_write = csv.writer(f)__
  csv_write позволяет сохранять данные в формате CSV
* __csv_write.writerow(line)__
  сохранение списка в одной строке файла в формате CSV
* __csv_write.writerows(all_data)__
  сохранение матрицы в нескольких строках файла в формате CSV

*.tsv - в качестве разделителя не ',', а табуляция

#### [Чтение](task_7.py) CSV в словарь

__csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age",
"height", "weight", "office"], restkey="new", restval="Main Office")__

* fieldnames — список заголовков столбцов, ключей словаря
* restkey — значение ключа для столбцов, которых нет в fieldnames
* restval — значение поля для ключей fieldnames, которых нет в файле CSV

#### [Запись](task_8.py) CSV из словаря

import csv \
Параметры класса DictWriter аналогичны параметрам DictReader

* __csv_write.writeheader()__
  сохранение первой строки с заголовками в порядке их перечисления в параметре fieldnames
* __csv_write.writerow(line)__
  сохранение списка в одной строке файла в формате CSV
* __csv_write.writerows(all_data)__
  сохранение матрицы в нескольких строках файла в формате CSV
