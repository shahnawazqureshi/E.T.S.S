import copy
from registered_courses import *
from rooms_timetable import generate_rooms_timetable
from teacher_clashes import get_teacher_clashes_count, get_teacher_clashes_data
from time_table import *
from rooms import *
from room_clashes import get_room_clashes_count, get_room_clashes_data
from teacher_slot_clashes import get_teacher_slot_violations_count, get_teacher_slot_violations_data
from student_clashes import *
import random
from numpy import random as rn
import time
import concurrent.futures
from test_sections_timetable import execute_function

crossover_probability = round(rn.uniform(low=0.3, high=1.0), 1)
mutation_probability = round(rn.uniform(low=0.3, high=0.4), 1)
population_size = 300

class Population:
    def __init__(self, number, fitness, chromosome, t_sections):
        self.number = number
        self.fitness = fitness
        self.chromosome = chromosome
        self.t_sections = t_sections

    def __repr__(self):
        return ('(Population Number: {0}\Student Clashes: {1}\nChromosome: \n{2})\n'.format(self.number, self.fitness,
                                                                                     self.chromosome))
    
all_sections = []

def get_fitness(timetable):
    teacher_clashes = get_teacher_clashes_count(timetable, reg_data)
    student_clashes = get_student_clashes(timetable, reg_data)
    teacher_slot_violations = get_teacher_slot_violations_count(timetable, reg_data)
    room_clashes = get_room_clashes_count(timetable, reg_data)
    return [teacher_clashes * 5 + student_clashes * 2.5 + room_clashes * 5 + teacher_slot_violations * 0.75, 
    ("Student Clashes: " + str(student_clashes), "Teacher Clashes: " + str(teacher_clashes),
    "Room Clashes: " + str(room_clashes), "Teacher Slot Violations: " + str(teacher_slot_violations))]

def initial_population():
    
    timetables = []  

    for z in range(population_size): # 300 Solutions will be generated. 
        timetable = [] 
        #generated_timetable = {} 
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
                #generated_timetable[i] = [["" for i in range(5)] for j in range(5)]

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
                #generated_timetable[i] = [["" for i in range(5)] for j in range(5)]

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
        timetable = assign_rooms(timetable, reg_data)
        fitness = get_fitness(timetable)
        # clash_count = get_student_clashes(timetable, reg_data)
        population = Population(z, fitness, timetable, t_sections)
        timetables.append(population)
    return timetables
 

# PARENT SELECTION 
# Roulette Wheel Selection 
def parent_selection(population):
    parents = []
    total_value = 1  # Total Fitness
    for individual in population:
        total_value += individual.fitness[0]
    # Applying Roulette Wheel
    # Check Total sum value of fittest individuals
    while len(parents) < population_size:
        # Finding  probability of all chromosomes
        probability_arr = []
        for i in range(0, len(population)):
            s = (round((population[i].fitness[0] / total_value), 2), i)
            probability_arr.append(s)

        # sorting the array having the probabilities
        probability_arr.sort(key=lambda val: val[0], reverse=True)
        # Making proper probability pie chart array
        temp_prob_arr = []
        check_temp = 0
        for i in range(0, len(population)):
            prob, ind = probability_arr[i]
            temp_prob_arr.append((prob + check_temp, ind))
            check_temp += prob
        # deciding the chromosome by random number generation and probability
        random_no = round(random.uniform(0, 1), 2)
        for i in range(0, len(temp_prob_arr)):
            prob, ind = temp_prob_arr[i]
            if random_no <= prob:
                parents.append(population[ind])
                break
    return parents



def find_fittest(population):
    population.sort(key=lambda val: val.fitness[0], reverse=False)

    return population[0],population[1]


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
            crossovered_sections1 = {}
            crossovered_sections2 = {}

            for k in range(len(all_sections)):
                if k <= int(len(all_sections) / 2):
                    # Getting first half of sections from first Parent
                    crossovered_sections1[all_sections[k]] = population[first].t_sections[all_sections[k]]
                    # Applying Mutation on each Gene and appending it to new Timetable
                    for index in range(0, len(crossovered_sections1[all_sections[k]])):
                        crossovered_sections1[all_sections[k]] = apply_mutation(
                            crossovered_sections1[all_sections[k]][index],
                            crossovered_sections1[all_sections[k]], index)
                        # Appending the new Slots into the Timetable. 
                        crossovered_timetable1.append(Timetable(crossovered_sections1[all_sections[k]][index][0],
                         crossovered_sections1[all_sections[k]][index][1]))
                        
                    # Getting first half of sections from second Parent
                    crossovered_sections2[all_sections[k]] = population[second].t_sections[all_sections[k]]
                    # Applying Mutation on each Gene and appending it to new Timetable
                    for index in range(0, len(crossovered_sections2[all_sections[k]])):
                        crossovered_sections2[all_sections[k]] = apply_mutation(
                            crossovered_sections2[all_sections[k]][index],
                            crossovered_sections2[all_sections[k]], index)
                        # Appending the new Slots into the Timetable. 
                        crossovered_timetable2.append(Timetable(crossovered_sections2[all_sections[k]][index][0],
                         crossovered_sections2[all_sections[k]][index][1]))


                    # for data in population[first].t_sections[all_sections[k]]:
                    #     crossovered_timetable1.append(Timetable(data[0], data[1]))
                    # for data in population[second].t_sections[all_sections[k]]:
                    #     crossovered_timetable2.append(Timetable(data[0], data[1]))
                    # crossovered_sections2[all_sections[k]] = population[first].t_sections[all_sections[k]]
                
                # If length has exceeded half the sections
                else:

                    # Getting second half of sections from second Parent
                    crossovered_sections1[all_sections[k]] = population[second].t_sections[all_sections[k]]
                    # Applying Mutation on each Gene and appending it to new Timetable
                    for index in range(0, len(crossovered_sections1[all_sections[k]])):
                        crossovered_sections1[all_sections[k]] = apply_mutation(
                            crossovered_sections1[all_sections[k]][index],
                            crossovered_sections1[all_sections[k]], index)
                        # Appending the new Slots into the Timetable. 
                        crossovered_timetable1.append(Timetable(crossovered_sections1[all_sections[k]][index][0],
                         crossovered_sections1[all_sections[k]][index][1]))

                    
                    # Getting second half of sections from second Parent
                    crossovered_sections2[all_sections[k]] = population[first].t_sections[all_sections[k]]
                    # Applying Mutation on each Gene and appending it to new Timetable
                    for index in range(0, len(crossovered_sections2[all_sections[k]])):
                        crossovered_sections2[all_sections[k]] = apply_mutation(
                            crossovered_sections2[all_sections[k]][index],
                            crossovered_sections2[all_sections[k]], index)
                        # Appending the new Slots into the Timetable. 
                        crossovered_timetable2.append(Timetable(crossovered_sections2[all_sections[k]][index][0],
                         crossovered_sections2[all_sections[k]][index][1]))


                    # for data in population[second].t_sections[all_sections[k]]:
                    #     crossovered_timetable1.append(Timetable(data[0], data[1]))
                    # crossovered_sections2[all_sections[k]] = population[first].t_sections[all_sections[k]]
                    # for data in population[first].t_sections[all_sections[k]]:
                    #     crossovered_timetable2.append(Timetable(data[0], data[1]))
                    # crossovered_sections1[all_sections[k]] = population[first].t_sections[all_sections[k]]

            # for k in range(chromosome_length):
            #     #print("For K: " + str(k))
            #     if k <= int(chromosome_length / 2):
            #         #print("First K: " + str(k))  
            #         crossovered_timetable1.append(population[first].chromosome[k])
            #         crossovered_timetable2.append(population[second].chromosome[k])
            #     else: 
            #         #print("Second K: " + str(k))
            #         crossovered_timetable1.append(population[second].chromosome[k])
            #         crossovered_timetable2.append(population[first].chromosome[k])

            # new_crossovered_exams1 = apply_mutation(crossovered_exams1.copy())
            # new_crossovered_exams2 = apply_mutation(crossovered_exams2.copy())
            crossovered_timetable1 = assign_rooms(crossovered_timetable1, reg_data)
            fitness_value = get_fitness(crossovered_timetable1)
            pops = Population(j, fitness_value, crossovered_timetable1, crossovered_sections1)
            crossover_population.append(pops)

            crossovered_timetable2 = assign_rooms(crossovered_timetable2, reg_data)
            fitness_value = get_fitness(crossovered_timetable2)
            pops = Population(j + 1, fitness_value, crossovered_timetable2, crossovered_sections2)
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


"""-------------------------------------Mutation Function--------------------------------"""


# Apply Mutation on chromosomes , given Mutation probability
def apply_mutation(chromosome, t_sections, lec_index):
    # Check if course or not 
    #for index in range(0, len(t_sections)):
    #    print(t_sections[index])
    # get_section_clashes(t_sections, chromosome)
    # print(t_sections[lec_index])
    # input("")

    if random.randint(0, 100) <= mutation_probability * 100:

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
                    t_sections[lec_index] = copy.deepcopy(temp)
                    # print("Modified: ", temp)
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
                    t_sections[lec_index] = copy.deepcopy(temp)
                    # print("Modified: ", temp)
                    break
                loop_count += 1
        # print(loop_count)
        # input("Input: ")
    return t_sections


# def apply_mutation(chromosome):
#     # Randomly switch values(Day, Time) of a chromosome
#     if random.randint(0, 100) <= mutation_probability * 100:
#         genes = random.randint(0, 3)
#         for i in range(genes):
#             gene = random.randint(0, len(chromosome) - 1)
#             temp = random.randint(0, len(days_data) - 1)

#             # Date Switch
#             chromosome[gene].day = days_data[temp].day
#             chromosome[gene].binary_value[4] = days_data[temp].binary_val

#             # Time Switch
#             temp = random.randint(0, len(times_data) - 1)
#             chromosome[gene].time = times_data[temp].time
#             chromosome[gene].binary_value[3] = times_data[temp].binary_val

#             # Room Switch
#             temp = random.randint(0, len(rooms_data) - 1)
#             while rooms_data[temp].num in chromosome[gene].room:
#                 temp = random.randint(0, len(rooms_data) - 1)

#             temp1 = random.randint(0, len(chromosome[gene].room) - 1)
#             chromosome[gene].room[temp1] = rooms_data[temp].num
#             chromosome[gene].binary_value[1][temp1] = rooms_data[temp].binary_val

#     return chromosome


def genetic_algo():
    best_solution = None
    max_iter = 50
    population = initial_population()
    #population = parent_selection(population.copy())
    count = 0
    # regen = 0
    population.sort(key = lambda x: x.fitness[0], reverse=False)
    # f = open("Folder/population 0.txt", "w")
    # f.write(str(population))
    for i in range(max_iter):
        print("Generation " + str(i) + " going on.....")
        population1 = apply_crossover(population, (len(population) - 1), (len(population[0].chromosome)))
        population = parent_selection(copy.deepcopy(population1))
        temp_best, _ = find_fittest(copy.deepcopy(population))
        if best_solution is None:
            best_solution = temp_best 
        elif temp_best.fitness[0] < best_solution.fitness[0]:
            best_solution = temp_best 
            # regen = 1
        
        population.sort(key = lambda x: x.fitness[0], reverse=False)
        # f = open("Folder/population " + str(i+1) + ".txt", "w")
        # f.write(str(population))
        # population[0].chromosome = assign_rooms(population[0].chromosome, reg_data)
        print("Fitness: ", get_fitness(population[0].chromosome))
        execute_function(population[0].chromosome, i)
        # generate_rooms_timetable(population[0].chromosome, reg_data)

        print("Generation " + str(i) + " Done!.....")
        print("Best Solution Fitness: " + str(best_solution.fitness))
        # input("")
        # if regen > 7:
        #     print("Re-Generating Population")
        #     population1 = initial_population()
        #     population = parent_selection(population1.copy())
        #     regen = 1


        count += 1 
        # regen += 1
    return best_solution



def main_fun(best_solution, best_fitness):
    fh = True 
    total_time = 0 
    count = 51
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
                if result[0] < best_fitness[0]:
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
    if courses_data[reg_data[solution[index].id].course_id].type == "Course":
            # print("Course\tCount: ", count, "\tCourse Index: ", index)
            for slot in range(0, 2):
                for i in range(1, 6):
                    for j in range(1, 6):
                        temp_timetable = copy.deepcopy(solution)
                        if (i != temp_timetable[index].slots[(slot + 1) % 2].day):
                            #if (temp_timetable[index].slots[slot].day) is not i and (temp_timetable[index].slots[slot].slot is not j):
                            temp_timetable[index].slots[slot].day = i
                            temp_timetable[index].slots[slot].slot = j
                            temp_timetable = assign_rooms(temp_timetable, reg_data)
                            fitness_value = get_fitness(temp_timetable)
                            # fitness_value = get_student_clashes(temp_timetable, reg_data)
                            # print("i: ", i, "\tj: ", j, "\t", fitness_value)
                            if (fitness_value[0] < best_fitness[0]):
                                best_solution = copy.deepcopy(temp_timetable)
                                best_fitness = fitness_value
                                # print("Found Better Path (through Course) --- FITNESS VALUE: ", best_fitness)
                                changed_course = courses_data[reg_data[solution[index].id].course_id].name
                                changed_section = sections_data[reg_data[solution[index].id].section_id].name
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
                # fitness_value = get_student_clashes(temp_timetable, reg_data)
                temp_timetable = assign_rooms(temp_timetable, reg_data)
                fitness_value = get_fitness(temp_timetable)
                # print("i: ", i, "\tj: ", j, "\t", fitness_value)
                if (fitness_value[0] < best_fitness[0]):
                    best_solution = copy.deepcopy(temp_timetable)
                    best_fitness = fitness_value
                    changed_course = courses_data[reg_data[solution[index].id].course_id].name
                    changed_section = sections_data[reg_data[solution[index].id].section_id].name
                    # print("Found Better Path (through Lab) --- FITNESS VALUE: ", best_fitness)
    return (best_solution, best_fitness, changed_course, changed_section)






if __name__ == "__main__":
    for reg_course in reg_data:
        i = sections.sections_data[reg_course.section_id].name[:5] # Getting Section Name. 
        if (i) not in all_sections:
            all_sections.append(i)
    
    ga_solution = genetic_algo()
    
    best_solution = copy.deepcopy(ga_solution.chromosome)
    print("Genetic Algorithm's Solution's Fitness Value: ", ga_solution.fitness)
    best_solution, best_fitness = main_fun(best_solution, ga_solution.fitness)
    best_solution = assign_rooms(best_solution, reg_data)
    get_student_clashes_data(best_solution, reg_data)
    get_teacher_clashes_data(best_solution, reg_data)
    get_room_clashes_data(best_solution, reg_data)
    generate_rooms_timetable(best_solution, reg_data)
    execute_function(best_solution, 1000)

    store_new_timetable(best_solution, reg_data)
    print("\n--------------------------------------\n")
    print("All Done!!!")
    print("Final Fitness Value: ", best_fitness)