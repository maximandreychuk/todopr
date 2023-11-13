Простой ToDo менеджер, реализованный на Django 
В качестве веб-интерфейса использован фреймворк Semantic UI

https://semras0tresh.pythonanywhere.com/



## Установка:
1. Клонировать репозиторий и перейти в него в командной строке:
    ```
    cd todopr
    ```
2. Cоздать и активировать виртуальное окружение:
    ```
    python3 -m venv todoenv 
    ```
    в папке с виртуальным окружением
    
    ```
    . todoenv/Scripts/activate
    ```
3. Установить зависимости из файла requirements.txt:
    ```
    cd todo
    ```
    ```
    cd todoapp
    ```
    ```
    python3 -m pip install --upgrade pip
    ```
    ```
    pip install -r requirements.txt
    ```
5. Выполнить миграции:
    ```
    cd ..
    ```
    ```
    python3 manage.py migrate
    ```
7. Создайте суперпользователя:
    ```
    python3 manage.py createsuperuser
    ```
8. Запустить проект:
    ```
    python3 manage.py runserver
    ```
