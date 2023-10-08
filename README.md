# django_tree_menu

### Описание
Приложение которое реализует древовидное меню

### Технологии
Python 3.9
Django 2.2.19

### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
- Установите зависимости из файла requirements.txt
```bash
pip install -r requirements.txt
``` 
- В папке с файлом manage.py выполните команду:
```bash
python3 manage.py runserver
```
- Внесите в БД меню (одно или несколько) через административную панель, и отобразите на любой нужной странице меню по названию.
Необходимо 'main_menu' заменить на название созданного вами меню.
```html
 {% draw_menu 'main_menu' %}
```


### Автор
Афанасьев Илья