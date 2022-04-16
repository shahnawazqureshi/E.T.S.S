from logging import LogRecord
# from timetable import *
from teachers import *
from sections import * 
from courses import * 

from clashed_courses import get_clashed_courses


def get_teacher_clashes_data(timetable, reg_data):
    clashed_sections = get_clashed_courses(timetable)
    arr = [[None for i in range(5)] for j in range(5)]
    count = 0
    i = 0
    f = open("teacher_final_clashes.txt", "w")
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
                if (teachers_data[reg_data[v[lec]].teacher_id].name == teachers_data[reg_data[v[x]].teacher_id].name):
                    count += 1
                    arr[row-1][col-1].append((teachers_data[reg_data[v[lec]].teacher_id].name, 
                    courses_data[reg_data[v[lec]].course_id].name, 
                    sections_data[reg_data[v[lec]].section_id].name,
                    courses_data[reg_data[v[x]].course_id].name, 
                    sections_data[reg_data[v[x]].section_id].name))

                    f.write(str(count) + ": " + k + "\n" + teachers_data[reg_data[v[lec]].teacher_id].name + 
                    "\n" + courses_data[reg_data[v[lec]].course_id].name + "\t" + 
                    sections_data[reg_data[v[lec]].section_id].name + "\n" + 
                    courses_data[reg_data[v[x]].course_id].name + "\t" + 
                    sections_data[reg_data[v[x]].section_id].name + "\n")

                # if (sections[v[x]].instructor == sections[v[lec]].instructor):
                #     count += 1
                #     arr[row-1][col-1].append((sections[v[lec]].instructor, 
                #     sections[v[lec]].course, sections[v[lec]].section,
                #     sections[v[x]].course, sections[v[x]].section))

                #     f.write(str(count) + ": " + k + "\n" + sections[v[lec]].instructor + 
                #     "\n" + sections[v[lec]].course + "\t" + sections[v[lec]].section + "\n" + 
                #     sections[v[x]].course + "\t" + sections[v[x]].section + "\n")

                    # print(sections[v[lec]].id, " ", sections[v[lec]].instructor, " ", sections[v[lec]].course, " ", sections[v[lec]].section, " ",
                    # sections[v[x]].id, " ", sections[v[x]].instructor, " ", sections[v[x]].course, " ", sections[v[x]].section)
            

            # # for student in sections[v[lec]].students:
            #     for x in range(lec + 1, size_of_classes):
            #         for z in sections[v[x]].students:
            #             if (student == z):
            #                 count += 1
            #                 arr[row-1][col-1].append((student, sections[v[lec]].course, sections[v[lec]].section,
            #                 sections[v[x]].course, sections[v[x]].section))
                            
        i += 1
    f.close()
    return arr, count

def get_teacher_clashes_count(timetable, reg_data):
    clashed_sections = get_clashed_courses(timetable)
    count = 0
    i = 0
    for _, v in clashed_sections.items():
        size_of_classes = len(v)
        for lec in range(0, size_of_classes):
            for x in range(lec + 1, size_of_classes):
                # print(sections[v[x]].course, " ", sections[v[x]].section, " ", sections[v[x]].instructor)
                # print(sections[v[lec]].course, " ", sections[v[lec]].section, " ", sections[v[lec]].instructor)
                # print()
                if (teachers_data[reg_data[v[lec]].teacher_id].name == teachers_data[reg_data[v[x]].teacher_id].name):
                    count += 1
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
    
    return count


def get_courses_with_teacher_clashes(timetable, reg_data):
    clashed_sections = get_clashed_courses(timetable)
    count = 0
    courses_list = []
    for _, v in clashed_sections.items():
        size_of_classes = len(v)
        for lec in range(0, size_of_classes):
            for x in range(lec + 1, size_of_classes):    
                if (teachers_data[reg_data[v[lec]].teacher_id].name == teachers_data[reg_data[v[x]].teacher_id].name):
                    courses_list.append(v[lec])
                    courses_list.append(v[x])
           
    
    return courses_list