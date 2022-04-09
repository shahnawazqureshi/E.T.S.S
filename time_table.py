from db import *
from rooms import rooms_data
class Timetable:
    def __init__(self,id,slots):
        self.id = id
        self.slots = slots
        self.binary_val = bin(int(id))[2:].zfill(8)
    def __repr__(self) -> str:
        return f'{self.id} {self.slots}'

class Slot:
    def __init__(self,day,slot,room = "1"):
        self.day  = day
        self.slot =  slot
        self.room = room
        self.day_binary = bin(int(day))[2:].zfill(8)
        #self.room_binary = bin(int(room))[2:].zfill(8)
        self.slot_binary = bin(int(slot))[2:].zfill(8)

    def __repr__(self) -> str:
        return f'{self.day} {self.slot} {self.room}'


def read_timetable(reg_data):
    timetable = []
    timetable_data = db.get_timetable()
    for reg_course in reg_data:
        list = []
        for i in timetable_data:
            if (i[0] == reg_course.id):
                for room in rooms_data: # Getting actual Room ID 
                    if room.db_id == i[3]:
                        room_id = room.id
                        break
                slot = Slot(i[1], i[2], room_id)
                list.append(slot)
        if list:
            timetable.append(Timetable(reg_course.id, list))
    return timetable


def store_new_timetable(timetable, reg_data):
    # Deleting Previous Timetable
    if db.delete_timetable():
        for reg_course in timetable:
            for slot_num in range(0, 2):
                room_id = 0
                for room in rooms_data:
                    if room.name == reg_course.slots[slot_num].room:
                        room_id = room.db_id
                        break
                    room_id = "1"
                if (room_id is not "1"):
                    db.insert_reg_course_timetable(reg_data[reg_course.id].db_id, reg_course.slots[slot_num].day,
                                            reg_course.slots[slot_num].slot, room_id)

