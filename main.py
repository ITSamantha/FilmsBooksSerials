from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
import sys

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
        if value == "Books":
            self.ui.pages.setCurrentIndex(2)
        elif value == "Films":
            self.ui.pages.setCurrentIndex(3)
        else:
            self.ui.pages.setCurrentIndex(1)


app = QtWidgets.QApplication([])
application = WorkWithApplication()
application.show()
sys.exit(app.exec())
