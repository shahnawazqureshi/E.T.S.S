# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceGufDiZ.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1310, 789)
        MainWindow.setStyleSheet(u"* {\n"
"border: none;\n"
"}\n"
"\n"
".QTableWidget\n"
"{\n"
"alternate-background-color: rgb(241, 241, 241);\n"
"background-color: white;\n"
"selection-background-color: transparent; \n"
"}\n"
"\n"
".QTableWidget:item\n"
"{\n"
"color: black;\n"
"padding: 5px;\n"
"}\n"
"\n"
".QHeaderView::section\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"font-weight: bold;\n"
"border: 0px;\n"
"border-bottom: 1px solid;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: white;")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_menu_container = QFrame(self.centralwidget)
        self.side_menu_container.setObjectName(u"side_menu_container")
        self.side_menu_container.setMaximumSize(QSize(230, 16777215))
        self.side_menu_container.setStyleSheet(u"background-color: #1b1b1b;\n"
"color: white;\n"
"font-size: 18px;\n"
"font-weight: 600;\n"
"text-align: center;\n"
"\n"
"")
        self.side_menu_container.setFrameShape(QFrame.StyledPanel)
        self.side_menu_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.side_menu_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 6, 0, 0)
        self.frame = QFrame(self.side_menu_container)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"margin-top: 5px;\n"
"margin-bottom: 10px;\n"
"margin-right: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(-1, 0, 0, 0)
        self.frame_46 = QFrame(self.frame)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setStyleSheet(u"font-size: 21px;\n"
"")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_46)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_46)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamily(u"Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font-size: 20px;\n"
"text-align: center;")

        self.verticalLayout_4.addWidget(self.label_2, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_42.addWidget(self.frame_46, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_45 = QFrame(self.side_menu_container)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setStyleSheet(u"background-color: #1e1e1e;")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_45)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.side_menu = QFrame(self.frame_45)
        self.side_menu.setObjectName(u"side_menu")
        self.side_menu.setMinimumSize(QSize(228, 0))
        self.side_menu.setStyleSheet(u"QPushButton\n"
"{\n"
"font-size: 16px;\n"
"padding: 5px 10px;\n"
"padding-top: 15px;\n"
"border-bottom: 1px solid rgba(255, 255, 255, 0.1);\n"
"color: #fff; \n"
"border-left: 1px solid transparent;\n"
"text-align: left; \n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: cyan;\n"
"color: black;\n"
"padding-left: 20px;\n"
"border-left: 1px solid cyan;\n"
" \n"
"}\n"
"\n"
"QToolBox:tab\n"
"{\n"
"border: none;\n"
"}\n"
"\n"
"QToolBox:tab::selected\n"
"{\n"
"color: cyan;\n"
"border-bottom: 1px solid rgb(176, 176, 176);\n"
"}\n"
"")
        self.side_menu.setFrameShape(QFrame.StyledPanel)
        self.side_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.side_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 0)
        self.frame_4 = QFrame(self.side_menu)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.toolBox = QToolBox(self.frame_4)
        self.toolBox.setObjectName(u"toolBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy1)
        self.toolBox.setMaximumSize(QSize(16777215, 1000))
        self.toolBox.setFont(font)
        self.toolBox.setLayoutDirection(Qt.LeftToRight)
        self.toolBox.setStyleSheet(u"icon-size: 30px; \n"
"")
        self.toolBox.setFrameShape(QFrame.NoFrame)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 213, 284))
        self.page_2.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.frame_5 = QFrame(self.page_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_5)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, -1, 0, 0)
        self.section_menu_button = QPushButton(self.frame_5)
        self.section_menu_button.setObjectName(u"section_menu_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.section_menu_button.sizePolicy().hasHeightForWidth())
        self.section_menu_button.setSizePolicy(sizePolicy2)
        self.section_menu_button.setFont(font)
        self.section_menu_button.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/New folder/section_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.section_menu_button.setIcon(icon)
        self.section_menu_button.setIconSize(QSize(32, 32))

        self.verticalLayout_19.addWidget(self.section_menu_button)

        self.course_menu_button = QPushButton(self.frame_5)
        self.course_menu_button.setObjectName(u"course_menu_button")
        self.course_menu_button.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/New folder/courses_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.course_menu_button.setIcon(icon1)

        self.verticalLayout_19.addWidget(self.course_menu_button)

        self.room_menu_button = QPushButton(self.frame_5)
        self.room_menu_button.setObjectName(u"room_menu_button")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/New folder/room_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.room_menu_button.setIcon(icon2)

        self.verticalLayout_19.addWidget(self.room_menu_button)

        self.teacher_menu_button = QPushButton(self.frame_5)
        self.teacher_menu_button.setObjectName(u"teacher_menu_button")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/New folder/teacher_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.teacher_menu_button.setIcon(icon3)

        self.verticalLayout_19.addWidget(self.teacher_menu_button)

        self.registered_menu_button = QPushButton(self.frame_5)
        self.registered_menu_button.setObjectName(u"registered_menu_button")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/New folder/registered_courses.png", QSize(), QIcon.Normal, QIcon.Off)
        self.registered_menu_button.setIcon(icon4)

        self.verticalLayout_19.addWidget(self.registered_menu_button)


        self.verticalLayout_6.addWidget(self.frame_5, 0, Qt.AlignTop)

        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/New folder/registration_details_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_2, icon5, u"Registration Details")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, -13, 207, 144))
        self.verticalLayout_13 = QVBoxLayout(self.page_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, -1, 0, -1)
        self.frame_32 = QFrame(self.page_3)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_32)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, -1, 0, -1)
        self.room_preference_menu_button = QPushButton(self.frame_32)
        self.room_preference_menu_button.setObjectName(u"room_preference_menu_button")
        self.room_preference_menu_button.setIcon(icon2)

        self.verticalLayout_14.addWidget(self.room_preference_menu_button)

        self.slot_preference_menu_button = QPushButton(self.frame_32)
        self.slot_preference_menu_button.setObjectName(u"slot_preference_menu_button")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/New folder/slot_preference_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.slot_preference_menu_button.setIcon(icon6)

        self.verticalLayout_14.addWidget(self.slot_preference_menu_button)


        self.verticalLayout_13.addWidget(self.frame_32, 0, Qt.AlignTop)

        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/New folder/Prefrence_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_3, icon7, u"Preferences")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 228, 168))
        self.verticalLayout_17 = QVBoxLayout(self.page)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, -1, 0, -1)
        self.frame_43 = QFrame(self.page)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_43)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, -1, 0, -1)
        self.student_clash_menu_button = QPushButton(self.frame_43)
        self.student_clash_menu_button.setObjectName(u"student_clash_menu_button")

        self.verticalLayout_18.addWidget(self.student_clash_menu_button)

        self.room_clash_menu_button = QPushButton(self.frame_43)
        self.room_clash_menu_button.setObjectName(u"room_clash_menu_button")

        self.verticalLayout_18.addWidget(self.room_clash_menu_button)

        self.instructor_clash_menu_button = QPushButton(self.frame_43)
        self.instructor_clash_menu_button.setObjectName(u"instructor_clash_menu_button")

        self.verticalLayout_18.addWidget(self.instructor_clash_menu_button)


        self.verticalLayout_17.addWidget(self.frame_43, 0, Qt.AlignTop)

        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/New folder/clash_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page, icon8, u"View Clashes")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 228, 132))
        self.page_4.setFont(font)
        self.horizontalLayout_62 = QHBoxLayout(self.page_4)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.frame_44 = QFrame(self.page_4)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_44)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.view_section_timetable = QPushButton(self.frame_44)
        self.view_section_timetable.setObjectName(u"view_section_timetable")

        self.verticalLayout_5.addWidget(self.view_section_timetable)

        self.view_teacher_timetable = QPushButton(self.frame_44)
        self.view_teacher_timetable.setObjectName(u"view_teacher_timetable")

        self.verticalLayout_5.addWidget(self.view_teacher_timetable)

        self.view_room_timetable = QPushButton(self.frame_44)
        self.view_room_timetable.setObjectName(u"view_room_timetable")
        self.view_room_timetable.setFont(font)

        self.verticalLayout_5.addWidget(self.view_room_timetable)


        self.horizontalLayout_62.addWidget(self.frame_44)

        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/New folder/result_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_4, icon9, u"Results")

        self.horizontalLayout_43.addWidget(self.toolBox, 0, Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.frame_4)


        self.verticalLayout_20.addWidget(self.side_menu)


        self.verticalLayout_2.addWidget(self.frame_45)


        self.horizontalLayout.addWidget(self.side_menu_container)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_body)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.main_body)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color: #1b1b1b;\n"
"")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.header_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"font-size: 25px;\n"
"color: white;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.loading_button = QPushButton(self.frame_2)
        self.loading_button.setObjectName(u"loading_button")
        self.loading_button.setStyleSheet(u"padding-top: 10px;\n"
"padding-bottom: 10px;")

        self.horizontalLayout_6.addWidget(self.loading_button)

        self.header_label_notification = QLabel(self.frame_2)
        self.header_label_notification.setObjectName(u"header_label_notification")
        self.header_label_notification.setStyleSheet(u"padding-top: 10px;\n"
"background-color: rgb(198, 13, 0);\n"
"padding-bottom: 10px;")

        self.horizontalLayout_6.addWidget(self.header_label_notification)


        self.horizontalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.header_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimize_window_button = QPushButton(self.frame_3)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/arrow-down-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon10)

        self.horizontalLayout_4.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.frame_3)
        self.restore_window_button.setObjectName(u"restore_window_button")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon11)

        self.horizontalLayout_4.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.frame_3)
        self.close_window_button.setObjectName(u"close_window_button")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon12)

        self.horizontalLayout_4.addWidget(self.close_window_button)


        self.horizontalLayout_3.addWidget(self.frame_3, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body_contents = QFrame(self.main_body)
        self.main_body_contents.setObjectName(u"main_body_contents")
        sizePolicy.setHeightForWidth(self.main_body_contents.sizePolicy().hasHeightForWidth())
        self.main_body_contents.setSizePolicy(sizePolicy)
        self.main_body_contents.setFrameShape(QFrame.StyledPanel)
        self.main_body_contents.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.main_body_contents)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(9, -1, -1, -1)
        self.stackedWidget = QStackedWidget(self.main_body_contents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.sections_page = QWidget()
        self.sections_page.setObjectName(u"sections_page")
        self.sections_page.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.sections_page)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_12 = QFrame(self.sections_page)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_3 = QLabel(self.frame_12)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: black;\n"
"")

        self.horizontalLayout_8.addWidget(self.label_3, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_10.addWidget(self.frame_12, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_9 = QFrame(self.sections_page)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy3)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setSpacing(25)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.add_section_button = QPushButton(self.frame_10)
        self.add_section_button.setObjectName(u"add_section_button")
        font2 = QFont()
        font2.setFamily(u"Calibri")
        font2.setBold(False)
        font2.setWeight(50)
        self.add_section_button.setFont(font2)
        self.add_section_button.setStyleSheet(u"QPushButton\n"
"{\n"
" display: inline-block;\n"
"  padding: 6px 12px;\n"
"  margin-bottom: 0;\n"
"  font-size: 18px;\n"
"  font-weight: normal;\n"
"  line-height: 1.42857143;\n"
"  text-align: center;\n"
"  white-space: nowrap;\n"
"  vertical-align: middle;\n"
"  -ms-touch-action: manipulation;\n"
"      touch-action: manipulation;\n"
"  cursor: pointer;\n"
"  -webkit-user-select: none;\n"
"     -moz-user-select: none;\n"
"      -ms-user-select: none;\n"
"          user-select: none;\n"
"  background-image: none;\n"
"  border: 1px solid transparent;\n"
"  border-radius: 4px;\n"
"color: #fff; \n"
"background-color: #5cb85c;\n"
"  border-color: #4cae4c;\n"
"}\n"
"\n"
"\n"
":hover\n"
"{\n"
" color: #fff;\n"
"  background-color: #449d44;\n"
"  border-color: #398439;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/icons8-add-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_section_button.setIcon(icon13)
        self.add_section_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.add_section_button, 0, Qt.AlignLeft)

        self.section_delete_all_button = QPushButton(self.frame_10)
        self.section_delete_all_button.setObjectName(u"section_delete_all_button")
        self.section_delete_all_button.setFont(font2)
        self.section_delete_all_button.setStyleSheet(u"QPushButton\n"
"{\n"
" display: inline-block;\n"
"  padding: 6px 12px;\n"
"  margin-bottom: 0;\n"
"  font-size: 18px;\n"
"  font-weight: normal;\n"
"  line-height: 1.42857143;\n"
"  text-align: center;\n"
"  white-space: nowrap;\n"
"  vertical-align: middle;\n"
"  -ms-touch-action: manipulation;\n"
"      touch-action: manipulation;\n"
"  cursor: pointer;\n"
"  -webkit-user-select: none;\n"
"     -moz-user-select: none;\n"
"      -ms-user-select: none;\n"
"          user-select: none;\n"
"  background-image: none;\n"
"  border: 1px solid transparent;\n"
"  border-radius: 4px;\n"
"color: #fff; \n"
"background-color: #5cb85c;\n"
"  border-color: #4cae4c;\n"
"}\n"
"QPushButton\n"
"{\n"
"color: #fff;\n"
"  background-color: #d9534f;\n"
"  border-color: #d43f3a;\n"
"\n"
"}\n"
"\n"
"\n"
":hover\n"
"{\n"
" color: #fff;\n"
"  background-color: #c9302c;\n"
"  border-color: #ac2925;\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/delete_icon_red.png", QSize(), QIcon.Normal, QIcon.Off)
        self.section_delete_all_button.setIcon(icon14)
        self.section_delete_all_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.section_delete_all_button, 0, Qt.AlignLeft)


        self.horizontalLayout_7.addWidget(self.frame_10, 0, Qt.AlignLeft)

        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.search_section_text = QLineEdit(self.frame_11)
        self.search_section_text.setObjectName(u"search_section_text")
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(11)
        self.search_section_text.setFont(font3)
        self.search_section_text.setStyleSheet(u"background-color: white; \n"
"border-bottom: 1px solid;")

        self.horizontalLayout_10.addWidget(self.search_section_text, 0, Qt.AlignRight)

        self.search_section_button = QPushButton(self.frame_11)
        self.search_section_button.setObjectName(u"search_section_button")
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/icons8-search-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_section_button.setIcon(icon15)
        self.search_section_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.search_section_button, 0, Qt.AlignLeft)


        self.horizontalLayout_7.addWidget(self.frame_11, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_10.addWidget(self.frame_9, 0, Qt.AlignTop)

        self.frame_8 = QFrame(self.sections_page)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.section_table = QTableWidget(self.frame_8)
        if (self.section_table.columnCount() < 3):
            self.section_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.section_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.section_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.section_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.section_table.setObjectName(u"section_table")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.section_table.sizePolicy().hasHeightForWidth())
        self.section_table.setSizePolicy(sizePolicy4)
        self.section_table.setStyleSheet(u"QTableWidget\n"
"{\n"
"font-size: 20px;\n"
"}")
        self.section_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.section_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.section_table.setAlternatingRowColors(True)
        self.section_table.setSortingEnabled(True)
        self.section_table.horizontalHeader().setProperty("showSortIndicator", True)
        self.section_table.verticalHeader().setVisible(False)

        self.horizontalLayout_11.addWidget(self.section_table)


        self.verticalLayout_10.addWidget(self.frame_8)

        self.stackedWidget.addWidget(self.sections_page)
        self.courses_page = QWidget()
        self.courses_page.setObjectName(u"courses_page")
        self.verticalLayout_12 = QVBoxLayout(self.courses_page)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_13 = QFrame(self.courses_page)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_4 = QLabel(self.frame_13)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: black;\n"
"")

        self.horizontalLayout_12.addWidget(self.label_4, 0, Qt.AlignLeft)


        self.verticalLayout_12.addWidget(self.frame_13, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_14 = QFrame(self.courses_page)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_14.setSpacing(25)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.add_course_button = QPushButton(self.frame_16)
        self.add_course_button.setObjectName(u"add_course_button")
        self.add_course_button.setFont(font2)
        self.add_course_button.setStyleSheet(u"QPushButton\n"
"{\n"
" display: inline-block;\n"
"  padding: 6px 12px;\n"
"  margin-bottom: 0;\n"
"  font-size: 18px;\n"
"  font-weight: normal;\n"
"  line-height: 1.42857143;\n"
"  text-align: center;\n"
"  white-space: nowrap;\n"
"  vertical-align: middle;\n"
"  -ms-touch-action: manipulation;\n"
"      touch-action: manipulation;\n"
"  cursor: pointer;\n"
"  -webkit-user-select: none;\n"
"     -moz-user-select: none;\n"
"      -ms-user-select: none;\n"
"          user-select: none;\n"
"  background-image: none;\n"
"  border: 1px solid transparent;\n"
"  border-radius: 4px;\n"
"color: #fff; \n"
"background-color: #5cb85c;\n"
"  border-color: #4cae4c;\n"
"}\n"
"\n"
"\n"
":hover\n"
"{\n"
" color: #fff;\n"
"  background-color: #449d44;\n"
"  border-color: #398439;\n"
"}")
        self.add_course_button.setIcon(icon13)
        self.add_course_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_14.addWidget(self.add_course_button)

        self.course_delete_all_button = QPushButton(self.frame_16)
        self.course_delete_all_button.setObjectName(u"course_delete_all_button")
        self.course_delete_all_button.setFont(font2)
        self.course_delete_all_button.setStyleSheet(u"QPushButton\n"
"{\n"
" display: inline-block;\n"
"  padding: 6px 12px;\n"
"  margin-bottom: 0;\n"
"  font-size: 18px;\n"
"  font-weight: normal;\n"
"  line-height: 1.42857143;\n"
"  text-align: center;\n"
"  white-space: nowrap;\n"
"  vertical-align: middle;\n"
"  -ms-touch-action: manipulation;\n"
"      touch-action: manipulation;\n"
"  cursor: pointer;\n"
"  -webkit-user-select: none;\n"
"     -moz-user-select: none;\n"
"      -ms-user-select: none;\n"
"          user-select: none;\n"
"  background-image: none;\n"
"  border: 1px solid transparent;\n"
"  border-radius: 4px;\n"
"color: #fff; \n"
"background-color: #5cb85c;\n"
"  border-color: #4cae4c;\n"
"}\n"
"QPushButton\n"
"{\n"
"color: #fff;\n"
"  background-color: #d9534f;\n"
"  border-color: #d43f3a;\n"
"\n"
"}\n"
"\n"
"\n"
":hover\n"
"{\n"
" color: #fff;\n"
"  background-color: #c9302c;\n"
"  border-color: #ac2925;\n"
"}\n"
"")
        self.course_delete_all_button.setIcon(icon14)
        self.course_delete_all_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_14.addWidget(self.course_delete_all_button)


        self.horizontalLayout_13.addWidget(self.frame_16, 0, Qt.AlignLeft)

        self.frame_17 = QFrame(self.frame_14)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.course_search_text = QLineEdit(self.frame_17)
        self.course_search_text.setObjectName(u"course_search_text")
        self.course_search_text.setFont(font3)
        self.course_search_text.setStyleSheet(u"background-color: white;\n"
"border-bottom: 1px solid; \n"
"color: black;")

        self.horizontalLayout_15.addWidget(self.course_search_text)

        self.pushButton = QPushButton(self.frame_17)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: white;\n"
"border-style: none; ")
        self.pushButton.setIcon(icon15)
        self.pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_15.addWidget(self.pushButton, 0, Qt.AlignLeft)


        self.horizontalLayout_13.addWidget(self.frame_17, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.frame_14, 0, Qt.AlignTop)

        self.frame_15 = QFrame(self.courses_page)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.course_table = QTableWidget(self.frame_15)
        if (self.course_table.columnCount() < 5):
            self.course_table.setColumnCount(5)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.course_table.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.course_table.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.course_table.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.course_table.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.course_table.setHorizontalHeaderItem(4, __qtablewidgetitem7)
        self.course_table.setObjectName(u"course_table")
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setBold(False)
        font4.setWeight(50)
        font4.setKerning(True)
        self.course_table.setFont(font4)
        self.course_table.setStyleSheet(u"")
        self.course_table.setLineWidth(1)
        self.course_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.course_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.course_table.setAlternatingRowColors(True)
        self.course_table.setGridStyle(Qt.NoPen)
        self.course_table.setSortingEnabled(True)
        self.course_table.setWordWrap(True)
        self.course_table.horizontalHeader().setMinimumSectionSize(47)
        self.course_table.horizontalHeader().setHighlightSections(True)
        self.course_table.horizontalHeader().setStretchLastSection(False)
        self.course_table.verticalHeader().setVisible(False)
        self.course_table.verticalHeader().setCascadingSectionResizes(False)
        self.course_table.verticalHeader().setMinimumSectionSize(28)
        self.course_table.verticalHeader().setHighlightSections(True)
        self.course_table.verticalHeader().setProperty("showSortIndicator", True)
        self.course_table.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_16.addWidget(self.course_table)


        self.verticalLayout_12.addWidget(self.frame_15)

        self.stackedWidget.addWidget(self.courses_page)
        self.rooms_page = QWidget()
        self.rooms_page.setObjectName(u"rooms_page")
        self.verticalLayout_7 = QVBoxLayout(self.rooms_page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_7 = QFrame(self.rooms_page)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.horizontalLayout_17.addWidget(self.label_5)


        self.verticalLayout_7.addWidget(self.frame_7, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_18 = QFrame(self.rooms_page)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(9, -1, 0, -1)
        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_19.setSpacing(25)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.room_add_button = QPushButton(self.frame_20)
        self.room_add_button.setObjectName(u"room_add_button")
        self.room_add_button.setStyleSheet(u"QPushButton\n"
"{\n"
" display: inline-block;\n"
"  padding: 6px 12px;\n"
"  margin-bottom: 0;\n"
"  font-size: 18px;\n"
"  font-weight: normal;\n"
"  line-height: 1.42857143;\n"
"  text-align: center;\n"
"  white-space: nowrap;\n"
"  vertical-align: middle;\n"
"  -ms-touch-action: manipulation;\n"
"      touch-action: manipulation;\n"
"  cursor: pointer;\n"
"  -webkit-user-select: none;\n"
"     -moz-user-select: none;\n"
"      -ms-user-select: none;\n"
"          user-select: none;\n"
"  background-image: none;\n"
"  border: 1px solid transparent;\n"
"  border-radius: 4px;\n"
"color: #fff; \n"
"background-color: #5cb85c;\n"
"  border-color: #4cae4c;\n"
"}\n"
"\n"
"\n"
":hover\n"
"{\n"
" color: #fff;\n"
"  background-color: #449d44;\n"
"  border-color: #398439;\n"
"}")
        self.room_add_button.setIcon(icon13)
        self.room_add_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_19.addWidget(self.room_add_button)

        self.room_delete_all_button = QPushButton(self.frame_20)
        self.room_delete_all_button.setObjectName(u"room_delete_all_button")
        self.room_delete_all_button.setStyleSheet(u"QPushButton\n"
"{\n"
" display: inline-block;\n"
"  padding: 6px 12px;\n"
"  margin-bottom: 0;\n"
"  font-size: 18px;\n"
"  font-weight: normal;\n"
"  line-height: 1.42857143;\n"
"  text-align: center;\n"
"  white-space: nowrap;\n"
"  vertical-align: middle;\n"
"  -ms-touch-action: manipulation;\n"
"      touch-action: manipulation;\n"
"  cursor: pointer;\n"
"  -webkit-user-select: none;\n"
"     -moz-user-select: none;\n"
"      -ms-user-select: none;\n"
"          user-select: none;\n"
"  background-image: none;\n"
"  border: 1px solid transparent;\n"
"  border-radius: 4px;\n"
"color: #fff; \n"
"background-color: #5cb85c;\n"
"  border-color: #4cae4c;\n"
"}\n"
"QPushButton\n"
"{\n"
"color: #fff;\n"
"  background-color: #d9534f;\n"
"  border-color: #d43f3a;\n"
"\n"
"}\n"
"\n"
"\n"
":hover\n"
"{\n"
" color: #fff;\n"
"  background-color: #c9302c;\n"
"  border-color: #ac2925;\n"
"}")
        self.room_delete_all_button.setIcon(icon14)
        self.room_delete_all_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_19.addWidget(self.room_delete_all_button)


        self.horizontalLayout_18.addWidget(self.frame_20, 0, Qt.AlignLeft)

        self.frame_21 = QFrame(self.frame_18)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.room_search_text = QLineEdit(self.frame_21)
        self.room_search_text.setObjectName(u"room_search_text")
        self.room_search_text.setFont(font3)
        self.room_search_text.setStyleSheet(u"border-bottom: 1px solid;")

        self.horizontalLayout_20.addWidget(self.room_search_text, 0, Qt.AlignLeft)

        self.pushButton_6 = QPushButton(self.frame_21)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setIcon(icon15)
        self.pushButton_6.setIconSize(QSize(24, 24))

        self.horizontalLayout_20.addWidget(self.pushButton_6, 0, Qt.AlignLeft)


        self.horizontalLayout_18.addWidget(self.frame_21, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_18, 0, Qt.AlignTop)

        self.frame_19 = QFrame(self.rooms_page)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.room_table = QTableWidget(self.frame_19)
        if (self.room_table.columnCount() < 5):
            self.room_table.setColumnCount(5)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.room_table.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.room_table.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.room_table.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.room_table.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.room_table.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        self.room_table.setObjectName(u"room_table")
        self.room_table.setStyleSheet(u"QTableWidget\n"
"{\n"
"font-size: 20px;\n"
"}")
        self.room_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.room_table.setAlternatingRowColors(True)
        self.room_table.setSortingEnabled(True)
        self.room_table.horizontalHeader().setProperty("showSortIndicator", True)
        self.room_table.verticalHeader().setVisible(False)

        self.horizontalLayout_21.addWidget(self.room_table)


        self.verticalLayout_7.addWidget(self.frame_19)

        self.stackedWidget.addWidget(self.rooms_page)
        self.teachers_page = QWidget()
        self.teachers_page.setObjectName(u"teachers_page")
        self.verticalLayout_8 = QVBoxLayout(self.teachers_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_22 = QFrame(self.teachers_page)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_6 = QLabel(self.frame_22)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.horizontalLayout_22.addWidget(self.label_6)


        self.verticalLayout_8.addWidget(self.frame_22, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_23 = QFrame(self.teachers_page)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(9, 9, 9, 9)
        self.frame_25 = QFrame(self.frame_23)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"QPushButton\n"
"{\n"
"margin-left: 5px;\n"
"}")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_24.setSpacing(25)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 9, 0, 9)
        self.add_teacher_button = QPushButton(self.frame_25)
        self.add_teacher_button.setObjectName(u"add_teacher_button")
        font5 = QFont()
        font5.setBold(False)
        font5.setWeight(50)
        self.add_teacher_button.setFont(font5)
        self.add_teacher_button.setStyleSheet(u"QPushButton\n"
"{\n"
" display: inline-block;\n"
"  padding: 6px 12px;\n"
"  margin-bottom: 0;\n"
"  font-size: 18px;\n"
"  font-weight: normal;\n"
"  line-height: 1.42857143;\n"
"  text-align: center;\n"
"  white-space: nowrap;\n"
"  vertical-align: middle;\n"
"  -ms-touch-action: manipulation;\n"
"      touch-action: manipulation;\n"
"  cursor: pointer;\n"
"  -webkit-user-select: none;\n"
"     -moz-user-select: none;\n"
"      -ms-user-select: none;\n"
"          user-select: none;\n"
"  background-image: none;\n"
"  border: 1px solid transparent;\n"
"  border-radius: 4px;\n"
"color: #fff; \n"
"background-color: #5cb85c;\n"
"  border-color: #4cae4c;\n"
"}\n"
"\n"
"\n"
":hover\n"
"{\n"
" color: #fff;\n"
"  background-color: #449d44;\n"
"  border-color: #398439;\n"
"}\n"
"")
        self.add_teacher_button.setIcon(icon13)
        self.add_teacher_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_24.addWidget(self.add_teacher_button)

        self.delete_all_teacher_button = QPushButton(self.frame_25)
        self.delete_all_teacher_button.setObjectName(u"delete_all_teacher_button")
        self.delete_all_teacher_button.setStyleSheet(u"QPushButton\n"
"{\n"
" display: inline-block;\n"
"  padding: 6px 12px;\n"
"  margin-bottom: 0;\n"
"  font-size: 18px;\n"
"  font-weight: normal;\n"
"  line-height: 1.42857143;\n"
"  text-align: center;\n"
"  white-space: nowrap;\n"
"  vertical-align: middle;\n"
"  -ms-touch-action: manipulation;\n"
"      touch-action: manipulation;\n"
"  cursor: pointer;\n"
"  -webkit-user-select: none;\n"
"     -moz-user-select: none;\n"
"      -ms-user-select: none;\n"
"          user-select: none;\n"
"  background-image: none;\n"
"  border: 1px solid transparent;\n"
"  border-radius: 4px;\n"
"color: #fff; \n"
"background-color: #5cb85c;\n"
"  border-color: #4cae4c;\n"
"}\n"
"QPushButton\n"
"{\n"
"color: #fff;\n"
"  background-color: #d9534f;\n"
"  border-color: #d43f3a;\n"
"\n"
"}\n"
"\n"
"\n"
":hover\n"
"{\n"
" color: #fff;\n"
"  background-color: #c9302c;\n"
"  border-color: #ac2925;\n"
"}")
        self.delete_all_teacher_button.setIcon(icon14)
        self.delete_all_teacher_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_24.addWidget(self.delete_all_teacher_button)


        self.horizontalLayout_23.addWidget(self.frame_25, 0, Qt.AlignLeft)

        self.frame_26 = QFrame(self.frame_23)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"margin-left: 10px;")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.teacher_search_text = QLineEdit(self.frame_26)
        self.teacher_search_text.setObjectName(u"teacher_search_text")
        self.teacher_search_text.setMinimumSize(QSize(140, 0))
        self.teacher_search_text.setFont(font3)
        self.teacher_search_text.setStyleSheet(u"padding: 1px;\n"
"border-bottom: 1px solid;")

        self.horizontalLayout_25.addWidget(self.teacher_search_text, 0, Qt.AlignLeft)

        self.search_teacher_button = QPushButton(self.frame_26)
        self.search_teacher_button.setObjectName(u"search_teacher_button")
        self.search_teacher_button.setIcon(icon15)
        self.search_teacher_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_25.addWidget(self.search_teacher_button, 0, Qt.AlignLeft)


        self.horizontalLayout_23.addWidget(self.frame_26, 0, Qt.AlignRight)


        self.verticalLayout_8.addWidget(self.frame_23, 0, Qt.AlignTop)

        self.frame_24 = QFrame(self.teachers_page)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.teacher_table = QTableWidget(self.frame_24)
        if (self.teacher_table.columnCount() < 3):
            self.teacher_table.setColumnCount(3)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.teacher_table.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.teacher_table.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.teacher_table.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        self.teacher_table.setObjectName(u"teacher_table")
        self.teacher_table.setStyleSheet(u"QTableWidget\n"
"{\n"
"font-size: 20px;\n"
"}")
        self.teacher_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.teacher_table.setAlternatingRowColors(True)
        self.teacher_table.setSortingEnabled(True)
        self.teacher_table.horizontalHeader().setProperty("showSortIndicator", True)
        self.teacher_table.horizontalHeader().setStretchLastSection(False)
        self.teacher_table.verticalHeader().setVisible(False)
        self.teacher_table.verticalHeader().setProperty("showSortIndicator", False)
        self.teacher_table.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_26.addWidget(self.teacher_table)


        self.verticalLayout_8.addWidget(self.frame_24)

        self.stackedWidget.addWidget(self.teachers_page)
        self.registered_courses_page = QWidget()
        self.registered_courses_page.setObjectName(u"registered_courses_page")
        self.verticalLayout_9 = QVBoxLayout(self.registered_courses_page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_27 = QFrame(self.registered_courses_page)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_27.setSpacing(6)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(9, 9, 9, 9)
        self.label_7 = QLabel(self.frame_27)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.horizontalLayout_27.addWidget(self.label_7, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.frame_27, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_28 = QFrame(self.registered_courses_page)
        self.frame_28.setObjectName(u"frame_28")
        font6 = QFont()
        font6.setFamily(u"Arial")
        self.frame_28.setFont(font6)
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_28.setSpacing(6)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(9, 9, 9, 9)
        self.frame_30 = QFrame(self.frame_28)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setStyleSheet(u"QPushButton\n"
"{\n"
"margin-left: 5px;\n"
"}")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_29.setSpacing(25)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(9, 9, 9, 9)
        self.add_registered_button = QPushButton(self.frame_30)
        self.add_registered_button.setObjectName(u"add_registered_button")
        self.add_registered_button.setStyleSheet(u"QPushButton\n"
"{\n"
" display: inline-block;\n"
"  padding: 6px 12px;\n"
"  margin-bottom: 0;\n"
"  font-size: 18px;\n"
"  font-weight: normal;\n"
"  line-height: 1.42857143;\n"
"  text-align: center;\n"
"  white-space: nowrap;\n"
"  vertical-align: middle;\n"
"  -ms-touch-action: manipulation;\n"
"      touch-action: manipulation;\n"
"  cursor: pointer;\n"
"  -webkit-user-select: none;\n"
"     -moz-user-select: none;\n"
"      -ms-user-select: none;\n"
"          user-select: none;\n"
"  background-image: none;\n"
"  border: 1px solid transparent;\n"
"  border-radius: 4px;\n"
"color: #fff; \n"
"background-color: #5cb85c;\n"
"  border-color: #4cae4c;\n"
"}\n"
"\n"
"\n"
":hover\n"
"{\n"
" color: #fff;\n"
"  background-color: #449d44;\n"
"  border-color: #398439;\n"
"}\n"
"")
        self.add_registered_button.setIcon(icon13)
        self.add_registered_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_29.addWidget(self.add_registered_button)

        self.delete_all_registered_button = QPushButton(self.frame_30)
        self.delete_all_registered_button.setObjectName(u"delete_all_registered_button")
        self.delete_all_registered_button.setStyleSheet(u"QPushButton\n"
"{\n"
" display: inline-block;\n"
"  padding: 6px 12px;\n"
"  margin-bottom: 0;\n"
"  font-size: 18px;\n"
"  font-weight: normal;\n"
"  line-height: 1.42857143;\n"
"  text-align: center;\n"
"  white-space: nowrap;\n"
"  vertical-align: middle;\n"
"  -ms-touch-action: manipulation;\n"
"      touch-action: manipulation;\n"
"  cursor: pointer;\n"
"  -webkit-user-select: none;\n"
"     -moz-user-select: none;\n"
"      -ms-user-select: none;\n"
"          user-select: none;\n"
"  background-image: none;\n"
"  border: 1px solid transparent;\n"
"  border-radius: 4px;\n"
"color: #fff; \n"
"background-color: #5cb85c;\n"
"  border-color: #4cae4c;\n"
"}\n"
"QPushButton\n"
"{\n"
"color: #fff;\n"
"  background-color: #d9534f;\n"
"  border-color: #d43f3a;\n"
"\n"
"}\n"
"\n"
"\n"
":hover\n"
"{\n"
" color: #fff;\n"
"  background-color: #c9302c;\n"
"  border-color: #ac2925;\n"
"}")
        self.delete_all_registered_button.setIcon(icon14)
        self.delete_all_registered_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_29.addWidget(self.delete_all_registered_button)


        self.horizontalLayout_28.addWidget(self.frame_30, 0, Qt.AlignLeft)

        self.frame_31 = QFrame(self.frame_28)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setStyleSheet(u"margin-left: 10px;")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.registered_search_text = QLineEdit(self.frame_31)
        self.registered_search_text.setObjectName(u"registered_search_text")
        self.registered_search_text.setFont(font3)
        self.registered_search_text.setStyleSheet(u"border-bottom: 1px solid;\n"
"padding: 1px;")

        self.horizontalLayout_30.addWidget(self.registered_search_text, 0, Qt.AlignRight)

        self.pushButton_7 = QPushButton(self.frame_31)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setIcon(icon15)
        self.pushButton_7.setIconSize(QSize(24, 24))

        self.horizontalLayout_30.addWidget(self.pushButton_7, 0, Qt.AlignRight)


        self.horizontalLayout_28.addWidget(self.frame_31, 0, Qt.AlignRight)


        self.verticalLayout_9.addWidget(self.frame_28, 0, Qt.AlignTop)

        self.frame_29 = QFrame(self.registered_courses_page)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 9, 0, 0)
        self.registered_table = QTableWidget(self.frame_29)
        if (self.registered_table.columnCount() < 6):
            self.registered_table.setColumnCount(6)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.registered_table.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.registered_table.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.registered_table.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.registered_table.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.registered_table.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.registered_table.setHorizontalHeaderItem(5, __qtablewidgetitem21)
        self.registered_table.setObjectName(u"registered_table")
        self.registered_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.registered_table.setAlternatingRowColors(True)
        self.registered_table.setSortingEnabled(True)
        self.registered_table.horizontalHeader().setProperty("showSortIndicator", True)
        self.registered_table.horizontalHeader().setStretchLastSection(False)
        self.registered_table.verticalHeader().setVisible(True)
        self.registered_table.verticalHeader().setProperty("showSortIndicator", False)
        self.registered_table.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_31.addWidget(self.registered_table)


        self.verticalLayout_9.addWidget(self.frame_29)

        self.stackedWidget.addWidget(self.registered_courses_page)
        self.room_preferences_page = QWidget()
        self.room_preferences_page.setObjectName(u"room_preferences_page")
        self.verticalLayout_15 = QVBoxLayout(self.room_preferences_page)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_33 = QFrame(self.room_preferences_page)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_8 = QLabel(self.frame_33)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.horizontalLayout_35.addWidget(self.label_8, 0, Qt.AlignTop)


        self.verticalLayout_15.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.room_preferences_page)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(-1, 9, 9, 9)
        self.frame_36 = QFrame(self.frame_34)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.delete_all_room_preferences = QPushButton(self.frame_36)
        self.delete_all_room_preferences.setObjectName(u"delete_all_room_preferences")
        self.delete_all_room_preferences.setStyleSheet(u"QPushButton\n"
"{\n"
" display: inline-block;\n"
"  padding: 6px 12px;\n"
"  margin-bottom: 0;\n"
"  font-size: 18px;\n"
"  font-weight: normal;\n"
"  line-height: 1.42857143;\n"
"  text-align: center;\n"
"  white-space: nowrap;\n"
"  vertical-align: middle;\n"
"  -ms-touch-action: manipulation;\n"
"      touch-action: manipulation;\n"
"  cursor: pointer;\n"
"  -webkit-user-select: none;\n"
"     -moz-user-select: none;\n"
"      -ms-user-select: none;\n"
"          user-select: none;\n"
"  background-image: none;\n"
"  border: 1px solid transparent;\n"
"  border-radius: 4px;\n"
"color: #fff; \n"
"background-color: #5cb85c;\n"
"  border-color: #4cae4c;\n"
"}\n"
"QPushButton\n"
"{\n"
"color: #fff;\n"
"  background-color: #d9534f;\n"
"  border-color: #d43f3a;\n"
"\n"
"}\n"
"\n"
"\n"
":hover\n"
"{\n"
" color: #fff;\n"
"  background-color: #c9302c;\n"
"  border-color: #ac2925;\n"
"}")
        self.delete_all_room_preferences.setIcon(icon14)
        self.delete_all_room_preferences.setIconSize(QSize(24, 24))

        self.horizontalLayout_33.addWidget(self.delete_all_room_preferences, 0, Qt.AlignLeft)


        self.horizontalLayout_32.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.frame_34)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.room_preferences_search_text = QLineEdit(self.frame_37)
        self.room_preferences_search_text.setObjectName(u"room_preferences_search_text")
        self.room_preferences_search_text.setFont(font3)
        self.room_preferences_search_text.setStyleSheet(u"border-bottom: 1px solid;\n"
"background-color: white;\n"
"color: black;")

        self.horizontalLayout_34.addWidget(self.room_preferences_search_text)

        self.room_preferences_search_button = QPushButton(self.frame_37)
        self.room_preferences_search_button.setObjectName(u"room_preferences_search_button")
        self.room_preferences_search_button.setIcon(icon15)
        self.room_preferences_search_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_34.addWidget(self.room_preferences_search_button)


        self.horizontalLayout_32.addWidget(self.frame_37, 0, Qt.AlignRight)


        self.verticalLayout_15.addWidget(self.frame_34, 0, Qt.AlignTop)

        self.frame_35 = QFrame(self.room_preferences_page)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.room_preferences_table = QTableWidget(self.frame_35)
        if (self.room_preferences_table.columnCount() < 4):
            self.room_preferences_table.setColumnCount(4)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.room_preferences_table.setHorizontalHeaderItem(0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.room_preferences_table.setHorizontalHeaderItem(1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.room_preferences_table.setHorizontalHeaderItem(2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.room_preferences_table.setHorizontalHeaderItem(3, __qtablewidgetitem25)
        self.room_preferences_table.setObjectName(u"room_preferences_table")
        self.room_preferences_table.setStyleSheet(u"QTableWidget\n"
"{\n"
"font-size: 20px;\n"
"}")
        self.room_preferences_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.room_preferences_table.setAlternatingRowColors(True)
        self.room_preferences_table.setSortingEnabled(True)
        self.room_preferences_table.horizontalHeader().setVisible(False)
        self.room_preferences_table.verticalHeader().setVisible(False)
        self.room_preferences_table.verticalHeader().setProperty("showSortIndicator", True)

        self.horizontalLayout_36.addWidget(self.room_preferences_table)


        self.verticalLayout_15.addWidget(self.frame_35)

        self.stackedWidget.addWidget(self.room_preferences_page)
        self.slot_preferences_page = QWidget()
        self.slot_preferences_page.setObjectName(u"slot_preferences_page")
        self.verticalLayout_16 = QVBoxLayout(self.slot_preferences_page)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_38 = QFrame(self.slot_preferences_page)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_9 = QLabel(self.frame_38)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.horizontalLayout_37.addWidget(self.label_9, 0, Qt.AlignTop)


        self.verticalLayout_16.addWidget(self.frame_38, 0, Qt.AlignTop)

        self.frame_39 = QFrame(self.slot_preferences_page)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.frame_41 = QFrame(self.frame_39)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.delete_all_slot_preferences = QPushButton(self.frame_41)
        self.delete_all_slot_preferences.setObjectName(u"delete_all_slot_preferences")
        self.delete_all_slot_preferences.setFont(font5)
        self.delete_all_slot_preferences.setStyleSheet(u"QPushButton\n"
"{\n"
" display: inline-block;\n"
"  padding: 6px 12px;\n"
"  margin-bottom: 0;\n"
"  font-size: 18px;\n"
"  font-weight: normal;\n"
"  line-height: 1.42857143;\n"
"  text-align: center;\n"
"  white-space: nowrap;\n"
"  vertical-align: middle;\n"
"  -ms-touch-action: manipulation;\n"
"      touch-action: manipulation;\n"
"  cursor: pointer;\n"
"  -webkit-user-select: none;\n"
"     -moz-user-select: none;\n"
"      -ms-user-select: none;\n"
"          user-select: none;\n"
"  background-image: none;\n"
"  border: 1px solid transparent;\n"
"  border-radius: 4px;\n"
"color: #fff; \n"
"background-color: #5cb85c;\n"
"  border-color: #4cae4c;\n"
"}\n"
"QPushButton\n"
"{\n"
"color: #fff;\n"
"  background-color: #d9534f;\n"
"  border-color: #d43f3a;\n"
"\n"
"}\n"
"\n"
"\n"
":hover\n"
"{\n"
" color: #fff;\n"
"  background-color: #c9302c;\n"
"  border-color: #ac2925;\n"
"}")
        self.delete_all_slot_preferences.setIcon(icon14)
        self.delete_all_slot_preferences.setIconSize(QSize(24, 24))

        self.horizontalLayout_39.addWidget(self.delete_all_slot_preferences, 0, Qt.AlignLeft)


        self.horizontalLayout_38.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.frame_39)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.slot_preferences_search_text = QLineEdit(self.frame_42)
        self.slot_preferences_search_text.setObjectName(u"slot_preferences_search_text")
        self.slot_preferences_search_text.setFont(font3)
        self.slot_preferences_search_text.setStyleSheet(u"border-bottom: 1px solid;\n"
"background-color: white; ")

        self.horizontalLayout_40.addWidget(self.slot_preferences_search_text, 0, Qt.AlignLeft)

        self.slot_preferences_search_button = QPushButton(self.frame_42)
        self.slot_preferences_search_button.setObjectName(u"slot_preferences_search_button")
        self.slot_preferences_search_button.setIcon(icon15)
        self.slot_preferences_search_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_40.addWidget(self.slot_preferences_search_button, 0, Qt.AlignLeft)


        self.horizontalLayout_38.addWidget(self.frame_42, 0, Qt.AlignRight)


        self.verticalLayout_16.addWidget(self.frame_39, 0, Qt.AlignTop)

        self.frame_40 = QFrame(self.slot_preferences_page)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.slot_preferences_table = QTableWidget(self.frame_40)
        if (self.slot_preferences_table.columnCount() < 4):
            self.slot_preferences_table.setColumnCount(4)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.slot_preferences_table.setHorizontalHeaderItem(0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.slot_preferences_table.setHorizontalHeaderItem(1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.slot_preferences_table.setHorizontalHeaderItem(2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.slot_preferences_table.setHorizontalHeaderItem(3, __qtablewidgetitem29)
        self.slot_preferences_table.setObjectName(u"slot_preferences_table")
        self.slot_preferences_table.setStyleSheet(u"QTableWidget\n"
"{\n"
"font-size: 20px;\n"
"}")
        self.slot_preferences_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.slot_preferences_table.setAlternatingRowColors(True)
        self.slot_preferences_table.setSortingEnabled(True)
        self.slot_preferences_table.verticalHeader().setVisible(False)

        self.horizontalLayout_41.addWidget(self.slot_preferences_table)


        self.verticalLayout_16.addWidget(self.frame_40)

        self.stackedWidget.addWidget(self.slot_preferences_page)
        self.student_clashes_page = QWidget()
        self.student_clashes_page.setObjectName(u"student_clashes_page")
        self.verticalLayout_21 = QVBoxLayout(self.student_clashes_page)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_47 = QFrame(self.student_clashes_page)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_47)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_56 = QFrame(self.frame_47)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.frame_49 = QFrame(self.frame_56)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_10 = QLabel(self.frame_49)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.horizontalLayout_45.addWidget(self.label_10)


        self.horizontalLayout_44.addWidget(self.frame_49)

        self.frame_50 = QFrame(self.frame_56)
        self.frame_50.setObjectName(u"frame_50")
        font7 = QFont()
        font7.setPointSize(12)
        font7.setBold(False)
        font7.setWeight(50)
        self.frame_50.setFont(font7)
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.total_student_clashes = QLabel(self.frame_50)
        self.total_student_clashes.setObjectName(u"total_student_clashes")
        font8 = QFont()
        font8.setFamily(u"Arial")
        font8.setPointSize(11)
        font8.setBold(True)
        font8.setWeight(75)
        self.total_student_clashes.setFont(font8)

        self.horizontalLayout_46.addWidget(self.total_student_clashes)


        self.horizontalLayout_44.addWidget(self.frame_50)


        self.verticalLayout_22.addWidget(self.frame_56)

        self.scrollArea = QScrollArea(self.frame_47)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1028, 621))
        self.horizontalLayout_51 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.frame_48 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_48.setObjectName(u"frame_48")
        sizePolicy.setHeightForWidth(self.frame_48.sizePolicy().hasHeightForWidth())
        self.frame_48.setSizePolicy(sizePolicy)
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, -1, 0, 0)
        self.frame_51 = QFrame(self.frame_48)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setStyleSheet(u"QFrame#frame_52 {border: 1px solid black;}")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_51)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_11 = QLabel(self.frame_51)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font-size: 19px;\n"
"font-weight: 600;\n"
"background-color: rgb(216, 215, 215);\n"
"padding: 5px;\n"
"padding-bottom: 10px;\n"
"padding-top: 10px;\n"
"border-radius: 2px;\n"
"border: 1px solid black;")

        self.verticalLayout_23.addWidget(self.label_11, 0, Qt.AlignTop)


        self.horizontalLayout_47.addWidget(self.frame_51, 0, Qt.AlignTop)


        self.horizontalLayout_51.addWidget(self.frame_48)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_22.addWidget(self.scrollArea)


        self.verticalLayout_21.addWidget(self.frame_47)

        self.stackedWidget.addWidget(self.student_clashes_page)
        self.teacher_clashes_page = QWidget()
        self.teacher_clashes_page.setObjectName(u"teacher_clashes_page")
        self.horizontalLayout_48 = QHBoxLayout(self.teacher_clashes_page)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.frame_52 = QFrame(self.teacher_clashes_page)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.frame_53 = QFrame(self.frame_52)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_53)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_57 = QFrame(self.frame_53)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.frame_54 = QFrame(self.frame_57)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_12 = QLabel(self.frame_54)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.horizontalLayout_50.addWidget(self.label_12)


        self.horizontalLayout_49.addWidget(self.frame_54)

        self.frame_55 = QFrame(self.frame_57)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFont(font7)
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.total_teacher_clashes = QLabel(self.frame_55)
        self.total_teacher_clashes.setObjectName(u"total_teacher_clashes")
        self.total_teacher_clashes.setFont(font8)

        self.horizontalLayout_52.addWidget(self.total_teacher_clashes)


        self.horizontalLayout_49.addWidget(self.frame_55)


        self.verticalLayout_24.addWidget(self.frame_57)

        self.scrollArea_2 = QScrollArea(self.frame_53)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1046, 645))
        self.horizontalLayout_53 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.frame_58 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_58.setObjectName(u"frame_58")
        sizePolicy.setHeightForWidth(self.frame_58.sizePolicy().hasHeightForWidth())
        self.frame_58.setSizePolicy(sizePolicy)
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, -1, 0, 0)
        self.frame_59 = QFrame(self.frame_58)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setStyleSheet(u"QFrame#frame_52 {border: 1px solid black;}")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_59)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_13 = QLabel(self.frame_59)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font-size: 19px;\n"
"font-weight: 600;\n"
"background-color: rgb(216, 215, 215);\n"
"padding: 5px;\n"
"padding-bottom: 10px;\n"
"padding-top: 10px;\n"
"border-radius: 2px;\n"
"border: 1px solid black;")

        self.verticalLayout_25.addWidget(self.label_13, 0, Qt.AlignTop)


        self.horizontalLayout_54.addWidget(self.frame_59, 0, Qt.AlignTop)


        self.horizontalLayout_53.addWidget(self.frame_58)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_24.addWidget(self.scrollArea_2)


        self.horizontalLayout_55.addWidget(self.frame_53)


        self.horizontalLayout_48.addWidget(self.frame_52)

        self.stackedWidget.addWidget(self.teacher_clashes_page)
        self.room_clashes_page = QWidget()
        self.room_clashes_page.setObjectName(u"room_clashes_page")
        self.horizontalLayout_56 = QHBoxLayout(self.room_clashes_page)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.frame_60 = QFrame(self.room_clashes_page)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.frame_61 = QFrame(self.frame_60)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_61)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_62 = QFrame(self.frame_61)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.frame_63 = QFrame(self.frame_62)
        self.frame_63.setObjectName(u"frame_63")
        font9 = QFont()
        font9.setPointSize(8)
        self.frame_63.setFont(font9)
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.label_14 = QLabel(self.frame_63)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.horizontalLayout_58.addWidget(self.label_14)


        self.horizontalLayout_57.addWidget(self.frame_63)

        self.frame_64 = QFrame(self.frame_62)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFont(font7)
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.total_room_clashes = QLabel(self.frame_64)
        self.total_room_clashes.setObjectName(u"total_room_clashes")
        self.total_room_clashes.setFont(font8)

        self.horizontalLayout_59.addWidget(self.total_room_clashes)


        self.horizontalLayout_57.addWidget(self.frame_64)


        self.verticalLayout_26.addWidget(self.frame_62)

        self.scrollArea_3 = QScrollArea(self.frame_61)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1046, 645))
        self.horizontalLayout_60 = QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.frame_65 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_65.setObjectName(u"frame_65")
        sizePolicy.setHeightForWidth(self.frame_65.sizePolicy().hasHeightForWidth())
        self.frame_65.setSizePolicy(sizePolicy)
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_65)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, -1, 0, 0)
        self.frame_66 = QFrame(self.frame_65)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setStyleSheet(u"QFrame#frame_52 {border: 1px solid black;}")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_66)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_15 = QLabel(self.frame_66)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font-size: 19px;\n"
"font-weight: 600;\n"
"background-color: rgb(216, 215, 215);\n"
"padding: 5px;\n"
"padding-bottom: 10px;\n"
"padding-top: 10px;\n"
"border-radius: 2px;\n"
"border: 1px solid black;")

        self.verticalLayout_27.addWidget(self.label_15, 0, Qt.AlignTop)


        self.horizontalLayout_61.addWidget(self.frame_66, 0, Qt.AlignTop)


        self.horizontalLayout_60.addWidget(self.frame_65)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_26.addWidget(self.scrollArea_3)


        self.horizontalLayout_63.addWidget(self.frame_61)


        self.horizontalLayout_56.addWidget(self.frame_60)

        self.stackedWidget.addWidget(self.room_clashes_page)
        self.sections_timetable_page = QWidget()
        self.sections_timetable_page.setObjectName(u"sections_timetable_page")
        self.horizontalLayout_64 = QHBoxLayout(self.sections_timetable_page)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.frame_67 = QFrame(self.sections_timetable_page)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setStyleSheet(u"")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_67)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.frame_68 = QFrame(self.frame_67)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setStyleSheet(u"padding-top: 20px;")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_68)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.frame_68)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.verticalLayout_28.addWidget(self.label_16, 0, Qt.AlignTop)

        self.label_17 = QLabel(self.frame_68)
        self.label_17.setObjectName(u"label_17")
        font10 = QFont()
        font10.setFamily(u"Arial")
        font10.setPointSize(10)
        self.label_17.setFont(font10)

        self.verticalLayout_28.addWidget(self.label_17, 0, Qt.AlignTop)


        self.horizontalLayout_65.addWidget(self.frame_68, 0, Qt.AlignTop)

        self.frame_69 = QFrame(self.frame_67)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setStyleSheet(u"padding-right: 5px;\n"
"padding-top: 150px;")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_69)
        self.horizontalLayout_67.setSpacing(0)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, -1, 0)
        self.generate_sections_timetable = QPushButton(self.frame_69)
        self.generate_sections_timetable.setObjectName(u"generate_sections_timetable")
        self.generate_sections_timetable.setFont(font5)
        self.generate_sections_timetable.setStyleSheet(u"QPushButton\n"
"{\n"
" display: inline-block;\n"
"  padding: 6px 10px;\n"
"  margin-bottom: 0;\n"
"  font-size: 23px;\n"
"  font-weight: normal;\n"
"  line-height: 1.42857143;\n"
"  text-align: center;\n"
"  white-space: nowrap;\n"
"  vertical-align: middle;\n"
"  -ms-touch-action: manipulation;\n"
"      touch-action: manipulation;\n"
"  cursor: pointer;\n"
"  -webkit-user-select: none;\n"
"     -moz-user-select: none;\n"
"      -ms-user-select: none;\n"
"          user-select: none;\n"
"  background-image: none;\n"
"  border: 1px solid transparent;\n"
"  border-radius: 4px;\n"
"color: #fff;\n"
"  background-color: #5bc0de;\n"
"  border-color: #46b8da;\n"
"}\n"
"\n"
"\n"
":hover\n"
"{\n"
" color: #fff;\n"
"  background-color: #31b0d5;\n"
"  border-color: #269abc;\n"
"}\n"
"")

        self.horizontalLayout_67.addWidget(self.generate_sections_timetable, 0, Qt.AlignRight|Qt.AlignTop)


        self.horizontalLayout_65.addWidget(self.frame_69, 0, Qt.AlignRight)


        self.horizontalLayout_64.addWidget(self.frame_67)

        self.stackedWidget.addWidget(self.sections_timetable_page)
        self.rooms_timetable_page = QWidget()
        self.rooms_timetable_page.setObjectName(u"rooms_timetable_page")
        self.horizontalLayout_66 = QHBoxLayout(self.rooms_timetable_page)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.frame_70 = QFrame(self.rooms_timetable_page)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_70)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(9, 9, 9, 9)
        self.frame_71 = QFrame(self.frame_70)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setStyleSheet(u"padding-top: 20px;")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_71)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_71)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)

        self.verticalLayout_29.addWidget(self.label_18)

        self.label_19 = QLabel(self.frame_71)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font10)

        self.verticalLayout_29.addWidget(self.label_19)


        self.horizontalLayout_68.addWidget(self.frame_71, 0, Qt.AlignTop)

        self.frame_72 = QFrame(self.frame_70)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setStyleSheet(u"padding-right: 5px;\n"
"padding-top: 150px;")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_72)
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, -1)
        self.generate_rooms_timetable = QPushButton(self.frame_72)
        self.generate_rooms_timetable.setObjectName(u"generate_rooms_timetable")
        self.generate_rooms_timetable.setStyleSheet(u"QPushButton\n"
"{\n"
" display: inline-block;\n"
"  padding: 6px 10px;\n"
"  margin-bottom: 0;\n"
"  font-size: 23px;\n"
"  font-weight: normal;\n"
"  line-height: 1.42857143;\n"
"  text-align: center;\n"
"  white-space: nowrap;\n"
"  vertical-align: middle;\n"
"  -ms-touch-action: manipulation;\n"
"      touch-action: manipulation;\n"
"  cursor: pointer;\n"
"  -webkit-user-select: none;\n"
"     -moz-user-select: none;\n"
"      -ms-user-select: none;\n"
"          user-select: none;\n"
"  background-image: none;\n"
"  border: 1px solid transparent;\n"
"  border-radius: 4px;\n"
"color: #fff;\n"
"  background-color: #5bc0de;\n"
"  border-color: #46b8da;\n"
"}\n"
"\n"
"\n"
":hover\n"
"{\n"
" color: #fff;\n"
"  background-color: #31b0d5;\n"
"  border-color: #269abc;\n"
"}\n"
"")

        self.horizontalLayout_69.addWidget(self.generate_rooms_timetable)


        self.horizontalLayout_68.addWidget(self.frame_72, 0, Qt.AlignRight|Qt.AlignTop)


        self.horizontalLayout_66.addWidget(self.frame_70)

        self.stackedWidget.addWidget(self.rooms_timetable_page)
        self.teachers_timetable_page = QWidget()
        self.teachers_timetable_page.setObjectName(u"teachers_timetable_page")
        self.horizontalLayout_70 = QHBoxLayout(self.teachers_timetable_page)
        self.horizontalLayout_70.setSpacing(0)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.frame_73 = QFrame(self.teachers_timetable_page)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.frame_73)
        self.horizontalLayout_71.setSpacing(0)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(0, 9, 9, 9)
        self.frame_74 = QFrame(self.frame_73)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setStyleSheet(u"padding-top: 20px;")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_74)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(-1, 0, 0, 0)
        self.label_20 = QLabel(self.frame_74)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)

        self.verticalLayout_30.addWidget(self.label_20)

        self.label_21 = QLabel(self.frame_74)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font10)

        self.verticalLayout_30.addWidget(self.label_21)


        self.horizontalLayout_71.addWidget(self.frame_74, 0, Qt.AlignTop)

        self.frame_75 = QFrame(self.frame_73)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setStyleSheet(u"padding-right: 5px;\n"
"padding-top: 150px;")
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_75)
        self.horizontalLayout_72.setSpacing(0)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(0, 0, -1, 0)
        self.generate_teachers_timetable = QPushButton(self.frame_75)
        self.generate_teachers_timetable.setObjectName(u"generate_teachers_timetable")
        self.generate_teachers_timetable.setStyleSheet(u"QPushButton\n"
"{\n"
" display: inline-block;\n"
"  padding: 6px 10px;\n"
"  margin-bottom: 0;\n"
"  font-size: 23px;\n"
"  font-weight: normal;\n"
"  line-height: 1.42857143;\n"
"  text-align: center;\n"
"  white-space: nowrap;\n"
"  vertical-align: middle;\n"
"  -ms-touch-action: manipulation;\n"
"      touch-action: manipulation;\n"
"  cursor: pointer;\n"
"  -webkit-user-select: none;\n"
"     -moz-user-select: none;\n"
"      -ms-user-select: none;\n"
"          user-select: none;\n"
"  background-image: none;\n"
"  border: 1px solid transparent;\n"
"  border-radius: 4px;\n"
"color: #fff;\n"
"  background-color: #5bc0de;\n"
"  border-color: #46b8da;\n"
"}\n"
"\n"
"\n"
":hover\n"
"{\n"
" color: #fff;\n"
"  background-color: #31b0d5;\n"
"  border-color: #269abc;\n"
"}\n"
"")

        self.horizontalLayout_72.addWidget(self.generate_teachers_timetable, 0, Qt.AlignRight)


        self.horizontalLayout_71.addWidget(self.frame_75, 0, Qt.AlignTop)


        self.horizontalLayout_70.addWidget(self.frame_73)

        self.stackedWidget.addWidget(self.teachers_timetable_page)

        self.verticalLayout_11.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.main_body_contents)

        self.footer = QFrame(self.main_body)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.footer)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.footer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"padding-left: 5px;")

        self.horizontalLayout_5.addWidget(self.label, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_6)

        self.size_grip = QFrame(self.footer)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.size_grip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(3)
        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Timetable Manager", None))
        self.section_menu_button.setText(QCoreApplication.translate("MainWindow", u"Sections", None))
        self.course_menu_button.setText(QCoreApplication.translate("MainWindow", u"Courses", None))
        self.room_menu_button.setText(QCoreApplication.translate("MainWindow", u"Rooms", None))
        self.teacher_menu_button.setText(QCoreApplication.translate("MainWindow", u"Teachers", None))
        self.registered_menu_button.setText(QCoreApplication.translate("MainWindow", u"Registered Courses", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Registration Details", None))
        self.room_preference_menu_button.setText(QCoreApplication.translate("MainWindow", u"Room Preferences", None))
        self.slot_preference_menu_button.setText(QCoreApplication.translate("MainWindow", u"Slot Preferences", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.student_clash_menu_button.setText(QCoreApplication.translate("MainWindow", u"Student Clashes", None))
        self.room_clash_menu_button.setText(QCoreApplication.translate("MainWindow", u"Room Clashes", None))
        self.instructor_clash_menu_button.setText(QCoreApplication.translate("MainWindow", u"Instructor Clashes", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"View Clashes", None))
        self.view_section_timetable.setText(QCoreApplication.translate("MainWindow", u"Sections Timetable", None))
        self.view_teacher_timetable.setText(QCoreApplication.translate("MainWindow", u"Teachers Timetable", None))
        self.view_room_timetable.setText(QCoreApplication.translate("MainWindow", u"Rooms Timetable", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"Results", None))
        self.loading_button.setText("")
        self.header_label_notification.setText(QCoreApplication.translate("MainWindow", u"Updation Successful", None))
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Sections Page", None))
        self.add_section_button.setText(QCoreApplication.translate("MainWindow", u"Add New", None))
        self.section_delete_all_button.setText(QCoreApplication.translate("MainWindow", u"Delete All", None))
        self.search_section_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Section", None))
        self.search_section_button.setText("")
        ___qtablewidgetitem = self.section_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Section Name", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Courses Page", None))
        self.add_course_button.setText(QCoreApplication.translate("MainWindow", u"Add New", None))
        self.course_delete_all_button.setText(QCoreApplication.translate("MainWindow", u" Delete All", None))
        self.course_search_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Course", None))
        self.pushButton.setText("")
        ___qtablewidgetitem1 = self.course_table.horizontalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Course Name", None));
        ___qtablewidgetitem2 = self.course_table.horizontalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Course Code", None));
        ___qtablewidgetitem3 = self.course_table.horizontalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Course Type", None));
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Rooms Page", None))
        self.room_add_button.setText(QCoreApplication.translate("MainWindow", u"Add New", None))
        self.room_delete_all_button.setText(QCoreApplication.translate("MainWindow", u"Delete All", None))
        self.room_search_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Rooms", None))
        self.pushButton_6.setText("")
        ___qtablewidgetitem4 = self.room_table.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Room Type", None));
        ___qtablewidgetitem5 = self.room_table.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem6 = self.room_table.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Department", None));
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Teachers Page", None))
        self.add_teacher_button.setText(QCoreApplication.translate("MainWindow", u"Add New", None))
        self.delete_all_teacher_button.setText(QCoreApplication.translate("MainWindow", u"Delete All", None))
        self.teacher_search_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Teachers", None))
        self.search_teacher_button.setText("")
        ___qtablewidgetitem7 = self.teacher_table.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Teacher Name", None));
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Registered Courses Page", None))
        self.add_registered_button.setText(QCoreApplication.translate("MainWindow", u"Add New", None))
        self.delete_all_registered_button.setText(QCoreApplication.translate("MainWindow", u"Delete All", None))
        self.registered_search_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
        self.pushButton_7.setText("")
        ___qtablewidgetitem8 = self.registered_table.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Section", None));
        ___qtablewidgetitem9 = self.registered_table.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Course", None));
        ___qtablewidgetitem10 = self.registered_table.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Teacher", None));
        ___qtablewidgetitem11 = self.registered_table.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Students", None));
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Teacher Room Preferences", None))
        self.delete_all_room_preferences.setText(QCoreApplication.translate("MainWindow", u"Delete All Preferences", None))
        self.room_preferences_search_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Teacher", None))
        self.room_preferences_search_button.setText("")
        ___qtablewidgetitem12 = self.room_preferences_table.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem13 = self.room_preferences_table.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem14 = self.room_preferences_table.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Teacher", None));
        ___qtablewidgetitem15 = self.room_preferences_table.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Preferences", None));
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Teacher Slot Preferences", None))
        self.delete_all_slot_preferences.setText(QCoreApplication.translate("MainWindow", u"Delete All Preferences", None))
        self.slot_preferences_search_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Teacher", None))
        self.slot_preferences_search_button.setText("")
        ___qtablewidgetitem16 = self.slot_preferences_table.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem17 = self.slot_preferences_table.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem18 = self.slot_preferences_table.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Teacher", None));
        ___qtablewidgetitem19 = self.slot_preferences_table.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Student Clashes", None))
        self.total_student_clashes.setText(QCoreApplication.translate("MainWindow", u"Total Clashes: ", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Details of Student Clashes", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Instructor Clashes", None))
        self.total_teacher_clashes.setText(QCoreApplication.translate("MainWindow", u"Total Clashes: ", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Details of Instructor Clashes", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Room Clashes", None))
        self.total_room_clashes.setText(QCoreApplication.translate("MainWindow", u"Total Clashes: ", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Details of Room Clashes", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Sections Timetable", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Timetable Generated will be stored in the Local Directory of the Software by the name of Sections Timetable.", None))
        self.generate_sections_timetable.setText(QCoreApplication.translate("MainWindow", u"Generate Sections Timetable", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Rooms Timetable", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Timetable will be stored in the Local Directory of the Software by the name of Rooms Timetable.", None))
        self.generate_rooms_timetable.setText(QCoreApplication.translate("MainWindow", u"Generate Rooms Timetable", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Teachers Timetable", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Timetable will be stored in the Local Directory of the Software by the name of Teachers Timetable.", None))
        self.generate_teachers_timetable.setText(QCoreApplication.translate("MainWindow", u"Generate Teachers Timetable", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Timetable Manager V 1.0", None))
    # retranslateUi

