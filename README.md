### ENG
[RU](#ru)

## Installation

```shell
pip install json-inline
```

## Usage Rules


|             Modificator               |             Description                                                     |
|                         ------------- |:-------------:                                                              |
| ```?key:value```  | Search first object's entry in array by key:value pair                                          |
| ```?key ```       | Search first object's entry in array by key                                                     |
| ```?+key ```      | Search first object's entry in array by key and return data by key                              |
| ```?key#num```    | Search object in array by key with specify entry's count (default #1)                           |
| ```?+key#num```   | Search object in array by key with specify entry's count and return data by key                 |
| ```.key```        | Move forward in object by key                                                                   |
| ```.#index ```    | Move forward in array by index                                                                  |


## Usage

### RU
[ENG](#eng)

## Установка

```shell
pip install json-inline
```

## Правила использования

|             Модификатор               |             Описание                                                        |
|                         ------------- |:-------------:                                                              |
| ```?key:value```  | Поиск первого вхождения объекта в массиве с нужным ключем и значением                           |
| ```?key ```       | Поиск первого вхождения объекта в массиве с нужным ключем                                       |
| ```?+key ```      | Поиск первого вхождения объекта в массиве с нужным ключем и возврат данных по ключу             |
| ```?key#num```    | Поиск объекта в массиве с нужным ключем и указанием номера вхождения  (по умолчанию #1)         |
| ```?+key#num```   | Поиск объекта в массиве с нужным ключем, указанием номера вхождения и возврат данных по ключу   |
| ```.key```        | Переход на новый уровень вложенности по ключу                                                   |
| ```.#index ```    | Переход на новый уровень вложенности по индексу массива                                         |


## Примеры использования

### Поиск в массиве по ключу и значению:

```python
import json_inline

test_struct = [
    {
        "fruit": "apple",
        "yummy": "true"
    },
    {
        "vegetable": "tomato",
        "yummy": "false"
    },
    {
        "vegetable": "cucumber",
        "yummy": "false"
    }
]

# Поиск первого вхождения объекта в массиве с ключем vegetable и значением cucumber,
# возврат значения yummy из найденной структуры
json_inline.fetch(test_struct, '?vegetable:cucumber.yummy')

# >>> "false"

# Поиск первого вхождения объекта в массиве с ключем vegetable и значением tomato
json_inline.fetch(test_struct, '?vegetable:tomato')

# >>> {"vegetable": "tomato", "yummy": "false"}
```


### Поиск в массиве по ключу:

```python
import json_inline

test_struct = [
    {
        "animal": "cat"
    },
    {
        "animal": "dog"
    },
    {
        "plant": "tomato"
    },
    {
        "thing": "book"
    }
]

# Поиск первого вхождения объекта в массиве с ключем animal
json_inline.fetch(test_struct, '?animal')

# >>> {"animal": "cat"}

# Поиск второго вхождения объекта в массиве с ключем animal
json_inline.fetch(test_struct, '?animal#2')

# >>> {"animal": "dog"}

# Поиск второго вхождения объекта в массиве с ключем animal,
# возврат значения из найденного ключа (animal)
json_inline.fetch(test_struct, '?+animal#2')

# >>> "dog"
```

### Навигация по структурам:

```python
import json_inline

test_struct = [
    {'item1': 'fail'},
    {'item2': 'fail'},
    {'item2': [
        {'item4': 'fail'},
        {'item4': 'fail'},
        {'item5': [
            {'item7': 'fail'},
            {'item7': 'fail', 'item9': [
                {'item10': 'fail'},
                {'item10': 'fail'},
                {'item10': 'fail'},
                {'item10': 'fail'},
                {'item10': 'success'},
            ]},
            {'item8': 'fail'},
        ]},
        {'item5': 'fail'},
        {'item6': 'fail'},
    ]},
    {'item3': 'fail'}
]

# Вариант с движением по массиву через индекс
json_inline.fetch(test_struct, '?+item2#2.?+item5.?item7:fail#2.item9.#4.item10')

# Более надежный вариант с поиском значения путем перебора
json_inline.fetch(test_struct, '?+item2#2.?+item5.?item7:fail#2.item9.?item10:success.item10')

# >>> "success"
```

