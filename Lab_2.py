# Задача 1: Проверить, равна ли сумма двух чисел разнице модулей двух других чисел

# Ввод четырёхзначного числа
number = input("Введите четырёхзначное число: ")

# Проверка на корректность ввода
if len(number) != 4 or not number.isdigit():
    print("Некорректный ввод. Введите четырёхзначное число.")
else:
    # Преобразование введённой строки в целое число
    number = int(number)

    # Разбиение числа на отдельные цифры
    thousands = number // 1000
    hundreds = (number % 1000) // 100
    tens = (number % 100) // 10
    ones = number % 10

    # Проверка условия
    if thousands + ones == tens - hundreds:
        print("ДА")
    else:
        print("НЕТ")


# Задача 2: Проверить возраст на доступ к чему-либо

print("Задача 2: ")

try:
    num_tests = int(input("Введите количество тестов: "))

    for _ in range(num_tests):
        age = int(input("Введите ваш возраст: "))

        if age >= 18:
            print("Доступ разрешен")
        else:
            print("Доступ запрещен")

except ValueError:
    print("Некорректный ввод")

# Задача 3: Проверить, являются ли три числа последовательными

print("Задача 3: ")

try:
    num_tests = int(input("Введите количество тестов: "))

    for _ in range(num_tests):
        n1 = int(input("Введите первое число: "))
        n2 = int(input("Введите второе число: "))
        n3 = int(input("Введите третье число: "))

        if n2 - n1 == 1 and n3 - n2 == 1:  # Проверяем, являются ли разницы равными 1
            print("Да")
        else:
            print("Нет")

except ValueError:
    print("Некорректный ввод")

# Задача 4: Проверить, находятся ли две позиции на одной линии (горизонтальной или вертикальной)

print("Задача 4: ")

try:
    num_tests = int(input("Введите количество тестов: "))

    for _ in range(num_tests):
        col1 = int(input("Введите координату столбца 1: "))
        row1 = int(input("Введите координату строки 1: "))
        col2 = int(input("Введите координату столбца 2: "))
        row2 = int(input("Введите координату строки 2: "))

        if col1 == col2 or row1 == row2:  # Если координаты совпадают по столбцу или строке, выводим "Да"
            print("Да")
        else:
            print("Нет")

except ValueError:
    print("Некорректный ввод")

# Задача 5: Проверить, находятся ли две позиции рядом друг с другом (ход короля)

print("Задача 5: ")

try:
    num_tests = int(input("Введите количество тестов: "))

    for _ in range(num_tests):
        king_col1 = int(input("Введите координату столбца короля 1: "))
        king_row1 = int(input("Введите координату строки короля 1: "))
        king_col2 = int(input("Введите координату столбца короля 2: "))
        king_row2 = int(input("Введите координату строки короля 2: "))

        if abs(king_col1 - king_col2) <= 1 and abs(king_row1 - king_row2) <= 1:
            print("Да")
        else:
            print("Нет")

except ValueError:
    print("Некорректный ввод")

# Задача 6: Вычислить среднее из трех чисел

print("Задача 6: ")

try:
    num_tests = int(input("Введите количество тестов: "))

    for _ in range(num_tests):
        num_a = int(input("Введите число A: "))
        num_b = int(input("Введите число B: "))
        num_c = int(input("Введите число C: "))

        # largest = max(num_a, num_b, num_c)  # Находим наибольшее число
        # smallest = min(num_a, num_b, num_c)  # Находим наименьшее число

        # average = (smallest + largest) / 2  # Вычисляем среднее

        average = (num_a+num_b+num_c)/3

        print("Среднее значение:", average)

except ValueError:
    print("Некорректный ввод")

# Задача 7: Получить количество дней в заданном месяце

print("Задача 7: ")

try:
    num_tests = int(input("Введите количество тестов: "))

    for _ in range(num_tests):
        month = int(input("Введите месяц (1-12): "))

        if 1 <= month <= 12:
            days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            num_days = days_in_month[month - 1]
            print("Количество дней:", num_days)
        else:
            print("Некорректный месяц")

except ValueError:
    print("Некорректный ввод")
    # Задача 8: Определить весовую категорию

print("Задача 8: ")

try:
    num_tests = int(input("Введите количество тестов: "))

    for _ in range(num_tests):
        weight = int(input("Введите вес: "))

        if weight <= 60:
            print("Легкий вес")
        elif 60 < weight <= 64:
            print("Первый полусредний вес")
        elif 64 < weight <= 69:
            print("Полусредний вес")
    else:
        print("Некорректная весовая категория")

except ValueError:
    print("Некорректный ввод")

# Задача 9: Проверить, совпадают ли два пароля

print("Задача 9: ")

try:
    num_tests = int(input("Введите количество тестов: "))

    for _ in range(num_tests):
        password = input("Введите пароль: ")
        password_check = input("Повторите пароль: ")

        if password_check == password:
            print("Пароль принят")
        else:
            print("Пароли не совпадают")

except ValueError:
    print("Некорректный ввод")

# Задача 10: Проверить, является ли число четным или нечетным

print("Задача 10: ")

try:
    num_tests = int(input("Введите количество тестов: "))

    for _ in range(num_tests):
        num = int(input("Введите число: "))

        if num % 2 == 0:
            print("Четное число")
        else:
            print("Нечетное число")

except ValueError:
    print("Некорректный ввод")

# Задача 11: Найти минимум из двух чисел

print("Задача 11: ")

try:
    num_tests = int(input("Введите количество тестов: "))

    for _ in range(num_tests):
        num1 = int(input("Введите число 1: "))
        num2 = int(input("Введите число 2: "))

        min_number = min(num1, num2)  # Находим минимум из двух чисел

        print("Минимальное число:", min_number)

except ValueError:
    print("Некорректный ввод")

# Задача 12: Определить возрастную категорию

print("Задача 12: ")

try:
    num_tests = int(input("Введите количество тестов: "))

    for _ in range(num_tests):
        age = int(input("Введите ваш возраст: "))

        if age <= 13:
            print("Детство (включительно)")
        elif 14 <= age <= 24:
            print("Молодость")
        elif 25 <= age <= 59:
            print("Зрелость")
        else:
            print("Пожилой возраст")

except ValueError:
    print("Некорректный ввод")

# Задача 13: Определить тип треугольника по сторонам

print("Задача 13: ")

try:
    num_tests = int(input("Введите количество тестов: "))

    for _ in range(num_tests):
        side1 = int(input("Введите длину стороны 1: "))
        side2 = int(input("Введите длину стороны 2: "))
        side3 = int(input("Введите длину стороны 3: "))

        if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
            if side1 == side2 == side3:
                print("Равносторонний треугольник")
            elif side1 == side2 or side1 == side3 or side2 == side3:
                print("Равнобедренный треугольник")
            else:
                print("Разносторонний треугольник")
        else:
            print("Треугольник с такими сторонами невозможен")

except ValueError:
    print("Некорректный ввод")

