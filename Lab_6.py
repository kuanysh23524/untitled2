from datetime import datetime
import math

print('Task 1')
# Task 1
def get_key(input_dict):
    return [key for key, value in input_dict.items() if value]

input_dict = {
    "a": True,
    "b": False,
    "c": True,
}
output_list = get_key(input_dict)
print(output_list)

print('Task 2')
# Task 2
def get_unique_elements(input_list):
    return [element for element in input_list if input_list.count(element) <= 1]

input_list = [1, 2, 3, 1, 2, 4]
output_list = get_unique_elements(input_list)
print(output_list)

print('Task 3')
# Task 3
def get_date_in_format(input_date):
    parsed_date = datetime.strptime(input_date, "%Y.%m.%d")
    formatted_date = parsed_date.strftime("%d.%m.%Y")
    return formatted_date

input_date = "2023.10.23"
output_date = get_date_in_format(input_date)
print(output_date)

print('Task 4')
# Task 4
def get_elements_with_no_more_than_two_occurrences(input_list):
    return [element for element in set(input_list) if input_list.count(element) <= 2]

input_list = [1, 2, 3, 1, 2, 4]
output_list = get_elements_with_no_more_than_two_occurrences(input_list)
print(output_list)

print('Task 5')
# Task 5
def get_words_from_string(input_string):
    return input_string.split()

input_string = input(str('write input string: '))
output_list = get_words_from_string(input_string)
print(output_list)

print('Task 6')
# Task 6
def get_unique_elements_with_count(input_list):
    unique_elements = set(input_list)
    count_dict = {element: input_list.count(element) for element in unique_elements}
    return count_dict

input_list = [1, 2, 3, 1, 2, 4, 1, 2]
output_dict = get_unique_elements_with_count(input_list)
print(output_dict)

print('Task 7')
# Task 7
def get_prime_numbers(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

n = 100
output_list = get_prime_numbers(n)
print(output_list)

print('Task 8')
# Task 8
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_prime_numbers_in_list(input_list):
    return [num for num in input_list if is_prime(num)]

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 27, 36, 48, 54, 67, 71, 73, 75, 83, 89, 99]
output_list = get_prime_numbers_in_list(input_list)
print(output_list)

print('Task 9')
# Task 9
def get_difference_between_dates(date1, date2):
    date_format = "%Y.%m.%d"
    datetime1 = datetime.strptime(date1, date_format)
    datetime2 = datetime.strptime(date2, date_format)
    difference = abs((datetime2 - datetime1).days)
    return difference

date1 = "2023.10.23"
date2 = "2023.10.24"
output_difference = get_difference_between_dates(date1, date2)
print(output_difference)

print('Task 10')
# Task 10
def get_decimal_number_from_binary_string(binary_string):
    decimal_number = int(binary_string, 2)
    return decimal_number

binary_string = "10110011"
output_decimal = get_decimal_number_from_binary_string(binary_string)
print(output_decimal)

print('Task 11')
# Task 11
def is_perfect_square(num):
    return math.isqrt(num) ** 2 == num

def get_perfect_squares(input_list):
    return [num for num in input_list if is_perfect_square(num)]

input_list = [4, 25, 81, 10, 16]
output_list = get_perfect_squares(input_list)
print(output_list)

print('Task 12')
# Task 12
def sort_by_price(shopping_list):
    return sorted(shopping_list, key=lambda item: item['price'])

shopping_list = [
    {"name": "Apple", "price": 100},
    {"name": "Banana", "price": 50},
    {"name": "Orange", "price": 20}
]

output_list = sort_by_price(shopping_list)
print(output_list)

print('Task 13')
# Task 13
def get_words_starting_with_vowel(words):
    vowels = set("aeiouAEIOU")
    return [word for word in words if word[0] in vowels]

input_words = ["apple", "banana", "orange", "bear", "cat"]
output_words = get_words_starting_with_vowel(input_words)
print(output_words)
