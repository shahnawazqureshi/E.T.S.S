from asyncore import loop
import threading
import concurrent.futures
from registered_courses import *
from time_table import *
from courses import *
from student_clashes import *
import random
import time
import copy
from numpy import random as rn
from test_sections_timetable import execute_function

crossover_probability = round(rn.uniform(low=0.3, high=1.0), 1)
mutation_probability = round(rn.uniform(low=0.0, high=0.5), 1)

class Population:
    def __init__(self, number, fitness, chromosome, t_sections):
        self.number = number
        self.fitness = fitness
        self.chromosome = chromosome
        self.t_sections = t_sections

    def __repr__(self):
        return ('(Population Number: {0}\Student Clashes: {1}\nChromosome: \n{2})\n'.format(self.number, self.fitness,
                                                                                     self.chromosome))
    



def initial_population():
    
    timetables = [] 

    for z in range(1): # 100 Solutions will be generated. 
        timetable = [] 
        generated_timetable = {} 
        t_sections = {}
        #timetables.append(generated_timetable)
        section_slots = {}
        for reg_course in reg_data:
            i = sections.sections_data[reg_course.section_id].name[:5] # Getting Section Name. 
            # Appending to Timetable Chromosome
            prev_day = 0
            if (i) not in t_sections.keys():
                t_sections[i] = []
                section_slots[i] = []
                generated_timetable[i] = [["" for i in range(5)] for j in range(5)]

            if courses.courses_data[reg_course.course_id].type == "Lab":
                day = random.randint(1, 4)
                slot = random.randint(1, 4)
                count = 0
                while ([day, slot] in section_slots[i] or [day, slot+1] in section_slots[i]):
                    day = random.randint(1, 4)
                    slot = random.randint(1, 4)
                    if (count > 500):
                        break
                    count = count + 1
                section_slots[i].append([day, slot])
                section_slots[i].append([day, slot+1])
                slots = []
                slots.append(Slot(day, slot))
                slots.append(Slot(day, slot+1))
                lecture = Timetable(reg_course.id, slots)
            else:
                continue
            timetable.append(lecture)
            t_sections[i].append([reg_course.id, slots])
        for reg_course in reg_data:
            i = sections.sections_data[reg_course.section_id].name[:5] # Getting Section Name. 
            # Appending to Timetable Chromosome
            prev_day = 0
            if (i) not in t_sections.keys():
                t_sections[i] = []
                section_slots[i] = []
                generated_timetable[i] = [["" for i in range(5)] for j in range(5)]

            if courses.courses_data[reg_course.course_id].type == "Course":
                slots = []
                for x in range(2):
                    day = random.randint(1, 5)
                    slot = random.randint(1, 5)
                    count = 0
                    while ([day, slot] in section_slots[i] or day == prev_day):
                        day = random.randint(1, 5)
                        slot = random.randint(1, 5)
                        if (count > 500):
                            break
                        count = count + 1
                    prev_day = day
                    section_slots[i].append([day, slot])
                    slots.append(Slot(day, slot))
                lecture = Timetable(reg_course.id, slots)
            else:
                continue
            timetable.append(lecture)
            t_sections[i].append([reg_course.id, slots])
        clash_count = get_student_clashes(timetable, reg_data)
        population = Population(z, clash_count, timetable, t_sections)
        timetables.append(population)
        #print(timetables)
    return timetables
 


def apply_crossover(population, length, chromosome_length):
    j = 0
    crossover_population = []
    for i in range(100):
        if random.randint(0, 100) <= crossover_probability * 100:

            # Randomly selecting two chromosomes
            first = random.randint(0, length)
            second = random.randint(0, length)
            # first, second = find_fittest(population)

            crossovered_timetable1 = [] 
            crossovered_timetable2 = []
            
            for k in range(chromosome_length):
                #print("For K: " + str(k))
                if k <= int(chromosome_length / 2):
                    #print("First K: " + str(k))
                    crossovered_timetable1.append(population[first].chromosome[k])
                    crossovered_timetable2.append(population[second].chromosome[k])
                else: 
                    #print("Second K: " + str(k))
                    crossovered_timetable1.append(population[second].chromosome[k])
                    crossovered_timetable2.append(population[first].chromosome[k])

            # new_crossovered_exams1 = apply_mutation(crossovered_exams1.copy())
            # new_crossovered_exams2 = apply_mutation(crossovered_exams2.copy())

            clash_count = get_student_clashes(crossovered_timetable1, reg_data)
            pops = Population(j, clash_count, crossovered_timetable1)
            crossover_population.append(pops)

            clash_count = get_student_clashes(crossovered_timetable2, reg_data)
            pops = Population(j + 1, clash_count, crossovered_timetable2)
            crossover_population.append(pops)

            # fitness = calculateFitness(new_crossovered_exams1, courses_data, students_data, teachers_data)
            # x, y = fitness
            # fitness = (x, (100 - y))
            # crossover_population.append(Population(j, fitness, crossovered_exams1))

            # fitness = calculateFitness(new_crossovered_exams2, courses_data, students_data, teachers_data)
            # x, y = fitness
            # fitness = (x, (100 - y))
            # crossover_population.append(Population(j + 1, fitness, crossovered_exams2))

            j += 2

    return crossover_population


# def check_fun(pop):

# execute_function(pop[0].chromosome, 0)
# print(pop[0].fitness)
# for k, v in pop[0].t_sections.items():
#     print(k, " :", v)

def apply_mutation(chromosome, t_sections, lec_index):
    # Check if course or not 
    #for index in range(0, len(t_sections)):
    #    print(t_sections[index])
    # get_section_clashes(t_sections, chromosome)
    # print(t_sections[lec_index])
    # input("")
    if (courses_data[reg_data[chromosome[0]].course_id].type == 'Course'):
        # Select the Slot (1st/2nd)
        lecture_index = random.randint(0, 1)
        #print(chromosome[1][0].day)
        # Switch the Day
        #ran_numbers = random.sample(range(0, 25), 25)
        #create all combinations of index values
        temp_ran = [[i, j]  for i in range(1, 6) for j in range(1, 6)]
        #shuffle the list
        random.shuffle(temp_ran)
        #subdivide into chunks
        ran_numbers = [temp_ran[i:i+5] for i in range(0, 5**2, 5)]
        # print(ran_numbers)
        row_loop_count = 0
        col_loop_count = 0
        while True:
            if col_loop_count > 4: 
                col_loop_count = 0
                row_loop_count += 1
            if row_loop_count > 4:                    
                break
            day_index = ran_numbers[row_loop_count][col_loop_count][0]
            while chromosome[1][(lecture_index + 1) % 2].day == day_index:
                col_loop_count += 1
                if col_loop_count > 4: 
                    col_loop_count = 0
                    row_loop_count += 1
                if row_loop_count > 4:
                    break
                day_index = ran_numbers[row_loop_count][col_loop_count][0]
            if row_loop_count > 4:
                break
            slot_index = ran_numbers[row_loop_count][col_loop_count][1]
            temp = copy.deepcopy(chromosome)
            temp[1][lecture_index].day = day_index
            temp[1][lecture_index].slot = slot_index
            if (get_section_clashes_course(t_sections, temp, reg_data, lecture_index)):
                # print(courses_data[reg_data[chromosome[0]].course_id].name, " ", 
                # temp[1][lecture_index].day, " ", temp[1][lecture_index].slot)
                t_sections[lec_index] = temp
                print("Modified: ", temp)
                break
            col_loop_count += 1
            # print(loop_count)
    else:
        temp_ran = [[i, j]  for i in range(1, 6) for j in range(1, 5)]
        random.shuffle(temp_ran)
        loop_count = 0 
        while True: 
            if loop_count > 19:
                break 
            day = temp_ran[loop_count][0]
            slot = temp_ran[loop_count][1]
            temp = copy.deepcopy(chromosome)
            temp[1][0].day = day 
            temp[1][0].slot = slot 
            temp[1][1].day = day 
            temp[1][1].slot = slot + 1
            if (get_section_clashes_lab(t_sections, temp, reg_data, 0) and get_section_clashes_lab(t_sections, temp, reg_data, 1)):
                # print(courses_data[reg_data[chromosome[0]].course_id].name, " ", 
                # temp[1][lecture_index].day, " ", temp[1][lecture_index].slot)
                t_sections[lec_index] = temp
                print("Modified: ", temp)
                break
            loop_count += 1

    # print(loop_count)
    # input("Input: ")
    return t_sections






chr = {}
li = []
all_sections = []
best_solution = None
pop = initial_population()

# for reg_course in reg_data:
#         i = sections.sections_data[reg_course.section_id].name[:5] # Getting Section Name. 
#         if (i) not in all_sections:
#             all_sections.append(i)

# chr[all_sections[23]] = pop[0].t_sections[all_sections[23]]
# for k in chr[all_sections[23]]:
#     print(k)
# execute_function(pop[0].chromosome, 0)
# print(pop[0].fitness)
# for index in range(0, len(chr[all_sections[23]])):
#     chr[all_sections[23]] = apply_mutation(chr[all_sections[23]][index], chr[all_sections[23]], index)
#     #print(chr[all_sections[0]][index])
#     li.append(Timetable(chr[all_sections[23]][index][0], chr[all_sections[23]][index][1]))

# # print(chr[all_sections[0]])
# # print(li)
# pop[0].t_sections[all_sections[23]] = chr[all_sections[23]]
# print(get_student_clashes(pop[0].chromosome, reg_data))
# execute_function(pop[0].chromosome, 1)




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
                        temp_timetable = copy.deepcopy(best_solution)
                        if (i != temp_timetable[index].slots[(slot + 1) % 2].day):
                            #if (temp_timetable[index].slots[slot].day) is not i and (temp_timetable[index].slots[slot].slot is not j):
                            temp_timetable[index].slots[slot].day = i
                            temp_timetable[index].slots[slot].slot = j
                            fitness_value = get_student_clashes(temp_timetable, reg_data)
                            # print("i: ", i, "\tj: ", j, "\t", fitness_value)
                            if (fitness_value < best_fitness):
                                best_solution = copy.deepcopy(temp_timetable)
                                best_fitness = fitness_value
                                changed_course = courses_data[reg_data[pop[0].chromosome[index].id].course_id].name
                                changed_section = sections_data[reg_data[pop[0].chromosome[index].id].section_id].name
    else: 
        # print("Lab\tCount: ", count, "\tCourse Index: ", index)
        for i in range(1, 6):
            for j in range(1, 5):
                temp_timetable = copy.deepcopy(best_solution)
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
                    print("FITNESS VALUE: ", best_fitness)
    return (best_solution, best_fitness, changed_course, changed_section)
    # print("-----------------Iteration #", count, " ----------------------")
    # for index in range(0, len(pop[0].chromosome)):
    #     if courses_data[reg_data[pop[0].chromosome[index].id].course_id].type == "Course":
    #         # print("Course\tCount: ", count, "\tCourse Index: ", index)
    #         for slot in range(0, 2):
    #             for i in range(1, 6):
    #                 for j in range(1, 6):
    #                     temp_timetable = copy.deepcopy(pop[0].chromosome)
    #                     #if (temp_timetable[index].slots[slot].day) is not i and (temp_timetable[index].slots[slot].slot is not j):
    #                     temp_timetable[index].slots[slot].day = i
    #                     temp_timetable[index].slots[slot].slot = j
    #                     fitness_value = get_student_clashes(temp_timetable, reg_data)
    #                     # print("i: ", i, "\tj: ", j, "\t", fitness_value)
    #                     if (fitness_value < best_fitness):
    #                         best_solution = copy.deepcopy(temp_timetable)
    #                         best_fitness = fitness_value
    #                         changed_course = courses_data[reg_data[pop[0].chromosome[index].id].course_id].name
    #                         changed_section = sections_data[reg_data[pop[0].chromosome[index].id].section_id].name
    #                         fh = True
    #     else: 
    #         # print("Lab\tCount: ", count, "\tCourse Index: ", index)
    #         for i in range(1, 6):
    #             for j in range(1, 5):
    #                 temp_timetable = copy.deepcopy(pop[0].chromosome)
    #                 # if (temp_timetable[index].slots[0].day) is not i and (temp_timetable[index].slots[0].slot is not j):
    #                 temp_timetable[index].slots[0].day = i
    #                 temp_timetable[index].slots[0].slot = j
    #                 temp_timetable[index].slots[1].day = i
    #                 temp_timetable[index].slots[1].slot = j+1
    #                 fitness_value = get_student_clashes(temp_timetable, reg_data)
    #                 # print("i: ", i, "\tj: ", j, "\t", fitness_value)
    #                 if (fitness_value < best_fitness):
    #                     best_solution = copy.deepcopy(temp_timetable)
    #                     best_fitness = fitness_value
    #                     changed_course = courses_data[reg_data[pop[0].chromosome[index].id].course_id].name
    #                     changed_section = sections_data[reg_data[pop[0].chromosome[index].id].section_id].name
    #                     print("FITNESS VALUE: ", best_fitness)
    #                     fh = True
    # stop = time.perf_counter()                
    # print("Fitness Value Changed to: ", best_fitness)
    # print(changed_course, " \t", changed_section, "\t is changed")
    # print("Finished this Step in ", ((round(stop-start), 2)), " seconds.")
# fh = True 
# count = 0
# while fh == True:
#     start = time.perf_counter()
#     pop[0].chromosome = copy.deepcopy(best_solution)
#     fh = False
#     count += 1
#     print("-----------------Iteration #", count, " ----------------------")
#     for index in range(0, len(pop[0].chromosome)):
#         if courses_data[reg_data[pop[0].chromosome[index].id].course_id].type == "Course":
#             # print("Course\tCount: ", count, "\tCourse Index: ", index)
#             for slot in range(0, 2):
#                 for i in range(1, 6):
#                     for j in range(1, 6):
#                         temp_timetable = copy.deepcopy(pop[0].chromosome)
#                         #if (temp_timetable[index].slots[slot].day) is not i and (temp_timetable[index].slots[slot].slot is not j):
#                         temp_timetable[index].slots[slot].day = i
#                         temp_timetable[index].slots[slot].slot = j
#                         fitness_value = get_student_clashes(temp_timetable, reg_data)
#                         # print("i: ", i, "\tj: ", j, "\t", fitness_value)
#                         if (fitness_value < best_fitness):
#                             best_solution = copy.deepcopy(temp_timetable)
#                             best_fitness = fitness_value
#                             changed_course = courses_data[reg_data[pop[0].chromosome[index].id].course_id].name
#                             changed_section = sections_data[reg_data[pop[0].chromosome[index].id].section_id].name
#                             fh = True
#         else: 
#             # print("Lab\tCount: ", count, "\tCourse Index: ", index)
#             for i in range(1, 6):
#                 for j in range(1, 5):
#                     temp_timetable = copy.deepcopy(pop[0].chromosome)
#                     # if (temp_timetable[index].slots[0].day) is not i and (temp_timetable[index].slots[0].slot is not j):
#                     temp_timetable[index].slots[0].day = i
#                     temp_timetable[index].slots[0].slot = j
#                     temp_timetable[index].slots[1].day = i
#                     temp_timetable[index].slots[1].slot = j+1
#                     fitness_value = get_student_clashes(temp_timetable, reg_data)
#                     # print("i: ", i, "\tj: ", j, "\t", fitness_value)
#                     if (fitness_value < best_fitness):
#                         best_solution = copy.deepcopy(temp_timetable)
#                         best_fitness = fitness_value
#                         changed_course = courses_data[reg_data[pop[0].chromosome[index].id].course_id].name
#                         changed_section = sections_data[reg_data[pop[0].chromosome[index].id].section_id].name
#                         print("FITNESS VALUE: ", best_fitness)
#                         fh = True
#     stop = time.perf_counter()                
#     print("Fitness Value Changed to: ", best_fitness)
#     print(changed_course, " \t", changed_section, "\t is changed")
#     print("Finished this Step in ", ((round(stop-start), 2)), " seconds.")

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
    

        # for row in range(0, 4):
        #     results.append(executor.submit(Hill_Climbing(row, pop[0].chromosome, reg_data, pop[0].fitness)))

        # for f in concurrent.futures.as_completed(results):
        #     print(f)

# allThreads = []
# for row in range(0, len(pop[0].chromosome)):
#     thread = threading.Thread(target=Hill_Climbing, args=(row, pop[0].chromosome))
#     allThreads.append(thread)
#     thread.start()

# for thread in allThreads:
#     thread.join()

# for x in solutions:
#     print("SOLUTION STARTS HERE")
#     print(x)

# print(pop[0].fitness)
# get_student_clashes(best_solution, reg_data)
# execute_function(best_solution, "_Hill_Climbing")

if __name__ == "__main__":
    for reg_course in reg_data:
        i = sections.sections_data[reg_course.section_id].name[:5] # Getting Section Name. 
        if (i) not in all_sections:
            all_sections.append(i)

    
    best_solution = copy.deepcopy(pop[0].chromosome)
    print("Actual Fitness Value: ", pop[0].fitness)
    best_solution, best_fitness = main_fun(best_solution, pop[0].fitness)
    print("\n--------------------------------------\n")
    print("All Done!!!")
    print("Final Fitness Value: ", best_fitness)