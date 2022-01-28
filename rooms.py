import db

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

# for r in rooms_data:
#     print(r.id, " ", r.name, " ", r.type, " ", r.department, " ", r.db_id)