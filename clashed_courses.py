from timetable import *

def get_clashed_courses():
    clashed_sections = {}
    for day in range(1, 6):
        for slot in range(1, 6):
            clashed_sections[str(day) + " " + str(slot)] = []
            for i in timetable:
                for s in i.slots:
                    if s.day == day and s.slot == slot:
                        for j in range(0, len(sections)):
                            if (sections[j].id == i.id):
                                clashed_sections[str(day) + " " + str(slot)].append(j)
                                break
    return clashed_sections


def get_clashed_rooms():
    mycursor = DB.cursor()
    clashed_sections = {}
    for day in range(1, 6):
        for slot in range(1, 6):
            clashed_sections[str(day) + " " + str(slot)] = []
            for i in timetable:
                for s in i.slots:
                    if s.day == day and s.slot == slot:
                        for row in sections:
                            if (row.id == i.id):
                                sql = "select room_name from tbl_room where room_id = %s"
                                val = (int(s.room), )
                                mycursor.execute(sql, val)
                                room_name=""
                                for v in mycursor.fetchall():
                                    room_name = v[0]
                                clashed_sections[str(day) + " " + str(slot)].append(
                                    (row.course, row.section, s.room, room_name))
                                break
                        
    return clashed_sections

get_clashed_rooms()