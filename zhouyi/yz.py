import sys
from PyQt5.QtCore import QEventLoop, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial
import zy


# 添加所有输出
def add_output(list2, list3, list4, number, flag, con):
    n = len(list2[0])  # 物理块使用个数
    Str0 = ''
    i = 0
    for i in range(n):
        Str0 = Str0 + list2[0][i] + '\n'
    list3[number] = Str0
    if flag == 0:
        Str1 = "此次置换发生缺页,"+"被置换的物理块为"+str(con)+"\n"
    else:
        Str1 = "此次置换未发生缺页"+"\n"
    list4[number] = Str1
    return 0

def sleep_1():
    loop = QEventLoop()
    QTimer.singleShot(2000, loop.quit)
    loop.exec_()

# 输出所有
def output_all0(list3, list4):
    i = 0
    ui.textEdit_100.append(list4[i])
    ui.textEdit_1.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_100.append(list4[i])
    ui.textEdit_2.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_100.append(list4[i])
    ui.textEdit_3.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_100.append(list4[i])
    ui.textEdit_4.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_100.append(list4[i])
    ui.textEdit_5.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_100.append(list4[i])
    ui.textEdit_6.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_100.append(list4[i])
    ui.textEdit_7.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_100.append(list4[i])
    ui.textEdit_8.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_100.append(list4[i])
    ui.textEdit_9.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_100.append(list4[i])
    ui.textEdit_10.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_100.append(list4[i])
    ui.textEdit_11.setPlainText(list3[i])
    sleep_1()
    ui.textEdit_100.append('执行完成！！！')
    return 0

def output_all1(list3, list4):
    i = 0
    ui.textEdit_200.append(list4[i])
    ui.textEdit_201.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_200.append(list4[i])
    ui.textEdit_202.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_200.append(list4[i])
    ui.textEdit_203.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_200.append(list4[i])
    ui.textEdit_204.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_200.append(list4[i])
    ui.textEdit_205.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_200.append(list4[i])
    ui.textEdit_206.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_200.append(list4[i])
    ui.textEdit_207.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_200.append(list4[i])
    ui.textEdit_208.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_200.append(list4[i])
    ui.textEdit_209.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_200.append(list4[i])
    ui.textEdit_210.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_200.append(list4[i])
    ui.textEdit_211.setPlainText(list3[i])
    sleep_1()
    ui.textEdit_200.append('执行完成！！！')
    return 0

def output_all2(list3, list4):
    i = 0
    ui.textEdit_300.append(list4[i])
    ui.textEdit_301.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_300.append(list4[i])
    ui.textEdit_302.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_300.append(list4[i])
    ui.textEdit_303.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_300.append(list4[i])
    ui.textEdit_304.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_300.append(list4[i])
    ui.textEdit_305.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_300.append(list4[i])
    ui.textEdit_306.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_300.append(list4[i])
    ui.textEdit_307.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_300.append(list4[i])
    ui.textEdit_308.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_300.append(list4[i])
    ui.textEdit_309.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_300.append(list4[i])
    ui.textEdit_310.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_300.append(list4[i])
    ui.textEdit_311.setPlainText(list3[i])
    sleep_1()
    ui.textEdit_300.append('执行完成！！！')
    return 0

def output_all3(list3, list4):
    i = 0
    ui.textEdit_400.append(list4[i])
    ui.textEdit_401.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_400.append(list4[i])
    ui.textEdit_402.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_400.append(list4[i])
    ui.textEdit_403.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_400.append(list4[i])
    ui.textEdit_404.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_400.append(list4[i])
    ui.textEdit_405.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_400.append(list4[i])
    ui.textEdit_406.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_400.append(list4[i])
    ui.textEdit_407.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_400.append(list4[i])
    ui.textEdit_408.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_400.append(list4[i])
    ui.textEdit_409.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_400.append(list4[i])
    ui.textEdit_410.setPlainText(list3[i])
    i += 1
    sleep_1()
    ui.textEdit_400.append(list4[i])
    ui.textEdit_411.setPlainText(list3[i])
    sleep_1()
    ui.textEdit_400.append('执行完成！！！')
    return 0

def select_li(list2, li):
    for lj in list2[0]:
        if lj == li:
            return 1
    return 0

def FIFO(number, list1, list3, list4):
    # 用于标志物理块是否被用完
    num = 0
    # 使用二维列表依次存储物理块存储的页面，以及其对应的运行时间
    list2 = [[], []]
    # 标志是否缺页
    flag = 0
    # 记录置换出去的页面
    con = 0
    # 存储所有输出数据
    for i in range(N):
        list2[1].append(0)
    for li in list1:
        if select_li(list2, li):
            for i in range(len(list2[1])):
                list2[1][i] += 1
            flag = 1
            add_output(list2, list3, list4, number, flag, con)
            number += 1
        elif num < N:
            for i in range(len(list2[0])):
                list2[1][i] += 1
            list2[0].append(li)
            list2[1][num] = 1
            con = num
            num += 1
            flag = 0
            add_output(list2, list3, list4, number, flag, con)
            number += 1
        else:
            f = list2[1].index(max(list2[1]))
            con = f
            list2[0][f] = li
            list2[1][f] = 0
            for i in range(len(list2[1])):
                list2[1][i] += 1
            flag = 0
            add_output(list2, list3, list4, number, flag, con)
            number += 1
    return 0

def LRU(number, list1, list3, list4):
    # 用于标志物理块是否被用完
    num = 0
    # 使用二维列表依次存储物理块存储的页面，以及其对应的运行时间
    list2 = [[], []]
    # 记录置换出去的页面
    con = 0
    # 标志是否缺页
    flag = 0
    for i in range(N):
        list2[1].append(0)
    for li in list1:
        if select_li(list2, li):
            f = list2[0].index(li)
            list2[1][f] = 0
            for i in range(len(list2[1])):
                list2[1][i] += 1
            flag = 1
            add_output(list2, list3, list4, number, flag, con)
            number += 1
        elif num < N:
            for i in range(len(list2[0])):
                list2[1][i] += 1
            list2[0].append(li)
            list2[1][num] = 1
            con = num
            num += 1
            flag = 0
            add_output(list2, list3, list4, number, flag, con)
            number += 1
        else:
            f = list2[1].index(max(list2[1]))
            con = f
            list2[0][f] = li
            list2[1][f] = 0
            for i in range(len(list2[1])):
                list2[1][i] += 1
            flag = 0
            add_output(list2, list3, list4, number, flag, con)
            number += 1

def LFU(number, list1, list3, list4):
    # 用于标志物理块是否被用完
    num = 0
    # 使用二维列表依次存储物理块存储的页面，以及其对应的运行时间
    list2 = [[], []]
    # 记录置换出去的页面
    con = 0
    # 标志是否缺页
    flag = 0
    for i in range(N):
        list2[1].append(0)
    for li in list1:
        if select_li(list2, li):
            f = list2[0].index(li)
            list2[1][f] = 0
            for i in range(len(list2[1])):
                list2[1][i] += 1
            flag = 1
            add_output(list2, list3, list4, number, flag, con)
            number += 1
        elif num < N:
            for i in range(len(list2[0])):
                list2[1][i] += 1
            list2[0].append(li)
            list2[1][num] = 1
            con = num
            num += 1
            flag = 0
            add_output(list2, list3, list4, number, flag, con)
            number += 1
        else:
            f = list2[1].index(max(list2[1]))
            con = f
            list2[0][f] = li
            list2[1][f] = 0
            for i in range(len(list2[1])):
                list2[1][i] += 1
            flag = 0
            add_output(list2, list3, list4, number, flag, con)
            number += 1

def clock(number, list1, list3, list4):
    # 用于标志物理块是否被用完
    num = 0
    # 使用二维列表依次存储物理块存储的页面，以及其对应的运行时间
    list2 = [[], []]
    # 记录置换出去的页面
    con = 0
    # 标志是否缺页
    flag = 0
    # 循环
    global x
    x = 0
    for i in range(N):
        list2[1].append(0)
    for li in list1:
        if select_li(list2, li):
            flag = 1
            add_output(list2, list3, list4, number, flag, con)
            number += 1
        elif num < N:
            list2[0].append(li)
            list2[1][num] = 1
            con = num
            num += 1
            flag = 0
            add_output(list2, list3, list4, number, flag, con)
            number += 1
        else:
            while 1:
                x = x % N
                con = x
                if list2[1][x] == 0:
                    list2[0][x] = li
                    list2[1][x] = 1
                    x += 1
                    break
                else:
                    list2[1][x] = 0
                    x += 1
            flag = 0
            add_output(list2, list3, list4, number, flag, con)
            number += 1

def create0(ui):
    global list1
    global N
    global number
    global list3   # 存储11个小窗口输出内容
    global list4   # 存储大窗口输出内容
    number = 0
    list1 = ui.lineEdit_101.text()
    N = int(ui.lineEdit_102.text())
    list3 = []
    for i in range(11):
        list3.append('')
    list4 = []
    for i in range(11):
        list4.append('')
    FIFO(number, list1, list3, list4)
    output_all0(list3, list4)

def create1(ui):
    global list1
    global N
    global number
    global list3   # 存储11个小窗口输出内容
    global list4   # 存储大窗口输出内容
    number = 0
    list1 = ui.lineEdit_201.text()
    N = int(ui.lineEdit_202.text())
    list3 = []
    for i in range(11):
        list3.append('')
    list4 = []
    for i in range(11):
        list4.append('')
    LRU(number, list1, list3, list4)
    output_all1(list3, list4)

def create2(ui):
    global list1
    global N
    global number
    global list3   # 存储11个小窗口输出内容
    global list4   # 存储大窗口输出内容
    number = 0
    list1 = ui.lineEdit_301.text()
    N = int(ui.lineEdit_302.text())
    list3 = []
    for i in range(11):
        list3.append('')
    list4 = []
    for i in range(11):
        list4.append('')
    LFU(number, list1, list3, list4)
    output_all2(list3, list4)

def create3(ui):
    global list1
    global N
    global number
    global list3   # 存储11个小窗口输出内容
    global list4   # 存储大窗口输出内容
    number = 0
    list1 = ui.lineEdit_401.text()
    N = int(ui.lineEdit_402.text())
    list3 = []
    for i in range(11):
        list3.append('')
    list4 = []
    for i in range(11):
        list4.append('')
    clock(number, list1, list3, list4)
    output_all3(list3, list4)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = zy.Ui_WindowMain()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton_101.clicked.connect(partial(create0, ui))
    ui.pushButton_201.clicked.connect(partial(create1, ui))
    ui.pushButton_301.clicked.connect(partial(create2, ui))
    ui.pushButton_401.clicked.connect(partial(create3, ui))
    sys.exit(app.exec_())
