import db

class Teacher:
    def __init__(self, id, name, db_id):
        self.id = id
        self.name = name 
        self.db_id = db_id
        self.teacher_binary = bin(int(id))[2:].zfill(8)
        def __repr__(self) -> str:
            return f'{self.id} {self.name}'


temp = db.db.get_all_teachers()
teachers_data = []
count = 0
for data in temp:
    course = Teacher(count, data[1], data[0])
    teachers_data.append(course)
    count += 1

# for t in teachers_data:
#     print(t.id, " ", t.name, " ", t.db_id, " ", t.teacher_binary)