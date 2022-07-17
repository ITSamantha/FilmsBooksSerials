from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import sys

from PyQt5.QtWidgets import QTableWidgetItem, QCheckBox, QTableWidget

import ControllerForDB
from ControllerForDB import ControllerForDB
from insert_into_books import Ui_InsertBooks
from mainform import Ui_MainWindow as MyWindow

# Constants
LOGO_IMAGE_DIRECTORY = "images\\insp.png"
CHECKBOX_CONST = 4





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
            lambda ch, btn=self.ui.booksButton: self.load_tables(btn.text()))  # If clicked, we get a signal
        self.ui.filmsButton.clicked.connect(
            lambda ch, btn=self.ui.filmsButton: self.load_tables(btn.text()))
        self.ui.serialsButton.clicked.connect(
            lambda ch, btn=self.ui.serialsButton: self.load_tables(btn.text()))
        #self.ui.books_addB.clicked.connect(
        #     lambda ch,btn = self.ui.books_addB:ControllerForDB.insert_into_books()
        #
        # )

    #def insert_rows_into_table(self,value,*args):


    def load_tables(self, value):
        if value == "Books":
            self.ui.pages.setCurrentIndex(2)
            if self.ui.books_table.rowCount() != 0:
                self.ui.books_table.setRowCount(0)
            result = ControllerForDB.select_all_from_tables('books')
            row_c = 0
            for i in result:
                self.ui.books_table.insertRow(row_c)
                for j in range(len(i)):
                    if j == CHECKBOX_CONST :
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
            result = ControllerForDB.select_all_from_tables('films')
            row_c = 0
            for i in result:
                self.ui.film_table.insertRow(row_c)
                for j in range(len(i)):
                    if j == CHECKBOX_CONST :
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
            result = ControllerForDB.select_all_from_tables('serials')
            row_c = 0
            for i in result:
                self.ui.serials_table.insertRow(row_c)
                for j in range(len(i)):
                    if j == CHECKBOX_CONST:
                        check = QCheckBox()
                        check.setStyleSheet('background-color:none;')
                        check.setChecked(i[j])
                        self.ui.serials_table.setCellWidget(row_c, j, check)
                    else:
                        self.ui.serials_table.setItem(row_c, j, QTableWidgetItem(str(i[j])))

                row_c += 1
            QTableWidget.resizeColumnsToContents(self.ui.serials_table)


class InsertBooks(QtWidgets.QMainWindow):

    def __init__(self):
        super(InsertBooks, self).__init__()
        self.ui = Ui_InsertBooks()
        self.ui.setupUi(self)
        self.ui.saveB.clicked.connect(
            lambda ch, btn=self.ui.saveB: self.insert_row())  # If clicked, we get a signal

    def insert_row(self):
        if ControllerForDB.insert_into_books(self.ui.titleTB.text(),
                                             self.ui.authorTB.text(),
                                             self.ui.impressionTB.text(),
                                             True if self.ui.likeCB.currentText() == 'Yes' else False,
                                             self.ui.datePicker.date()):
            print('All right.')
        self.close()







# Create application form

app = QtWidgets.QApplication([])
application = WorkWithApplication()


application.show()
sys.exit(app.exec())

# app = QtWidgets.QApplication([])
# appl = InsertBooks()
#
# appl.show()
# sys.exit(app.exec())


