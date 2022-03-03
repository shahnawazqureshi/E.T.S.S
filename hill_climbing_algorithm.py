from registered_courses import *
from time_table import *
from courses import *
from student_clashes import *
import concurrent.futures
import random
import time
import copy
from test_sections_timetable import execute_function


def main_fun(best_solution, best_fitness):
    fh = True 
    total_time = 0 
    count = 1
    while fh == True: 
        fh = False
        execute_function(best_solution, count)
        print("TimeTable Generated!")
        print("-------------- ITERATION #", count, " ----------------------") 
        count += 1
        start = time.perf_counter()
        with concurrent.futures.ProcessPoolExecutor() as executor: 
            # results = [executor.submit(Hill_Climbing, ) for row in range(0, 2)]
            arguments = []
            for index in range(0, len(best_solution)):
                arguments.append((index, best_solution, reg_data, best_fitness))
            results = executor.map(Hill_Climbing, arguments)
            for chromosome, result, ch_course, ch_section in results:
                if result < best_fitness:
                    best_fitness = result 
                    best_solution = copy.deepcopy(chromosome)
                    change_in_timetable = ch_course + "\t" + ch_section
                    fh = True
        print("--------------- ITERATION OVER! -----------------")
        print(change_in_timetable, "\tis changed.")
        print("Fitness Value Changed to ", best_fitness)
        stop = time.perf_counter()
        print("Finished this Step in ", (round(((stop-start) / 60), 2)), " minutes.")
        total_time += ((stop-start) / 60)
        print("Total Time: ", round(total_time, 2), " minutes")
        
    
    return best_solution, best_fitness


def Hill_Climbing(arguments):
    index, solution, reg_data, best_fitness = arguments
    best_solution = copy.deepcopy(solution)
    changed_course = "Nothing"
    changed_section = "No Section"
    if courses_data[reg_data[pop[0].chromosome[index].id].course_id].type == "Course":
            # print("Course\tCount: ", count, "\tCourse Index: ", index)
            for slot in range(0, 2):
                for i in range(1, 6):
                    for j in range(1, 6):
                        temp_timetable = copy.deepcopy(solution)
                        if (i != temp_timetable[index].slots[(slot + 1) % 2].day):
                            #if (temp_timetable[index].slots[slot].day) is not i and (temp_timetable[index].slots[slot].slot is not j):
                            temp_timetable[index].slots[slot].day = i
                            temp_timetable[index].slots[slot].slot = j
                            fitness_value = get_student_clashes(temp_timetable, reg_data)
                            # print("i: ", i, "\tj: ", j, "\t", fitness_value)
                            if (fitness_value < best_fitness):
                                best_solution = copy.deepcopy(temp_timetable)
                                best_fitness = fitness_value
                                print("Found Better Path (through Course) --- FITNESS VALUE: ", best_fitness)
                                changed_course = courses_data[reg_data[pop[0].chromosome[index].id].course_id].name
                                changed_section = sections_data[reg_data[pop[0].chromosome[index].id].section_id].name
    else: 
        # print("Lab\tCount: ", count, "\tCourse Index: ", index)
        for i in range(1, 6):
            for j in range(1, 5):
                temp_timetable = copy.deepcopy(solution)
                # if (temp_timetable[index].slots[0].day) is not i and (temp_timetable[index].slots[0].slot is not j):
                temp_timetable[index].slots[0].day = i
                temp_timetable[index].slots[0].slot = j
                temp_timetable[index].slots[1].day = i
                temp_timetable[index].slots[1].slot = j+1
                fitness_value = get_student_clashes(temp_timetable, reg_data)
                # print("i: ", i, "\tj: ", j, "\t", fitness_value)
                if (fitness_value < best_fitness):
                    best_solution = copy.deepcopy(temp_timetable)
                    best_fitness = fitness_value
                    changed_course = courses_data[reg_data[pop[0].chromosome[index].id].course_id].name
                    changed_section = sections_data[reg_data[pop[0].chromosome[index].id].section_id].name
                    print("Found Better Path (through Lab) --- FITNESS VALUE: ", best_fitness)
    return (best_solution, best_fitness, changed_course, changed_section)