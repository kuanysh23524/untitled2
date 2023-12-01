import requests
import json
import random

# Task 1

# 1.1: GET Request
post_id = 1
url = f"https://jsonplaceholder.typicode.com/todos/{post_id}"
response = requests.get(url)

# Print response content
print("Response Content:")
print(response.json())

# Check status code
if response.status_code >= 400:
    print(f"Error: {response.status_code} - {response.text}")

# 1.2: Create a class "ToDo"
class ToDo:
    def __init__(self, userId, id, title, completed):
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed

# 1.3: Create a new object of class ToDo
new_todo_object = ToDo(userId=1, id=post_id, title="Sample Todo", completed=False)

# 1.4: POST Request
new_todo_dict = {
    "userId": new_todo_object.userId,
    "title": new_todo_object.title,
    "completed": new_todo_object.completed
}
post_url = "https://jsonplaceholder.typicode.com/todos"
post_response = requests.post(post_url, json=new_todo_dict)

# Print response content
print("\nPOST Response Content:")
print(post_response.json())

# Check status code
if post_response.status_code >= 400:
    print(f"POST Error: {post_response.status_code} - {post_response.text}")

# 1.5: Edit some data of your attributes of your todo item
new_todo_object.completed = True

# 1.6: PUT Request
put_url = f"https://jsonplaceholder.typicode.com/todos/{post_id}"
put_response = requests.put(put_url, json=new_todo_dict)

# Print response content
print("\nPUT Response Content:")
print(put_response.json())

# Check status code
if put_response.status_code >= 400:
    print(f"PUT Error: {put_response.status_code} - {put_response.text}")


# Task 2

# 2.1 Random Character Request
random_character_id = random.randint(1, 826)
character_url = f"https://rickandmortyapi.com/api/character/{random_character_id}"
character_response = requests.get(character_url).json()

# 2.2 Response Output
print("\nCharacter JSON Response:")
print(json.dumps(character_response, indent=2))

# Display keys
print("\nKeys in the JSON structure:")
print(character_response.keys())

# 2.3 Save to File
file_name = f"info_character_{random_character_id}.json"
with open(file_name, 'w') as file:
    json.dump(character_response, file, indent=2)

# 2.4 Episode List
episode_urls = character_response['episode']
episode_ids = [int(url.split("/")[-1]) for url in episode_urls]

# Create a file and append episode URLs
episodes_file_name = f"all_episodes_with_character_{random_character_id}.txt"
with open(episodes_file_name, 'a') as episodes_file:
    for episode_url in episode_urls:
        episodes_file.write(f"{episode_url}\n")

# 2.5 Episode Response Structure
episode_response = requests.get("https://rickandmortyapi.com/api/episode/1").json()
print("\nEpisode JSON Response Structure:")
print(json.dumps(episode_response, indent=2))

# 2.6 Episode Class Creation
# Assuming EpisodeClass.py contains the Episode class definition in the same directory
from EpisodeClass import Episode

# 2.7 Episode Data Retrieval
episode_objects = []
for episode_id in episode_ids:
    episode_url = f"https://rickandmortyapi.com/api/episode/{episode_id}"
    episode_data = requests.get(episode_url).json()
    episode_objects.append(Episode(**episode_data))

# 2.8 Class Methods
for episode in episode_objects:
    episode.print_info()

# 2.9 Character Response Structure
character_response = requests.get("https://rickandmortyapi.com/api/character/1").json()
print("\nCharacter JSON Response Structure:")
print(json.dumps(character_response, indent=2))

# 2.10 Character Class Creation
# Assuming CharacterClass.py contains the Character class definition in the same directory
from CharacterClass import Character

# 2.11 Character Object Creation
random_character_object = Character(**character_response)

# 2.12 Character Class Methods
random_character_object.print_info()

# 2.13 Result
print("\nRandom Character ID:", random_character_id)
print("All tasks completed successfully!")
