## ООП

__Класс__ — универсальный, комплексный тип данных, состоящий из тематически единого набора *«полей»* (переменных 
более элементарных типов) и *«методов»* (функций для работы с этими полями), то есть он является моделью
информационной сущности с внутренним и внешним интерфейсами для оперирования своим содержимым.

### Инкапсуляция

#### Модификаторы доступа

В классическом ООП выделяют следующие модификаторы доступа: \
[**public**](task_3.py) — публичный доступ, т.е. возможность обратиться к свойству или методу из любого другого класса и экземпляра \
[**_protected**](task_4.py) — защищённый доступ, позволяющий обращаться к свойствам и методам из класса и из классов
наследников. \
[**__private**](task_5.py) — приватный доступ, т.е. отсутствие возможности обратиться к свойству или методы из другого
класса или экземпляра.
> В Python по умолчанию все свойства и методы публичные. \
> Однако существуют соглашения по стилю имён, которые делают атрибуты защищёнными/приватным.   
> Речь в очередной раз пойдёт о символе подчеркивания

> Доступ к приватным переменным:
>> class Person: \
__max_up = 3 \
> > ... \
> > print(f'{p1._Person__max_up = }')

### [Наследование](task_6.py)

#### [Множественное наследование](task_7.py)

#### MRO

*MRO* - method resolution order переводится как “порядок разрешения методов”.
Относится этот порядок не только к методам, но и ко всем атрибутам класса.
Это внутренний механизм, определяющий порядок наследования.

> Чтобы его узнать:
>> ClassName.mro() \
> > print(*Class.mro() sep='\n')

### [Полиморфизм](task_8.py)

__Полиморфизм__ — свойство системы, позволяющее использовать объекты с одинаковым интерфейсом без информации о типе и
внутренней структуре объекта. 
