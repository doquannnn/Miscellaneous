# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testing_graph.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import D_graph as weighted_graph
import DFS_graph as depth_graph
import BFS_graph as breadth_graph

class Ui_MainWindow(object):
    def __init__(self):
        self.DFS_activate = False
        self.BFS_activate = False
        self.Dijkstra_activate = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(934, 588)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background_label = QtWidgets.QLabel(self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(0, -40, 931, 581))
        self.background_label.setText("")
        self.background_label.setPixmap(QtGui.QPixmap("Landscape.png"))
        self.background_label.setObjectName("background_label")
        self.BFS_button = QtWidgets.QPushButton(self.centralwidget)
        self.BFS_button.setGeometry(QtCore.QRect(60, 10, 113, 32))
        self.BFS_button.setObjectName("BFS_button")
        self.DFS_button = QtWidgets.QPushButton(self.centralwidget)
        self.DFS_button.setGeometry(QtCore.QRect(60, 40, 113, 32))
        self.DFS_button.setObjectName("DFS_button")
        self.d_button = QtWidgets.QPushButton(self.centralwidget)
        self.d_button.setGeometry(QtCore.QRect(60, 70, 113, 32))
        self.d_button.setObjectName("d_button")
        self.comboBox_source = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_source.setGeometry(QtCore.QRect(220, 40, 61, 26))
        self.comboBox_source.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_source.setObjectName("comboBox_source")
        self.comboBox_source.addItem("")
        self.comboBox_source.addItem("")
        self.comboBox_source.addItem("")
        self.comboBox_source.addItem("")
        self.comboBox_source.addItem("")
        self.comboBox_source.addItem("")
        self.label_source = QtWidgets.QLabel(self.centralwidget)
        self.label_source.setGeometry(QtCore.QRect(210, 20, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_source.setFont(font)
        self.label_source.setTextFormat(QtCore.Qt.AutoText)
        self.label_source.setAlignment(QtCore.Qt.AlignCenter)
        self.label_source.setObjectName("label_source")
        self.label_path = QtWidgets.QLabel(self.centralwidget)
        self.label_path.setGeometry(QtCore.QRect(570, 80, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_path.setFont(font)
        self.label_path.setObjectName("label_path")
        self.label_traverse = QtWidgets.QLabel(self.centralwidget)
        self.label_traverse.setGeometry(QtCore.QRect(190, 70, 350, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_traverse.setFont(font)
        self.label_traverse.setObjectName("label_traverse")
        self.from_label = QtWidgets.QLabel(self.centralwidget)
        self.from_label.setGeometry(QtCore.QRect(580, 20, 41, 16))
        self.from_label.setObjectName("from_label")
        self.to_label = QtWidgets.QLabel(self.centralwidget)
        self.to_label.setGeometry(QtCore.QRect(680, 20, 21, 16))
        self.to_label.setObjectName("to_label")
        self.comboBox_from = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_from.setGeometry(QtCore.QRect(570, 40, 61, 26))
        self.comboBox_from.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_from.setObjectName("comboBox_from")
        self.comboBox_from.addItem("")
        self.comboBox_from.addItem("")
        self.comboBox_from.addItem("")
        self.comboBox_from.addItem("")
        self.comboBox_from.addItem("")
        self.comboBox_from.addItem("")
        self.comboBox_to = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_to.setGeometry(QtCore.QRect(660, 40, 61, 26))
        self.comboBox_to.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_to.setObjectName("comboBox_to")
        self.comboBox_to.addItem("")
        self.comboBox_to.addItem("")
        self.comboBox_to.addItem("")
        self.comboBox_to.addItem("")
        self.comboBox_to.addItem("")
        self.comboBox_to.addItem("")
        self.pushButton_go = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_go.setGeometry(QtCore.QRect(320, 40, 71, 32))
        self.pushButton_go.setObjectName("pushButton_go")
        self.pushButton_find = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_find.setGeometry(QtCore.QRect(750, 40, 81, 31))
        self.pushButton_find.setObjectName("pushButton_find")
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(20, 110, 871, 421))
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 934, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.BFS_button.clicked.connect(self.show_BFS)
        self.DFS_button.clicked.connect(self.show_DFS)
        self.d_button.clicked.connect(self.show_Dijkstra)

        self.pushButton_go.clicked.connect(self.source_pressed)
        self.pushButton_find.clicked.connect(self.path_pressed)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pathfinding Algorithms Demo"))
        self.BFS_button.setText(_translate("MainWindow", "BFS"))
        self.DFS_button.setText(_translate("MainWindow", "DFS"))
        self.d_button.setText(_translate("MainWindow", "Dijkstra"))
        self.comboBox_source.setCurrentText(_translate("MainWindow", "0"))
        self.comboBox_source.setItemText(0, _translate("MainWindow", "0"))
        self.comboBox_source.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_source.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_source.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_source.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_source.setItemText(5, _translate("MainWindow", "5"))
        self.label_source.setText(_translate("MainWindow", "SOURCE"))
        self.label_path.setText(_translate("MainWindow", "PATH:"))
        self.label_traverse.setText(_translate("MainWindow", "TRAVERSE:"))
        self.from_label.setText(_translate("MainWindow", "FROM"))
        self.to_label.setText(_translate("MainWindow", "TO"))
        self.comboBox_from.setCurrentText(_translate("MainWindow", "0"))
        self.comboBox_from.setItemText(0, _translate("MainWindow", "0"))
        self.comboBox_from.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_from.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_from.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_from.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_from.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_to.setCurrentText(_translate("MainWindow", "0"))
        self.comboBox_to.setItemText(0, _translate("MainWindow", "0"))
        self.comboBox_to.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_to.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_to.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_to.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_to.setItemText(5, _translate("MainWindow", "5"))
        self.pushButton_go.setText(_translate("MainWindow", "GO!"))
        self.pushButton_find.setText(_translate("MainWindow", "FIND!"))

    def source_pressed(self):
        source = int(self.comboBox_source.currentText())
        traverse_path = ""
                                                                                                                                             
        if self.BFS_activate:    
            breadth_graph.BFS(source)
            traversed_path = ' '.join(breadth_graph.trace)

        elif self.DFS_activate:
            depth_graph.DFS(source)
            traversed_path = ' '.join(depth_graph.trace)

        elif self.Dijkstra_activate:
            weighted_graph.Dijkstra(source)
            traversed_path = ' '.join(weighted_graph.trace) 

        else:
            traversed_path = "Please select one algorithm!"

        self.label_traverse.setText(f'TRAVERSE: {traversed_path}')

    def path_pressed(self):
        fro = int(self.comboBox_from.currentText())
        to = int(self.comboBox_to.currentText())
        path = ""

        
        if self.BFS_activate:
            breadth_graph.BFS(fro)
            path = breadth_graph.tracePath(fro, to)
        elif self.DFS_activate:
            depth_graph.DFS(fro)
            path = depth_graph.tracePath(fro, to)
        elif self.Dijkstra_activate:
            weighted_graph.Dijkstra(fro)
            path = f"{weighted_graph.tracePath(fro, to)} Total Weight: {weighted_graph.dist[to]}"
        else:
            path = "Please select one algorithm!"

        self.label_path.setText(f'PATH: {path}')


    def show_DFS(self):
        self.DFS_activate = True
        self.BFS_activate = False
        self.Dijkstra_activate = False
        self.label_image.setPixmap(QtGui.QPixmap("DFS_BFS.png"))

    def show_BFS(self):
        self.BFS_activate = True
        self.DFS_activate = False
        self.Dijkstra_activate = False
        self.label_image.setPixmap(QtGui.QPixmap("DFS_BFS.png"))

    def show_Dijkstra(self):
        self.Dijkstra_activate = True
        self.BFS_activate = False
        self.DFS_activate = False
        self.label_image.setPixmap(QtGui.QPixmap("d.png"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
