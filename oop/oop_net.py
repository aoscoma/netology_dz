# Исходя из квиза к предыдущему занятию, у нас уже есть класс преподавателей и класс студентов 
# (вы можете взять этот код за основу или написать свой). 
# Студентов пока оставим без изменения, а вот преподаватели бывают разные, поэтому теперь класс Mentor должен стать родительским классом, 
# а от него нужно реализовать наследование классов Lecturer (лекторы) и Reviewer (эксперты, проверяющие домашние задания). 
# Очевидно, имя, фамилия и список закрепленных курсов логично реализовать на уровне родительского класса. 
# А чем же будут специфичны дочерние классы? Об этом в следующих заданиях.


# В квизе к предыдущей лекции мы реализовали возможность выставлять студентам оценки за домашние задания. 
# Теперь это могут делать только Reviewer (реализуйте такой метод)! А что могут делать лекторы? 
# Получать оценки за лекции от студентов :) Реализуйте метод выставления оценок лекторам у класса Student 
# (оценки по 10-балльной шкале, хранятся в атрибуте-словаре у Lecturer, в котором ключи – названия курсов, а значения – списки оценок). 
# Лектор при этом должен быть закреплен за тем курсом, на который записан студент.


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
lecturer = Mentor()

reviewer = Mentor()
    def rate_hw(self, student, course, grade):
            if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка'



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
 
print(best_student.grades)
print()
