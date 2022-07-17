from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import sys

from PyQt5.QtWidgets import QTableWidgetItem, QCheckBox, QTableWidget, QMessageBox

import ControllerForDB
from ControllerForDB import ControllerForDB
from insert_into_books import Ui_InsertBooks
from mainform import Ui_MainWindow as MyWindow

# Constants
LOGO_IMAGE_DIRECTORY = "images\\insp.png"
CHECKBOX_CONST = 4

def formingMessageBox(message,title):
    msg = QMessageBox()
    msg.setText(message)
    msg.setWindowTitle(title)
    msg.setWindowIcon(QIcon(LOGO_IMAGE_DIRECTORY))
    return msg

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
                                             f"{'0' if self.ui.datePicker.date().day()<10 else ''}{self.ui.datePicker.date().day()}."
                                             f"{'0' if self.ui.datePicker.date().month()<10 else ''}{self.ui.datePicker.date().month()}."
                                             f"{self.ui.datePicker.date().year()}"):
            formingMessageBox('This book was succesfully added!','Information').exec()
        self.close()

    def close(self) -> bool:
        self.clear_boxes()
        super(InsertBooks, self).close()


    def clear_boxes(self):
        self.ui.titleTB.clear()
        self.ui.authorTB.clear()
        self.ui.impressionTB.clear()
        self.ui.likeCB.setCurrentIndex(0)
        self.ui.datePicker.clear()



class WorkWithApplication(QtWidgets.QMainWindow):

    def __init__(self):
        super(WorkWithApplication, self).__init__()
        self.InsertBooks = None
        self.ui = MyWindow()
        self.ui.setupUi(self)
        self.init_form()

    def init_form(self):
        self.InsertBooks = InsertBooks()
        self.ui.pages.setCurrentIndex(0)
        self.setWindowIcon(QIcon(LOGO_IMAGE_DIRECTORY))
        self.ui.booksButton.clicked.connect(
            lambda ch, btn=self.ui.booksButton: self.load_tables(btn.text()))  # If clicked, we get a signal
        self.ui.filmsButton.clicked.connect(
            lambda ch, btn=self.ui.filmsButton: self.load_tables(btn.text()))
        self.ui.serialsButton.clicked.connect(
            lambda ch, btn=self.ui.serialsButton: self.load_tables(btn.text()))
        self.ui.books_addB.clicked.connect(
            lambda ch, btn=self.ui.books_addB: self.InsertBooks.show())

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
                    if j == CHECKBOX_CONST:
                        check = QCheckBox()
                        check.setChecked(i[j])
                        check.setStyleSheet('background-color:none;')
                        self.ui.books_table.setCellWidget(row_c, j, check)
                    else:
                        self.ui.books_table.setItem(row_c, j, QTableWidgetItem(str(i[j])))
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
                    if j == CHECKBOX_CONST:
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


def main():
    # Create application form
    app = QtWidgets.QApplication([])
    application = WorkWithApplication()
    application.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
