from registered_courses import *
from time_table import *
from courses import *
from student_clashes import *
import random
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

    
all_sections = []
for reg_course in reg_data:
    i = sections.sections_data[reg_course.section_id].name[:5] # Getting Section Name. 
    if (i) not in all_sections:
        all_sections.append(i)

pop = initial_population()
execute_function(pop[0].chromosome)

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
        loop_count = 0
        while True:
            day_index = random.randint(1, 5)
            while chromosome[1][(lecture_index + 1) % 2].day == day_index:
                day_index = random.randint(1, 5)
            slot_index = random.randint(1, 5)
            temp = chromosome
            temp[1][lecture_index].day = day_index
            temp[1][lecture_index].slot = slot_index
            if (get_section_clashes(t_sections, temp)):
                t_sections[lec_index] = temp
                break
            if loop_count > 15:                    
                break
            loop_count += 1
    return t_sections

def get_section_clashes(t_section, chromosome):
    for index in range(0, len(t_section)):
        if (chromosome[0] is not t_section[index][0]):
            for x_student in reg_data[chromosome[0]].students:
                for y_student in reg_data[t_section[index][0]].students:
                    if (x_student == y_student):
                        return False
    return True
    

# chr = {}
# li = []
# chr[all_sections[0]] = pop[0].t_sections[all_sections[0]]
# print(chr[all_sections[0]])
# for index in range(0, len(chr[all_sections[0]])):
#     chr[all_sections[0]] = apply_mutation(chr[all_sections[0]][index], chr[all_sections[0]], index)
#     #print(chr[all_sections[0]][index])
#     li.append(Timetable(chr[all_sections[0]][index][0], chr[all_sections[0]][index][1]))

# print(chr[all_sections[0]])
# print(li)


# print(chr)

# print(pop[0].chromosome[0])
# print("Here")
# for k in pop:
#     for b in k.t_sections['CS-1A']:
#         print(b[0], b[1])
#         pop[0].chromosome[1] = Timetable(b[0], b[1])
# print("Here")
# print(pop[0].chromosome[1])



# arr = [1, 2, 3, 4]

# for i in range(0, len(arr)):
#     arr[i] = 6 

# for data in arr:
#     print(data)