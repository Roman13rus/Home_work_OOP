class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def lecture_grades(self, lecturer, course, grade): # оценки лекторам за лекции
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_lections:
                lecturer.grades_lections[course] += [grade]
            else:
                lecturer.grades_lections[course] = [grade]
        else:
            return 'Ошибка'
        
    def average_score_hw(self): #функция опеределения среднего балла за ДЗ для __str__
        score = []
        for grade in self.grades.keys():
            score += self.grades[grade]
        return sum(score) / len(score) 

    def __str__(self):
        result_print = f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания: {self.average_score_hw()}\n Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n Завершенные курсы: {", ".join(self.finished_courses)}'
        return result_print
    
    def __lt__(self, other): # Сравнение студентов (print реализован для наглядности, функция возвращает boolean)
        if not isinstance(self, Student) or not isinstance(other, Student) :
            print("Это не студент(ы)")
            return
        else:
            if self.average_score_hw() < other.average_score_hw():
                print (f' Студент {self.name} {self.surname} делает домашнюю работу хуже чем студент {other.name} {other.surname}')
            elif self.average_score_hw() > other.average_score_hw():
                print (f' Студент {self.name} {self.surname} делает домашнюю работу лучше чем студент {other.name} {other.surname}') 
            else:
                print (f' Студент {self.name} {self.surname} и студент {other.name} {other.surname} делают домашнюю работу одинаково')
        return self.average_score_hw() < other.average_score_hw()
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname) # создание нового атрибута класса лекторов, с наследованием остальных атрибутов от менторов
        self.grades_lections = {}

    def average_score(self): #функция опеределения среднего балла за лекции для __str__
        score = []
        for grades in self.grades_lections.keys():
            score += self.grades_lections[grades]
        return sum(score) / len(score) 
    
    def __str__(self):
        result_print = f' Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {self.average_score()}'
        return result_print

    def __lt__(self, other): # Сравнение лекторов (print реализован для наглядности, функция возвращает boolean)
        if not isinstance(self, Lecturer) or not isinstance(other, Lecturer) :
            print("Это не лекторы")
            return
        else:
            if self.average_score() < other.average_score():
                print (f' Лекции {self.name} {self.surname} нравятся студентам меньше чем лектора {other.name} {other.surname}')
            elif self.average_score() > other.average_score():
                print (f' Лекции {self.name} {self.surname} нравятся студентам больше чем лектора {other.name} {other.surname}')
            else:
                print (f' Лекции обоих преподавателей одинаково нравятся студентам')
        return self.average_score() < other.average_score()

class Reviewer(Mentor):
    def rate_hw_code(self,student, course, grade):
        self.rate_hw(student, course, grade) #наследование выставления оценок студентами ревьюэрами от менторов.

    def __str__(self):
        result_print = f' Имя: {self.name}\n Фамилия: {self.surname}'
        return result_print
first_student = Student('Ruoy', 'Eman', 'male')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Git']
first_student.finished_courses += ['Введение в программирование']
first_student.finished_courses += ['Дизайн']

second_student = Student('Roman', 'Nikolaev', 'male')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Git']
second_student.courses_in_progress += ['SQL']
second_student.finished_courses += ['Введение в программирование']

first_mentor_rev = Reviewer('Igor', 'Nikolaev')
first_mentor_rev.courses_attached += ['Python']
first_mentor_rev.courses_attached += ['Git']
first_mentor_rev.courses_attached += ['SQL']

second_mentor_rev = Reviewer('Anatoly', 'Bykov')
second_mentor_rev.courses_attached += ['Python']
second_mentor_rev.courses_attached += ['Git']
second_mentor_rev.courses_attached += ['SQL']

first_mentor_lec = Lecturer('Ivan', 'Petrov')
first_mentor_lec.courses_attached += ['Python']
first_mentor_lec.courses_attached += ['Git']
first_mentor_lec.courses_attached += ['SQL']

second_mentor_lec = Lecturer('Egor', 'Arsenev')
second_mentor_lec.courses_attached += ['Python']
second_mentor_lec.courses_attached += ['Git']
second_mentor_lec.courses_attached += ['SQL']

first_mentor_rev.rate_hw_code(first_student, 'Python', 10)
first_mentor_rev.rate_hw_code(first_student, 'Python', 8)
first_mentor_rev.rate_hw_code(first_student, 'Python', 6)
first_mentor_rev.rate_hw_code(first_student, 'Git', 9)
first_mentor_rev.rate_hw_code(first_student, 'Git', 8)
first_mentor_rev.rate_hw_code(second_student, 'SQL', 6)

second_mentor_rev.rate_hw_code(second_student, 'Python', 7)
second_mentor_rev.rate_hw_code(second_student, 'Python', 9)
second_mentor_rev.rate_hw_code(second_student, 'Python', 10)
second_mentor_rev.rate_hw_code(second_student, 'Git', 5)
second_mentor_rev.rate_hw_code(second_student, 'SQL', 8)
second_mentor_rev.rate_hw_code(first_student, 'SQL', 4)


first_student.lecture_grades(first_mentor_lec,'Python',7)
first_student.lecture_grades(first_mentor_lec,'Git',6)
first_student.lecture_grades(first_mentor_lec,'SQL',7)
first_student.lecture_grades(second_mentor_lec,'Git',6)
second_student.lecture_grades(second_mentor_lec,'Python',9)
second_student.lecture_grades(first_mentor_lec,'Git',6)
second_student.lecture_grades(first_mentor_lec,'SQL',8)
second_student.lecture_grades(second_mentor_lec,'Git',9)


print(first_student.grades)
print(second_student.grades)
print(first_mentor_lec.grades_lections)
print(second_mentor_lec.grades_lections)
print(first_student)
print(second_student)
print(first_mentor_lec)
print(second_mentor_lec)
print(first_student.__lt__(second_student))
print(first_mentor_lec.__lt__(second_mentor_lec))

# функция подсчёта среденего балла студентов в рамках курса
def calculation_score_subjects(students, kurse):
    score = []
    for student in students:
        if isinstance(student, Student) and kurse in student.courses_in_progress:
            for grade in student.grades[kurse]:
                score += [grade]
    return sum(score) / len(score) 
a = [first_student, second_student]   # пример списка на вход        
print(calculation_score_subjects(a, 'SQL'))

def calculation_score_lections(mentor_lec, kurse):
    score = []
    for mentor in mentor_lec:
        if isinstance(mentor, Lecturer) and kurse in mentor.courses_attached:
            for grade in mentor.grades_lections[kurse]:
                score += [grade]
    return sum(score) / len(score)
b = [first_mentor_lec, second_mentor_lec] # пример списка на вход
print(calculation_score_lections(b, "Python"))
