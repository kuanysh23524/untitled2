def translateLetter(*letters):
    translation_table = {'A+': 4.3, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7,
                         'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'D-': 0.7}
    return [translation_table[letter] for letter in letters]

def translatePercentage(*percentages):
    return [translateLetter('A+', 'D', 'C-', 'A-')[int((percentage - 45) / 5)] for percentage in percentages]

def calculateGPA(*args):
    points = args[::2]
    credits = args[1::2]
    return sum([point * credit for point, credit in zip(points, credits)]) / sum(credits)




def read_grades(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file.readlines()]

def calculate_and_save_gpas(directory):
    credits = read_grades(f"{directory}/credits.txt")
    overall_gpas = []

    with open(f"{directory}/overallGPAs.txt", 'w') as result_file:
        for course in ['math', 'chemistry', 'english']:
            scores = read_grades(f"{directory}/{course}.txt")
            points = translatePercentage(*scores)
            gpa = calculateGPA(*points, *credits)
            overall_gpas.append(gpa)
            result_file.write(f"{course} GPA: {gpa:.2f}\n")

    return overall_gpas


class Student:
    def __init__(self, name, num_courses, scores):
        self.name = name
        self.num_courses = num_courses
        self.scores = scores
        self.overall_gpa = self.calculateGPA()
        self.status = self.setStatus()

    def calculateGPA(self):
        points = [self.scores[course]['score'] for course in self.scores]
        credits = [self.scores[course]['credits'] for course in self.scores]
        return sum([point * credit for point, credit in zip(points, credits)]) / sum(credits)

    def setStatus(self):
        return "Passed" if self.overall_gpa >= 1.0 else "Not Passed"

    def showGPA(self):
        print(f"{self.name}'s GPA: {self.overall_gpa:.2f}")

    def showStatus(self):
        print(f"{self.name}'s Status: {self.status}")

student_data = {'math': {'score': 4.3, 'credits': 4}, 'chemistry': {'score': 3.3, 'credits': 3},
                'english': {'score': 4.0, 'credits': 4}}
student = Student("Kuanysh Omarov", 3, student_data)
student.showGPA()
student.showStatus()

# 4 What is API? What are the use cases of API?
# Give an example with code snippets of using API with Python.
# What are the limitations of API?


# 4
# API is (Application Programming Interface) -  is a set of rules and tools that allows different software application to communicate in each other.
# And we in this case with this application programm methods in other project.
# API это в целом система при помощи которой мы дальше можем взаимодействовать между собой несколько сервисов из разных программ .
# Получается мы можем связать какую либо часть какой либо программы , и использовать его в своей программе отображая его пир желании .
# К примеру есть у меня есть мини проект на котором я притянул API видео в YouTube , и таким образом я притянул API менно видео а потом дальше
# визуально отобразил его .
# API будет делать запросы в сервер программы , из которой мы ее притянули


# 5
# Socket:
# A socket is a software endpoint that establishes communication between two computers over a network.
# It provides a bidirectional communication channel, allowing data to be sent and received.


# Варианты использования сокетов:
#
# Сеть. Сокеты имеют основополагающее значение для сетевого программирования, обеспечивая связь между устройствами.
# Приложения реального времени: используются в приложениях, требующих передачи данных в реальном времени, таких как чат-приложения или онлайн-игры.
# Передача файлов: Сокеты облегчают передачу файлов между компьютерами.
# Архитектура клиент-сервер: обычно используется в архитектурах клиент-сервер для связи между клиентами и серверами.