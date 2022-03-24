import db

class Course:
    def __init__(self, id, name, code, type, db_id, course_for):
        self.id = id
        self.name = name 
        self.type = type
        self.code = code 
        self.db_id = db_id
        self.course_for = course_for
        self.course_binary = bin(int(id))[2:].zfill(8)
        def __repr__(self) -> str:
            return f'{self.id} {self.name} {self.type} {self.code}'


temp = db.db.get_all_courses()
courses_data = []
count = 0
for data in temp:
    course = Course(count, data[1], data[2], data[3], data[0], data[4])
    courses_data.append(course)
    count += 1

# for c in courses_data:
#     print(c.id, " ", c.name, " ", c.type, " ", c.code, " ", c.db_id, " ", c.course_binary)