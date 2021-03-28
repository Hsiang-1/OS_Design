# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windows_05.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import QPixmap, QPainter, QCursor, QBitmap
from PyQt5.QtCore import Qt, QSize, QTimer
from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QWidget,
                            QPushButton, QGridLayout, QSpacerItem,
                            QSizePolicy, QLabel, QApplication)
from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(946, 572)
        MainWindow.setFixedSize(946, 572)
        MainWindow.layout = QtWidgets.QGridLayout()
        MainWindow.layout.setContentsMargins(0, 0, 0, 0)
        MainWindow.setObjectName('body')
        MainWindow.setStyleSheet('''
                           QMainWindow#body{
                               background-color:none;
                           }
                           QToolButton,QPushButton{
                               border: none;
                               color: #f6f6f6;
                               border: 1px solid #9FA3A9;
                           }
                           QToolButton,QPushButton:hover{
                               color:#fff;
                               border: 1px solid #9FA3A9;
                               background-color:  rgba(250, 128, 144, 0.5);
                           }
                           QWidget#acount_group,#pwd_gourp{
                               border-bottom:1px solid #E0E0E0;
                           }
                           QCheckBox,QLabel,QRadioButton,QTextEdit{
                               color:white;
                           }
                           QToolButton#wx_icon{
                               color:#9FA3A9;
                           }
                           QToolButton#wx_icon:hover{
                               color:#1ABB0E;
                           }
                           QToolButton#qq_icon{
                               color:#378AFE;
                           }
                           QToolButton#qq_icon:hover{
                               color:#378AFE;
                           }
                           QTextBrowser{
                                background-color:  rgba(250, 128, 144, 0.2);
                                border: 1px solid #E0E0E0;
                                border-style:outset;
                           }
                           QTableWidget{
                                background-color : rgba(250, 128, 144, 0.2);
                                border: 1px solid #E0E0E0;
                                border-style:outset;
                           }
                           QHeaderView::section{
                                background-color: transparent;
                                color: black;
                           }
                           '''
                                 )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        # self.graphicsView.setGeometry(QtCore.QRect(-70, -30, 1151, 681))
        # self.graphicsView.setStyleSheet("background-color: rgb(240, 240, 240);")
        # self.graphicsView.setObjectName("graphicsView")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 350, 851, 171))
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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 70, 91, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 70, 91, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 70, 91, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 110, 91, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 110, 91, 23))
        self.pushButton_5.setObjectName("pushButton_5")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 40, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(600, 40, 54, 12))
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(370, 70, 211, 241))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(600, 70, 301, 241))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 320, 54, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 160, 54, 12))
        self.label_5.setObjectName("label_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 180, 91, 101))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(250, 180, 91, 101))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(150, 180, 91, 101))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(810, 30, 91, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 530, 81, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(480, 530, 111, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(150, 530, 61, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(590, 530, 61, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(220, 530, 61, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(660, 530, 61, 16))
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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
        self.pushButton.setText(_translate("MainWindow", "先进先出"))
        self.pushButton_2.setText(_translate("MainWindow", "短作业优先"))
        self.pushButton_3.setText(_translate("MainWindow", "优先级算法"))
        self.pushButton_4.setText(_translate("MainWindow", "时间片轮转"))
        self.pushButton_5.setText(_translate("MainWindow", "多级队列"))
        self.label.setText(_translate("MainWindow", "算法选择"))
        self.label_2.setText(_translate("MainWindow", "算法简介"))
        self.label_3.setText(_translate("MainWindow", "执行步骤"))
        self.label_4.setText(_translate("MainWindow", "运行结果"))
        self.label_5.setText(_translate("MainWindow", "执行程序"))
        self.pushButton_6.setText(_translate("MainWindow", "用户输入"))
        self.pushButton_7.setText(_translate("MainWindow", "清空"))
        self.pushButton_8.setText(_translate("MainWindow", "随机输入"))
        self.pushButton_9.setText(_translate("MainWindow", "返回"))
        self.label_6.setText(_translate("MainWindow", "平均周转时间"))
        self.label_7.setText(_translate("MainWindow", "平均带权周转时间"))
        self.label_8.setText(_translate("MainWindow", "TextLable"))
        self.label_9.setText(_translate("MainWindow", "TextLable"))
        self.label_10.setText(_translate("MainWindow", "s"))
        self.label_11.setText(_translate("MainWindow", "s"))

class Container(QtWidgets.QWidget):
    def __init__(self, window):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(window)
        lay.setContentsMargins(10, 10, 10, 10)
        shadow = QtWidgets.QGraphicsDropShadowEffect(self,
                                                                 blurRadius=9.0,
                                                                 color=QtGui.QColor(116, 116, 116),
                                                                 offset=QtCore.QPointF(0, 0)
                                                                 )

        window.setGraphicsEffect(shadow)

    def mousePressEvent(self, event):  # 鼠标长按事件
        if event.button() == QtCore.Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):  # 鼠标移动事件
        if QtCore.Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):  # 鼠标释放事件
        self.m_drag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

class AMainWindow(QWidget):
    BorderColor     = QtGui.QColor(0, 0, 0, 255)
    BackgroundColor = QtGui.QColor(255, 165, 0, 180)

    def __init__(self, window):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Size = QWidget.setFixedSize(self, 1000, 647)
        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(window)
        lay.setContentsMargins(10, 10, 10, 10)
        shadow = QtWidgets.QGraphicsDropShadowEffect(self,
                                                     blurRadius=9.0,
                                                     color=QtGui.QColor(116, 116, 116),
                                                     offset=QtCore.QPointF(0, 0)
                                                     )

        window.setGraphicsEffect(shadow)
        self.initUI()  # 界面绘制交给InitUi方法
        quit = QPushButton('Close', self)  # button 对象
        quit.setGeometry(930, 10, 50, 20)  # 设置按钮的位置 和 大小
        quit.setStyleSheet("background-color: red")  # 设置按钮的风格和颜色
        quit.clicked.connect(self.close)  # 点击按钮之后关闭窗口

    def initUI(self):
        pix = QPixmap('bigone.jpg')
        lb1 = QLabel(self)
        lb1.setGeometry(0, 0, 1000, 647)
        lb1.setStyleSheet("background-color:rgba(255,0,0,30)")
        lb1.setPixmap(pix)
        lb1.setScaledContents(True)
        print(lb1.size())
        lb1.lower()

    def mousePressEvent(self, event):  # 鼠标长按事件
            if event.button() == QtCore.Qt.LeftButton:
                    self.m_drag = True
                    self.m_DragPosition = event.globalPos() - self.pos()
                    event.accept()
                    self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):  # 鼠标移动事件
            if QtCore.Qt.LeftButton and self.m_drag:
                    self.move(QMouseEvent.globalPos() - self.m_DragPosition)
                    QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):  # 鼠标释放事件
            self.m_drag = False
            self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    ui = Ui_MainWindow()  # 根据上面所创建的类的名字更改

    ui.setupUi(MainWindow)
    MainWindow=AMainWindow(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
