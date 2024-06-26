README.md для запуска проекта на Django

# Запуск проекта на Django

## Требования
- Python 3.8+
- Django 3.0+
- Установленные зависимости из `req.txt`

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone <URL вашего репозитория>
   ```

2. Перейдите в директорию проекта:
   ```bash
   cd <название проекта>
   ```

3. Создайте виртуальное окружение:
   ```bash
   python -m venv venv
   ```

4. Активируйте виртуальное окружение:

   - На Windows:
     ```bash
     venv\Scripts\activate
     ```
   - На MacOS и Linux:
     ```bash
     source venv/bin/activate
     ```

5. Установите зависимости:
   ```bash
   pip install -r req.txt
   ```

## Настройка

1. Создайте файл `.env` в корневой директории проекта и добавьте необходимые переменные окружения. Пример:
   ```env
   DEBUG=True
   SECRET_KEY=ваш_секретный_ключ
   DATABASE_URL=sqlite:///db.sqlite3
   ```

2. Выполните миграции базы данных:
   ```bash
   python manage.py makemigration
   python manage.py migrate
   ```

3. Создайте суперпользователя для доступа к админ-панели:
   ```bash
   python manage.py createsuperuser
   ```

## Запуск

1. Запустите сервер разработки:
   ```bash
   python manage.py runserver
   ```

2. Откройте браузер и перейдите по адресу:
   ```
   http://127.0.0.1:8000/
   ```

## Структура проекта

- `.idea/` - Настройки проекта для IDE
- `post/` - приложение
- `crypto/` - Основной модуль проекта
- `.gitignore` - Файл для исключения файлов из контроля версий
- `manage.py` - Управляющий скрипт Django
- `req.txt` - Список зависимостей проекта

