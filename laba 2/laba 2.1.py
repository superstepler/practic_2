class Students:
    def __init__(self, surname,date_birth, group_num, acad_perf):
        self.surname = surname
        self.date_birth = date_birth
        self.group_num = group_num
        self.acad_perf = acad_perf

    def set_surname(self, surname):
        self.surname = surname
    def set_date_birth(self, date_birth):
        self.date_birth = date_birth
    def set_group_num(self, group_num):
        self.group_num = group_num
    def __str__(self):
        return f"Surname: {self.surname}, Birth date: {self.date_birth}, Group: {self.group_num}, Performance: {self.acad_perf} "

students = [Students("Klimov", "2007-02-05", 435, [2,4,5,5,5,5]),
            Students("Skulkov", "2007-09-03", 754, [4,3,2,5,4,4])]

def find_student(students):
    search_name = input("Enter surname: ")
    search_birth_date = input("Enter birth date: ")
    for student in students:
        if student.surname == search_name:
            if search_birth_date == search_birth_date:
                return student

def add_student(students):
    surname = input("Enter surname: ")
    date_birth = input("Enter birth date: ")
    group_num = int(input("Enter number group: "))
    acad_perf_1 = input("Enter academic performance: ")
    acad_perf = [int(i.strip()) for i in acad_perf_1.split(",")]
    new_student = Students(surname, date_birth, group_num, acad_perf)
    students.append(new_student)

while True:
    Choice = input("1 - student search, 2 - add student , 3 - Exit: ")
    if Choice == "1":
        student_search = find_student(students)
        print(f"found student: {student_search}")

    elif Choice == "2":
        add_student(students)

    elif Choice == "3":
        break





