import mysql.connector as mc


class Database:
    def __init__(self):
        try:
            self.db = mc.connect(host="localhost", user="root", password="", database="timetable_manager")
        except mc.Error as e:
            print("Error")

    def get_all_rooms(self):
        sql = "select room_id, room_name, room_type, room_for from tbl_room"
        c = self.db.cursor() 
        c.execute(sql)
        return c.fetchall()

    def get_all_courses(self):
        sql = "select course_id, course_name, course_code, course_type from tbl_course"
        c = self.db.cursor() 
        c.execute(sql)
        return c.fetchall()

    def get_all_sections(self):
        sql = "select section_id, section_name from tbl_section"
        c = self.db.cursor() 
        c.execute(sql)
        return c.fetchall()

    def get_all_teachers(self):
        sql = "select teacher_id, teacher_name from tbl_teacher"
        c = self.db.cursor() 
        c.execute(sql)
        return c.fetchall()

    def get_all_registered_courses(self):
        sql = "select registered_id, section_id, course_id, teacher_id from tbl_registered_courses"
        c = self.db.cursor() 
        c.execute(sql)
        return c.fetchall()

    def get_all_students(self):
        sql = "select registered_id, roll_number from tbl_section_students"
        c = self.db.cursor() 
        c.execute(sql)
        return c.fetchall()

    def delete_timetable(self):
        sql = "delete from tbl_timetable"
        c = self.db.cursor()
        c.execute(sql)
        self.db.commit()
        return True

    def insert_reg_course_timetable(self, reg_id, day, slot, room):
        sql = "Insert into tbl_timetable (registered_id, day, slot, room) VALUES (%s, %s, %s, %s)"
        val = (reg_id, day, slot, 7)
        c = self.db.cursor()
        c.execute(sql, val)
        self.db.commit()


db = Database() 