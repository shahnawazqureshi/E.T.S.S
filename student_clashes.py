#from timetable import *
#from population import *
from clashed_courses import get_clashed_courses
# clashed_sections = get_clashed_courses()

# for i, key in clashed_sections.items():
#     for z in key:
#         print(sections[z].course, end=" ")
#     print()
# arr = [[None for i in range(5)] for j in range(5)]
# def get_student_clashes():
    # count = 0
    # i = 0
    # for k, v in clashed_sections.items():
    #     row = int(k[0])
    #     col = int(k[2])
    #     arr[row-1][col-1] = []
    #     size_of_classes = len(v)
    #     for lec in range(0, size_of_classes):
    #         for student in sections[v[lec]].students:
    #             for x in range(lec + 1, size_of_classes):
    #                 for z in sections[v[x]].students:
    #                     if (student == z):
    #                         count += 1
    #                         arr[row-1][col-1].append((student, sections[v[lec]].course, sections[v[lec]].section,
    #                         sections[v[x]].course, sections[v[x]].section))

    #                         # print(student, " : ", k, " ", sections[v[lec]].id, " ",
    #                         #       sections[v[lec]].course, sections[v[lec]].section,
    #                         #       " ", sections[v[lec]].code, " and ",
    #                         #       sections[v[x]].id, " ", sections[v[x]].course, " ",
    #                         #       sections[v[x]].section, " ",
    #                         #       sections[v[x]].code)
    #     i += 1
    
#     return arr, count

def get_student_clashes(timetable, reg_data):
    clashed_sections = get_clashed_courses(timetable)

    count = 0
    i = 0
    for k, v in clashed_sections.items():
        size_of_classes = len(v)
        for lec in range(0, size_of_classes):
            for student in reg_data[v[lec]].students:
                for x in range(lec + 1, size_of_classes):
                    for z in reg_data[v[x]].students:
                        if (student == z):
                            count += 1

                            # print(student, " : ", k, " ", sections[v[lec]].id, " ",
                            #       sections[v[lec]].course, sections[v[lec]].section,
                            #       " ", sections[v[lec]].code, " and ",
                            #       sections[v[x]].id, " ", sections[v[x]].course, " ",
                            #       sections[v[x]].section, " ",
                            #       sections[v[x]].code)
        i += 1
    return count
    
