
# Task - 1
# Случай первый

# Sample User Input 1:
# Enter your name please: Adam
# Enter your desired salary level: 20 000

# Sample Code Output 1:
# Adam, the tax level you will pay with the salary 20000 is 4000

# Случай второй

# Sample User Input 2:
# Enter your name please: Bob
# Enter your desired salary level: 15k

# Sample Code Output 2:
# Bob, please enter your desired salary as a digit

# Запрос имени пользователя
user_name = input("Введите ваше имя: ")

# Проверка на пустое имя
if not user_name:
    print("Имя не может быть пустым. Пожалуйста, введите ваше имя.")
else:
    try:
        # Ввод желаемой зарплаты , когда пишешь зп также нужно писать без пробела!!!
        desired_salary = int(input("Введите вашу желаемую зарплату: "))

        # Расчет уровня налога
        tax_level = desired_salary * 0.2

        # Вывод приветствия и уровня налога
        print(f"Привет, {user_name}! Ваш уровень налога для уплаты составляет: {tax_level}")
    except ValueError:
        print("Неверный ввод. Пожалуйста, введите правильную сумму зарплаты , в виде цифр!!!")



# task - 2

operations = {
    1: lambda x, y: x + y,
    2: lambda x, y: x * y,
    3: lambda x, y: x / y,
    4: lambda x, y: x ** y
}

# Выводим меню операций
print("Select an operation:")
print("1. Addition")
print("2. Multiplication")
print("3. Division")
print("4. Exponentiation")

# Вводим число для дальнейших операции
choice = int(input("Enter the operation number (1/2/3/4): "))

# Получается сравниваем наше число choice с условиями,
# и если они равны выполняем какую либо операцию которые подходят по условиям
if choice in operations:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == 3 and num2 == 0:
            print("Division by zero!!!")
        else:
            # Выполняем выбранную операцию
            result = operations[choice](num1, num2)
            operation = "addition" if choice == 1 else "multiplication" if choice == 2 else "division" if choice == 3 else "exponentiation"

            print(f"Result of {operation} is: {result}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
else:
    print("Invalid choice. Please select a valid operation.")



# Мой любимый фибоначчи
# task - 3
FIB = int(input("ведите число "))
a, b = 0, 1

for _ in range(2, FIB + 1):
    a, b = b, a + b

result = b
print(f"Число Фибоначчи с индексом {FIB} равно {result}")


# Task - 4
# Инициализация ввода и разбивка на элементы
u = input("Enter items separated by commas: ")
l = u.split(',')

# Создание словаря для частот
d = {}
for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

# Создание кортежей с частотами
t = [(k, v) for k, v in d.items()]

# Вывод результатов
print("Unique elements:", list(d.keys()))
print("Tuples with item frequencies:", t)

# Послдняя задачка
import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def add_task(tasks, task):
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Task added: ", task)

def view_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
    else:
        print("\nTasks:")
        for index, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index}. {task['task']} ({status})")

def mark_task_completed(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print(f'Task "{tasks[index]["task"]}" marked as completed.')
    else:
        print("Invalid task number.")

def edit_task(tasks, index, new_task):
    if 0 <= index < len(tasks):
        tasks[index]["task"] = new_task
        save_tasks(tasks)
        print(f'Task edited: "{new_task}"')

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        deleted_task = tasks.pop(index)
        save_tasks(tasks)
        print(f'Task "{deleted_task["task"]}" deleted.')
    else:
        print("Invalid task number.")

tasks = load_tasks()

while True:
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Edit Task")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(tasks, task)
    elif choice == '2':
        view_tasks(tasks)
    elif choice == '3':
        if not tasks:
            print("No tasks to mark as completed.")
        else:
            view_choice = input("Enter the number of the task to mark as completed: ")
            try:
                index = int(view_choice) - 1
                mark_task_completed(tasks, index)
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
    elif choice == '4':
        view_tasks(tasks)
        edit_choice = input("Enter the number of the task to edit: ")
        try:
            index = int(edit_choice) - 1
            new_task = input("Enter the new task: ")
            edit_task(tasks, index, new_task)
        except ValueError:
            print("Invalid input. Please enter a valid task number.")
    elif choice == '5':
        view_tasks(tasks)
        delete_choice = input("Enter the number of the task to delete: ")
        try:
            index = int(delete_choice) - 1
            delete_task(tasks, index)
        except ValueError:
            print("Invalid input. Please enter a valid task number.")
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")