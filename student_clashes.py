#from timetable import *
#from population import *
from courses import *
from sections import *
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
    # f = open("damn_man.txt", "w")
    count = 0
    for _, v in clashed_sections.items():
        size_of_classes = len(v)
        for lec in range(0, size_of_classes):
            for student in reg_data[v[lec]].students:
                for x in range(lec + 1, size_of_classes):
                    for z in reg_data[v[x]].students:
                        if (student == z):
                            
                            count += 1
                            # f.write(str(count) + " : " + student + " : " + k + "\n" + courses_data[reg_data[v[lec]].course_id].name + " " + sections_data[reg_data[v[lec]].section_id].name + " \n" + 
                            # courses_data[reg_data[v[x]].course_id].name + " " + 
                            # sections_data[reg_data[v[x]].section_id].name + " \n\n")
                            # print(student, " : ", k, " ", sections[v[lec]].id, " ",
                            #       sections[v[lec]].course, sections[v[lec]].section,
                            #       " ", sections[v[lec]].code, " and ",
                            #       sections[v[x]].id, " ", sections[v[x]].course, " ",
                            #       sections[v[x]].section, " ",
                            #       sections[v[x]].code)
                            # print(student, " : ", k, " ", sections[v[lec]].id, " ",
                            #       sections[v[lec]].course, sections[v[lec]].section,
                            #       " ", sections[v[lec]].code, " and ",
                            #       sections[v[x]].id, " ", sections[v[x]].course, " ",
                            #       sections[v[x]].section, " ",
                            #       sections[v[x]].code)
    # f.close()
    return count


def get_student_clashes_data(timetable, reg_data):
    clashed_sections = get_clashed_courses(timetable)
    f = open("student_final_clashes.txt", "w")
    count = 0
    for k, v in clashed_sections.items():
        size_of_classes = len(v)
        for lec in range(0, size_of_classes):
            for student in reg_data[v[lec]].students:
                for x in range(lec + 1, size_of_classes):
                    for z in reg_data[v[x]].students:
                        if (student == z):
                            
                            count += 1
                            f.write(str(count) + " : " + student + " : " + k + "\n" + courses_data[reg_data[v[lec]].course_id].name + " " + sections_data[reg_data[v[lec]].section_id].name + " \n" + 
                            courses_data[reg_data[v[x]].course_id].name + " " + 
                            sections_data[reg_data[v[x]].section_id].name + " \n\n")
                            # print(student, " : ", k, " ", sections[v[lec]].id, " ",
                            #       sections[v[lec]].course, sections[v[lec]].section,
                            #       " ", sections[v[lec]].code, " and ",
                            #       sections[v[x]].id, " ", sections[v[x]].course, " ",
                            #       sections[v[x]].section, " ",
                            #       sections[v[x]].code)
                            # print(student, " : ", k, " ", sections[v[lec]].id, " ",
                            #       sections[v[lec]].course, sections[v[lec]].section,
                            #       " ", sections[v[lec]].code, " and ",
                            #       sections[v[x]].id, " ", sections[v[x]].course, " ",
                            #       sections[v[x]].section, " ",
                            #       sections[v[x]].code)
    f.close()
    return count




def get_section_clashes_course(t_section, chromosome, reg_data, lec_index):
    # print("yes")
    for index in range(0, len(t_section)):
        if (chromosome[0] is not t_section[index][0]):
            for lecture_slot in range(0, 2):
                if (chromosome[1][lec_index].day == t_section[index][1][lecture_slot].day) and (chromosome[1][lec_index].slot == t_section[index][1][lecture_slot].slot):
                    for x_student in reg_data[chromosome[0]].students:
                        # print(courses_data[reg_data[chromosome[0]].course_id].name)
                        # print("For X STUDENT ----- " , x_student)
                        for y_student in reg_data[t_section[index][0]].students:
                            # print(courses_data[reg_data[t_section[index][0]].course_id].name)
                            # print("Y Student: ", y_student)
                            if (x_student == y_student):
                                return False
        else: 
            if (chromosome[1][lec_index].day == t_section[index][1][(lec_index + 1) % 2].day) and (chromosome[1][lec_index].slot == t_section[index][1][(lec_index + 1) % 2].slot):
                return False

    return True


def get_section_clashes_lab(t_section, chromosome, reg_data, lec_index):
    # print("yes")
    for index in range(0, len(t_section)):
        if (chromosome[0] is not t_section[index][0]):
            for lecture_slot in range(0, 2):
                if (chromosome[1][lec_index].day == t_section[index][1][lecture_slot].day) and (chromosome[1][lec_index].slot == t_section[index][1][lecture_slot].slot):
                    for x_student in reg_data[chromosome[0]].students:
                        # print(courses_data[reg_data[chromosome[0]].course_id].name)
                        # print("For X STUDENT ----- " , x_student)
                        for y_student in reg_data[t_section[index][0]].students:
                            # print(courses_data[reg_data[t_section[index][0]].course_id].name)
                            # print("Y Student: ", y_student)
                            if (x_student == y_student):
                                return False
        else: 
            # Making sure that the lecture is not allocated in the same slot of 2nd lecture of same course
            if (chromosome[1][lec_index].day == t_section[index][1][(lec_index + 1) % 2].day) and (chromosome[1][lec_index].slot == t_section[index][1][(lec_index + 1) % 2].slot):
                return False

    return True
    
