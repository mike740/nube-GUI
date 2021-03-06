# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gra.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_answer(object):
    def setupUi(self, answer):
        answer.setObjectName("answer")
        answer.resize(697, 669)
        self.centralwidget = QtWidgets.QWidget(answer)
        self.centralwidget.setObjectName("centralwidget")
        self.area = QtWidgets.QTextEdit(self.centralwidget)
        self.area.setGeometry(QtCore.QRect(230, 70, 91, 31))
        self.area.setObjectName("area")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 80, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 120, 71, 16))
        self.label_2.setObjectName("label_2")
        self.pc = QtWidgets.QTextEdit(self.centralwidget)
        self.pc.setGeometry(QtCore.QRect(230, 110, 91, 31))
        self.pc.setObjectName("pc")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(430, 80, 91, 51))
        self.button.setObjectName("button")
        self.ans = QtWidgets.QTextEdit(self.centralwidget)
        self.ans.setGeometry(QtCore.QRect(180, 270, 311, 71))
        self.ans.setObjectName("ans")
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(430, 140, 91, 51))
        self.button2.setObjectName("button2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 160, 71, 16))
        self.label_4.setObjectName("label_4")
        self.period = QtWidgets.QTextEdit(self.centralwidget)
        self.period.setGeometry(QtCore.QRect(230, 150, 91, 31))
        self.period.setObjectName("period")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(180, 350, 311, 241))
        self.graphicsView.setObjectName("graphicsView")
        self.period_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.period_2.setGeometry(QtCore.QRect(230, 190, 91, 31))
        self.period_2.setObjectName("period_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 200, 71, 16))
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(510, 270, 101, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 10, 251, 51))
        self.label_3.setStyleSheet("border-image: url(:/cct/UOL logo.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        answer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(answer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 697, 18))
        self.menubar.setObjectName("menubar")
        answer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(answer)
        self.statusbar.setObjectName("statusbar")
        answer.setStatusBar(self.statusbar)

        self.retranslateUi(answer)
        QtCore.QMetaObject.connectSlotsByName(answer)

    def retranslateUi(self, answer):
        _translate = QtCore.QCoreApplication.translate
        answer.setWindowTitle(_translate("answer", "MainWindow"))
        self.label.setText(_translate("answer", "Area"))
        self.label_2.setText(_translate("answer", "Postcode"))
        self.button.setText(_translate("answer", "Push"))
        self.button2.setText(_translate("answer", "Erase"))
        self.label_4.setText(_translate("answer", "Period"))
        self.label_5.setText(_translate("answer", "Loan"))
        self.comboBox.setItemText(0, _translate("answer", "Residential"))
        self.comboBox.setItemText(1, _translate("answer", "Business"))
        self.comboBox.setItemText(2, _translate("answer", "Industrial"))

from pyqtgraph import PlotWidget
import logo3_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    answer = QtWidgets.QMainWindow()
    ui = Ui_answer()
    ui.setupUi(answer)
    answer.show()
    sys.exit(app.exec_())

