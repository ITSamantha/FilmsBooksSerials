from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
import sys

from mainform import Ui_MainWindow as MyWindow


class WorkWithApplication(QtWidgets.QMainWindow):

    def __init__(self):
        super(WorkWithApplication, self).__init__()
        self.ui = MyWindow()
        self.ui.setupUi(self)
        self.init_form()

    def init_form(self):

        self.ui.pages.setCurrentIndex(0)
        self.setWindowIcon(QIcon("images\\insp.png"))



app = QtWidgets.QApplication([])
application = WorkWithApplication()
application.show()

sys.exit(app.exec_())
