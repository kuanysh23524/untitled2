# Задача 1.1
user_input = input("Введите строку с пробелами: ")
input_list = list(user_input.lower())
input_list

# Задача 1.2
char_freq = {}

for char in input_list:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

freq_list = list(char_freq.items())
freq_list

# Задача 1.3
vowels = {'a', 'e', 'i', 'o', 'u'}
consonants = set("abcdefghijklmnopqrstuvwxyz") - vowels

list_vowels = []
list_consonants = []
list_symbols = []

for symbol, frequency in freq_list:
    if symbol in vowels:
        list_vowels.append((symbol, frequency))
    elif symbol in consonants:
        list_consonants.append((symbol, frequency))
    else:
        list_symbols.append((symbol, frequency))

list_vowels
list_consonants
list_symbols

# Задача 1.4
numbers = [1, 5, 8, 7, 9, 6, 7, 5, 8, 3, 9, 10, 2, 1, 3, 4]

sorted_numbers = sorted(numbers)

n = len(sorted_numbers)
quartile_size = n // 4
q1_size = quartile_size
q2_size = quartile_size
q3_size = quartile_size

if n % 4 != 0:
    q1_size += n % 4

q1 = sorted_numbers[:q1_size]
q2 = sorted_numbers[q1_size:q1_size + q2_size]
q3 = sorted_numbers[q1_size + q2_size:q1_size + q2_size + q3_size]
q4 = sorted_numbers[q1_size + q2_size + q3_size]

q1
q2
q3
q4

# Задача 2.1
student_name = 'kukonty'
assignments_scores = [89, 70, 85, 87]
labs_scores = [95.25, 90.75]
tests_scores = [78, 77]

student = {
    'name': student_name,
    'assignments': assignments_scores,
    'tests': tests_scores,
    'labs': labs_scores
}
student

# Задача 2.2
submission_check = {student['name']: 0}

if len(student['assignments']) == 4:
    submission_check[student['name']] += 4
if len(student['labs']) == 2:
    submission_check[student['name']] += 2
if len(student['tests']) == 2:
    submission_check[student['name']] += 2

submission_check

# Задача 2.3
if submission_check[student['name']] >= 4:
    final_grade = 0.3 * (sum(student['assignments']) * 0.25) + 0.5 * (sum(student['labs']) * 0.5) + 0.2 * (sum(student['tests']) * 0.5)
    student['final_grade'] = final_grade
else:
    student['final_grade'] = 0

student

# Задача 2.4
students_dict = {
    student['name']: student
}
students_dict

# Задача 3.1
transactions = [(1001, 2), (1001, 1), (1003, 2), (1005, 2), (1001, 3), (1007, 1), (1007, 2), (1100, 2), (1003, 2), (1001, 1)]

transaction_stats = {}

for user_id, transaction_type in transactions:
    if user_id not in transaction_stats:
        transaction_stats[user_id] = {1: 0, 2: 0, 3: 0, 'most_frequent_type': transaction_type, 'least_frequent_type': transaction_type}

    transaction_stats[user_id][transaction_type] += 1

for user_id, user_stats in transaction_stats.items():
    most_frequent_type = max(user_stats, key=lambda x: user_stats[x] if x != 'most_frequent_type' and x != 'least_frequent_type' else 0)
    least_frequent_type = min(user_stats, key=lambda x: user_stats[x] if x != 'most_frequent_type' and x != 'least_frequent_type' else float('inf'))
    user_stats['most_frequent_type'] = most_frequent_type
    user_stats['least_frequent_type'] = least_frequent_type

transaction_stats