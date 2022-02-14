from registered_courses import *
from time_table import *
from student_clashes import *
import random
from numpy import random as rn

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


#def check_fun(pop):
        

pop = initial_population()

print(pop[0].chromosome[0])
print("Here")
for k in pop:
    for b in k.t_sections['CS-1A']:
        print(b[0], b[1])
        pop[0].chromosome[1] = Timetable(b[0], b[1])
print("Here")
print(pop[0].chromosome[1])

