import requests
import json
import random

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
        print(f"Episode {self.episode} - {self.name}")
        print(f"Air Date: {self.air_date}")
        print(f"Characters: {len(self.characters)}")


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

def explore_rick_and_morty_api():
    # 2.1 Random Character Request:
    random_character_id = random.randint(1, 826)
    random_character_url = f"https://rickandmortyapi.com/api/character/{random_character_id}"
    random_character_response = requests.get(random_character_url)
    random_character_data = random_character_response.json()

    # 2.2
    print("2.2: Response Output:")
    print(random_character_data)

    # Display the keys of the JSON structure
    print("\nKeys of the JSON structure:")
    print(random_character_data.keys())

    # 2.3 Save to File:
    filename = f"info_character_{random_character_id}.json"
    with open(filename, 'w') as file:
        file.write(json.dumps(random_character_data))

    # 2.4 Episode List:
    episode_urls = random_character_data.get("episode", [])
    episode_ids = [url.split("/")[-1] for url in episode_urls]

    with open(f"all_episodes_with_character_{random_character_id}.txt", 'a') as file:
        for episode_url in episode_urls:
            file.write(f"{episode_url}\n")

    # 2.5 Episode Response Structure:
    episode_1_url = "https://rickandmortyapi.com/api/episode/1"
    episode_1_response = requests.get(episode_1_url)
    episode_1_data = episode_1_response.json()

    print("2.5: Episode Response Structure:")
    print(json.dumps(episode_1_data, indent=2))

    # 2.6 Episode Class Creation:
    class Episode:
        def __init__(self, id, name, air_date, episode, characters, url, created):
            self.id = id
            self.name = name
            self.air_date = air_date
            self.episode = episode
            self.characters = characters
            self.url = url
            self.created = created

    # 2.7 Episode Data Retrieval:
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

    # 2.8 Class Methods:
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
            print(f"Episode {self.episode} - {self.name}")
            print(f"Air Date: {self.air_date}")
            print(f"Characters: {len(self.characters)}")

    # 2.9 Character Response Structure:
    character_1_url = "https://rickandmortyapi.com/api/character/1"
    character_1_response = requests.get(character_1_url)
    character_1_data = character_1_response.json()

    print("2.9: Character Response Structure:")
    print(json.dumps(character_1_data, indent=2))

    # 2.10 Character Class Creation:
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

    # 2.11 Character Object Creation:
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

    # 2.12 Character Class Methods:
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

        # Add methods as needed

    # 2.13 Result

explore_rick_and_morty_api()