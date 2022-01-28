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