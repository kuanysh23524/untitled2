import requests
def task1():
    import requests

    class ToDo:
        def __init__(self, user_id, title, completed):
            self.user_id = user_id
            self.title = title
            self.completed = completed

    # Task 1.1: GET Request
    def make_get_request(post_id):
        try:
            url = f"https://jsonplaceholder.typicode.com/todos/{post_id}"
            response = requests.get(url)

            print("1.1: GET Request:")
            print("Response Content (JSON):")
            print(response.json())

            if response.status_code >= 400:
                print(f"Error: {response.status_code}")

        except:
            print("Error")

    # Task 1.2 and 1.3: Create a class ToDo and create a new object
    def create_todo_object(post_id):
        try:
            url = f"https://jsonplaceholder.typicode.com/todos/{post_id}"
            response = requests.get(url)

            data = response.json()
            todo_object = ToDo(user_id=data.get("userId"), title=data.get("title"), completed=data.get("completed"))

            print("\n1.2: Create a class ToDo:")
            print(todo_object.__dict__)

            return todo_object

        except:
            print("Error")

    # Task 1.4: POST Request
    def make_post_request(new_todo):
        try:
            url = "https://jsonplaceholder.typicode.com/todos"
            payload = {
                "userId": new_todo.user_id,
                "title": new_todo.title,
                "completed": new_todo.completed
            }

            response = requests.post(url, json=payload)

            print("\n1.4: POST Request:")
            print("Response Content:")
            print(response.json())

            if response.status_code >= 400:
                print(f"Error: {response.status_code}")

        except:
            print("Error")

    # Task 1.5: Edit some data of attributes of the todo item
    def edit_todo_data(todo_object):
        try:
            print("\n1.5: Edit ToDo Data:")

            # Edit
            todo_object.title = "Updated Title"

            print(todo_object.__dict__)

        except:
            print("Error")

    # Task 1.6: PUT Request
    def make_put_request(chosen_id, updated_todo):
        try:
            url = f"https://jsonplaceholder.typicode.com/todos/{chosen_id}"
            payload = {
                "userId": updated_todo.user_id,
                "title": updated_todo.title,
                "completed": updated_todo.completed
            }

            response = requests.put(url, json=payload)

            print("\n1.6: PUT Request:")
            print("Response Content:")
            print(response.json())

            if response.status_code >= 400:
                print(f"Error: {response.status_code}")

        except:
            print("Error")

    # Task 1.1: GET Request
    post_id = 1
    make_get_request(post_id)

    # Task 1.2 and 1.3: Create a class ToDo and create a new object
    new_todo_object = create_todo_object(post_id)

    # Task 1.4: POST Request
    make_post_request(new_todo_object)

    # Task 1.5: Edit some data of attributes of the todo item
    edit_todo_data(new_todo_object)

    # Task 1.6: PUT Request
    chosen_id = 1
    make_put_request(chosen_id, new_todo_object)


task1()