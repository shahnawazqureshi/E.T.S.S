import db

class Section:
    def __init__(self, id, name, db_id):
        self.id = id
        self.name = name 
        self.db_id = db_id
        self.section_binary = bin(int(id))[2:].zfill(8)
        def __repr__(self) -> str:
            return f'{self.id} {self.name}'


temp = db.db.get_all_sections()
sections_data = []
count = 0
for data in temp:
    course = Section(count, data[1], data[0])
    sections_data.append(course)
    count += 1

# for s in sections_data:
#     print(s.id, " ", s.name, " ", s.db_id, " ", s.section_binary)