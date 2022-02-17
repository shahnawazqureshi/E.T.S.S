from distutils.util import execute
from data import * 
from timetable import * 
from registered_courses import *
from courses import *
from sections import *
from teachers import *
from typing import List
import pdfkit
from pdfkit.api import configuration
from jinja2 import FileSystemLoader, Environment
wkhtml_path = pdfkit.configuration(wkhtmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")  #by using configuration you can add path value.


def generate_data(timetable):

    sections_timetable = {}

    for i in timetable:
        sec = sections_data[reg_data[i.id].section_id].name
        sec = sec[:5]

        if (sec) not in sections_timetable.keys():
            sections_timetable[sec] = [["" for y in range(5)] for z in range(5)]

        t_course = courses_data[reg_data[i.id].course_id].name.replace(" ", "_")
        t_instructor = teachers_data[reg_data[i.id].teacher_id].name.replace(" ", "_")
        t_room = i.slots[0].room.replace(" ", "_")
        sections_timetable[sec][i.slots[0].day-1][i.slots[0].slot-1] += t_course + "@" + t_room + "@" + t_instructor + " "
        t_room = i.slots[1].room.replace(" ", "_")
        sections_timetable[sec][i.slots[1].day-1][i.slots[1].slot-1] += t_course + "@" + t_room + "@" + t_instructor + " "
    #             t_room = time.slots[0].room.replace(" ", "_")
    #             t_course = sec.course.replace(" ", "_")
    #             t_instructor = sec.instructor.replace(" ", "_")
    #             sections_timetable[i][time.slots[0].day-1][time.slots[0].slot-1] += t_course + "@" + t_room + "@" + t_instructor + " "
    #             if (len(time.slots) > 1):
    #                 t_room = time.slots[1].room.replace(" ", "_")
    #                 sections_timetable[i][time.slots[1].day-1][time.slots[1].slot-1] += t_course + "@" + t_room + "@" + t_instructor + " "
    #             #sections_timetable[i]
    return sections_timetable



def organise_input_data(elements: List[List[str]]) -> List[List]:
    """
    Organises the input data to find double courses for easier use in templates
    """
    new_elements = []
    for day in elements:
        last_course = None
        course_list = []
        index = 0
        for course in day:
            # cleanup data
            course = course.strip().replace(" ", "<hr>")
            # check if long course (and not lunch time)
            if course != "" and course == last_course and index != 3:
                course_list.remove((course, 1))
                course_list.append((course, 2))
                course_list.append(("none", 0))
            else:
                course_list.append((course.replace(" ", "<hr>"), 1))
            last_course = course
            index += 1
        new_elements.append(course_list)

    return new_elements


def generate_html(template, name: str, elements: List[List]) -> str:

    new_elements = organise_input_data(elements=elements)

    rendered = template.render(
        name=name,
        monday=new_elements[0],
        tuesday=new_elements[1],
        wednesday=new_elements[2],
        thursday=new_elements[3],
        friday=new_elements[4]
    )

    with open(f"out_{name}.html", "w+") as file:
        file.write(rendered)

    return rendered


def run(input_data):
    # Init jinja
    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader)
    template = env.get_template('template.html')

    full_text = ""
    for name, elements in input_data.items():
        full_text += generate_html(template=template, name=name, elements=elements)

    pdfkit.from_string(full_text, "Sections Timetable.pdf", configuration = wkhtml_path)



def execute_function(data):

    sections_timetable = generate_data(data)
    sections_timetable = dict(sorted(sections_timetable.items()))
    run(sections_timetable)

# execute_function()