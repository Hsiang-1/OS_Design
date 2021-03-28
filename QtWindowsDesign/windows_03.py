# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windows_03.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(946, 637)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(-70, -40, 1151, 681))
        self.graphicsView.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.graphicsView.setObjectName("graphicsView")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 420, 851, 131))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 6, item)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 60, 111, 21))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(78, 112, 133);\n"
"font: 12pt \"微软雅黑\";\n"
"border: none")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 60, 111, 21))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(78, 112, 133);\n"
"font: 12pt \"微软雅黑\";\n"
"border: none")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 60, 121, 21))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(78, 112, 133);\n"
"font: 12pt \"微软雅黑\";\n"
"border: none")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(420, 60, 121, 21))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(78, 112, 133);\n"
"font: 12pt \"微软雅黑\";\n"
"border: none")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(560, 60, 111, 21))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(78, 112, 133);\n"
"font: 12pt \"微软雅黑\";\n"
"border: none")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 150, 71, 21))
        self.label_2.setStyleSheet("color: rgb(69, 136, 248);\n"
"font: 11pt \"微软雅黑\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(600, 150, 71, 21))
        self.label_3.setStyleSheet("color: rgb(69, 136, 248);\n"
"font: 11pt \"微软雅黑\";")
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(360, 180, 211, 161))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(600, 180, 321, 161))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 390, 71, 21))
        self.label_4.setStyleSheet("color: rgb(69, 136, 248);\n"
"font: 11pt \"微软雅黑\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 250, 54, 12))
        self.label_5.setObjectName("label_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 270, 91, 71))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(230, 270, 91, 71))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(130, 270, 91, 71))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(810, 10, 111, 31))
        self.pushButton_9.setStyleSheet("background:#19A9FF;\n"
"border-radius:12px;\n"
"border:none;\n"
"\n"
"\n"
"font-size:13px;\n"
"font: 12pt \"微软雅黑\";\n"
"color: #E5F5FF;\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.pushButton_9.setCheckable(False)
        self.pushButton_9.setAutoExclusive(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 570, 81, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(460, 570, 111, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 190, 54, 12))
        self.label_8.setObjectName("label_8")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(50, 210, 41, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(110, 210, 41, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(170, 210, 41, 16))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(230, 210, 41, 16))
        self.radioButton_4.setObjectName("radioButton_4")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(-30, -20, 1081, 71))
        self.graphicsView_2.setStyleSheet("background-color: rgb(4, 131, 213);")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 10, 231, 31))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 20pt \"微软雅黑\";")
        self.label_9.setObjectName("label_9")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(0, 100, 961, 31))
        self.graphicsView_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: none")
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_4.setGeometry(QtCore.QRect(-10, 140, 961, 231))
        self.graphicsView_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: none")
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.graphicsView_5 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_5.setGeometry(QtCore.QRect(-10, 380, 961, 231))
        self.graphicsView_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: none")
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.graphicsView_6 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_6.setGeometry(QtCore.QRect(0, 50, 961, 41))
        self.graphicsView_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: none")
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 150, 71, 21))
        self.label_10.setStyleSheet("color: rgb(69, 136, 248);\n"
"font: 11pt \"微软雅黑\";")
        self.label_10.setObjectName("label_10")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 170, 301, 16))
        self.line.setStyleSheet("border-color: rgb(106, 181, 230);\n"
"selection-color: rgb(106, 181, 230);\n"
"color: rgb(106, 181, 230);\n"
"gridline-color: rgb(106, 181, 230);\n"
"line-color: rgb(106, 181, 230);\n"
"alternate-background-color: rgb(106, 181, 230);\n"
"")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 106, 91, 20))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(78, 112, 133);\n"
"font: 11pt \"微软雅黑\";\n"
"border: none")
        self.label.setObjectName("label")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(120, 106, 91, 20))
        self.label_11.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(78, 112, 133);\n"
"font: 12pt \"微软雅黑\";\n"
"border: none")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(210, 570, 16, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(630, 570, 16, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(140, 570, 51, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(570, 570, 51, 16))
        self.label_15.setObjectName("label_15")
        self.graphicsView.raise_()
        self.graphicsView_6.raise_()
        self.graphicsView_5.raise_()
        self.graphicsView_4.raise_()
        self.graphicsView_3.raise_()
        self.graphicsView_2.raise_()
        self.tableWidget.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.textBrowser.raise_()
        self.textBrowser_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        self.radioButton_3.raise_()
        self.radioButton_4.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.line.raise_()
        self.label.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "作业号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "到达时间"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "开始时间"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "运行时间"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "完成时间"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "周转时间"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "带权周转时间"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.item(0, 6)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.item(1, 4)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.item(1, 5)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.item(1, 6)
        item.setText(_translate("MainWindow", "7"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "先进先出算法"))
        self.pushButton_2.setText(_translate("MainWindow", "短作业优先算法"))
        self.pushButton_3.setText(_translate("MainWindow", "优先级调度算法"))
        self.pushButton_4.setText(_translate("MainWindow", "时间片轮转调度"))
        self.pushButton_5.setText(_translate("MainWindow", "多级队列调度"))
        self.label_2.setText(_translate("MainWindow", "算法简介"))
        self.label_3.setText(_translate("MainWindow", "执行步骤"))
        self.label_4.setText(_translate("MainWindow", "运行结果"))
        self.label_5.setText(_translate("MainWindow", "执行程序"))
        self.pushButton_6.setText(_translate("MainWindow", "用户输入"))
        self.pushButton_7.setText(_translate("MainWindow", "清空"))
        self.pushButton_8.setText(_translate("MainWindow", "随机输入"))
        self.pushButton_9.setText(_translate("MainWindow", "安全退出"))
        self.label_6.setText(_translate("MainWindow", "平均周转时间"))
        self.label_7.setText(_translate("MainWindow", "平均带权周转时间"))
        self.label_8.setText(_translate("MainWindow", "作业数量"))
        self.radioButton.setText(_translate("MainWindow", "3"))
        self.radioButton_2.setText(_translate("MainWindow", "4"))
        self.radioButton_3.setText(_translate("MainWindow", "5"))
        self.radioButton_4.setText(_translate("MainWindow", "6"))
        self.label_9.setText(_translate("MainWindow", "作业调度演示系统"))
        self.label_10.setText(_translate("MainWindow", "输入选择"))
        self.label.setText(_translate("MainWindow", "当前位置  --"))
        self.label_11.setText(_translate("MainWindow", "TextLabel"))
        self.label_12.setText(_translate("MainWindow", "s"))
        self.label_13.setText(_translate("MainWindow", "s"))
        self.label_14.setText(_translate("MainWindow", "TextLable"))
        self.label_15.setText(_translate("MainWindow", "TextLable"))
import icons_rc
