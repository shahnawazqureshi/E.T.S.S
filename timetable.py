from data import *

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

sql = "select registered_id, day, slot, "
sql += "(select r.room_name from tbl_room r where r.room_id = t.room) from tbl_timetable t"

mycursor = DB.cursor()
mycursor.execute(sql)

timetable_rooms = []
timetable_data = mycursor.fetchall()


for row in sections:
    list = []
    for i in timetable_data:
        if (i[0] == row.id):
            slot = Slot(i[1], i[2], i[3])
            list.append(slot)
    if list:
        timetable_rooms.append(Timetable(row.id, list))


sql = "select registered_id, day, slot, room from tbl_timetable"

mycursor = DB.cursor()
mycursor.execute(sql)

timetable = []
timetable_data = mycursor.fetchall()


for row in sections:
    list = []
    for i in timetable_data:
        if (i[0] == row.id):
            slot = Slot(i[1], i[2], i[3])
            list.append(slot)
    if list:
        timetable.append(Timetable(row.id, list))

mycursor.close()
