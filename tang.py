# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tang.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_jinchengdiaodusuanfa(object):
    def setupUi(self, jinchengdiaodusuanfa):
        jinchengdiaodusuanfa.setObjectName("jinchengdiaodusuanfa")
        jinchengdiaodusuanfa.resize(1120, 630)
        jinchengdiaodusuanfa.setMinimumSize(QtCore.QSize(800, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        jinchengdiaodusuanfa.setFont(font)
        self.centralwidget = QtWidgets.QWidget(jinchengdiaodusuanfa)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 80, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 80, 91, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 80, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 120, 93, 171))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 80, 87, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(470, 20, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(610, 80, 491, 451))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(30, 120, 291, 171))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 330, 561, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
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
        jinchengdiaodusuanfa.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(jinchengdiaodusuanfa)
        self.statusbar.setObjectName("statusbar")
        jinchengdiaodusuanfa.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(jinchengdiaodusuanfa)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1120, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuFCFS = QtWidgets.QMenu(self.menuBar)
        self.menuFCFS.setObjectName("menuFCFS")
        self.menuSJF = QtWidgets.QMenu(self.menuBar)
        self.menuSJF.setObjectName("menuSJF")
        self.menuPA = QtWidgets.QMenu(self.menuBar)
        self.menuPA.setObjectName("menuPA")
        self.menuRR = QtWidgets.QMenu(self.menuBar)
        self.menuRR.setObjectName("menuRR")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        jinchengdiaodusuanfa.setMenuBar(self.menuBar)
        self.menuBar.addAction(self.menuFCFS.menuAction())
        self.menuBar.addAction(self.menuSJF.menuAction())
        self.menuBar.addAction(self.menuPA.menuAction())
        self.menuBar.addAction(self.menuRR.menuAction())
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())

        self.retranslateUi(jinchengdiaodusuanfa)
        QtCore.QMetaObject.connectSlotsByName(jinchengdiaodusuanfa)

    def retranslateUi(self, jinchengdiaodusuanfa):
        _translate = QtCore.QCoreApplication.translate
        jinchengdiaodusuanfa.setWindowTitle(_translate("jinchengdiaodusuanfa", "进程调度算法"))
        self.pushButton.setText(_translate("jinchengdiaodusuanfa", "手动输入"))
        self.pushButton_2.setText(_translate("jinchengdiaodusuanfa", "随机输入"))
        self.pushButton_3.setText(_translate("jinchengdiaodusuanfa", "清空"))
        self.pushButton_4.setText(_translate("jinchengdiaodusuanfa", "执行"))
        self.comboBox.setItemText(0, _translate("jinchengdiaodusuanfa", "3"))
        self.comboBox.setItemText(1, _translate("jinchengdiaodusuanfa", "4"))
        self.comboBox.setItemText(2, _translate("jinchengdiaodusuanfa", "5"))
        self.comboBox.setItemText(3, _translate("jinchengdiaodusuanfa", "6"))
        self.label.setText(_translate("jinchengdiaodusuanfa", "FCFS"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("jinchengdiaodusuanfa", "进程号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("jinchengdiaodusuanfa", "到达时间"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("jinchengdiaodusuanfa", "执行时间"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("jinchengdiaodusuanfa", "开始执行时间"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("jinchengdiaodusuanfa", "结束时间"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("jinchengdiaodusuanfa", "周转时间"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("jinchengdiaodusuanfa", "带权周转时间"))
        self.menuFCFS.setTitle(_translate("jinchengdiaodusuanfa", "FCFS"))
        self.menuSJF.setTitle(_translate("jinchengdiaodusuanfa", "SJF"))
        self.menuPA.setTitle(_translate("jinchengdiaodusuanfa", "PA"))
        self.menuRR.setTitle(_translate("jinchengdiaodusuanfa", "RR"))
        self.menu.setTitle(_translate("jinchengdiaodusuanfa", "多进程反馈"))
        self.menu_2.setTitle(_translate("jinchengdiaodusuanfa", "返回"))
