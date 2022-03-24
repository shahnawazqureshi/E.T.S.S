import db
from courses import *
class Room:
    def __init__(self, id, name, type, department, db_id):
        self.id = id
        self.name = name 
        self.type = type
        self.department = department 
        self.db_id = db_id
        self.room_binary = bin(int(id))[2:].zfill(8)
        def __repr__(self) -> str:
            return f'{self.id} {self.name} {self.type} {self.department}'


temp = db.db.get_all_rooms()
rooms_data = []
count = 0
for data in temp:
    room = Room(count, data[1], data[2], data[3], data[0])
    rooms_data.append(room)
    count += 1

# for data in rooms_data: 
#     print(data.id, "\t", data.name, "\t", data.department, "\t", data.type)


def assign_rooms(best_solution, reg_data):
    total_slots = {}
    for day in range(1, 6):
        for slot in range(1, 6):
            total_slots[str(day) + str(slot)] = []
    for lec in best_solution:
        if (courses_data[reg_data[lec.id].course_id].type == "Course"):
            for slot in lec.slots:
                for room in rooms_data:
                    if (room.type == "Course" 
                    and courses_data[reg_data[lec.id].course_id].course_for == room.department):
                        if (room.id not in total_slots[str(slot.day)+str(slot.slot)]):
                            slot.room = room.name
                            total_slots[str(slot.day)+str(slot.slot)].append(room.id)
                            break
        else:
            fh = False
            for room in rooms_data:
                if (room.type == "Lab" and 
                courses_data[reg_data[lec.id].course_id].course_for == room.department):
                    if (room.id not in total_slots[str(lec.slots[0].day)+str(lec.slots[0].slot)] and 
                    room.id not in total_slots[str(lec.slots[1].day)+str(lec.slots[1].slot)]):
                        lec.slots[0].room = room.name
                        lec.slots[1].room = room.name 
                        total_slots[str(lec.slots[0].day)+str(lec.slots[0].slot)].append(room.id)
                        total_slots[str(lec.slots[1].day)+str(lec.slots[1].slot)].append(room.id)
                        fh = True
                        break
            if (fh == False):
                for room in rooms_data:
                    if (room.type == "Lab" and 
                    courses_data[reg_data[lec.id].course_id].course_for == room.department):
                        lec.slots[0].room = room.name
                        lec.slots[1].room = room.name 
                        total_slots[str(lec.slots[0].day)+str(lec.slots[0].slot)].append(room.id)
                        total_slots[str(lec.slots[1].day)+str(lec.slots[1].slot)].append(room.id)
                        break

                    

    return best_solution