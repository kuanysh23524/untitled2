print("Salem Alem")

print("Task 1.1")
# 1.1 The popular TV series "Stay Alive" used a sequence of numbers 4 8 15 16 23 42,
# which brought the heroes good luck and helped to hit the jackpot in the lottery.
# Write a code snippet that outputs a given sequence of numbers with one space between them. [ 5 point ]point/

print(f"{4} {8} {15} {16} {23} {42}")

# 1.2 Change the previous code so that each number of the sequence
# 4
# 8
# 15
# 16
# 23
# 42
# is printed on a separate line. [ 5 point ]
print("Task 1.2")
print(f"{4}\n{8}\n{15}\n{16}\n{23}\n{42}")

# 1.3 Write a code to display three consecutive numbers, each on a separate line.
# The first number is entered by the user,
# the remaining numbers are calculated in the code. Handle possible exceptions. [ 5 point ]

print("Task 1.3")
try:
    num1 = int(input("Insert a num 1\n"))
    print(num1)
    print(num1+1)
    print(num1+2)
except:
    print("insert a number please")

# 1.4 Write a code that reads three integers and displays their sum on the screen.
# Each number is written in a separate line. [ 5 point ]

print("Task 1.4")

try:
    num2 = int(input("Insert a number 1\n"))
    num3 = int(input("Insert a number 2\n"))
    num4 = int(input("Insert a number 4\n"))
    print(num2 + num3 + num4)
except:
    print("Insert a integer type valie please")

# 1.5 Write a code that calculates the volume of a cube and
# the area of its full surface, based on the entered value of the edge length. [ 10 point ]

print("Task 1.5")

# Input the edge length from the user
edge_length = float(input("Enter the edge length of the cube: "))

# Calculate the volume of the cube

volume = edge_length ** 3

# Calculate the surface area of the cube (all six faces)
surface_area = 6 * (edge_length ** 2)

# Print the results
print(f"volume {volume}")
print(f"surface area {surface_area}")

print("Task 2. Arithmetic, logic and bitwise ops.")
# 2.1 N schoolchildren divide K tangerines equally, the non-dividing remainder remains in the basket.
# # How many whole tangerines will each student get?
# # How many whole tangerines will remain in the basket? [ 5 point ]

print("Task 2.1")

# Вводим количество школьников (N) и количество мандаринов (K)
N = int(input("Введите количество школьников: "))
K = int(input("Введите количество мандаринов: "))

# Вычисляем, сколько мандаринов получит каждый ученик
mandarins_per_student = K // N  # Используем оператор "//" для целочисленного деления

# Вычисляем, сколько мандаринов останется в корзинке
remaining_mandarins = K % N  # Используем оператор "%" для получения остатка от деления

# Выводим результаты
print(f"Каждый ученик получит {mandarins_per_student} целых мандаринов.")
print(f"В корзинке останется {remaining_mandarins} целых мандаринов.")

# 2.2 Write a program to find the digits of a four-digit number. [ 10 point ]

print("Task 2.2")

# Input a four-digit number from the user
number = int(input("Enter a four-digit number: "))

# Check if the input number is indeed four digits
if 1000 <= number <= 9999:
    # Extract each digit using integer division and modulo
    thousands_digit = number // 1000
    hundreds_digit = (number // 100) % 10
    tens_digit = (number // 10) % 10
    ones_digit = number % 10

    # Print the digits
    print(f"Thousands Digit: {thousands_digit}")
    print(f"Hundreds Digit: {hundreds_digit}")
    print(f"Tens Digit: {tens_digit}")
    print(f"Ones Digit: {ones_digit}")
else:
    print("Please enter a valid four-digit number.")

print("Task 2.3")
# Вводим начальное количество жителей вселенной
population = int(input("Введите начальное количество жителей вселенной: "))

# Проверяем, является ли количество жителей нечетным
if population % 2 == 1:
    # Если количество жителей нечетное, то округляем вверх до ближайшего четного числа
    survivors = (population + 1) // 2
else:
    # Если количество жителей четное, то просто делим пополам
    survivors = population // 2

# Выводим количество выживших
print(f"Количество выживших: {survivors}")

print("Task 2.4")
# 2.4 Write a code that accepts a number  input from the user, and performs “<<” and outputs the result.
# If the result is zero the code should output the warning message.  [ 10 point ]

try:
    # Get a number from the user
    number = int(input("Enter a number: "))

    # Perform the left shift operation "<<"
    result = number << 1

    if result == 0:
        print("Warning: The result is zero.")
    else:
        print(f"The result of << is {result}")
except ValueError:
    print("Invalid input. Please enter an integer.")
except Exception as e:
    print(f"An error occurred: {e}")

print("Task 2.5")

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Ask the user to choose an operation
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter the operation number (1/2/3/4): ")

    # Perform the selected operation and display the result
    if choice == "1":
        result = num1 + num2
        print(f"The result of addition is: {result}")
    elif choice == "2":
        result = num1 - num2
        print(f"The result of subtraction is: {result}")
    elif choice == "3":
        result = num1 * num2
        print(f"The result of multiplication is: {result}")
    elif choice == "4":
        if num2 == 0:
            print("Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result of division is: {result}")
    else:
        print("Invalid choice. Please enter a valid operation number (1/2/3/4).")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
except Exception as e:
    print(f"An error occurred: {e}")


