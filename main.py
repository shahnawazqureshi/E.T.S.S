## IMPORTS
import sys
import os
from PyQt5.sip import delete
from PySide2 import shiboken2
# import iconify as ico
from iconify.qt import QtGui as IconQtGui, QtWidgets as IconQtWidgets
import PySide2
import mysql.connector as mc
from qt_material import *
from PyQt5 import QtWidgets, uic, QtGui
from functools import partial
from PyQt5.QtCore import Qt
from registered_courses import reg_data
from add_section_page import Ui_Add_Section_Window
from edit_section_page import Ui_Edit_Section_Window
from add_course_page import Ui_Add_Course_Window
from edit_course_page import Ui_Edit_Course_Window
from add_room_page import Ui_Add_Room_Window
from edit_room_page import Ui_Edit_Room_Window
from add_teacher_page import Ui_Add_Teacher_Window
from edit_teacher_page import Ui_Edit_Teacher_Window
from add_registered_course import Ui_Add_Registered_Course_Window
from edit_registered_course import Ui_Edit_Registered_Course_Window
from registered_section_student_details import Ui_Registered_Section_Students_Window
from add_section_student_page import Ui_Add_Section_Student_Window
from add_room_preferences import Ui_Add_Room_Preferences_Teacher_Window 
from add_slot_preferences import Ui_Add_Slot_PReferences_Teacher_Window
import sections_timetable
import rooms_timetable
import teachers_timetable
from time_table import *
from student_clashes import *
from teacher_clashes import *
from room_clashes import *
from stylesheet import *
from util import *

timetable = read_timetable(reg_data)

#####################################

# Import GUI File
from ui_interface import *
######################################

# Main Window Class
class MainWindow(QMainWindow):
    def __init__(self): 
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        try:
            self.DB = mc.connect(host="localhost", user="root", password="", database="timetable_manager")
        except mc.Error as e:
            print("Error")

        self.menu_buttons = [] # List that contains all the Menu Buttons 


        # Remove Window Title Bar
        self.setWindowFlags(PySide2.QtCore.Qt.FramelessWindowHint)

        # Set main background to transparent
        self.setAttribute(PySide2.QtCore.Qt.WA_TranslucentBackground)

        # Shadow Style Effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))
        
        # Apply shadow to central widget 
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        self.setWindowIcon(PySide2.QtGui.QIcon(":/icons/airplay.svg"))
        # Set Window Title
        self.setWindowTitle("Timetable Manager")

        # Window Size grip to resize window
        QSizeGrip(self.ui.size_grip)

        # Minimize Window
        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())

        # Close Window
        self.ui.close_window_button.clicked.connect(lambda: self.close())

        # Maximize Window
        self.ui.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())
        


        # Navigate to Section Page 
        self.ui.section_menu_button.clicked.connect(lambda: self.navigate_to_section_page())
        self.ui.add_section_button.clicked.connect(self.executeAddSectionPage)
        self.ui.search_section_text.textChanged.connect(self.SectionSearch)
        self.ui.section_delete_all_button.clicked.connect(self.deleteAllSections)
        self.menu_buttons.append(self.ui.section_menu_button)
        # Navigate to Course Page
        self.ui.course_menu_button.clicked.connect(lambda: self.navigate_to_course_page())
        self.ui.add_course_button.clicked.connect(self.executeAddCoursePage)
        self.ui.course_search_text.textChanged.connect(self.CourseSearch)
        self.ui.course_delete_all_button.clicked.connect(self.deleteAllCourses)
        self.menu_buttons.append(self.ui.course_menu_button)

        # Navigate to Room Page
        self.ui.room_menu_button.clicked.connect(lambda: self.navigate_to_room_page())
        self.ui.room_add_button.clicked.connect(self.executeAddRoomPage)
        self.ui.room_search_text.textChanged.connect(self.RoomSearch)
        self.ui.room_delete_all_button.clicked.connect(self.deleteAllRooms)
        self.menu_buttons.append(self.ui.room_menu_button)

        # Navigate to Teacher Page
        self.ui.teacher_menu_button.clicked.connect(lambda: self.navigate_to_teacher_page())
        self.ui.add_teacher_button.clicked.connect(self.executeAddTeacherPage)
        self.ui.teacher_search_text.textChanged.connect(self.TeacherSearch)
        self.ui.delete_all_teacher_button.clicked.connect(self.deleteAllTeachers)
        self.menu_buttons.append(self.ui.teacher_menu_button)

         # Navigate to Registered Courses Page
        self.ui.registered_menu_button.clicked.connect(lambda: self.navigate_to_registered_courses_page())
        self.ui.add_registered_button.clicked.connect(self.executeAddRegisteredCoursePage)
        self.ui.registered_search_text.textChanged.connect(self.RegisteredSearch)
        self.ui.delete_all_registered_button.clicked.connect(self.deleteAllRegisteredCourses)
        self.menu_buttons.append(self.ui.registered_menu_button)

        # Navigate to Room Preferences Page
        self.ui.room_preference_menu_button.clicked.connect(lambda: self.navigate_to_room_preferences_page())
        self.ui.room_preferences_search_text.textChanged.connect(self.RoomPreferencesSearch)
        self.ui.delete_all_room_preferences.clicked.connect(self.deleteAllRoomPreferences)
        self.menu_buttons.append(self.ui.room_preference_menu_button)

        # Navigate to Slot Preferences Page
        self.ui.slot_preference_menu_button.clicked.connect(lambda: self.navigate_to_slot_preferences_page())
        self.ui.slot_preferences_search_text.textChanged.connect(self.SlotPreferencesSearch)
        self.ui.delete_all_slot_preferences.clicked.connect(self.deleteAllSlotPreferences)
        self.menu_buttons.append(self.ui.slot_preference_menu_button)


        # Navigate to Student Clashes Page
        self.ui.student_clash_menu_button.clicked.connect(lambda: self.navigate_to_student_clashes_page())
        #self.ui.slot_preferences_search_text.textChanged.connect(self.SlotPreferencesSearch)
        self.menu_buttons.append(self.ui.student_clash_menu_button)

        # Navigate to Teacher Clashes Page
        self.ui.instructor_clash_menu_button.clicked.connect(lambda: self.navigate_to_teacher_clashes_page())
        self.menu_buttons.append(self.ui.instructor_clash_menu_button)

        # Navigate to Room Clashes Page
        self.ui.room_clash_menu_button.clicked.connect(lambda: self.navigate_to_room_clashes_page())
        self.menu_buttons.append(self.ui.room_clash_menu_button)

        # Navigate to Print Sections Timetable Page
        self.ui.view_section_timetable.clicked.connect(lambda: self.navigate_to_sections_timetable_page())
        self.ui.generate_sections_timetable.clicked.connect(lambda: self.print_sections_timetable())
        self.menu_buttons.append(self.ui.view_section_timetable)

        # Navigate to Print Teachers Timetable Page
        self.ui.view_teacher_timetable.clicked.connect(lambda: self.navigate_to_teachers_timetable_page())
        self.ui.generate_teachers_timetable.clicked.connect(lambda: self.print_teachers_timetable())
        self.menu_buttons.append(self.ui.view_teacher_timetable)
        
        # Navigate to Print Rooms Timetable Page
        self.ui.view_room_timetable.clicked.connect(lambda: self.navigate_to_rooms_timetable_page())
        self.ui.generate_rooms_timetable.clicked.connect(lambda: self.print_rooms_timetable())
        self.menu_buttons.append(self.ui.view_room_timetable)
        # Connect the ToolBox Click to Icon Changes
        self.ui.toolBox.currentChanged.connect(self.update_values)


        # Opening Page 
        self.navigate_to_sections_timetable_page()
        self.define_icons()
        self.default_icons()
        self.update_values(3)
        self.show()

   
#########################################################################
#############--------------------Section MENU----------------############
#########################################################################

    def navigate_to_section_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.sections_page)
        self.clear_all_buttons_stylesheet()
        self.ui.section_menu_button.setStyleSheet("padding-left: 15px; color: cyan; border-bottom: 1px solid cyan; border-left: 1px solid cyan;")
        self.default_icons()
        icon = QIcon()
        icon.addFile(u":/icons/icons/New folder/section_icon_active.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.section_menu_button.setIcon(icon)
        self.ui.section_menu_button.setIconSize(QSize(32, 32))
        self.ui.section_table.setRowCount(0)
        self.get_section_data()


    def on_section_table_click(self): # Whenever the Delete button gets clicked for section
        selected = self.ui.section_table.selectionModel().selectedIndexes()[0]
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Are you sure you want to delete the selected Section?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        if (msg.exec_() == 16384): # Means "YES"
            mycursor = self.DB.cursor()
            sql = "Delete from tbl_section where section_name = %s"
            val = (self.ui.section_table.item(selected.row(), 0).text(),)
            mycursor.execute(sql, val)
            self.DB.commit()
            self.ui.section_table.setRowCount(0)
            self.get_section_data()
            self.SectionSearch()
            self.ui.header_label_notification.setText("Section already exists in Database.")
            self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
            "background-color: rgb(198, 13, 0);\n"
            "padding-bottom: 10px; ")

    def executeAddSectionPage(self):
        self.window = QtWidgets.QMainWindow()
        self.add_section_form = Ui_Add_Section_Window()
        self.add_section_form.setupUi(self.window)
        self.window.show()
        self.add_section_form.section_add_form_button.clicked.connect(self.insert_section_info)
        self.add_section_form.section_name_add.textChanged.connect(self.addSectionEmpty)

        
    def insert_section_info(self):
        name = self.add_section_form.section_name_add.text()
        mycursor = self.DB.cursor()
        sql = "select * from tbl_section where section_name = %s"
        val = (name, )
        mycursor.execute(sql, val)
        numrows = len(mycursor.fetchall())
        if (numrows > 0): # That is, a section already exists with same name... 
            self.ui.header_label_notification.setText(name + " already exists in Database.")
            self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
            "background-color: rgb(198, 13, 0);\n"
            "padding-bottom: 10px; ")
            self.window.close()
        else: # Otherwise, insert the section into Database. 
            sql = "Insert into tbl_section (section_name) VALUES (%s)"
            val = (name, )
            mycursor.execute(sql, val)
            self.DB.commit()
            self.window.close()
            self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
            "background-color: rgb(41, 182, 31);\n"
            "padding-bottom: 10px;")
            self.ui.header_label_notification.setText("Section " + name + " Inserted Successfully")
        self.ui.header_label_notification.show() 
        self.fade(self.ui.header_label_notification)
        self.get_section_data() # Reload the Table

    # For the Editing of Section 
    def on_section_edit_click(self):      
        self.window = QtWidgets.QMainWindow()
        self.edit_section_form = Ui_Edit_Section_Window()
        selected = self.ui.section_table.selectionModel().selectedIndexes()[0]
        selected = self.ui.section_table.item(selected.row(), 0).text()
        mycursor = self.DB.cursor()
        sql = "Select section_id from tbl_section where section_name = %s"
        val = (selected, )
        mycursor.execute(sql, val)
        row = mycursor.fetchall()
        selected = row[0][0]
        tablerow = int(selected)
        sql = "Select section_name from tbl_section where section_id = %s"
        val = (tablerow, )
        mycursor.execute(sql, val)
        row = mycursor.fetchall()
        self.edit_section_form.setupUi(self.window)
        self.edit_section_form.edit_section_name.setText(row[0][0])
        self.window.show()
        self.edit_section_form.edit_section_name.textChanged.connect(self.editSectionEmpty)
        self.edit_section_form.section_edit_form_button.clicked.connect(lambda: self.edit_section_function(tablerow))

    # When the Edit Button is pressed.
    def edit_section_function(self, tablerow):     
        name = self.edit_section_form.edit_section_name.text()
        mycursor = self.DB.cursor()
        sql = "select section_name from tbl_section where section_name = %s"
        val = (name, )
        mycursor.execute(sql, val)
        numrows = len(mycursor.fetchall())
        if (numrows > 0):
            self.ui.header_label_notification.setText("Section already exists in Database.")
            self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
            "background-color: rgb(198, 13, 0);\n"
            "padding-bottom: 10px; ")
            self.window.close()
        else:
            sql = "Update tbl_section set section_name = %s where section_id = %s"
            val = (name, int(tablerow))
            mycursor.execute(sql, val)
            self.DB.commit()
            self.window.close()
            self.get_course_data() # Reload the Table    
            self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
                "background-color: rgb(41, 182, 31);\n"
                "padding-bottom: 10px;")
            self.ui.header_label_notification.setText("Section Updated Successfully")
        self.ui.header_label_notification.show() 
        self.fade(self.ui.header_label_notification)
        self.SectionSearch()
        self.get_section_data()

    def get_section_data(self):
        mycursor = self.DB.cursor()
        Subquery = "Select section_name from tbl_section"
        mycursor.execute(Subquery)

        numcols = len(mycursor.fetchall()[0])
        mycursor.execute(Subquery)
        numrows = len(mycursor.fetchall())
        self.ui.section_table.setRowCount(numrows)
        self.ui.section_table.setColumnCount(numcols+2)
        mycursor.execute(Subquery)
        tablerow = 0
        for row in mycursor.fetchall():
            tablecol = 0
            delete_button = QPushButton()
            icon = QIcon()
            icon.addFile(u":/icons/icons/Delete-button.png", QSize(), QIcon.Normal, QIcon.Off)
            delete_button.setIcon(icon)
            index = PySide2.QtCore.QPersistentModelIndex(self.ui.section_table.model().index(tablerow, tablecol))
            self.ui.section_table.setCellWidget(tablerow, 2, delete_button)
            delete_button.clicked.connect(lambda *args, index=index: self.on_section_table_click())
            edit_button = QPushButton()
            icon = QIcon()
            icon.addFile(u":/icons/icons/edit-button.png", QSize(), QIcon.Normal, QIcon.Off)
            edit_button.setIcon(icon)
            index = PySide2.QtCore.QPersistentModelIndex(self.ui.section_table.model().index(tablerow, tablecol))
            self.ui.section_table.setCellWidget(tablerow, 1, edit_button)
            edit_button.clicked.connect(lambda *args, index=index: self.on_section_edit_click())
            edit_button.setStyleSheet("background-color: transparent; border-style: none")
            delete_button.setStyleSheet("background-color: transparent; border-style: none")
            while tablecol < numcols:
                self.ui.section_table.setItem(tablerow, tablecol, PySide2.QtWidgets.QTableWidgetItem(str(row[tablecol])))
                tablecol += 1
            tablerow += 1
        self.ui.section_table.horizontalHeader().setSectionResizeMode(PySide2.QtWidgets.QHeaderView.Stretch)

    def deleteAllSections(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Are you sure you want to delete all the Sections?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        if (msg.exec_() == 16384): # Means "YES"
            mycursor = self.DB.cursor()
            sql = "Delete from tbl_section"
            mycursor.execute(sql)
            self.DB.commit()
            self.ui.section_table.setRowCount(0)
            self.get_section_data()
            self.SectionSearch()
            self.ui.header_label_notification.setText("All Sections Deleted")
            self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
            "background-color: rgb(198, 13, 0);\n"
            "padding-bottom: 10px; ")
            self.ui.header_label_notification.show()    
            self.fade(self.ui.header_label_notification)
        
        self.SectionSearch()
        self.get_section_data()

    # Section Search Function 
    def SectionSearch(self):
        name = self.ui.search_section_text.text().lower()
        for row in range(self.ui.section_table.rowCount()):
            item = self.ui.section_table.item(row, 0)
            self.ui.section_table.setRowHidden(row, name not in item.text().lower())

    # Checking for Empty Field in Add Section 
    def addSectionEmpty(self):
        if  not (len(self.add_section_form.section_name_add.text()) > 0):
            self.add_section_form.section_add_form_button.setEnabled(False)
        else:
            self.add_section_form.section_add_form_button.setEnabled(True)

    # Checking for Empty Field in Edit Section 
    def editSectionEmpty(self):
        if  not (len(self.edit_section_form.edit_section_name.text()) > 0):
            self.edit_section_form.section_edit_form_button.setEnabled(False)
        else:
            self.edit_section_form.section_edit_form_button.setEnabled(True)

    
######################################################################
#############--------------------COURSE MENU----------------##########
######################################################################
    
    # Navigate to Course Page 
    def navigate_to_course_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.courses_page)
        self.clear_all_buttons_stylesheet()
        self.ui.course_menu_button.setStyleSheet("padding-left: 15px; color: cyan; border-bottom: 1px solid cyan; border-left: 1px solid cyan;")
        self.default_icons()
        icon = QIcon()
        icon.addFile(u":/icons/icons/New folder/courses_icon_active.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.course_menu_button.setIcon(icon)
        self.ui.course_menu_button.setIconSize(QSize(32, 32))
        self.ui.course_table.setRowCount(0)
        self.get_course_data()
    
    def get_course_data(self):
        mycursor = self.DB.cursor()
        Subquery = "Select course_name, course_code, course_type from tbl_course"
        mycursor.execute(Subquery)

        numcols = len(mycursor.fetchall()[0])
        mycursor.execute(Subquery)
        numrows = len(mycursor.fetchall())
        self.ui.course_table.setRowCount(numrows)
        self.ui.course_table.setColumnCount(numcols+2)
        mycursor.execute(Subquery)
        tablerow = 0
        for row in mycursor.fetchall():
            tablecol = 0
            index = PySide2.QtCore.QPersistentModelIndex(self.ui.course_table.model().index(tablerow, tablecol))
            delete_button = QPushButton()
            delete_button.clicked.connect(lambda *args, index=index: self.on_course_delete_button())
            icon_delete = QIcon()
            icon_delete.addFile(u":/icons/icons/Delete-button.png", QSize(), QIcon.Normal, QIcon.Off)
            delete_button.setIcon(icon_delete)
            edit_button = QPushButton()
            edit_button.clicked.connect(lambda *args, index=index: self.on_course_edit_click())
            icon_edit = QIcon()
            icon_edit.addFile(u":/icons/icons/edit-button.png", QSize(), QIcon.Normal, QIcon.Off)
            edit_button.setIcon(icon_edit)
           
            edit_button.setStyleSheet("background-color: transparent; border-style: none")
            delete_button.setStyleSheet("background-color: transparent; border-style: none")
            self.ui.course_table.setCellWidget(tablerow, 3, edit_button)
            self.ui.course_table.setCellWidget(tablerow, 4, delete_button)

            while tablecol < numcols:
                self.ui.course_table.setItem(tablerow, tablecol, PySide2.QtWidgets.QTableWidgetItem(str(row[tablecol])))
                tablecol += 1
            tablerow += 1
        #self.ui.course_table.setColumnHidden(0, True)
        self.ui.course_table.horizontalHeader().setSectionResizeMode(PySide2.QtWidgets.QHeaderView.Stretch)

    # Execute the "Add Course" Page
    def executeAddCoursePage(self):
        self.window = QtWidgets.QMainWindow()
        self.add_course_form = Ui_Add_Course_Window()
        self.add_course_form.setupUi(self.window)
        self.window.show()
        self.add_course_form.add_course_submit.clicked.connect(self.insert_course_info)
        self.add_course_form.add_course_code.textChanged.connect(self.addCourseEmpty)
        self.add_course_form.add_course_name.textChanged.connect(self.addCourseEmpty)


    def insert_course_info(self):
        name = self.add_course_form.add_course_name.text()
        code = self.add_course_form.add_course_code.text()
        type = self.add_course_form.add_course_type.currentText()
        mycursor = self.DB.cursor()
        sql = "select course_name from tbl_course where course_name = %s OR course_code = %s"
        val = (name, code)
        mycursor.execute(sql, val)
        numrows = len(mycursor.fetchall())
        if (numrows > 0):
            self.ui.header_label_notification.setText("Course already exists in Database.")
            self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
            "background-color: rgb(198, 13, 0);\n"
            "padding-bottom: 10px; ")
            self.window.close()
        else: 
            sql = "Insert into tbl_course (course_name, course_code, course_type) VALUES (%s, %s, %s)"
            val = (name, code, type)
            mycursor.execute(sql, val)
            self.DB.commit()
            self.window.close()
            self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
                "background-color: rgb(41, 182, 31);\n"
                "padding-bottom: 10px;")
            self.ui.header_label_notification.setText("Course Inserted Successfully")
        self.ui.header_label_notification.show() 
        self.fade(self.ui.header_label_notification)
        self.get_course_data() # Reload the Table    
        self.CourseSearch()
    # For the Editing of Course 
    def on_course_edit_click(self):      
        self.window = QtWidgets.QMainWindow()
        self.edit_course_form = Ui_Edit_Course_Window()
        selected = self.ui.course_table.selectionModel().selectedIndexes()[0]
        selected = self.ui.course_table.item(selected.row(), 0).text()
        mycursor = self.DB.cursor()
        sql = "Select course_id from tbl_course where course_name = %s"
        val = (selected, )
        mycursor.execute(sql, val)
        row = mycursor.fetchall()
        selected = row[0][0]
        print(selected)
        tablerow = int(selected)
        sql = "Select * from tbl_course where course_id = %s"
        val = (tablerow, )
        mycursor.execute(sql, val)
        row = mycursor.fetchall()
        self.edit_course_form.setupUi(self.window)
        self.edit_course_form.edit_course_name.setText(row[0][1])
        self.edit_course_form.edit_course_code.setText(row[0][2])
        self.edit_course_form.edit_course_type.setCurrentText(row[0][3])
        self.window.show()
        self.edit_course_form.edit_course_name.textChanged.connect(self.editCourseEmpty)
        self.edit_course_form.edit_course_code.textChanged.connect(self.editCourseEmpty)
        self.edit_course_form.edit_course_submit.clicked.connect(lambda: self.edit_course_function(tablerow))

    # When the Edit Button is pressed.
    def edit_course_function(self, tablerow):     
        name = self.edit_course_form.edit_course_name.text()
        code = self.edit_course_form.edit_course_code.text()
        type = self.edit_course_form.edit_course_type.currentText()
        mycursor = self.DB.cursor()
        sql = "select course_name from tbl_course where course_name = %s OR course_code = %s"
        val = (name, code)
        mycursor.execute(sql, val)
        numrows = len(mycursor.fetchall())
        if (numrows > 0):
            self.ui.header_label_notification.setText("Course already exists in Database.")
            self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
            "background-color: rgb(198, 13, 0);\n"
            "padding-bottom: 10px; ")
            self.window.close()
        else:
            sql = "Update tbl_course set course_name = %s, course_code = %s, course_type = %s where course_id = %s"
            val = (name, code, type, int(tablerow))
            mycursor.execute(sql, val)
            self.DB.commit()
            self.window.close()
            self.get_course_data() # Reload the Table    
            self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
                "background-color: rgb(41, 182, 31);\n"
                "padding-bottom: 10px;")
            self.ui.header_label_notification.setText("Course Updated Successfully")
        self.ui.header_label_notification.show() 
        self.fade(self.ui.header_label_notification)
        self.CourseSearch()
    # For the Deletion of Course
    def on_course_delete_button(self):
        
        selected = self.ui.course_table.selectionModel().selectedIndexes()[0]
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Are you sure you want to delete the selected Course?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        if (msg.exec_() == 16384): # Means "YES"
            mycursor = self.DB.cursor()
            sql = "Delete from tbl_course where course_name = %s"
            val = (self.ui.course_table.item(selected.row(), 0).text(), )
            mycursor.execute(sql, val)
            self.DB.commit()
            self.ui.course_table.setRowCount(0)
            self.get_course_data()
            print("Deleted")
        else:
            print("Not Deleted")

    def deleteAllCourses(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Are you sure you want to delete all the Courses?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        if (msg.exec_() == 16384): # Means "YES"
            mycursor = self.DB.cursor()
            sql = "Delete from tbl_course"
            mycursor.execute(sql)
            self.DB.commit()
            self.ui.course_table.setRowCount(0)
            self.get_course_data()
            self.CourseSearch()
            self.ui.header_label_notification.setText("All Courses Deleted")
            self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
            "background-color: rgb(198, 13, 0);\n"
            "padding-bottom: 10px; ")
            self.ui.header_label_notification.show() 
            self.fade(self.ui.header_label_notification)

    # Course Search Function 
    def CourseSearch(self):
        search_text = self.ui.course_search_text.text().lower()
        for row in range(self.ui.course_table.rowCount()):
            name = self.ui.course_table.item(row, 0)
            code = self.ui.course_table.item(row, 1)
            type = self.ui.course_table.item(row, 2)
            if (search_text not in name.text().lower() and search_text not in code.text().lower()
            and search_text not in type.text().lower()):
                self.ui.course_table.setRowHidden(row, True)
            else:
                self.ui.course_table.setRowHidden(row, False)

    def addCourseEmpty(self):
        if  not (len(self.add_course_form.add_course_name.text()) > 0
         and len(self.add_course_form.add_course_code.text()) > 0):
            self.add_course_form.add_course_submit.setEnabled(False)
        else:
            self.add_course_form.add_course_submit.setEnabled(True)

    def editCourseEmpty(self):
        if  not (len(self.edit_course_form.edit_course_name.text()) > 0
         and len(self.edit_course_form.edit_course_code.text()) > 0):
            self.edit_course_form.edit_course_submit.setEnabled(False)
        else:
            self.edit_course_form.edit_course_submit.setEnabled(True)

######################################################################
#############--------------------ROOM MENU----------------############
######################################################################

    # Navigate to Room Menu
    def navigate_to_room_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.rooms_page)
        self.clear_all_buttons_stylesheet()
        self.ui.room_menu_button.setStyleSheet("padding-left: 15px; color: cyan; border-bottom: 1px solid cyan; border-left: 1px solid cyan;")
        self.default_icons()
        icon = QIcon()
        icon.addFile(u":/icons/icons/New folder/room_icon_active.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.room_menu_button.setIcon(icon)
        self.ui.room_menu_button.setIconSize(QSize(32, 32))
        self.ui.room_table.setRowCount(0)
        self.get_room_data()

    
    def get_room_data(self):
        mycursor = self.DB.cursor()
        Subquery = "Select room_type, room_name, room_for from tbl_room"
        mycursor.execute(Subquery)

        numcols = len(mycursor.fetchall()[0])
        mycursor.execute(Subquery)
        numrows = len(mycursor.fetchall())
        self.ui.room_table.setRowCount(numrows)
        self.ui.room_table.setColumnCount(numcols+2)
        mycursor.execute(Subquery)
        tablerow = 0
        for row in mycursor.fetchall():
            tablecol = 0
           
            index = PySide2.QtCore.QPersistentModelIndex(self.ui.room_table.model().index(tablerow, tablecol))
            delete_button = QPushButton()
            delete_button.clicked.connect(lambda *args, index=index: self.on_room_delete_button())
            icon_delete = QIcon()
            icon_delete.addFile(u":/icons/icons/Delete-button.png", QSize(), QIcon.Normal, QIcon.Off)
            delete_button.setIcon(icon_delete)
            edit_button = QPushButton()
            edit_button.clicked.connect(lambda *args, index=index: self.on_room_edit_click())
            icon_edit = QIcon()
            icon_edit.addFile(u":/icons/icons/edit-button.png", QSize(), QIcon.Normal, QIcon.Off)
            edit_button.setIcon(icon_edit)        
            edit_button.setStyleSheet("background-color: transparent; border-style: none")
            delete_button.setStyleSheet("background-color: transparent; border-style: none")
            self.ui.room_table.setCellWidget(tablerow, 3, edit_button)
            self.ui.room_table.setCellWidget(tablerow, 4, delete_button)

            while tablecol < numcols:
                self.ui.room_table.setItem(tablerow, tablecol, PySide2.QtWidgets.QTableWidgetItem(str(row[tablecol])))
                tablecol += 1
            tablerow += 1
        #self.ui.room_table.setColumnHidden(0, True)
        self.ui.room_table.horizontalHeader().setSectionResizeMode(PySide2.QtWidgets.QHeaderView.Stretch)

        #self.ui.room_table.resizeColumnsToContents()

    # Execute the "Add Room" Page
    def executeAddRoomPage(self):
        self.window = QtWidgets.QMainWindow()
        self.add_room_form = Ui_Add_Room_Window()
        self.add_room_form.setupUi(self.window)
        self.window.show()
        self.add_room_form.add_room_submit.clicked.connect(self.insert_room_info)
        self.add_room_form.add_room_name.textChanged.connect(self.addRoomEmpty)


    def insert_room_info(self):
        type = self.add_room_form.add_room_type.currentText()
        name = self.add_room_form.add_room_name.text()
        room_for = self.add_room_form.add_room_for.currentText()
        mycursor = self.DB.cursor()
        sql = "select room_name from tbl_room where room_name = %s"
        val = (name, )
        mycursor.execute(sql, val)
        numrows = len(mycursor.fetchall())
        if (numrows > 0):
            self.ui.header_label_notification.setText("Room already exists in Database.")
            self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
            "background-color: rgb(198, 13, 0);\n"
            "padding-bottom: 10px; ")
            self.window.close()
        else:
            sql = "Insert into tbl_room (room_type, room_name, room_for) VALUES (%s, %s, %s)"
            val = (type, name, room_for)
            mycursor.execute(sql, val)
            self.DB.commit()
            self.window.close()
            self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
                "background-color: rgb(41, 182, 31);\n"
                "padding-bottom: 10px;")
            self.ui.header_label_notification.setText("Room Added Successfully")
        self.ui.header_label_notification.show() 
        self.fade(self.ui.header_label_notification)
        self.get_room_data() # Reload the Table    
        self.RoomSearch()
    # For the Editing of Room 
    def on_room_edit_click(self):      
        self.window = QtWidgets.QMainWindow()
        self.edit_room_form = Ui_Edit_Room_Window()
        selected = self.ui.room_table.selectionModel().selectedIndexes()[0]
        mycursor = self.DB.cursor()
        tablerow = self.ui.room_table.item(selected.row(), 1).text()
        sql = "Select room_id from tbl_room where room_name = %s"
        val = (tablerow, )
        mycursor.execute(sql, val)
        row = mycursor.fetchall()
        tablerow = row[0][0]
        sql = "Select * from tbl_room where room_id = %s"
        val = (tablerow, )
        mycursor.execute(sql, val)
        row = mycursor.fetchall()
        self.edit_room_form.setupUi(self.window)
        self.edit_room_form.edit_room_type.setCurrentText(row[0][1])
        self.edit_room_form.edit_room_name.setText(row[0][2])
        self.edit_room_form.edit_room_for.setCurrentText(row[0][3])
        self.window.show()
        self.edit_room_form.edit_room_submit.clicked.connect(lambda: self.edit_room_function(tablerow))
        self.edit_room_form.edit_room_name.textChanged.connect(self.editRoomEmpty)

    # When the Edit Button is pressed.
    def edit_room_function(self, tablerow):     
        type = self.edit_room_form.edit_room_type.currentText()
        name = self.edit_room_form.edit_room_name.text()
        room_for = self.edit_room_form.edit_room_for.currentText()
        mycursor = self.DB.cursor()
        sql = "select room_name from tbl_room where room_name = %s"
        val = (name, )
        mycursor.execute(sql, val)
        numrows = len(mycursor.fetchall())
        if (numrows > 0):
            self.ui.header_label_notification.setText("Room already exists in Database.")
            self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
            "background-color: rgb(198, 13, 0);\n"
            "padding-bottom: 10px; ")
            self.window.close()
        else:
            sql = "Update tbl_room set room_type = %s, room_name = %s, room_for = %s where room_id = %s"
            val = (type, name, room_for, int(tablerow))
            mycursor.execute(sql, val)
            self.DB.commit()
            self.window.close()
            self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
                "background-color: rgb(41, 182, 31);\n"
                "padding-bottom: 10px;")
            self.ui.header_label_notification.setText("Room Updated Successfully")
        
        self.ui.header_label_notification.show() 
        self.fade(self.ui.header_label_notification)        
        self.get_room_data() # Reload the Table
        self.RoomSearch()
    # For the Deletion of Room
    def on_room_delete_button(self):
        
        selected = self.ui.room_table.selectionModel().selectedIndexes()[0]
        mycursor = self.DB.cursor()
        tablerow = self.ui.room_table.item(selected.row(), 1).text()
        sql = "Select room_id from tbl_room where room_name = %s"
        val = (tablerow, )
        mycursor.execute(sql, val)
        row = mycursor.fetchall()
        tablerow = row[0][0]
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Are you sure you want to delete the selected Room?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        if (msg.exec_() == 16384): # Means "YES"
            mycursor = self.DB.cursor()
            sql = "Delete from tbl_room where room_id = %s"
            val = (tablerow,)
            mycursor.execute(sql, val)
            self.DB.commit()
            self.ui.room_table.setRowCount(0)
            self.ui.header_label_notification.setText("Room Deleted Successfully")
            self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
            "background-color: rgb(198, 13, 0);\n"
            "padding-bottom: 10px; ")
            self.ui.header_label_notification.show() 
            self.fade(self.ui.header_label_notification)
            self.get_room_data()
            self.RoomSearch()

    def deleteAllRooms(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Are you sure you want to delete all the Rooms?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        if (msg.exec_() == 16384): # Means "YES"
            mycursor = self.DB.cursor()
            sql = "Delete from tbl_room"
            mycursor.execute(sql)
            self.DB.commit()
            self.ui.room_table.setRowCount(0)
            self.get_room_data()
            self.RoomSearch()
            self.ui.header_label_notification.setText("All Sections Deleted")
            self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
            "background-color: rgb(198, 13, 0);\n"
            "padding-bottom: 10px; ")
            self.ui.header_label_notification.show() 
            self.fade(self.ui.header_label_notification)


    # Room Search Function 
    def RoomSearch(self):
        search_text = self.ui.room_search_text.text().lower()
        for row in range(self.ui.room_table.rowCount()):
            type = self.ui.room_table.item(row, 0)
            name = self.ui.room_table.item(row, 1)
            room_for = self.ui.room_table.item(row, 2)
            if (search_text not in type.text().lower() and search_text not in name.text().lower()
            and search_text not in room_for.text().lower()):
                self.ui.room_table.setRowHidden(row, True)
            else:
                self.ui.room_table.setRowHidden(row, False)
    
    def addRoomEmpty(self):
        if  not (len(self.add_room_form.add_room_name.text()) > 0):
            self.add_room_form.add_room_submit.setEnabled(False)
        else:
            self.add_room_form.add_room_submit.setEnabled(True)

    def editRoomEmpty(self):
        if  not (len(self.edit_room_form.edit_room_name.text()) > 0):
            self.edit_room_form.edit_room_submit.setEnabled(False)
        else:
            self.edit_room_form.edit_room_submit.setEnabled(True)

######################################################################
#############--------------------TEACHER MENU----------------#########
######################################################################

    # Navigate to Teacher Menu
    def navigate_to_teacher_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.teachers_page)
        self.clear_all_buttons_stylesheet()
        self.ui.teacher_menu_button.setStyleSheet("padding-left: 15px; color: cyan; border-bottom: 1px solid cyan; border-left: 1px solid cyan;")
        self.default_icons()
        icon = QIcon()
        icon.addFile(u":/icons/icons/New folder/teacher_icon_active.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.teacher_menu_button.setIcon(icon)
        self.ui.teacher_menu_button.setIconSize(QSize(32, 32))
        self.ui.teacher_table.setRowCount(0)
        self.get_teacher_data()
    
    def get_teacher_data(self):
        mycursor = self.DB.cursor()
        Subquery = "Select teacher_name from tbl_teacher"
        mycursor.execute(Subquery)

        numcols = len(mycursor.fetchall()[0])
        mycursor.execute(Subquery)
        numrows = len(mycursor.fetchall())
        self.ui.teacher_table.setRowCount(numrows)
        self.ui.teacher_table.setColumnCount(numcols+2)
        mycursor.execute(Subquery)
        tablerow = 0
        for row in mycursor.fetchall():
            tablecol = 0
            layout = QHBoxLayout()
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(0)
            index = PySide2.QtCore.QPersistentModelIndex(self.ui.teacher_table.model().index(tablerow, tablecol))
            delete_button = QPushButton()
            delete_button.clicked.connect(lambda *args, index=index: self.on_teacher_delete_button())
            icon_delete = QIcon()
            icon_delete.addFile(u":/icons/icons/Delete-button.png", QSize(), QIcon.Normal, QIcon.Off)
            delete_button.setIcon(icon_delete)
            layout.addWidget(delete_button)
            edit_button = QPushButton()
            edit_button.clicked.connect(lambda *args, index=index: self.on_teacher_edit_click())
            icon_edit = QIcon()
            icon_edit.addFile(u":/icons/icons/edit-button.png", QSize(), QIcon.Normal, QIcon.Off)
            edit_button.setIcon(icon_edit)
            layout.addWidget(edit_button)
            cellWidget = QWidget()
            cellWidget.setLayout(layout)
            edit_button.setStyleSheet("background-color: transparent; border-style: none")
            delete_button.setStyleSheet("background-color: transparent; border-style: none")
            self.ui.teacher_table.setCellWidget(tablerow, 1, edit_button)
            self.ui.teacher_table.setCellWidget(tablerow, 2, delete_button)
            while tablecol < numcols:
                self.ui.teacher_table.setItem(tablerow, tablecol, PySide2.QtWidgets.QTableWidgetItem(str(row[tablecol])))
                tablecol += 1
            tablerow += 1
        #self.ui.teacher_table.setColumnHidden(0, True)
        self.ui.teacher_table.horizontalHeader().setSectionResizeMode(PySide2.QtWidgets.QHeaderView.Stretch)
        #self.ui.teacher_table.resizeColumnsToContents()

    # Execute the "Add Teacher" Page
    def executeAddTeacherPage(self):
        self.window = QtWidgets.QMainWindow()
        self.add_teacher_form = Ui_Add_Teacher_Window()
        self.add_teacher_form.setupUi(self.window)
        self.window.show()
        self.add_teacher_form.add_teacher_submit.clicked.connect(self.insert_teacher_info)
        self.add_teacher_form.add_teacher_name.textChanged.connect(self.addTeacherEmpty)

    # Teacher Add Function
    def insert_teacher_info(self):
        name = self.add_teacher_form.add_teacher_name.text()
        mycursor = self.DB.cursor()
        sql = "select teacher_name from tbl_teacher where teacher_name = %s"
        val = (name, )
        mycursor.execute(sql, val)
        numrows = len(mycursor.fetchall())
        if (numrows > 0):
            self.ui.header_label_notification.setText("Teacher already exists in Database.")
            self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
            "background-color: rgb(198, 13, 0);\n"
            "padding-bottom: 10px; ")
            self.window.close()
        else:
            sql = "Insert into tbl_teacher (teacher_name) VALUES (%s)"
            val = (name, )
            mycursor.execute(sql, val)
            self.DB.commit()
            self.window.close()
            self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
                "background-color: rgb(41, 182, 31);\n"
                "padding-bottom: 10px;")
            self.ui.header_label_notification.setText("Teacher Added Successfully")
        self.ui.header_label_notification.show() 
        self.fade(self.ui.header_label_notification)
        self.get_teacher_data() # Reload the Table
        self.TeacherSearch()    

    # For the Editing of Teacher 
    def on_teacher_edit_click(self):      
        self.window = QtWidgets.QMainWindow()
        self.edit_teacher_form = Ui_Edit_Teacher_Window()
        selected = self.ui.teacher_table.selectionModel().selectedIndexes()[0]
        mycursor = self.DB.cursor()
        sql = "select teacher_id from tbl_teacher where teacher_name = %s"
        tablerow = self.ui.teacher_table.item(selected.row(), 0).text()
        val = (tablerow, )
        mycursor.execute(sql, val)
        row = mycursor.fetchall()
        tablerow = row[0][0]
        sql = "Select * from tbl_teacher where teacher_id = %s"
        val = (tablerow, )
        mycursor.execute(sql, val)
        row = mycursor.fetchall()
        self.edit_teacher_form.setupUi(self.window)
        self.edit_teacher_form.edit_teacher_name.setText(row[0][1])
        self.window.show()
        self.edit_teacher_form.edit_teacher_submit.clicked.connect(lambda: self.edit_teacher_function(tablerow))

    # When the Edit Button is pressed.
    def edit_teacher_function(self, tablerow):     
        name = self.edit_teacher_form.edit_teacher_name.text()
        mycursor = self.DB.cursor()
        sql = "select teacher_name from tbl_teacher where teacher_name = %s"
        val = (name, )
        mycursor.execute(sql, val)
        numrows = len(mycursor.fetchall())
        if (numrows > 0):
            self.ui.header_label_notification.setText("Teacher already exists in Database.")
            self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
            "background-color: rgb(198, 13, 0);\n"
            "padding-bottom: 10px; ")
            self.window.close()
        else:
            sql = "Update tbl_teacher set teacher_name = %s where teacher_id = %s"
            val = (name, int(tablerow))
            mycursor.execute(sql, val)
            self.DB.commit()
            self.window.close()
            self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
                "background-color: rgb(41, 182, 31);\n"
                "padding-bottom: 10px;")
            self.ui.header_label_notification.setText("Teacher Updated Successfully")
        self.ui.header_label_notification.show() 
        self.fade(self.ui.header_label_notification)
        self.get_teacher_data() # Reload the Table
        self.TeacherSearch()
    # For the Deletion of Room
    def on_teacher_delete_button(self):
        
        selected = self.ui.teacher_table.selectionModel().selectedIndexes()[0]
        sql = "select teacher_id from tbl_teacher where teacher_name = %s"
        mycursor = self.DB.cursor()
        tablerow = self.ui.teacher_table.item(selected.row(), 0).text()
        val = (tablerow, )
        mycursor.execute(sql, val)
        row = mycursor.fetchall()
        tablerow = row[0][0]
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Are you sure you want to delete the selected Teacher?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        if (msg.exec_() == 16384): # Means "YES"
            
            sql = "Delete from tbl_teacher where teacher_id = %s"
            val = (tablerow,)
            mycursor.execute(sql, val)
            self.DB.commit()
            self.ui.teacher_table.setRowCount(0)
            self.ui.header_label_notification.setText("Teacher Deleted from Database.")
            self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
            "background-color: rgb(198, 13, 0);\n"
            "padding-bottom: 10px; ")
            self.ui.header_label_notification.show() 
            self.fade(self.ui.header_label_notification)
            self.get_teacher_data()
            self.TeacherSearch()

    def deleteAllTeachers(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Are you sure you want to delete all the Teachers?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        if (msg.exec_() == 16384): # Means "YES"
            mycursor = self.DB.cursor()
            sql = "Delete from tbl_teacher"
            mycursor.execute(sql)
            self.DB.commit()
            self.ui.teacher_table.setRowCount(0)
            self.get_teacher_data()
            self.TeacherSearch()
            self.ui.header_label_notification.setText("All Teachers Deleted")
            self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
            "background-color: rgb(198, 13, 0);\n"
            "padding-bottom: 10px; ")
            self.ui.header_label_notification.show() 
            self.fade(self.ui.header_label_notification)

    # Teacher Search Function 
    def TeacherSearch(self):
        search_text = self.ui.teacher_search_text.text().lower()
        for row in range(self.ui.teacher_table.rowCount()):
            name = self.ui.teacher_table.item(row, 0)
            if (search_text not in name.text().lower()):
                self.ui.teacher_table.setRowHidden(row, True)
            else:
                self.ui.teacher_table.setRowHidden(row, False)

    def addTeacherEmpty(self):
        if  not (len(self.add_teacher_form.add_teacher_name.text()) > 0):
            self.add_teacher_form.add_teacher_submit.setEnabled(False)
        else:
            self.add_teacher_form.add_teacher_submit.setEnabled(True)

    def editTeacherEmpty(self):
        if  not (len(self.edit_teacher_form.edit_teacher_name.text()) > 0):
            self.edit_teacher_form.edit_teacher_submit.setEnabled(False)
        else:
            self.edit_teacher_form.edit_teacher_submit.setEnabled(True)

######################################################################
#############---------REGISTERED COURSES MENU-------------############
######################################################################


    # Navigate to Registered Courses Menu
    def navigate_to_registered_courses_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.registered_courses_page)
        self.clear_all_buttons_stylesheet()
        self.ui.registered_menu_button.setStyleSheet("padding-left: 15px; color: cyan; border-bottom: 1px solid cyan; border-left: 1px solid cyan;")
        self.default_icons()
        icon = QIcon()
        icon.addFile(u":/icons/icons/New folder/registeted_courses_active.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.registered_menu_button.setIcon(icon)
        self.ui.registered_menu_button.setIconSize(QSize(32, 32))
        self.ui.registered_table.setRowCount(0)
        self.get_registered_courses_data()
    
    def get_registered_courses_data(self):
        mycursor = self.DB.cursor()
        Subquery = "select "
        Subquery += "(select s.section_name from tbl_section s where s.section_id = r.section_id) 'section'"
        Subquery += ", (select c.course_name from tbl_course c where c.course_id = r.course_id) 'course', "
        Subquery += "(select t.teacher_name from tbl_teacher t where t.teacher_id = r.teacher_id) 'teacher'"
        Subquery += " from tbl_registered_courses r"
        mycursor.execute(Subquery)
        numcols = len(mycursor.fetchall()[0])
        mycursor.execute(Subquery)
        numrows = len(mycursor.fetchall())
        self.ui.registered_table.setRowCount(numrows)
        self.ui.registered_table.setColumnCount(numcols+3)
        mycursor.execute(Subquery)
        tablerow = 0
        for row in mycursor.fetchall():
            tablecol = 0
            index = PySide2.QtCore.QPersistentModelIndex(self.ui.registered_table.model().index(tablerow, tablecol))
            delete_button = QPushButton()
            delete_button.clicked.connect(lambda *args, index=index: self.on_registered_delete_button())
            icon_delete = QIcon()
            icon_delete.addFile(u":/icons/icons/Delete-button.png", QSize(), QIcon.Normal, QIcon.Off)
            delete_button.setIcon(icon_delete)
            edit_button = QPushButton()
            edit_button.clicked.connect(lambda *args, index=index: self.on_registered_edit_click())
            icon_edit = QIcon()
            icon_edit.addFile(u":/icons/icons/edit-button.png", QSize(), QIcon.Normal, QIcon.Off)
            edit_button.setIcon(icon_edit)

            #Get Count of Total Registered Students for the Specific Section
            count_cursor = self.DB.cursor()
            query = "select count(*) from tbl_section_students ss where ss.registered_id = ("
            query += "select r.registered_id from tbl_registered_courses r where"
            query += " r.section_id = (select s.section_id from tbl_section s where s.section_name = %s) "
            query += "and r.course_id = (select c.course_id from tbl_course c where c.course_name = %s) "
            query += "and r.teacher_id = (select t.teacher_id from tbl_teacher t where t.teacher_name = %s))"
            val = (row[0], row[1], row[2])
            count_cursor.execute(query, val)
            for value in count_cursor.fetchall():
               val = value[0]
            # Button for Get Students
            get_students = QPushButton(".Get Students(" + str(val) + ").")
            get_students.clicked.connect(lambda *args, index=index: self.executeSectionStudentsPage())
            get_students.setStyleSheet(primary_push_button)
            edit_button.setStyleSheet("background-color: transparent; border-style: none")
            delete_button.setStyleSheet("background-color: transparent; border-style: none")
            self.ui.registered_table.setCellWidget(tablerow, 3, get_students)
            self.ui.registered_table.setCellWidget(tablerow, 4, edit_button)
            self.ui.registered_table.setCellWidget(tablerow, 5, delete_button)
            while tablecol < numcols:
                self.ui.registered_table.setItem(tablerow, tablecol, PySide2.QtWidgets.QTableWidgetItem(str(row[tablecol])))
                tablecol += 1
            tablerow += 1
        #self.ui.registered_table.setColumnHidden(0, True)
        #self.ui.registered_table.horizontalHeader().setSectionResizeMode(PySide2.QtWidgets.QHeaderView.Stretch)
        self.ui.registered_table.resizeColumnsToContents()


    # Execute the "Add Registered Course" Page
    def executeAddRegisteredCoursePage(self):
        self.window = QtWidgets.QMainWindow()
        self.add_registered_form = Ui_Add_Registered_Course_Window()
        self.add_registered_form.setupUi(self.window)
        mycursor = self.DB.cursor()
        subquery = "Select section_name from tbl_section"
        mycursor.execute(subquery)
        for row in mycursor.fetchall():
            self.add_registered_form.add_registration_section.addItem(row[0])
        subquery = "Select course_name from tbl_course"
        mycursor.execute(subquery)
        for row in mycursor.fetchall():
            self.add_registered_form.add_registration_course.addItem(row[0])
        subquery = "Select teacher_name from tbl_teacher"
        mycursor.execute(subquery)
        for row in mycursor.fetchall():
            self.add_registered_form.add_registration_teacher.addItem(row[0])

        self.window.show()
        self.add_registered_form.add_registration_submit.clicked.connect(self.insert_registered_info)

    # Registered Courses Add Function
    def insert_registered_info(self):
        course = self.add_registered_form.add_registration_course.currentText()
        section = self.add_registered_form.add_registration_section.currentText()
        teacher = self.add_registered_form.add_registration_teacher.currentText()
        mycursor = self.DB.cursor()
        sql = "select * from tbl_registered_courses r "
        sql += "where r.course_id = (select c.course_id from tbl_course c where c.course_name = %s) and"
        sql += " r.section_id = (select s.section_id from tbl_section s where s.section_name = %s) and"
        sql += " r.teacher_id = (select t.teacher_id from tbl_teacher t where t.teacher_name = %s)"
        val = (course, section, teacher)
        mycursor.execute(sql, val)
        numrows = len(mycursor.fetchall())
        if (numrows > 0):
            self.ui.header_label_notification.setText("Registered Course already exists in Database.")
            self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
            "background-color: rgb(198, 13, 0);\n"
            "padding-bottom: 10px; ")
            self.window.close()
        else:
            sql = "insert into tbl_registered_courses (section_id, course_id, teacher_id)"
            sql += "values ((select section_id from tbl_section where section_name = %s), "
            sql += "(select course_id from tbl_course where course_name = %s), "
            sql += "(select teacher_id from tbl_teacher where teacher_name = %s));"
            val = (section, course, teacher)
            mycursor.execute(sql, val)
            self.DB.commit()
            self.window.close()
            self.ui.header_label_notification.setText("New Record inserted into Database")
            self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
            "background-color: rgb(41, 182, 31);\n"
            "padding-bottom: 10px; ")
        self.ui.header_label_notification.show() 
        self.fade(self.ui.header_label_notification)
        self.get_registered_courses_data() # Reload the Table
        self.RegisteredSearch()    

    # For the Editing of Registered Course 
    def on_registered_edit_click(self):      
        self.window = QtWidgets.QMainWindow()
        self.edit_registered_form = Ui_Edit_Registered_Course_Window()
        selected = self.ui.registered_table.selectionModel().selectedIndexes()[0]
        mycursor = self.DB.cursor()
        section = self.ui.registered_table.item(selected.row(), 0).text()
        course = self.ui.registered_table.item(selected.row(), 1).text()
        teacher = self.ui.registered_table.item(selected.row(), 2).text()
        Subquery = "select registered_id from tbl_registered_courses r "
        Subquery += "where r.course_id = (select c.course_id from tbl_course c where c.course_name = %s) and"
        Subquery += " r.section_id = (select s.section_id from tbl_section s where s.section_name = %s) and"
        Subquery += " r.teacher_id = (select t.teacher_id from tbl_teacher t where t.teacher_name = %s)"
        val = (course, section, teacher)
        mycursor.execute(Subquery, val)
        row = mycursor.fetchall()
        tablerow = row[0][0] # Getting Registered ID for that row
        subquery = "Select section_name from tbl_section"
        mycursor.execute(subquery)
        for row in mycursor.fetchall():
            self.edit_registered_form.edit_registration_section.addItem(row[0])
        subquery = "Select course_name from tbl_course"
        mycursor.execute(subquery)
        for row in mycursor.fetchall():
            self.edit_registered_form.edit_registration_course.addItem(row[0])
        subquery = "Select teacher_name from tbl_teacher"
        mycursor.execute(subquery)
        for row in mycursor.fetchall():
            self.edit_registered_form.edit_registration_teacher.addItem(row[0])
        
        # Setting the selected names
        Subquery = "select registered_id, "
        Subquery += "(select s.section_name from tbl_section s where s.section_id = r.section_id) 'section'"
        Subquery += ", (select c.course_name from tbl_course c where c.course_id = r.course_id) 'course', "
        Subquery += "(select t.teacher_name from tbl_teacher t where t.teacher_id = r.teacher_id) 'teacher'"
        Subquery += " from tbl_registered_courses r where registered_id = %s"
        val = (tablerow, )
        mycursor.execute(Subquery, val)
        row = mycursor.fetchall()
        self.edit_registered_form.setupUi(self.window)
        self.edit_registered_form.edit_registration_section.setCurrentText(row[0][1])
        self.edit_registered_form.edit_registration_course.setCurrentText(row[0][2])
        self.edit_registered_form.edit_registration_teacher.setCurrentText(row[0][3])
        self.window.show()
        self.edit_registered_form.edit_registration_submit.clicked.connect(lambda: self.edit_registered_function(tablerow))

    # When the Edit Button is pressed.
    def edit_registered_function(self, tablerow):     
        name = self.edit_teacher_form.edit_teacher_name.text()
        mycursor = self.DB.cursor()
        sql = "Update tbl_teacher set teacher_name = %s where teacher_id = %s"
        val = (name, int(tablerow))
        mycursor.execute(sql, val)
        self.DB.commit()
        self.window.close()
        self.get_teacher_data() # Reload the Table
        self.TeacherSearch()
    # For the Deletion of Room
    def on_registered_delete_button(self):
        
        selected = self.ui.registered_table.selectionModel().selectedIndexes()[0]
        mycursor = self.DB.cursor()

        section = self.ui.registered_table.item(selected.row(), 0).text()
        course = self.ui.registered_table.item(selected.row(), 1).text()
        teacher = self.ui.registered_table.item(selected.row(), 2).text()
        Subquery = "select registered_id from tbl_registered_courses r "
        Subquery += "where r.course_id = (select c.course_id from tbl_course c where c.course_name = %s) and"
        Subquery += " r.section_id = (select s.section_id from tbl_section s where s.section_name = %s) and"
        Subquery += " r.teacher_id = (select t.teacher_id from tbl_teacher t where t.teacher_name = %s)"
        val = (course, section, teacher)
        mycursor.execute(Subquery, val)
        row = mycursor.fetchall()
        tablerow = row[0][0] # Getting Registered ID for that row
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Are you sure you want to delete the selected Registered Course?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        if (msg.exec_() == 16384): # Means "YES"
            sql = "Delete from tbl_registered_courses where registered_id = %s"
            val = (tablerow,)
            print(tablerow)
            mycursor.execute(sql, val)
            self.DB.commit()
            self.ui.registered_table.setRowCount(0)
            self.ui.header_label_notification.setText("Registered Course Deleted from Database.")
            self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
            "background-color: rgb(198, 13, 0);\n"
            "padding-bottom: 10px; ")
            self.ui.header_label_notification.show() 
            self.fade(self.ui.header_label_notification)
            self.get_registered_courses_data()
            self.RegisteredSearch()


    def deleteAllRegisteredCourses(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Are you sure you want to delete all the Registered Courses?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        if (msg.exec_() == 16384): # Means "YES"
            mycursor = self.DB.cursor()
            sql = "Delete from tbl_registered_courses"
            mycursor.execute(sql)
            self.DB.commit()
            self.ui.registered_table.setRowCount(0)
            self.get_registered_courses_data()
            self.RegisteredSearch()
            self.ui.header_label_notification.setText("All Registered Courses Deleted")
            self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
            "background-color: rgb(198, 13, 0);\n"
            "padding-bottom: 10px; ")
            self.ui.header_label_notification.show() 
            self.fade(self.ui.header_label_notification)

    # Registered Course Search Function 
    def RegisteredSearch(self):
        search_text = self.ui.registered_search_text.text().lower()
        for row in range(self.ui.registered_table.rowCount()):
            section = self.ui.registered_table.item(row, 0)
            course = self.ui.registered_table.item(row, 1)
            teacher = self.ui.registered_table.item(row, 2)
            if (search_text not in section.text().lower() and search_text not in course.text().lower()
            and search_text not in teacher.text().lower()):
                self.ui.registered_table.setRowHidden(row, True)
            else:
                self.ui.registered_table.setRowHidden(row, False)

    def addRegisteredEmpty(self):
        if  not (len(self.add_room_form.add_room_name.text()) > 0):
            self.add_room_form.add_room_submit.setEnabled(False)
        else:
            self.add_room_form.add_room_submit.setEnabled(True)

    def editRegisteredEmpty(self):
        if  not (len(self.edit_room_form.edit_room_name.text()) > 0):
            self.edit_room_form.edit_room_submit.setEnabled(False)
        else:
            self.edit_room_form.edit_room_submit.setEnabled(True)
    
######################################################################
#############---------SECTION STUDENT MENU-------------###############
######################################################################


    # Navigate to Section Students Menu
    def executeSectionStudentsPage(self):
        table_row = self.ui.registered_table.selectionModel().selectedIndexes()[0]
        mycursor = self.DB.cursor()
        Subquery = "select r.registered_id from tbl_registered_courses r where "
        Subquery += "r.section_id = (select s.section_id from tbl_section s where s.section_name = %s) and "
        Subquery += "r.course_id = (select c.course_id from tbl_course c where c.course_name = %s) and "
        Subquery += "r.teacher_id = (select t.teacher_id from tbl_teacher t where t.teacher_name = %s)"
        val = (self.ui.registered_table.item(table_row.row(), 0).text(), 
        self.ui.registered_table.item(table_row.row(), 1).text(), 
        self.ui.registered_table.item(table_row.row(), 2).text())
        mycursor.execute(Subquery, val)
        for row in mycursor.fetchall():
            print(row)
            self.course_selected = row[0]
        self.window = QtWidgets.QMainWindow()
        self.registered_section_students_window = Ui_Registered_Section_Students_Window()
        self.registered_section_students_window.setupUi(self.window)
        # Load Teachers, Course and Section Data
        Subquery = "select  "
        Subquery += "(select s.section_name from tbl_section s where s.section_id = r.section_id) 'section'"
        Subquery += ", (select c.course_name from tbl_course c where c.course_id = r.course_id) 'course', "
        Subquery += "(select t.teacher_name from tbl_teacher t where t.teacher_id = r.teacher_id) 'teacher'"
        Subquery += " from tbl_registered_courses r where r.registered_id = %s"
        val = (self.course_selected, )

        mycursor.execute(Subquery, val)
        for row in mycursor.fetchall():
            self.registered_section_students_window.registered_section_section_name.setText(row[0])
            self.registered_section_students_window.registered_section_course_name.setText(row[1])
            self.registered_section_students_window.registered_section_teacher_name.setText(row[2])
        # Load Data and Associate Buttons
        self.get_section_students_data()
        self.registered_section_students_window.add_registered_section_student.clicked.connect(self.executeAddSectionStudentPage)
        self.registered_section_students_window.delete_all_registered_section_student.clicked.connect(self.deleteAllStudents)
        self.registered_section_students_window.registered_section_student_search_text.textChanged.connect(self.SectionStudentSearch)
        self.window.show()
        
    
    def get_section_students_data(self):
        mycursor = self.DB.cursor()
        Subquery = "select id, roll_number from tbl_section_students where registered_id = %s"
        val = (self.course_selected, )
        #mycursor.execute(Subquery, val)
        numcols = 3
        mycursor.execute(Subquery, val)
        numrows = len(mycursor.fetchall())
        self.registered_section_students_window.registered_section_student_table.setRowCount(numrows)
        self.registered_section_students_window.registered_section_student_table.setColumnCount(numcols+1)
        mycursor.execute(Subquery, val)
        tablerow = 0
        for row in mycursor.fetchall():
            delete_button = QtWidgets.QPushButton("Delete")
            delete_button.clicked.connect(self.on_registered_section_student_delete_button)
            icon_delete = QIcon()
            icon_delete.addFile(u":/icons/icons/Delete-button.png", QSize(), QIcon.Normal, QIcon.Off)
            #delete_button.PySide2.QtGui.setIcon(icon_delete)
            #layout.addWidget(delete_button)
            edit_button = QtWidgets.QPushButton("Edit")
            #edit_button.clicked.connect(self.on_registered_section_student_edit_click())
            icon_edit =QIcon()
            icon_edit.addFile(u":/icons/icons/edit-button.png", QSize(), QIcon.Normal, QIcon.Off)
            #edit_button.setIcon(icon_edit)
            #layout.addWidget(edit_button)
            #cellWidget = QWidget()
            #cellWidget.setLayout(layout)
            delete_button.setStyleSheet("background-color: transparent; border-style: none")
            self.registered_section_students_window.registered_section_student_table.setCellWidget(tablerow, 3, delete_button)
            #self.registered_section_students_window.registered_section_student_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            #self.registered_section_students_window.registered_section_student_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(tablerow)))
            self.registered_section_students_window.registered_section_student_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[1])))
            tablerow += 1
        self.registered_section_students_window.registered_section_student_table.setColumnHidden(0, True)
        self.registered_section_students_window.registered_section_student_table.setColumnHidden(1, True)

        self.registered_section_students_window.registered_section_student_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        #self.registered_section_students_window.registered_section_student_table.resizeColumnsToContents()

    # Execute the "Add Section Student Course" Page
    def executeAddSectionStudentPage(self):
        self.window2 = QtWidgets.QMainWindow()
        self.add_section_student_form = Ui_Add_Section_Student_Window()
        self.add_section_student_form.setupUi(self.window2)
        self.window2.show()
        self.add_section_student_form.add_section_student_submit.clicked.connect(self.insert_section_student_info)


    # Section Student Add Function
    def insert_section_student_info(self):
        roll_number = self.add_section_student_form.add_section_student_name.text()
        mycursor = self.DB.cursor()
        sql = "insert into tbl_section_students (roll_number, registered_id)"
        sql += "values (%s, %s)"
        val = (roll_number, self.course_selected)
        mycursor.execute(sql, val)
        self.DB.commit()
        self.window2.close()
        self.registered_section_students_window.registered_section_student_table.setRowCount(0)
        self.get_section_students_data() # Reload the Table
        self.SectionStudentSearch()   

    def deleteAllStudents(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Are you sure you want to delete all the Students of this section?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        if (msg.exec_() == 16384): # Means "YES"
            mycursor = self.DB.cursor()
            sql = "Delete from tbl_section_students where registered_id = %s"
            val = (self.course_selected, )
            mycursor.execute(sql, val)
            self.DB.commit()
            self.registered_section_students_window.registered_section_student_table.setRowCount(0)
            self.get_section_students_data()
            self.SectionStudentSearch()
            self.ui.header_label_notification.setText("All Students Deleted")
            self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
            "background-color: rgb(198, 13, 0);\n"
            "padding-bottom: 10px; ")
            self.ui.header_label_notification.show() 
            self.fade(self.ui.header_label_notification) 
    
    def on_registered_section_student_delete_button(self):
        
        selected = self.registered_section_students_window.registered_section_student_table.selectionModel().selectedIndexes()[0]
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Are you sure you want to delete the selected Student from this Section?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        if (msg.exec_() == 16384): # Means "YES"
            mycursor = self.DB.cursor()
            roll_num = self.registered_section_students_window.registered_section_student_table.item(selected.row(), 2).text()
            sql = "Delete from tbl_section_students where roll_number = %s and registered_id = %s"
            val = (roll_num, self.course_selected)
            #print(self.registered_section_students_window.registered_section_student_table.item(selected.row(), 0).text())
            mycursor.execute(sql, val)
            self.DB.commit()
            self.registered_section_students_window.registered_section_student_table.setRowCount(0)
            self.get_section_students_data()
            self.SectionStudentSearch()
            print("Deleted")
        else:
            print("Not Deleted")

    # Section Student Search Function 
    def SectionStudentSearch(self):
        search_text = self.registered_section_students_window.registered_section_student_search_text.text().lower()
        for row in range(self.registered_section_students_window.registered_section_student_table.rowCount()):
            roll_number = self.registered_section_students_window.registered_section_student_table.item(row, 2)
            if (search_text not in roll_number.text().lower()):
                self.registered_section_students_window.registered_section_student_table.setRowHidden(row, True)
            else:
                self.registered_section_students_window.registered_section_student_table.setRowHidden(row, False)

    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            #self.ui.restore_window_button.setIcon()
        else:
            self.showMaximized()
            #self.ui.restore_window_button.setIcon()

   

######################################################################
#############---------ROOM PREFERENCES MENU-------------##############
######################################################################

# Navigate to Room Preferences Menu
    def navigate_to_room_preferences_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.room_preferences_page)
        self.clear_all_buttons_stylesheet()
        self.ui.room_preference_menu_button.setStyleSheet("padding-left: 15px; color: cyan; border-bottom: 1px solid cyan; border-left: 1px solid cyan;")
        self.default_icons()
        icon = QIcon()
        icon.addFile(u":/icons/icons/New folder/room_icon_active.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.room_preference_menu_button.setIcon(icon)
        self.ui.room_preference_menu_button.setIconSize(QSize(32, 32))
        self.ui.room_preferences_table.setRowCount(0)
        self.get_room_preferences_data()

    def get_room_preferences_data(self):
        mycursor = self.DB.cursor()
        Subquery = "select teacher_id, teacher_name "
        Subquery += " from tbl_teacher"
        mycursor.execute(Subquery)
        numcols = len(mycursor.fetchall()[0])
        mycursor.execute(Subquery)
        numrows = len(mycursor.fetchall())
        self.ui.room_preferences_table.setRowCount(numrows)
        self.ui.room_preferences_table.setColumnCount(numcols+2)
        mycursor.execute(Subquery)
        tablerow = 0
        for row in mycursor.fetchall():
            layout = QHBoxLayout()
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(0)
            # Button for Get Preferences
            get_preferences = QPushButton(".Edit Preferences.")
            get_preferences.clicked.connect(self.executeRoomPreferencesPage)
            get_preferences.setStyleSheet(primary_push_button)
            self.ui.room_preferences_table.setItem(tablerow, 0, PySide2.QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.room_preferences_table.setItem(tablerow, 1, PySide2.QtWidgets.QTableWidgetItem(str(tablerow+1)))
            self.ui.room_preferences_table.setItem(tablerow, 2, PySide2.QtWidgets.QTableWidgetItem(str(row[1])))
            self.ui.room_preferences_table.setCellWidget(tablerow, 3, get_preferences)
            tablerow += 1
        self.ui.room_preferences_table.setColumnHidden(0, True)
        #self.ui.room_preferences_table.horizontalHeader().setSectionResizeMode(PySide2.QtWidgets.QHeaderView.Stretch)
        self.ui.room_preferences_table.resizeColumnsToContents()



    # Execute the "Add Room Preferences" Page
    def executeRoomPreferencesPage(self):
        self.window = QtWidgets.QMainWindow()
        self.add_room_preferences = Ui_Add_Room_Preferences_Teacher_Window()
        self.add_room_preferences.setupUi(self.window)
        mycursor = self.DB.cursor()
        index = self.ui.room_preferences_table.selectionModel().selectedIndexes()[0]
        self.teacher_selected = self.ui.room_preferences_table.item(index.row(), 2).text()
        self.add_room_preferences.room_preference_teacher_name.setText("Teacher Name: " + self.teacher_selected)
        query = "select teacher_id from tbl_teacher where teacher_name = %s"
        val = (self.teacher_selected, )
        mycursor.execute(query, val)
        for row in mycursor.fetchall():
            self.teacher_selected = str(row[0])

        self.add_room_preferences.launch_window(self.teacher_selected)
        self.window.show()
        for i in range(0, len(self.add_room_preferences.checkboxes)):
            self.add_room_preferences.checkboxes[i].stateChanged.connect(partial(self.state_changed, 
            self.add_room_preferences.checkbox_ids[i], i))

    def state_changed(self, room_id, checkbox_id):
        mycursor = self.DB.cursor()
        if (self.add_room_preferences.checkboxes[checkbox_id].isChecked() == False):
            query = "delete from junc_room_preferences where teacher_id = %s and room_id = %s"
            val = (int(self.teacher_selected), int(room_id))
            mycursor.execute(query, val)
            print(mycursor.rowcount)
            self.DB.commit()
        else:
            query = "insert into junc_room_preferences (teacher_id, room_id) values (%s, %s)"
            val = (int(self.teacher_selected), int(room_id))
            mycursor.execute(query, val)
            self.DB.commit()       
        self.add_room_preferences.updation_message_label.show()
        self.add_room_preferences.fade(self.add_room_preferences.updation_message_label)

    def deleteAllRoomPreferences(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Are you sure you want to delete all the Room Preferences?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        if (msg.exec_() == 16384): # Means "YES"
            mycursor = self.DB.cursor()
            sql = "Delete from junc_room_preferences"
            mycursor.execute(sql)
            self.DB.commit()
            self.RoomPreferencesSearch()
            self.ui.header_label_notification.setText("All Room Preferences Deleted")
            self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
            "background-color: rgb(198, 13, 0);\n"
            "padding-bottom: 10px; ")
            self.ui.header_label_notification.show() 
            self.fade(self.ui.header_label_notification)
    # Room Preferences Search Function 
    def RoomPreferencesSearch(self):
        search_text = self.ui.room_preferences_search_text.text().lower()
        for row in range(self.ui.room_preferences_table.rowCount()):
            teacher = self.ui.room_preferences_table.item(row, 2)
            if (search_text not in teacher.text().lower()):
                self.ui.room_preferences_table.setRowHidden(row, True)
            else:
                self.ui.room_preferences_table.setRowHidden(row, False)


######################################################################
#############---------SLOT PREFERENCES MENU-------------##############
######################################################################

# Navigate to Slot Preferences Menu
    def navigate_to_slot_preferences_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.slot_preferences_page)
        self.clear_all_buttons_stylesheet()
        self.ui.slot_preference_menu_button.setStyleSheet("padding-left: 15px; color: cyan; border-bottom: 1px solid cyan; border-left: 1px solid cyan;")
        self.default_icons()
        icon = QIcon()
        icon.addFile(u":/icons/icons/New folder/slot_preference_icon_active.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.slot_preference_menu_button.setIcon(icon)
        self.ui.slot_preference_menu_button.setIconSize(QSize(32, 32))
        self.ui.slot_preferences_table.setRowCount(0)
        self.get_slot_preferences_data()

    def get_slot_preferences_data(self):
        mycursor = self.DB.cursor()
        Subquery = "select teacher_id, teacher_name "
        Subquery += " from tbl_teacher"
        mycursor.execute(Subquery)
        numcols = len(mycursor.fetchall()[0])
        mycursor.execute(Subquery)
        numrows = len(mycursor.fetchall())
        self.ui.slot_preferences_table.setRowCount(numrows)
        self.ui.slot_preferences_table.setColumnCount(numcols+2)
        mycursor.execute(Subquery)
        tablerow = 0
        for row in mycursor.fetchall():
            layout = QHBoxLayout()
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(0)
            # Button for Get Preferences
            get_preferences = QPushButton(".Edit Preferences.")
            get_preferences.clicked.connect(self.executeSlotPreferencesPage)
            get_preferences.setStyleSheet(primary_push_button)
            self.ui.slot_preferences_table.setItem(tablerow, 0, PySide2.QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.slot_preferences_table.setItem(tablerow, 1, PySide2.QtWidgets.QTableWidgetItem(str(tablerow+1)))
            self.ui.slot_preferences_table.setItem(tablerow, 2, PySide2.QtWidgets.QTableWidgetItem(str(row[1])))
            self.ui.slot_preferences_table.setCellWidget(tablerow, 3, get_preferences)
            tablerow += 1
        self.ui.slot_preferences_table.setColumnHidden(0, True)
        #self.ui.slot_preferences_table.horizontalHeader().setSectionResizeMode(PySide2.QtWidgets.QHeaderView.Stretch)
        self.ui.slot_preferences_table.resizeColumnsToContents()



    # Execute the "Add Slot Preferences" Page
    def executeSlotPreferencesPage(self):
        self.window = QtWidgets.QMainWindow()
        self.add_slot_preferences = Ui_Add_Slot_PReferences_Teacher_Window()
        self.add_slot_preferences.setupUi(self.window)
        mycursor = self.DB.cursor()
        index = self.ui.slot_preferences_table.selectionModel().selectedIndexes()[0]
        self.teacher_selected = self.ui.slot_preferences_table.item(index.row(), 2).text()
        self.add_slot_preferences.slot_preference_teacher_name.setText("Teacher Name: " + self.teacher_selected)
        query = "select teacher_id from tbl_teacher where teacher_name = %s"
        val = (self.teacher_selected, )
        mycursor.execute(query, val)
        for row in mycursor.fetchall():
            self.teacher_selected = str(row[0])

        self.add_slot_preferences.launch_window(self.teacher_selected)
        self.window.show()
        self.add_slot_preferences.slot_preference_table.cellClicked.connect(self.Cell_Clicked)
    def Cell_Clicked(self, row, col):
        value = self.add_slot_preferences.slot_preference_table.item(row, col).text()
        mycursor = self.DB.cursor()
        if (value == "Available"):
            query = "insert into junc_slot_preferences (teacher_id, day_id, slot_id) values (%s, %s, %s)"
            val = (int(self.teacher_selected), int(row+1), int(col+1))
            mycursor.execute(query, val)
            print(mycursor.rowcount)
            self.DB.commit()
            self.add_slot_preferences.slot_preference_table.setItem(row, col, QtWidgets.QTableWidgetItem(str("Not Available")))
            self.add_slot_preferences.slot_preference_table.item(row, col).setBackground(QtGui.QColor(217, 83, 79))       
        else:
            query = "delete from junc_slot_preferences where teacher_id = %s and day_id = %s and slot_id = %s"
            val = (int(self.teacher_selected), int(row+1), int(col+1))
            mycursor.execute(query, val)
            self.DB.commit()    
            self.add_slot_preferences.slot_preference_table.setItem(row, col, QtWidgets.QTableWidgetItem(str("Available")))
            self.add_slot_preferences.slot_preference_table.item(row, col).setBackground(QtGui.QColor(92, 184, 92))
        self.add_slot_preferences.updation_message_label.show()
        self.add_slot_preferences.fade(self.add_slot_preferences.updation_message_label)

    def deleteAllSlotPreferences(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Are you sure you want to delete all the Slot Preferences?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        if (msg.exec_() == 16384): # Means "YES"
            mycursor = self.DB.cursor()
            sql = "Delete from junc_slot_preferences"
            mycursor.execute(sql)
            self.DB.commit()
            self.SlotPreferencesSearch()
            self.ui.header_label_notification.setText("All Slot Preferences Deleted")
            self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
            "background-color: rgb(198, 13, 0);\n"
            "padding-bottom: 10px; ")
            self.ui.header_label_notification.show() 
            self.fade(self.ui.header_label_notification)
    # Slot Preferences Search Function 
    def SlotPreferencesSearch(self):
        search_text = self.ui.slot_preferences_search_text.text().lower()
        for row in range(self.ui.slot_preferences_table.rowCount()):
            teacher = self.ui.slot_preferences_table.item(row, 2)
            if (search_text not in teacher.text().lower()):
                self.ui.slot_preferences_table.setRowHidden(row, True)
            else:
                self.ui.slot_preferences_table.setRowHidden(row, False)


######################################################################
#############--------------Student CLASHES PAGE-----------############
######################################################################

# Navigate to Student Clashes Menu
    def navigate_to_student_clashes_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.student_clashes_page)
        self.clear_all_buttons_stylesheet()
        self.ui.student_clash_menu_button.setStyleSheet("padding-left: 15px; color: cyan; border-bottom: 1px solid cyan; border-left: 1px solid cyan;")
        self.default_icons()
        icon = QIcon()
        icon.addFile(u":/icons/icons/New folder/student_icon_active.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.student_clash_menu_button.setIcon(icon)
        self.ui.student_clash_menu_button.setIconSize(QSize(32, 32))
        self.display_student_clashes_data()
    
    def display_student_clashes_data(self):
        arr, count = get_student_clashes_data(timetable, reg_data)
        self.ui.total_student_clashes.setText("Total Clashes: " + str(count))

        # Deleting Previously stored widgets in layouts
        # self.delete_layout_widgets(self.ui.horizontalLayout_50)
        # self.delete_layout_widgets(self.ui.verticalLayout_23)
        # self.delete_layout_widgets(self.ui.verticalLayout_24)
        # self.delete_layout_widgets(self.ui.horizontalLayout_48)
        # self.delete_layout_widgets(self.ui.horizontalLayout_49)
        
        clash_row = 1
        day = 0
        for data in arr:
            day += 1
            slot = 0
            for row in data:
                slot += 1
                for col in row:
                    self.ui.frame_52 = QFrame(self.ui.frame_51)
                    self.ui.frame_52.setObjectName(u"frame_52")
                    if (clash_row % 2 == 0):
                        self.ui.frame_52.setStyleSheet(u"font-size: 17px;\n"
                "background-color: rgb(226, 226, 226);")
                    else:
                        self.ui.frame_52.setStyleSheet(u"font-size: 17px;\n"
                "background-color: rgb(255, 255, 255);")
                    self.ui.frame_52.setFrameShape(QFrame.StyledPanel)
                    self.ui.frame_52.setFrameShadow(QFrame.Raised)
                    self.ui.verticalLayout_24 = QVBoxLayout(self.ui.frame_52)
                    self.ui.verticalLayout_24.setSpacing(0)
                    self.ui.verticalLayout_24.setObjectName(u"verticalLayout_24")
                    self.ui.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
                    self.ui.frame_53 = QFrame(self.ui.frame_52)
                    self.ui.frame_53.setObjectName(u"frame_53")
                    self.ui.frame_53.setStyleSheet(u"font-weight: 500;")
                    self.ui.frame_53.setFrameShape(QFrame.StyledPanel)
                    self.ui.frame_53.setFrameShadow(QFrame.Raised)
                    self.ui.horizontalLayout_48 = QHBoxLayout(self.ui.frame_53)
                    self.ui.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
                    self.ui.label_12 = QLabel(self.ui.frame_53)
                    self.ui.label_12.setObjectName(u"label_12")
                    # Encrypting the Roll Number 
                    encStudent = col[0][:1] + 'Z' + col[0][4:6]
                    self.ui.label_12.setText("Roll Number: " + encStudent + "\t\t"
                     + get_day(day) + "\tSlot # 0" + str(slot))
                    self.ui.horizontalLayout_48.addWidget(self.ui.label_12)

                    self.ui.label_13 = QLabel(self.ui.frame_53)
                    self.ui.label_13.setObjectName(u"label_13")
                    self.ui.label_13.setText("#"+str(clash_row))

                    self.ui.horizontalLayout_48.addWidget(self.ui.label_13, 0, Qt.AlignRight)


                    self.ui.verticalLayout_24.addWidget(self.ui.frame_53, 0, Qt.AlignTop)

                    self.ui.frame_54 = QFrame(self.ui.frame_52)
                    self.ui.frame_54.setObjectName(u"frame_54")
                    self.ui.frame_54.setFrameShape(QFrame.StyledPanel)
                    self.ui.frame_54.setFrameShadow(QFrame.Raised)
                    self.ui.horizontalLayout_49 = QHBoxLayout(self.ui.frame_54)
                    self.ui.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
                    self.ui.label_14 = QLabel(self.ui.frame_54)
                    self.ui.label_14.setObjectName(u"label_14")
                    self.ui.label_14.setText("Course: " + col[1] + " ( " + col[2] + " )")
                    self.ui.horizontalLayout_49.addWidget(self.ui.label_14, 0, Qt.AlignTop)


                    self.ui.verticalLayout_24.addWidget(self.ui.frame_54)

                    self.ui.frame_55 = QFrame(self.ui.frame_52)
                    self.ui.frame_55.setObjectName(u"frame_55")
                    self.ui.frame_55.setFrameShape(QFrame.StyledPanel)
                    self.ui.frame_55.setFrameShadow(QFrame.Raised)
                    self.ui.horizontalLayout_50 = QHBoxLayout(self.ui.frame_55)
                    self.ui.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
                    self.ui.label_15 = QLabel(self.ui.frame_55)
                    self.ui.label_15.setObjectName(u"label_15")
                    self.ui.label_15.setText("Course: " + col[3] + " ( " + col[4] + " )")
                    self.ui.horizontalLayout_50.addWidget(self.ui.label_15, 0, Qt.AlignTop)


                    self.ui.verticalLayout_24.addWidget(self.ui.frame_55)


                    self.ui.verticalLayout_23.addWidget(self.ui.frame_52, 0, Qt.AlignTop)



                    clash_row += 1
        


######################################################################
#############--------------Teacher CLASHES PAGE-----------############
######################################################################

# Navigate to Teacher Clashes Menu
    def navigate_to_teacher_clashes_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.teacher_clashes_page)
        self.clear_all_buttons_stylesheet()
        self.ui.instructor_clash_menu_button.setStyleSheet("padding-left: 15px; color: cyan; border-bottom: 1px solid cyan; border-left: 1px solid cyan;")
        self.default_icons()
        icon = QIcon()
        icon.addFile(u":/icons/icons/New folder/teacher_icon_active.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.instructor_clash_menu_button.setIcon(icon)
        self.ui.instructor_clash_menu_button.setIconSize(QSize(32, 32))
        self.display_teacher_clashes_data()
    
    def display_teacher_clashes_data(self):
        arr, count = get_teacher_clashes_data(timetable, reg_data)
        self.ui.total_teacher_clashes.setText("Total Clashes: " + str(count))
        
        clash_row = 1
        day = 0
        for data in arr:
            day += 1
            slot = 0
            for row in data:
                slot += 1
                for col in row:
                    self.ui.frame_52 = QFrame(self.ui.frame_51)
                    self.ui.frame_52.setObjectName(u"frame_52")
                    if (clash_row % 2 == 0):
                        self.ui.frame_52.setStyleSheet(u"font-size: 17px;\n"
                "background-color: rgb(226, 226, 226);")
                    else:
                        self.ui.frame_52.setStyleSheet(u"font-size: 17px;\n"
                "background-color: rgb(255, 255, 255);")
                    self.ui.frame_52.setFrameShape(QFrame.StyledPanel)
                    self.ui.frame_52.setFrameShadow(QFrame.Raised)
                    self.ui.verticalLayout_24 = QVBoxLayout(self.ui.frame_52)
                    self.ui.verticalLayout_24.setSpacing(0)
                    self.ui.verticalLayout_24.setObjectName(u"verticalLayout_24")
                    self.ui.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
                    self.ui.frame_53 = QFrame(self.ui.frame_52)
                    self.ui.frame_53.setObjectName(u"frame_53")
                    self.ui.frame_53.setStyleSheet(u"font-weight: 500;")
                    self.ui.frame_53.setFrameShape(QFrame.StyledPanel)
                    self.ui.frame_53.setFrameShadow(QFrame.Raised)
                    self.ui.horizontalLayout_48 = QHBoxLayout(self.ui.frame_53)
                    self.ui.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
                    self.ui.label_12 = QLabel(self.ui.frame_53)
                    self.ui.label_12.setObjectName(u"label_12")
                    self.ui.label_12.setText("Teacher Name: " + col[0] + "\t\t"
                     + get_day(day) + "\tSlot # 0" + str(slot))
                    self.ui.horizontalLayout_48.addWidget(self.ui.label_12)

                    self.ui.label_13 = QLabel(self.ui.frame_53)
                    self.ui.label_13.setObjectName(u"label_13")
                    self.ui.label_13.setText("#"+str(clash_row))

                    self.ui.horizontalLayout_48.addWidget(self.ui.label_13, 0, Qt.AlignRight)


                    self.ui.verticalLayout_24.addWidget(self.ui.frame_53, 0, Qt.AlignTop)

                    self.ui.frame_54 = QFrame(self.ui.frame_52)
                    self.ui.frame_54.setObjectName(u"frame_54")
                    self.ui.frame_54.setFrameShape(QFrame.StyledPanel)
                    self.ui.frame_54.setFrameShadow(QFrame.Raised)
                    self.ui.horizontalLayout_49 = QHBoxLayout(self.ui.frame_54)
                    self.ui.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
                    self.ui.label_14 = QLabel(self.ui.frame_54)
                    self.ui.label_14.setObjectName(u"label_14")
                    self.ui.label_14.setText("Course: " + col[1] + " ( " + col[2] + " )")
                    self.ui.horizontalLayout_49.addWidget(self.ui.label_14, 0, Qt.AlignTop)


                    self.ui.verticalLayout_24.addWidget(self.ui.frame_54)

                    self.ui.frame_55 = QFrame(self.ui.frame_52)
                    self.ui.frame_55.setObjectName(u"frame_55")
                    self.ui.frame_55.setFrameShape(QFrame.StyledPanel)
                    self.ui.frame_55.setFrameShadow(QFrame.Raised)
                    self.ui.horizontalLayout_50 = QHBoxLayout(self.ui.frame_55)
                    self.ui.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
                    self.ui.label_15 = QLabel(self.ui.frame_55)
                    self.ui.label_15.setObjectName(u"label_15")
                    self.ui.label_15.setText("Course: " + col[3] + " ( " + col[4] + " )")
                    self.ui.horizontalLayout_50.addWidget(self.ui.label_15, 0, Qt.AlignTop)


                    self.ui.verticalLayout_24.addWidget(self.ui.frame_55)


                    self.ui.verticalLayout_25.addWidget(self.ui.frame_52, 0, Qt.AlignTop)



                    clash_row += 1



######################################################################
#############--------------Room CLASHES PAGE-----------###############
######################################################################

# Navigate to Room Clashes Menu
    def navigate_to_room_clashes_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.room_clashes_page)
        self.clear_all_buttons_stylesheet()
        self.ui.room_clash_menu_button.setStyleSheet("padding-left: 15px; color: cyan; border-bottom: 1px solid cyan; border-left: 1px solid cyan;")
        self.default_icons()
        icon = QIcon()
        icon.addFile(u":/icons/icons/New folder/room_icon_active.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.room_clash_menu_button.setIcon(icon)
        self.ui.room_clash_menu_button.setIconSize(QSize(32, 32))
        self.display_room_clashes_data()
    
    def display_room_clashes_data(self):
        arr, count = get_room_clashes_data(timetable, reg_data)
        self.ui.total_room_clashes.setText("Total Clashes: " + str(count))
        
        clash_row = 1
        day = 0
        for data in arr:
            day += 1
            slot = 0
            for row in data:
                slot += 1
                for col in row:
                    self.ui.frame_52 = QFrame(self.ui.frame_51)
                    self.ui.frame_52.setObjectName(u"frame_52")
                    if (clash_row % 2 == 0):
                        self.ui.frame_52.setStyleSheet(u"font-size: 17px;\n"
                "background-color: rgb(226, 226, 226);")
                    else:
                        self.ui.frame_52.setStyleSheet(u"font-size: 17px;\n"
                "background-color: rgb(255, 255, 255);")
                    self.ui.frame_52.setFrameShape(QFrame.StyledPanel)
                    self.ui.frame_52.setFrameShadow(QFrame.Raised)
                    self.ui.verticalLayout_24 = QVBoxLayout(self.ui.frame_52)
                    self.ui.verticalLayout_24.setSpacing(0)
                    self.ui.verticalLayout_24.setObjectName(u"verticalLayout_24")
                    self.ui.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
                    self.ui.frame_53 = QFrame(self.ui.frame_52)
                    self.ui.frame_53.setObjectName(u"frame_53")
                    self.ui.frame_53.setStyleSheet(u"font-weight: 500;")
                    self.ui.frame_53.setFrameShape(QFrame.StyledPanel)
                    self.ui.frame_53.setFrameShadow(QFrame.Raised)
                    self.ui.horizontalLayout_48 = QHBoxLayout(self.ui.frame_53)
                    self.ui.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
                    self.ui.label_12 = QLabel(self.ui.frame_53)
                    self.ui.label_12.setObjectName(u"label_12")
                    self.ui.label_12.setText("Room Name: " + col[0] + "\t\t"
                     + get_day(day) + "\tSlot # 0" + str(slot))
                    self.ui.horizontalLayout_48.addWidget(self.ui.label_12)

                    self.ui.label_13 = QLabel(self.ui.frame_53)
                    self.ui.label_13.setObjectName(u"label_13")
                    self.ui.label_13.setText("#"+str(clash_row))

                    self.ui.horizontalLayout_48.addWidget(self.ui.label_13, 0, Qt.AlignRight)


                    self.ui.verticalLayout_24.addWidget(self.ui.frame_53, 0, Qt.AlignTop)

                    self.ui.frame_54 = QFrame(self.ui.frame_52)
                    self.ui.frame_54.setObjectName(u"frame_54")
                    self.ui.frame_54.setFrameShape(QFrame.StyledPanel)
                    self.ui.frame_54.setFrameShadow(QFrame.Raised)
                    self.ui.horizontalLayout_49 = QHBoxLayout(self.ui.frame_54)
                    self.ui.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
                    self.ui.label_14 = QLabel(self.ui.frame_54)
                    self.ui.label_14.setObjectName(u"label_14")
                    self.ui.label_14.setText("Course: " + col[1] + " ( " + col[2] + " )")
                    self.ui.horizontalLayout_49.addWidget(self.ui.label_14, 0, Qt.AlignTop)


                    self.ui.verticalLayout_24.addWidget(self.ui.frame_54)

                    self.ui.frame_55 = QFrame(self.ui.frame_52)
                    self.ui.frame_55.setObjectName(u"frame_55")
                    self.ui.frame_55.setFrameShape(QFrame.StyledPanel)
                    self.ui.frame_55.setFrameShadow(QFrame.Raised)
                    self.ui.horizontalLayout_50 = QHBoxLayout(self.ui.frame_55)
                    self.ui.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
                    self.ui.label_15 = QLabel(self.ui.frame_55)
                    self.ui.label_15.setObjectName(u"label_15")
                    self.ui.label_15.setText("Course: " + col[3] + " ( " + col[4] + " )")
                    self.ui.horizontalLayout_50.addWidget(self.ui.label_15, 0, Qt.AlignTop)


                    self.ui.verticalLayout_24.addWidget(self.ui.frame_55)


                    self.ui.verticalLayout_27.addWidget(self.ui.frame_52, 0, Qt.AlignTop)



                    clash_row += 1



######################################################################
#############--------------Print Sections Timetable-----------########
######################################################################

    def navigate_to_sections_timetable_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.sections_timetable_page)
        self.clear_all_buttons_stylesheet()
        self.ui.view_section_timetable.setStyleSheet("padding-left: 15px; color: cyan; border-bottom: 1px solid cyan; border-left: 1px solid cyan;")


    def print_sections_timetable(self):
        sections_timetable.execute_function()
        self.ui.header_label_notification.setText("Sections Timetable Generated")
        self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
        "background-color: rgb(41, 182, 31);\n"
        "padding-bottom: 10px; ")
        self.ui.header_label_notification.show() 
        self.fade(self.ui.header_label_notification)


######################################################################
#############--------------Print Rooms Timetable--------------########
######################################################################

    def navigate_to_rooms_timetable_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.rooms_timetable_page)
        self.clear_all_buttons_stylesheet()
        self.ui.view_room_timetable.setStyleSheet("padding-left: 15px; color: cyan; border-bottom: 1px solid cyan; border-left: 1px solid cyan;")


    def print_rooms_timetable(self):
        rooms_timetable.execute_function()
        self.ui.header_label_notification.setText("Rooms Timetable Generated")
        self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
        "background-color: rgb(41, 182, 31);\n"
        "padding-bottom: 10px; ")
        self.ui.header_label_notification.show() 
        self.fade(self.ui.header_label_notification)



######################################################################
#############------------Print Teachers Timetable-------------########
######################################################################

    def navigate_to_teachers_timetable_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.teachers_timetable_page)
        self.clear_all_buttons_stylesheet()
        self.ui.view_teacher_timetable.setStyleSheet("padding-left: 15px; color: cyan; border-bottom: 1px solid cyan; border-left: 1px solid cyan;")


    def print_teachers_timetable(self):
        teachers_timetable.execute_function()
        self.ui.header_label_notification.setText("Teachers Timetable Generated")
        self.ui.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
        "background-color: rgb(41, 182, 31);\n"
        "padding-bottom: 10px; ")
        self.ui.header_label_notification.show() 
        self.fade(self.ui.header_label_notification)




######################################################################
#############--------------Utility Functions-----------###############
######################################################################

    def loading_button(self, status):
        anim = ico.anim.Spin()
        if status == True:
            self.loading_icon = ico.Icon('feather:loader', color=IconQtGui.QColor('white'), anim=anim)
            self.loading_icon.setAsButtonIcon(self.ui.loading_button)
            anim.start() 
            self.ui.loading_button.setIconSize(QSize(48, 48))
            self.ui.loading_button.setText("Loading Content")       
        else:
            self.loading_icon = ico.Icon('feather:loader', color=IconQtGui.QColor('white'), anim=anim)
            self.loading_icon.setAsButtonIcon(self.ui.loading_button)
            anim.start() 
            self.ui.loading_button.setIconSize(QSize(0, 0))
            self.ui.loading_button.setText()       

    def default_icons(self):
        icon = QIcon()
        icon.addFile(u":/icons/icons/New folder/section_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.section_menu_button.setIcon(icon)
        self.ui.section_menu_button.setIconSize(QSize(32, 32))

        icon.addFile(u":/icons/icons/New folder/courses_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.course_menu_button.setIcon(icon)
        self.ui.course_menu_button.setIconSize(QSize(32, 32))

        icon.addFile(u":/icons/icons/New folder/teacher_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.teacher_menu_button.setIcon(icon)
        self.ui.teacher_menu_button.setIconSize(QSize(32, 32))
        self.ui.instructor_clash_menu_button.setIcon(icon)
        self.ui.instructor_clash_menu_button.setIconSize(QSize(32, 32))

        icon.addFile(u":/icons/icons/New folder/room_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.room_menu_button.setIcon(icon)
        self.ui.room_menu_button.setIconSize(QSize(32, 32))
        self.ui.room_clash_menu_button.setIcon(icon)
        self.ui.room_clash_menu_button.setIconSize(QSize(32, 32))

        icon.addFile(u":/icons/icons/New folder/registered_courses.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.registered_menu_button.setIcon(icon)
        self.ui.registered_menu_button.setIconSize(QSize(32, 32))
        
        icon.addFile(u":/icons/icons/New folder/slot_preference_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.slot_preference_menu_button.setIcon(icon)
        self.ui.slot_preference_menu_button.setIconSize(QSize(32, 32))

        icon.addFile(u":/icons/icons/New folder/room_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.room_preference_menu_button.setIcon(icon)
        self.ui.room_preference_menu_button.setIconSize(QSize(32, 32))

        icon.addFile(u":/icons/icons/New folder/student_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.student_clash_menu_button.setIcon(icon)
        self.ui.student_clash_menu_button.setIconSize(QSize(32, 32))

        # icon.addFile(u":/icons/icons/New folder/registration_details_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        # self.ui.toolBox.setItemIcon(0, icon)

        # icon.addFile(u":/icons/icons/New folder/Prefrence_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        # self.ui.toolBox.setItemIcon(1, icon)

        # icon.addFile(u":/icons/icons/New folder/clash_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        # self.ui.toolBox.setItemIcon(2, icon)

        # icon.addFile(u":/icons/icons/New folder/result_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        # self.ui.toolBox.setItemIcon(3, icon)


    def define_icons(self):

        self.ui.header_label_notification.setVisible(False)
        anim = ico.anim.Spin()
        self.loading_icon = ico.Icon('feather:loader', color=IconQtGui.QColor('white'), anim=anim)
        self.ui.loading_button.setIconSize(QSize(0, 0))

        #self.ui.loading_button.setVisible(False)
        # self.ui.minimize_window_button.setIcon(ico.Icon('font-awesome:regular:window-minimize', 
        # color=IconQtGui.QColor('white')))

        # self.ui.close_window_button.setIcon(ico.Icon('font-awesome:regular:window-close', 
        # color=IconQtGui.QColor('white')))

        # self.ui.restore_window_button.setIcon(ico.Icon('font-awesome:regular:window-restore', 
        # color=IconQtGui.QColor('white')))

        self.registration_details_icon = []
        self.registration_details_icon.append(ico.Icon('font-awesome:regular:address-card', 
        color=IconQtGui.QColor('white')))
        self.registration_details_icon.append(ico.Icon('font-awesome:regular:address-card', 
        color=IconQtGui.QColor('aqua')))

        self.teacher_preferences_icon = []
        self.teacher_preferences_icon.append(ico.Icon('font-awesome:solid:chalkboard-teacher'
        ,color=IconQtGui.QColor('white')))

        self.teacher_preferences_icon.append(ico.Icon('font-awesome:solid:chalkboard-teacher'
        ,color=IconQtGui.QColor('aqua')))

        self.view_clashes_icon = []
        self.view_clashes_icon.append(ico.Icon('dash:media-spreadsheet', color=IconQtGui.QColor('white')))
        self.view_clashes_icon.append(ico.Icon('dash:media-spreadsheet', color=IconQtGui.QColor('aqua')))

        self.view_results_icon = []
        self.view_results_icon.append(ico.Icon('dash:schedule', color=IconQtGui.QColor('white')))
        self.view_results_icon.append(ico.Icon('dash:schedule', color=IconQtGui.QColor('aqua')))

    def update_values(self, index):
        self.ui.toolBox.setItemIcon(0, self.registration_details_icon[0])

        self.ui.toolBox.setItemIcon(1, self.teacher_preferences_icon[0])

        self.ui.toolBox.setItemIcon(2, self.view_clashes_icon[0])

        self.ui.toolBox.setItemIcon(3, self.view_results_icon[0])
        
        if (index == 0):
            self.ui.toolBox.setItemIcon(0, self.registration_details_icon[1])

        if (index == 1):
            self.ui.toolBox.setItemIcon(1, self.teacher_preferences_icon[1])

        if (index == 2):
            self.ui.toolBox.setItemIcon(2, self.view_clashes_icon[1])

        if (index == 3):
            self.ui.toolBox.setItemIcon(3, self.view_results_icon[1]) 
    
    def clear_all_buttons_stylesheet(self):
        for x in self.menu_buttons:
            x.setStyleSheet(""); 

    def fade(self, widget):
        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)

        self.animation = PySide2.QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(2500)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()

    


    def delete_layout_widgets(self, layout):
        for i in reversed(range(layout.count())): 
            widgetToRemove = layout.itemAt(i).widget()
            # remove it from the layout list
            layout.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.setParent(None)


## EXECUTE APP  
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())