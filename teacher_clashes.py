from logging import LogRecord
from timetable import *
from clashed_courses import get_clashed_courses
clashed_sections = get_clashed_courses()


arr = [[None for i in range(5)] for j in range(5)]
def get_teacher_clashes():

    count = 0
    i = 0
    for k, v in clashed_sections.items():
        row = int(k[0])
        col = int(k[2])
        arr[row-1][col-1] = []
        size_of_classes = len(v)
        for lec in range(0, size_of_classes):
            for x in range(lec + 1, size_of_classes):
                # print(sections[v[x]].course, " ", sections[v[x]].section, " ", sections[v[x]].instructor)
                # print(sections[v[lec]].course, " ", sections[v[lec]].section, " ", sections[v[lec]].instructor)
                # print()
                if (sections[v[x]].instructor == sections[v[lec]].instructor):
                    count += 1
                    arr[row-1][col-1].append((sections[v[lec]].instructor, 
                    sections[v[lec]].course, sections[v[lec]].section,
                    sections[v[x]].course, sections[v[x]].section))
            #         print(sections[v[lec]].id, " ", sections[v[lec]].instructor, " ", sections[v[lec]].course, " ", sections[v[lec]].section, " ",
            #         sections[v[x]].id, " ", sections[v[x]].instructor, " ", sections[v[x]].course, " ", sections[v[x]].section)
            # # for student in sections[v[lec]].students:
            #     for x in range(lec + 1, size_of_classes):
            #         for z in sections[v[x]].students:
            #             if (student == z):
            #                 count += 1
            #                 arr[row-1][col-1].append((student, sections[v[lec]].course, sections[v[lec]].section,
            #                 sections[v[x]].course, sections[v[x]].section))
                            
        i += 1
    
    return arr, count

