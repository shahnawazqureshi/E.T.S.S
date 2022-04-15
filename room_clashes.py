from logging import LogRecord
from timetable import *
from courses import courses_data
from sections import sections_data
from rooms import rooms_data
from clashed_courses import get_clashed_rooms


# def get_room_clashes():
#     arr = [[None for i in range(5)] for j in range(5)]
#     clashed_sections = get_clashed_rooms()
#     count = 0
#     i = 0
#     for k, v in clashed_sections.items():
#         row = int(k[0])
#         col = int(k[2])
#         arr[row-1][col-1] = []
#         size_of_classes = len(v)
#         for lec in range(0, size_of_classes):
#             for x in range(lec + 1, size_of_classes):
#                 if (v[lec][2] == v[x][2]):
#                     count += 1
#                     arr[row-1][col-1].append((v[x][3],v[x][0], v[x][1], v[lec][0], v[lec][1]))
#                     # print(k, ": ", v[lec])
#                     # print(k, ": ", v[x])
#                     # print()
           
#         i += 1
    
#     return arr, count

def get_room_clashes_count(timetable, reg_data):
    clashed_sections = get_clashed_rooms(timetable)
    count = 0
    i = 0
    # f = open("room_final_clashes.txt", "w")
    # for k, v in clashed_sections.items():
    #     for lec in v: 
    #         print(k, "\t", lec, "\t", timetable[lec[0]])
    for k, v in clashed_sections.items():
        row = int(k[0])
        col = int(k[2])
        size_of_classes = len(v)
        for lec in range(0, size_of_classes):
            for x in range(lec + 1, size_of_classes):
                if (v[lec][1] == v[x][1]):
                    count += 1
    return count
                


def get_room_clashes_data(timetable, reg_data):
    clashed_sections = get_clashed_rooms(timetable)
    arr = [[None for i in range(5)] for j in range(5)]
    count = 1
    i = 0
    f = open("room_final_clashes.txt", "w")
    # for k, v in clashed_sections.items():
        # for lec in v: 
        #     print(k, "\t", lec, "\t", timetable[lec[0]])
    for k, v in clashed_sections.items():
        row = int(k[0])
        col = int(k[2])
        arr[row-1][col-1] = []
        size_of_classes = len(v)
        for lec in range(0, size_of_classes):
            for x in range(lec + 1, size_of_classes):
                if (v[lec][1] == v[x][1]):
                   
                    # print(v[lec][1], " ", v[x][1])
                    f.write("Clash #" + str(count) + "\t" + k + "\n" + v[lec][1])
                    f.write("\n" + courses_data[reg_data[v[lec][0]].course_id].name + "\t" + sections_data[reg_data[v[lec][0]].section_id].name)
                    f.write("\n" + courses_data[reg_data[v[x][0]].course_id].name + "\t" + sections_data[reg_data[v[x][0]].section_id].name + "\n\n")

                    # print((v[lec][1], 
                    # courses_data[reg_data[v[lec][0]].course_id].name, 
                    # sections_data[reg_data[v[lec][0]].section_id].name, 
                    # courses_data[reg_data[v[x][0]].course_id].name,
                    # sections_data[reg_data[v[x][0]].section_id].name))

                    # print("Clash # ", count, "\t - ", row, " ", col)
                    # print(rooms_data[v[lec][1]].name, " ", rooms_data[v[x][1]].name)
                    # print(courses_data[reg_data[v[lec][0]].course_id].name, "\t", 
                    # sections_data[reg_data[v[lec][0]].section_id].name)

                    # print(courses_data[reg_data[v[x][0]].course_id].name, "\t", 
                    # sections_data[reg_data[v[x][0]].section_id].name)

                    count += 1
    return arr, count




# def get_room_clashes():
#     arr = [[None for i in range(5)] for j in range(5)]
#     clashed_sections = get_clashed_rooms()
#     count = 0
#     i = 0
#     for k, v in clashed_sections.items():
#         row = int(k[0])
#         col = int(k[2])
#         arr[row-1][col-1] = []
#         size_of_classes = len(v)
#         for lec in range(0, size_of_classes):
#             for x in range(lec + 1, size_of_classes):
#                 if (v[lec][2] == v[x][2]):
#                     count += 1
#                     arr[row-1][col-1].append((v[x][3],v[x][0], v[x][1], v[lec][0], v[lec][1]))
#                     # print(k, ": ", v[lec])
#                     # print(k, ": ", v[x])
#                     # print()
           
#         i += 1
    
#     return arr, count
