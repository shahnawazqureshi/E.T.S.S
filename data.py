import mysql.connector as mc

class section:
    def __init__(self):
        self.id = None
        self.course = ""
        self.code = ""
        self.section = ""
        self.instructor = ""
        self.students = []

sections = []

try:
    DB = mc.connect(host="localhost", user="root", password="", database="timetable_manager")
except mc.Error as e:
    print("Error")

mycursor = DB.cursor()
get_students = DB.cursor()
sql = "select r.registered_id, c.course_name, c.course_code, s.section_name, t.teacher_name"
sql += " from tbl_registered_courses r inner join tbl_course c on r.course_id = c.course_id inner join tbl_section s"
sql += " on r.section_id = s.section_id inner join tbl_teacher t on r.teacher_id = t.teacher_id"

mycursor.execute(sql)

for row in mycursor.fetchall():
    obj = section()
    obj.id = row[0]
    obj.course = row[1]
    obj.code = row[2]
    obj.section = row[3]
    obj.instructor = row[4]
    # Query to Get Students of the specific section. 
    query_for_students = "select s.roll_number from tbl_section_students s where s.registered_id = %s"
    val = (obj.id, )
    get_students.execute(query_for_students, val)
    for student in get_students.fetchall():
        obj.students.append(student[0])
    sections.append(obj)

mycursor.close()
get_students.close()
