from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import sys

from PyQt5.QtWidgets import QTableWidgetItem, QCheckBox, QTableWidget

import ControllerForDB
from mainform import Ui_MainWindow as MyWindow

# Constants
LOGO_IMAGE_DIRECTORY = "images\\insp.png"



class WorkWithApplication(QtWidgets.QMainWindow):

    def __init__(self):
        super(WorkWithApplication, self).__init__()
        self.ui = MyWindow()
        self.ui.setupUi(self)
        self.init_form()

    def init_form(self):
        self.ui.pages.setCurrentIndex(0)
        self.setWindowIcon(QIcon(LOGO_IMAGE_DIRECTORY))
        self.ui.booksButton.clicked.connect(
            lambda ch, btn=self.ui.booksButton: self.button_clicked(btn.text()))  # If clicked, we get a signal
        self.ui.filmsButton.clicked.connect(
            lambda ch, btn=self.ui.filmsButton: self.button_clicked(btn.text()))
        self.ui.serialsButton.clicked.connect(
            lambda ch, btn=self.ui.serialsButton: self.button_clicked(btn.text()))

    def button_clicked(self, value):
        controller = ControllerForDB.ControllerForDB()
        if value == "Books":
            self.ui.pages.setCurrentIndex(2)
            if self.ui.books_table.rowCount() != 0:
                self.ui.books_table.setRowCount(0)
            result = controller.select_all_from_tables('books')
            row_c = 0
            for i in result:
                self.ui.books_table.insertRow(row_c)
                for j in range(len(i)):
                    if j == 4:
                        check = QCheckBox()
                        check.setChecked(i[j])
                        check.setStyleSheet('background-color:none;')
                        self.ui.books_table.setCellWidget(row_c, j, check)
                    else:
                        self.ui.books_table.setItem(row_c, j,  QTableWidgetItem(str(i[j])))
                row_c += 1
            QTableWidget.resizeColumnsToContents(self.ui.books_table)
        elif value == "Films":
            self.ui.pages.setCurrentIndex(3)
            if self.ui.film_table.rowCount() != 0:
                self.ui.film_table.setRowCount(0)
            result = controller.select_all_from_tables('films')
            row_c = 0
            for i in result:
                self.ui.film_table.insertRow(row_c)
                for j in range(len(i)):
                    if j == 4:
                        check = QCheckBox()
                        check.setStyleSheet('background-color:none;')
                        check.setChecked(i[j])
                        self.ui.film_table.setCellWidget(row_c, j, check)
                    else:
                        self.ui.film_table.setItem(row_c, j, QTableWidgetItem(str(i[j])))
                row_c += 1
            QTableWidget.resizeColumnsToContents(self.ui.film_table)
        else:
            self.ui.pages.setCurrentIndex(1)
            if self.ui.serials_table.rowCount() != 0:
                self.ui.serials_table.setRowCount(0)
            result = controller.select_all_from_tables('serials')
            row_c = 0
            for i in result:
                self.ui.serials_table.insertRow(row_c)
                for j in range(len(i)):
                    if j == 4:
                        check = QCheckBox()
                        check.setStyleSheet('background-color:none;')
                        check.setChecked(i[j])
                        self.ui.serials_table.setCellWidget(row_c, j, check)
                    else:
                        self.ui.serials_table.setItem(row_c, j, QTableWidgetItem(str(i[j])))

                row_c += 1
            QTableWidget.resizeColumnsToContents(self.ui.serials_table)





# Create application form

app = QtWidgets.QApplication([])
application = WorkWithApplication()


application.show()
sys.exit(app.exec())
