import db
from courses import *
from teachers import * 
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

class Room_Preference:
    def __init__(self, id, teacher_id, room_id):
        self.id = id 
        self.teacher_id = teacher_id 
        self.room_id = room_id

temp = db.db.get_all_rooms()
rooms_data = []
count = 0
for data in temp:
    room = Room(count, data[1], data[2], data[3], data[0])
    rooms_data.append(room)
    count += 1

# for data in rooms_data: 
#     print(data.id, "\t", data.name, "\t", data.department, "\t", data.type)



temp = db.db.get_all_teacher_room_preferences()
teachers_room_preferences = {}
rooms_preference_count = {} 
count = 0 
for data in temp:
    for teacher in teachers_data:
        if teacher.db_id == data[1]:
            teacher_id = teacher.id
            break
    for room in rooms_data:
        if room.db_id == data[2]:
            room_id = room.id
    room_preference = Room_Preference(count, teacher_id, room_id)
    if teacher_id not in teachers_room_preferences.keys():
        teachers_room_preferences[teacher_id] = []
    teachers_room_preferences[teacher_id].append(room_preference)
    
    # Adding the Room to Room Preference Count
    if room_id not in rooms_preference_count.keys():
        rooms_preference_count[room_id] = 2
    else:
        rooms_preference_count[room_id] += 2

    count += 1 


def get_sorted_preferences(teachers_dictionary, rooms_preferences):
    result = {} 
    for v in teachers_dictionary:
        if rooms_preferences[v.room_id] > 0:
            result[v.room_id] = rooms_preferences[v.room_id]
    return dict(sorted(result.items(), key=lambda item: item[1], reverse=True))


def assign_rooms(best_solution, reg_data):
    total_slots = {}
    # cc = 0
    # # for rr in teachers_data:
    # #     print(cc, "\t", rr.name)
    # #     cc += 1
    # result = get_sorted_preferences(teachers_room_preferences[16], rooms_preference_count)
    # print("\n", teachers_data[16].name)
    # for k, v in result.items():
    #     print(k, " :\t", v, "\t", rooms_data[k].name)
    for day in range(1, 6):
        for slot in range(1, 6):
            total_slots[str(day) + str(slot)] = []

    for lec in best_solution:
        if (courses_data[reg_data[lec.id].course_id].type == "Course"):
            for slot in lec.slots:
                if reg_data[lec.id].teacher_id in teachers_room_preferences.keys():
                    preferences = get_sorted_preferences(teachers_room_preferences[reg_data[lec.id].teacher_id],
                     rooms_preference_count)
                    for room_id, preference in preferences.items():
                        if (rooms_data[room_id].type == "Course" 
                        and courses_data[reg_data[lec.id].course_id].course_for == rooms_data[room_id].department):
                            if (room_id not in total_slots[str(slot.day)+str(slot.slot)]):
                                slot.room = rooms_data[room_id].name
                                total_slots[str(slot.day)+str(slot.slot)].append(room_id)
                                preferences[room_id] -= 1 
                                rooms_preference_count[room_id] -= 1
                                # Delete the Teacher from Preferences because now he got no rooms left.
                                if (len(preferences) <= 1):
                                    if preferences[room_id] <= 0:
                                        teachers_room_preferences.pop(reg_data[lec.id].teacher_id, 'None')
                                # assigned = True
                                break
                    # for preference in teachers_room_preferences[reg_data[lec.id].teacher_id]:
                    #     if (rooms_data[preference.room_id].type == "Course" 
                    #     and courses_data[reg_data[lec.id].course_id].course_for == rooms_data[preference.room_id].department):
                    #         if (preference.room_id not in total_slots[str(slot.day)+str(slot.slot)]):
                    #             slot.room = rooms_data[preference.room_id].name
                    #             total_slots[str(slot.day)+str(slot.slot)].append(preference.room_id)
                    #             assigned = True
                    #             break
               
        else:
            # fh = False
            # assigned = False
            if reg_data[lec.id].teacher_id in teachers_room_preferences.keys():
                preferences = get_sorted_preferences(teachers_room_preferences[reg_data[lec.id].teacher_id],
                     rooms_preference_count)
                for room_id, preference in preferences.items():
                    if (rooms_data[room_id].type == "Lab" and 
                    courses_data[reg_data[lec.id].course_id].course_for 
                    == rooms_data[room_id].department):
                        if (rooms_data[room_id].id not in total_slots[str(lec.slots[0].day)+str(lec.slots[0].slot)] and 
                        rooms_data[room_id].id not in total_slots[str(lec.slots[1].day)+str(lec.slots[1].slot)]):
                            lec.slots[0].room = rooms_data[room_id].name
                            lec.slots[1].room = rooms_data[room_id].name 
                            total_slots[str(lec.slots[0].day)+str(lec.slots[0].slot)].append(rooms_data[room_id].id)
                            total_slots[str(lec.slots[1].day)+str(lec.slots[1].slot)].append(rooms_data[room_id].id)
                            # assigned = True
                            # fh = True
                            preferences[room_id] -= 1 
                            rooms_preference_count[room_id] -= 1
                            # Delete the Teacher from Preferences because now he got no rooms left.
                            if (len(preferences) <= 1):
                                if preferences[room_id] <= 0:
                                    teachers_room_preferences.pop(reg_data[lec.id].teacher_id, 'None')
                            # assigned = True
                            break
                # for preference in teachers_room_preferences[reg_data[lec.id].teacher_id]:
                    # if (rooms_data[preference.room_id].type == "Lab" and 
                    # courses_data[reg_data[lec.id].course_id].course_for == rooms_data[preference.room_id].department):
                    #     if (rooms_data[preference.room_id].id not in total_slots[str(lec.slots[0].day)+str(lec.slots[0].slot)] and 
                    #     rooms_data[preference.room_id].id not in total_slots[str(lec.slots[1].day)+str(lec.slots[1].slot)]):
                    #         lec.slots[0].room = rooms_data[preference.room_id].name
                    #         lec.slots[1].room = rooms_data[preference.room_id].name 
                    #         total_slots[str(lec.slots[0].day)+str(lec.slots[0].slot)].append(rooms_data[preference.room_id].id)
                    #         total_slots[str(lec.slots[1].day)+str(lec.slots[1].slot)].append(rooms_data[preference.room_id].id)
                    #         assigned = True
                    #         fh = True
                    #         break
            # if assigned == False:
            #     for room in rooms_data:
            #         if (room.type == "Lab" and 
            #         courses_data[reg_data[lec.id].course_id].course_for == room.department):
            #             if (room.id not in total_slots[str(lec.slots[0].day)+str(lec.slots[0].slot)] and 
            #             room.id not in total_slots[str(lec.slots[1].day)+str(lec.slots[1].slot)]):
            #                 lec.slots[0].room = room.name
            #                 lec.slots[1].room = room.name 
            #                 total_slots[str(lec.slots[0].day)+str(lec.slots[0].slot)].append(room.id)
            #                 total_slots[str(lec.slots[1].day)+str(lec.slots[1].slot)].append(room.id)
            #                 fh = True
            #                 break
                # if fh == False:
                #     for room in rooms_data:
                #         if (room.type == "Lab" and 
                #         courses_data[reg_data[lec.id].course_id].course_for == room.department):
                #             lec.slots[0].room = room.name
                #             lec.slots[1].room = room.name 
                #             total_slots[str(lec.slots[0].day)+str(lec.slots[0].slot)].append(room.id)
                #             total_slots[str(lec.slots[1].day)+str(lec.slots[1].slot)].append(room.id)
                #             break

    for lec in best_solution:
        if (courses_data[reg_data[lec.id].course_id].type == "Course"):
            for slot in lec.slots:
                if slot.room == "1":
                    for room in rooms_data:
                        if (room.type == "Course" 
                        and courses_data[reg_data[lec.id].course_id].course_for == room.department):
                            if (room.id not in total_slots[str(slot.day)+str(slot.slot)]):
                                slot.room = room.name
                                total_slots[str(slot.day)+str(slot.slot)].append(room.id)
                                break
        else:
            if lec.slots[0].room == "1":
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
                if fh == False:
                    for room in rooms_data:
                        if (room.type == "Course" and courses_data[reg_data[lec.id].course_id].course_for == "English"):
                            if (room.id not in total_slots[str(lec.slots[0].day)+str(lec.slots[0].slot)] and 
                        room.id not in total_slots[str(lec.slots[1].day)+str(lec.slots[1].slot)]):
                                lec.slots[0].room = room.name
                                lec.slots[1].room = room.name 
                                total_slots[str(lec.slots[0].day)+str(lec.slots[0].slot)].append(room.id)
                                total_slots[str(lec.slots[1].day)+str(lec.slots[1].slot)].append(room.id)
                                fh = True
                                break
                if fh == False:
                    for room in rooms_data:
                        if (room.type == "Lab" and 
                        courses_data[reg_data[lec.id].course_id].course_for == room.department):
                            lec.slots[0].room = room.name
                            lec.slots[1].room = room.name 
                            total_slots[str(lec.slots[0].day)+str(lec.slots[0].slot)].append(room.id)
                            total_slots[str(lec.slots[1].day)+str(lec.slots[1].slot)].append(room.id)
                            break


                    

    return best_solution