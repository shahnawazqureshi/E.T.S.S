import os
from PySide2 import *
import sys

from add_course_page import *

class Add_Course_Page(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Add_Course_Window()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())