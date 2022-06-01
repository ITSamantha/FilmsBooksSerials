from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(901, 650)
        MainWindow.setMinimumSize(QtCore.QSize(901, 650))
        MainWindow.setMaximumSize(QtCore.QSize(901, 650))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 901, 51))
        self.widget.setStyleSheet("background-color: rgb(223, 220, 255);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 0, 41, 41))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/insp.png"))
        self.label.setObjectName("label")
        self.logo = QtWidgets.QLabel(self.widget)
        self.logo.setGeometry(QtCore.QRect(40, 0, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.logo.setFont(font)
        self.logo.setStyleSheet("color: rgb(120, 46, 172);")
        self.logo.setObjectName("logo")
        self.serialsButton = QtWidgets.QPushButton(self.widget)
        self.serialsButton.setGeometry(QtCore.QRect(690, 0, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.serialsButton.setFont(font)
        self.serialsButton.setStyleSheet("QPushButton:hover{\n"
                                         "font:bold ;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton{\n"
                                         "font: 16pt \"Garamond\";\n"
                                         "border:0px;\n"
                                         "border:0px;\n"
                                         "border-radius:5px\n"
                                         "}")
        self.serialsButton.setAutoDefault(False)
        self.serialsButton.setDefault(False)
        self.serialsButton.setFlat(False)
        self.serialsButton.setObjectName("serialsButton")
        self.booksButton = QtWidgets.QPushButton(self.widget)
        self.booksButton.setGeometry(QtCore.QRect(470, 0, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.booksButton.setFont(font)
        self.booksButton.setStyleSheet("QPushButton:hover{\n"
                                       "font:bold;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton{\n"
                                       "font: 16pt \"Garamond\";\n"
                                       "border:0px;\n"
                                       "border:0px;\n"
                                       "border-radius:5px\n"
                                       "\n"
                                       "}")
        self.booksButton.setAutoDefault(False)
        self.booksButton.setDefault(False)
        self.booksButton.setFlat(False)
        self.booksButton.setObjectName("booksButton")
        self.filmsButton = QtWidgets.QPushButton(self.widget)
        self.filmsButton.setGeometry(QtCore.QRect(260, 0, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.filmsButton.setFont(font)
        self.filmsButton.setStyleSheet("QPushButton:hover{\n"
                                       "font:bold;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton{\n"
                                       "font: 16pt \"Garamond\";\n"
                                       "border:0px;\n"
                                       "border-radius:5px\n"
                                       "}")
        self.filmsButton.setAutoDefault(False)
        self.filmsButton.setDefault(False)
        self.filmsButton.setFlat(False)
        self.filmsButton.setObjectName("filmsButton")
        self.pages = QtWidgets.QStackedWidget(self.centralwidget)
        self.pages.setGeometry(QtCore.QRect(0, 40, 901, 611))
        self.pages.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pages.setObjectName("pages")
        self.welcome_page = QtWidgets.QWidget()
        self.welcome_page.setObjectName("welcome_page")
        self.photo = QtWidgets.QLabel(self.welcome_page)
        self.photo.setGeometry(QtCore.QRect(140, 20, 651, 461))
        self.photo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.photo.setAutoFillBackground(False)
        self.photo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.photo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("images/welcome.jpg"))
        self.photo.setObjectName("photo")
        self.welcome_label = QtWidgets.QLabel(self.welcome_page)
        self.welcome_label.setGeometry(QtCore.QRect(190, 480, 551, 41))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        font.setItalic(False)
        self.welcome_label.setFont(font)
        self.welcome_label.setObjectName("welcome_label")
        self.pages.addWidget(self.welcome_page)
        self.serials = QtWidgets.QWidget()
        self.serials.setObjectName("serials")
        self.serials_table = QtWidgets.QTableView(self.serials)
        self.serials_table.setGeometry(QtCore.QRect(30, 70, 861, 531))
        self.serials_table.setStyleSheet("border:0px")
        self.serials_table.setFrameShadow(QtWidgets.QFrame.Plain)
        self.serials_table.setGridStyle(QtCore.Qt.SolidLine)
        self.serials_table.setObjectName("serials_table")
        self.serials_l = QtWidgets.QLabel(self.serials)
        self.serials_l.setGeometry(QtCore.QRect(410, 20, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        font.setItalic(False)
        self.serials_l.setFont(font)
        self.serials_l.setObjectName("serials_l")
        self.pages.addWidget(self.serials)
        self.books = QtWidgets.QWidget()
        self.books.setObjectName("books")
        self.book_table = QtWidgets.QTableView(self.books)
        self.book_table.setGeometry(QtCore.QRect(30, 70, 861, 531))
        self.book_table.setStyleSheet("border:0px")
        self.book_table.setFrameShadow(QtWidgets.QFrame.Plain)
        self.book_table.setGridStyle(QtCore.Qt.SolidLine)
        self.book_table.setObjectName("book_table")
        self.book_l = QtWidgets.QLabel(self.books)
        self.book_l.setGeometry(QtCore.QRect(410, 20, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        font.setItalic(False)
        self.book_l.setFont(font)
        self.book_l.setObjectName("book_l")
        self.pages.addWidget(self.books)
        self.films = QtWidgets.QWidget()
        self.films.setObjectName("films")
        self.film_l = QtWidgets.QLabel(self.films)
        self.film_l.setGeometry(QtCore.QRect(400, 20, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        font.setItalic(False)
        self.film_l.setFont(font)
        self.film_l.setObjectName("film_l")
        self.film_table = QtWidgets.QTableView(self.films)
        self.film_table.setGeometry(QtCore.QRect(20, 70, 861, 531))
        self.film_table.setStyleSheet("border:0px")
        self.film_table.setFrameShadow(QtWidgets.QFrame.Plain)
        self.film_table.setGridStyle(QtCore.Qt.SolidLine)
        self.film_table.setObjectName("film_table")
        self.pages.addWidget(self.films)
        self.pages.raise_()
        self.widget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pages.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FilmsBooksSerials"))
        self.logo.setText(_translate("MainWindow", "FilmsBooksSerials"))
        self.serialsButton.setText(_translate("MainWindow", "Serials"))
        self.booksButton.setText(_translate("MainWindow", "Books"))
        self.filmsButton.setText(_translate("MainWindow", "Films"))
        self.welcome_label.setText(_translate("MainWindow", "Welcome to FilmsBooksSerials..."))
        self.serials_l.setText(_translate("MainWindow", "Serials"))
        self.book_l.setText(_translate("MainWindow", "Books"))
        self.film_l.setText(_translate("MainWindow", "Films"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
