from logging import LogRecord
from timetable import *
from clashed_courses import get_clashed_rooms


def get_room_clashes():
    arr = [[None for i in range(5)] for j in range(5)]
    clashed_sections = get_clashed_rooms()
    count = 0
    i = 0
    for k, v in clashed_sections.items():
        row = int(k[0])
        col = int(k[2])
        arr[row-1][col-1] = []
        size_of_classes = len(v)
        for lec in range(0, size_of_classes):
            for x in range(lec + 1, size_of_classes):
                if (v[lec][2] == v[x][2]):
                    count += 1
                    arr[row-1][col-1].append((v[x][3],v[x][0], v[x][1], v[lec][0], v[lec][1]))
                    # print(k, ": ", v[lec])
                    # print(k, ": ", v[x])
                    # print()
           
        i += 1
    
    return arr, count



def get_room_clashes():
    arr = [[None for i in range(5)] for j in range(5)]
    clashed_sections = get_clashed_rooms()
    count = 0
    i = 0
    for k, v in clashed_sections.items():
        row = int(k[0])
        col = int(k[2])
        arr[row-1][col-1] = []
        size_of_classes = len(v)
        for lec in range(0, size_of_classes):
            for x in range(lec + 1, size_of_classes):
                if (v[lec][2] == v[x][2]):
                    count += 1
                    arr[row-1][col-1].append((v[x][3],v[x][0], v[x][1], v[lec][0], v[lec][1]))
                    # print(k, ": ", v[lec])
                    # print(k, ": ", v[x])
                    # print()
           
        i += 1
    
    return arr, count
