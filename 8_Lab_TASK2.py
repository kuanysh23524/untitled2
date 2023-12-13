import requests
import json
import random

class Episode:
    # Что то на подобие конструктора , для обращение к данным элемента
    def __init__(self, id, name, air_date, episode, characters, url, created):
        self.id = id
        self.name = name
        self.air_date = air_date
        self.episode = episode
        self.characters = characters
        self.url = url
        self.created = created

    # Метод для вывода деталей эпизода
    def print_details(self):
        print(f"Эпизод {self.episode} - {self.name}")
        print(f"Дата выхода: {self.air_date}")
        print(f"Персонажи: {len(self.characters)}")

#  класс 'Character' для представления персонажа Rick and Morty , конструктор
class Character:
    def __init__(self, id, name, status, species, type, gender, origin, location, image, episode, url, created):
        self.id = id
        self.name = name
        self.status = status
        self.species = species
        self.type = type
        self.gender = gender
        self.origin = origin
        self.location = location
        self.image = image
        self.episode = episode
        self.url = url
        self.created = created

# Функция для исследования API Rick and Morty
def explore_rick_and_morty_api():
    # 2.1 Запрос случайного персонажа
    random_character_id = random.randint(1, 826)
    random_character_url = f"https://rickandmortyapi.com/api/character/{random_character_id}"
    random_character_response = requests.get(random_character_url)
    random_character_data = random_character_response.json()

    # 2.2 Вывод ответа на запрос
    print("2.2: Ответ:")
    print(random_character_data)

    # Выводим ключи JSON-структуры
    print("\nКлючи JSON-структуры:")
    print(random_character_data.keys())

    # 2.3 Сохранение в файл
    filename = f"info_character_{random_character_id}.json"
    with open(filename, 'w') as file:
        file.write(json.dumps(random_character_data))

    # 2.4 Получение списка эпизодов с участием персонажа
    episode_urls = random_character_data.get("episode", [])
    episode_ids = [url.split("/")[-1] for url in episode_urls]

    with open(f"all_episodes_with_character_{random_character_id}.txt", 'a') as file:
        for episode_url in episode_urls:
            file.write(f"{episode_url}\n")

    # 2.5 Структура ответа на запрос эпизода
    episode_1_url = "https://rickandmortyapi.com/api/episode/1"
    episode_1_response = requests.get(episode_1_url)
    episode_1_data = episode_1_response.json()

    print("2.5: Структура ответа на запрос эпизода:")
    print(json.dumps(episode_1_data, indent=2))

    # 2.6 Создание класса 'Episode'
    class Episode:
        def __init__(self, id, name, air_date, episode, characters, url, created):
            self.id = id
            self.name = name
            self.air_date = air_date
            self.episode = episode
            self.characters = characters
            self.url = url
            self.created = created

    # 2.7 Получение данных об эпизодах
    episode_objects = []

    for episode_id in episode_ids:
        episode_url = f"https://rickandmortyapi.com/api/episode/{episode_id}"
        episode_response = requests.get(episode_url)
        episode_data = episode_response.json()

        episode_objects.append(
            Episode(
                episode_data["id"],
                episode_data["name"],
                episode_data["air_date"],
                episode_data["episode"],
                episode_data["characters"],
                episode_data["url"],
                episode_data["created"]
            )
        )

    # 2.8 Методы класса 'Episode'
    class Episode:
        def __init__(self, id, name, air_date, episode, characters, url, created):
            self.id = id
            self.name = name
            self.air_date = air_date
            self.episode = episode
            self.characters = characters
            self.url = url
            self.created = created

        def print_details(self):
            print(f"Эпизод {self.episode} - {self.name}")
            print(f"Дата выхода: {self.air_date}")
            print(f"Персонажи: {len(self.characters)}")

    # 2.9 Структура ответа на запрос персонажа
    character_1_url = "https://rickandmortyapi.com/api/character/1"
    character_1_response = requests.get(character_1_url)
    character_1_data = character_1_response.json()

    print("2.9: Структура ответа на запрос персонажа:")
    print(json.dumps(character_1_data, indent=2))

    # 2.10 Создание класса 'Character'
    class Character:
        def __init__(self, id, name, status, species, type, gender, origin, location, image, episode, url, created):
            self.id = id
            self.name = name
            self.status = status
            self.species = species
            self.type = type
            self.gender = gender
            self.origin = origin
            self.location = location
            self.image = image
            self.episode = episode
            self.url = url
            self.created = created

    # 2.11 Создание объекта персонажа
    random_character_url = f"https://rickandmortyapi.com/api/character/{random_character_id}"
    random_character_response = requests.get(random_character_url)
    random_character_data = random_character_response.json()

    random_character = Character(
        random_character_data["id"],
        random_character_data["name"],
        random_character_data["status"],
        random_character_data["species"],
        random_character_data["type"],
        random_character_data["gender"],
        random_character_data["origin"],
        random_character_data["location"],
        random_character_data["image"],
        random_character_data["episode"],
        random_character_data["url"],
        random_character_data["created"]
    )

    # 2.12 Методы класса 'Character'
    class Character:
        def __init__(self, id, name, status, species, type, gender, origin, location, image, episode, url, created):
            self.id = id
            self.name = name
            self.status = status
            self.species = species
            self.type = type
            self.gender = gender
            self.origin = origin
            self.location = location
            self.image = image
            self.episode = episode
            self.url = url
            self.created = created

    # Можно добавлять методы по мере необходимости

# 2.13 Результат

# Вызываем функцию для исследования API Rick and Morty
explore_rick_and_morty_api()

           
