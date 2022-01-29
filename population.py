from registered_courses import *
from time_table import *
from student_clashes import *
import random

class Population:
    def __init__(self, number, fitness, chromosome):
        self.number = number
        self.fitness = fitness
        self.chromosome = chromosome

    def __repr__(self):
        return ('(Population Number: {0}\Student Clashes: {1}\nChromosome: \n{2})\n'.format(self.number, self.fitness,
                                                                                     self.chromosome))



def initial_population():
    
    timetables = [] 

    for z in range(100): # 100 Solutions will be generated. 
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
        clash_count = get_student_clashes(timetable, reg_data)
        population = Population(z, clash_count, timetable)
        timetables.append(population)
        #print(timetables)
    return timetables
 
pop = initial_population()
pop.sort(key=lambda x: x.fitness, reverse=False)
# f = open("damn_man.txt", "w")
# f.write(str(pop))
