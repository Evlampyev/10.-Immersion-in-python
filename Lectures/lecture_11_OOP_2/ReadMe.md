## Особенности ООП

* Контроль создания класса через [__new__](task_1.py)
* Расширение неизменяемых классов через [__new__](task_2.py)
* Шаблон Одиночка = [Singleton](task_3.py)
* Хранение документации в [__doc__](task_3.py)
* Представления экземпляра класса:
    * для пользователя: [__str__](task_4.py)
    * для программиста, скопировав результат можно создавать новый экземпляр класса [__repr__](task_5.py)
> Приоритет методов \
Варианты срабатывания __str__ и __repr__
>> * print(user) \
>>__str__ 
>> * print(f'{user}') \
>>__str__ 
>> * print(repr(user)) \
>>__repr__ 
>> * print(f'{user = }') \
>>__repr__ 
>> * print(collections) \
>>__repr__

### Математика и логика в классах
#### Обычные методы

#### Right методы
>Right методы срабатывают в том случае, если у левого аргумента в выражении
метод не был найден. Например при записи x + y вначале производится поиска
дандер метода x.__add__. Если он не найден, вызываем y.__radd__.

* Сдвиг вправо, [__rshift__](task_7.py)
* Умножение текста на “продвинутый текст” методом [__rmul__](task_8.py)

#### in place методы
>In place методы используются при короткой записи математического символа
слитно со знаком равенства: a += b. Такая запись подразумевает внесение
изменений в исходный объект, а не возврат нового экземпляра. Возвращать надо
самого себя — self.
* Вычисление процентов [__imod__](task_9.py)

### Сравнение экземпляров класса

>Числа сравниваются по значению, строки посимвольно. Но при желании можно
сравнивать любые объекты Python реализовав перечисленные ниже дандер
методы.

* __eq__ - равно, ==
* __ne__ - не равно, !=
* __gt__ - больше, >
* __ge__ - не больше, меньше или равно, <=
* __lt__ - меньше, <
* __le__ - не меньше, больше или равно, >=
Пример, дандер [методы  lt, eq](task_10.py)

> Сравнение и [сортировка](task_10.py) экземпляров класса

 



 