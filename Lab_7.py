def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None


def ex_1(file_path):
    """
    Task 1: Read and display the content of the file.
    """
    print('Task 1:')
    content = read_file(file_path)
    return content


def ex_2(file_path):
    """
    Task 2: Randomly select and display a line from the file.
    """
    import random
    print('Task 2')

    content = read_file(file_path)
    if content is not None:
        lines = content.split('\n')
        random_line = random.choice(lines)
        return random_line


def ex_3(file_path):
    """
    Task 3: Count and display the number of uppercase characters in the file.
    """
    print('Task 3')

    content = read_file(file_path)
    if content is not None:
        uppercase_count = sum(1 for char in content if char.isupper())
        return uppercase_count


def ex_4(file_path):
    """
    Task 4: Count and display the number of lines not starting with 'D'.
    """
    print('Task 4')

    content = read_file(file_path)
    if content is not None:
        lines = content.split('\n')
        count = sum(1 for line in lines if not line.startswith('D'))
        return count


def ex_5(file_path):
    """
    Task 5: Count and display the number of words ending with 'F' or 'f'.
    """
    print('Task 5')

    content = read_file(file_path)
    if content is not None:
        words = content.split()
        count = sum(1 for word in words if word.lower().endswith('f'))
        return count


def ex_6(file_path):
    """
    Task 6: Count and display the occurrences of 'all' and 'none' in the file.
    """
    print('Task 6')

    content = read_file(file_path)
    if content is not None:
        words = content.split()
        count_all = words.count("all")
        count_none = words.count("none")
        return count_all, count_none


def ex_7(file_path):
    """
    Task 7: Display word frequency in the file.
    """
    print('Task 7')

    content = read_file(file_path)
    if content is not None:
        from collections import Counter
        words = content.split()
        word_freq = Counter(words)
        return word_freq


def ex_8(file_path):
    """
    Task 8: Display the longest word in the file.
    """
    print('Task 8')

    content = read_file(file_path)
    if content is not None:
        words = content.split()
        longest_word = max(words, key=len)
        return longest_word


def ex_9(file_path):
    """
    Task 9: Replace 'B' and 'b' with 'J' and 'j' in the content and display the corrected content.
    """
    print('Task 9')

    content = read_file(file_path)
    if content is not None:
        corrected_content = content.replace('B', 'J').replace('b', 'j')
        return corrected_content


def ex_10(file_path):
    """
    Task 10: Count and display the occurrences of 'a' and 'b' (case-insensitive) in the content.
    """
    print('Task 10')

    content = read_file(file_path)
    if content is not None:
        content_lower = content.lower()
        count_a = content_lower.count('a')
        count_b = content_lower.count('b')
        return count_a, count_b


# Запрос пути к файлу у пользователя
file_path = input("Введите путь к файлу: ")

# Отображение результатов
print(ex_1(file_path))
print(ex_2(file_path))
print(ex_3(file_path))
print(ex_4(file_path))
print(ex_5(file_path))
print(ex_6(file_path))
print(ex_7(file_path))
print(ex_8(file_path))
print(ex_9(file_path))
print(ex_10(file_path))
