from itertools import combinations, groupby

# Задача 1: Работа с кортежами

# 1.1 Создание кортежа из ввода пользователя (строка без пробелов)
user_input = input("Enter a string without spaces: ")
my_tuple = tuple(user_input)  # Создание кортежа из введенной строки
print("Created tuple:", my_tuple)  # Вывод созданного кортежа

# 1.2 Преобразование кортежа в строку (используя кортеж из задачи 1.1)
my_tuple = ('T', 'h', 'e', 'B', 'i', 'g', 'B', 'e', 'n')
my_string = ''.join(my_tuple)  # Преобразование кортежа в строку
print("String: ", my_string)  # Вывод строки

# 1.3 Сцепление двух кортежей (первая половина кортежа A с второй половиной кортежа B)
tuple_A = (1, 2, 3, 4, 5, 6, 7)
tuple_B = (5, 6, 7, 9, 7, 1, 10, 10)
combined_tuple = tuple_A[:4] + tuple_B[4:]  # Сцепление двух кортежей
print(combined_tuple)  # Вывод комбинированного кортежа

# 1.4 Подсчет и создание кортежа с количеством вхождений элементов
my_tuple = (55, 6, 777, 54, 6, 76, 7777, 1, 777, 6)
element_count = {}  # Создание словаря для подсчета вхождений элементов
for element in my_tuple:
    element_count[element] = element_count.get(element, 0) + 1  # Подсчет вхождений элементов
result_tuple = tuple((k, v) for k, v in element_count.items())  # Создание кортежа с парами (элемент, количество)
print("Elements and their occurrences:", result_tuple)  # Вывод элементов и их количества

# 1.5 Создание кортежей для хранения разных типов данных
data = (55, 6, 777, 70.0, '7', 'A')
integers = tuple(x for x in data if isinstance(x, int))  # Создание кортежа с целыми числами
floats = tuple(x for x in data if isinstance(x, float))  # Создание кортежа с числами с плавающей точкой
strings = tuple(x for x in data if isinstance(x, str))  # Создание кортежа со строками
print("Integers:", integers)  # Вывод кортежа с целыми числами
print("Floats:", floats)  # Вывод кортежа с числами с плавающей точкой
print("Strings:", strings)  # Вывод кортежа со строками

# Задача 2: Работа с множествами и генераторами множеств

# 2.1 Создание множества из ввода пользователя (строка без пробелов) с использованием генератора множеств
user_input = input("Enter a string without spaces: ")
my_set = {char for char in user_input}  # Создание множества из введенной строки
print("Created set:", my_set)  # Вывод созданного множества

# 2.2 Поиск различий между двумя множествами
set_A = {1, 2, 3, 4, 5}
set_B = {5, 7, 8, 9, 2, 10}
difference_set = set_A.difference(set_B)  # Поиск разницы между множествами
print("Set difference:", difference_set)  # Вывод разницы

# 2.3 Удаление элементов из множества A, которые также присутствуют в множестве B
set_A = {1, 2, 3, 4, 5}
set_B = {5, 7, 8, 9, 2, 10}
set_A.difference_update(set_B)  # Удаление элементов, общих для обоих множеств
print("Updated set A:", set_A)  # Вывод обновленного множества A

# 2.4 Обновление множеств на основе элементов в множестве C
set_A = {1, 2, 3, 4, 7}
set_B = {8, 7, 9, 4, 2, 0, 10}
set_C = {4, 0, 1}
set_C.update(set_A.intersection(set_C))  # Обновление множества C на основе пересечения с множеством A
set_A.difference_update(set_A.intersection(set_C))  # Удаление элементов, общих для A и C из A
print("Updated set C:", set_C)  # Вывод обновленного множества C

# 2.5 Создание списка множеств размера m из комбинаций из супермножества A
A = {1, 2, 3, 4, 5, 6}
n = 3  # Размер комбинаций
m = 5  # Количество комбинаций
result = [set(combo) for combo in combinations(A, n)][:m]  # Создание списка множеств
print("List of sets:", result)  # Вывод списка множеств


# Задача 3: Группировка данных по производителю

cars_list = [('BMW', 'X6'), ('Toyota', 'Yaris'), ('Fiat', '500'), ('Fiat', 'Panda'), ('Toyota', 'Camry 30')]

# Сортировка списка автомобилей по производителю
sorted_cars = sorted(cars_list, key=lambda x: x[0])

# Группировка автомобилей по производителю и вывод результата
for manufacturer, group in groupby(sorted_cars, key=lambda x: x[0]):
    group_list = list(group)  # Преобразование объекта group в список
    count = len(group_list)  # Подсчет количества автомобилей для каждого производителя
    models = [car[1] for car in group_list]  # Извлечение моделей автомобилей
    print(f"{manufacturer} {count} - {', '.join(models)}")  # Вывод информации о производителе и моделях автомобилей

