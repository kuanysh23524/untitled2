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
    credits_path = input("Enter the path to credits file: ")
    credits = read_grades(credits_path)
    overall_gpas = []

    with open(f"{directory}/overallGPAs.txt", 'w') as result_file:
        for course in ['math', 'chemistry', 'english']:
            course_path = input(f"Enter the path to {course} file: ")
            scores = read_grades(course_path)
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

# Get user input for file paths
directory_path = input("Enter the directory path: ")
calculate_and_save_gpas(directory_path)

# Example of creating a student with data
student_data = {'math': {'score': 4.3, 'credits': 4}, 'chemistry': {'score': 3.3, 'credits': 3},
                'english': {'score': 4.0, 'credits': 4}}
student = Student("Kuanysh Omarov", 3, student_data)
student.showGPA()
student.showStatus()
