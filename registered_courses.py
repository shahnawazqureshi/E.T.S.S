import db
import rooms, courses, sections, teachers, students
class Registered_Course:
    def __init__(self, id, section_id, course_id, teacher_id, db_id):
        self.id = id
        self.section_id = section_id 
        self.course_id = course_id
        self.teacher_id = teacher_id
        self.db_id = db_id
        self.reg_binary = bin(int(id))[2:].zfill(8)
        self.students = []
        def __repr__(self) -> str:
            return f'{self.id} {self.section_id} {self.course_id} {self.teacher_id}'


temp = db.db.get_all_registered_courses()
reg_data = []
count = 0
for data in temp:
    for teacher in teachers.teachers_data:
        if teacher.db_id == data[3]:
            teacher_id = teacher.id 
            break
    for course in courses.courses_data:
        if course.db_id == data[2]:
            course_id = course.id 
            break
    for section in sections.sections_data:
        if section.db_id == data[1]:
            section_id = section.id 
            break
    reg_course = Registered_Course(count, section_id, course_id, teacher_id, data[0])

    for student in students.students_data:
        if data[0] == student.reg_id:
            reg_course.students.append(student.roll_number)

    reg_data.append(reg_course)
    count += 1

# for t in reg_data:
#     print(t.id, " ", t.section_id, " ", t.course_id, " ", t.teacher_id, " ", t.reg_binary)

# for t in reg_data:
#     print(t.id, " ", sections.sections_data[t.section_id].name, " ", 
#     courses.courses_data[t.course_id].name, " ", teachers.teachers_data[t.teacher_id].name, " ", t.reg_binary)

# for t in reg_data[1].students:
#     print(t)