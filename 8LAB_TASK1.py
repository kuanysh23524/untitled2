
import requests


class ToDo:
    def __init__(self, user_id, title, completed):
        self.user_id = user_id
        self.title = title
        self.completed = completed

# Задача 1.1: GET-запрос для получения данных
def make_get_request(post_id):
    try:
        # Создание  URL для GET-запроса
        url = f"https://jsonplaceholder.typicode.com/todos/{post_id}"
        # переходим к  GET-запросу
        response = requests.get(url)

        print("1.1: GET-запрос:")
        print("Содержимое ответа (JSON):")
        print(response.json())

        # Обработка ошибок, если код состояния больше или равен 400
        if response.status_code >= 400:
            print(f"Ошибка: {response.status_code}")

    except:
        print("Ошибка")

# Задачи 1.2 и 1.3: Создание объекта класса , получаем данные с гет запроса
def create_todo_object(post_id):
    try:
        # Формирование URL для GET-запроса
        url = f"https://jsonplaceholder.typicode.com/todos/{post_id}"
        # Выполнение GET-запроса
        response = requests.get(url)

        # Извлечение данных в формате JSON из ответа
        data = response.json()
        # Создание объекта класса ToDo на основе данных из ответа
        todo_object = ToDo(user_id=data.get("userId"), title=data.get("title"), completed=data.get("completed"))

        print("\n1.2: Создание класса ToDo:")
        print(todo_object.__dict__)

        return todo_object

    except:
        print("Ошибка")

# Задача 1.4: POST-запрос для создания новой задачи
def make_post_request(new_todo):
    try:
        # Формирование URL для POST-запроса
        url = "https://jsonplaceholder.typicode.com/todos"
        # Подготовка данных для отправки в формате JSON
        payload = {
            "userId": new_todo.user_id,
            "title": new_todo.title,
            "completed": new_todo.completed
        }

        # Выполнение POST-запроса с передачей данных
        response = requests.post(url, json=payload)

        print("\n1.4: POST-запрос:")
        print("Содержимое ответа:")
        print(response.json())

        # Обработка ошибок, если код состояния больше или равен 400
        if response.status_code >= 400:
            print(f"Ошибка: {response.status_code}")

    except:
        print("Ошибка")

# Задача 1.5: Редактирование данных атрибутов задачи
def edit_todo_data(todo_object):
    try:
        print("\n1.5: Редактирование данных ToDo:")

        # Редактирование заголовка задачи
        todo_object.title = "Обновленное название"

        print(todo_object.__dict__)

    except:
        print("Ошибка")

# Задача 1.6: PUT-запрос для обновления данных задачи
def make_put_request(chosen_id, updated_todo):
    try:
        #  СЧИТЫВАЕМ URL ДАЛЕЕ ПОТОМ В СКОБКАХ УКАЗЫВАЕМ КАКОГО ИМЕННО ЭЛЕМЕНТА ДАННЫЕ НАМ ДОЛЖЕН ВЫВЕСТИ КОД
        url = f"https://jsonplaceholder.typicode.com/todos/{chosen_id}"
        # Подготовка данных для отправки в формате JSON
        payload = {
            "userId": updated_todo.user_id,
            "title": updated_todo.title,
            "completed": updated_todo.completed
        }

        # Выполнение PUT-запроса с передачей данных
        response = requests.put(url, json=payload)

        print("\n1.6: PUT-запрос:")
        print("Содержимое ответа:")
        print(response.json())

        # Обработка ошибок, если код состояния больше или равен 400
        if response.status_code >= 400:
            print(f"Ошибка: {response.status_code}")

    except:
        print("Ошибка")

# Задача 1.1: GET-запрос
post_id = 1
make_get_request(post_id)

# Задачи 1.2 и 1.3: Создание объекта класса ToDo исходя из данных GET-запроса
new_todo_object = create_todo_object(post_id)

# Задача 1.4: POST-запрос
make_post_request(new_todo_object)

# Задача 1.5: Редактирование данных атрибутов задачи
edit_todo_data(new_todo_object)

# Задача 1.6: PUT-запрос
chosen_id = 1
make_put_request(chosen_id, new_todo_object)
