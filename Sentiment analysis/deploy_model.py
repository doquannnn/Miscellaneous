# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sent_ana.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import pandas as pd
import joblib
import re
from nltk.stem import PorterStemmer
from CustomTransformer import TextPreprocessing
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        self.model = joblib.load('grid_tfidf.joblib').best_estimator_

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 561))
        self.label.setText("HEL")
        self.label.setPixmap(QtGui.QPixmap("images/Landscape.png"))
        self.label.setObjectName("label")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(270, 10, 271, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.text = QtWidgets.QTextEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(220, 80, 391, 131))
        self.text.setObjectName("text")
        self.predict = QtWidgets.QPushButton(self.centralwidget)
        self.predict.setGeometry(QtCore.QRect(330, 220, 161, 32))
        self.predict.setObjectName("predict")
        self.emotion = QtWidgets.QLabel(self.centralwidget)
        self.emotion.setGeometry(QtCore.QRect(280, 250, 291, 281))
        self.emotion.setText("")
        self.emotion.setObjectName("emotion")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.predict.clicked.connect(self.predict_pressed)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Sentiment Analysis"))
        self.predict.setText(_translate("MainWindow", "PREDICT"))

    def predict_pressed(self):
        self.status = pd.DataFrame([self.text.toPlainText()], columns=['text'])
        result = self.model.predict(self.status)[0]

        if result == 0:
            self.emotion.setPixmap(QtGui.QPixmap("images/Sad.png"))
        else:
            self.emotion.setPixmap(QtGui.QPixmap("images/Happy.png"))
        # print(self.text.toPlainText())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
