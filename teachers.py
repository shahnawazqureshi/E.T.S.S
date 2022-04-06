import db

class Teacher:
    def __init__(self, id, name, db_id):
        self.id = id
        self.name = name 
        self.db_id = db_id
        self.teacher_binary = bin(int(id))[2:].zfill(8)
        def __repr__(self) -> str:
            return f'{self.id} {self.name}'


class Slot_Preference:
    def __init__(self, id, teacher_id, day, slot):
        self.id = id 
        self.teacher_id = teacher_id 
        self.day = day 
        self.slot = slot
        
temp = db.db.get_all_teachers()
teachers_data = []
count = 0
for data in temp:
    course = Teacher(count, data[1], data[0])
    teachers_data.append(course)
    count += 1

# for t in teachers_data:
#     print(t.id, " ", t.name, " ", t.db_id, " ", t.teacher_binary)


temp = db.db.get_all_teacher_slot_preferences()
teachers_slot_preferences = {}
count = 0 
for data in temp:
    for teacher in teachers_data:
        if teacher.db_id == data[1]:
            teacher_id = teacher.id
            break
    slot_preference = Slot_Preference(count, teacher_id, data[2], data[3])
    if teacher_id not in teachers_slot_preferences.keys():
        teachers_slot_preferences[teacher_id] = []
    teachers_slot_preferences[teacher_id].append(slot_preference)
    count += 1 

# for k, v in teachers_slot_preferences.items():
#     print(k, "\t", teachers_data[k].name)
#     for r in v:
#         print(r.id, r.teacher_id, r.day, r.slot)


# for t in teachers_slot_preferences:
#     print(t.id, t.teacher_id, t.day, t.slot, teachers_data[t.teacher_id].name)