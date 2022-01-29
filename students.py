import db

class Student:
    def __init__(self, id, roll_number, reg_id):
        self.id = id
        self.roll_number = roll_number 
        self.reg_id = reg_id
        def __repr__(self) -> str:
            return f'{self.id} {self.roll_number}'


temp = db.db.get_all_students()
students_data = []
count = 0
for data in temp:
    student = Student(count, data[1], data[0])
    students_data.append(student)
    count += 1

# for t in teachers_data:
#     print(t.id, " ", t.name, " ", t.db_id, " ", t.teacher_binary)