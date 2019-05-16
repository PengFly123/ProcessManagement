# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\FengFly123\Desktop\os\os\eric1\1\MianWindows.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,  QInputDialog
import create
from PyQt5.QtGui  import *
class createWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child_create = create.Ui_Dialog()
        self.child_create.setupUi(self)

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(775, 562)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-80, 20, 404, 32))
        # 读取文件的初始化按钮
        self.fileButton = QtWidgets.QPushButton(self.centralwidget)
        self.fileButton.setGeometry(QtCore.QRect(600, 220, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.fileButton.setFont(font)
        self.fileButton.setObjectName("fileButton")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.fileButton.clicked.connect(self.openfile)
        # 加载文件按钮结束
        # 开始模拟按钮
        self.beginButton = QtWidgets.QPushButton(MainWindow)
        self.beginButton.setGeometry(QtCore.QRect(600, 340, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.beginButton.setFont(font)
        self.beginButton.setObjectName("beginButton")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.beginButton.clicked.connect(self.beginProcess)
        # 开始模拟按钮结束
        # 保存文件
        self.baocunButton = QtWidgets.QPushButton(MainWindow)
        self.baocunButton.setGeometry(QtCore.QRect(600, 440, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.baocunButton.setFont(font)
        self.baocunButton.setObjectName("baocunButton")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.baocunButton.clicked.connect(self.baocunwenjian)
        #保存文件结束
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 70, 550, 440))
        self.tableWidget.setMinimumSize(QtCore.QSize(400, 0))
        self.tableWidget.setMidLineWidth(1)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(86)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
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
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 775, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actioncreate = QtWidgets.QAction(MainWindow)
        self.actioncreate.setObjectName("actioncreate")
        self.actiondiaodu = QtWidgets.QAction(MainWindow)
        self.actiondiaodu.setObjectName("actiondiaodu")
        self.actionzuse = QtWidgets.QAction(MainWindow)
        self.actionzuse.setObjectName("actionzuse")
        self.actionhuanxing = QtWidgets.QAction(MainWindow)
        self.actionhuanxing.setObjectName("actionhuanxing")
        self.actionchexiao = QtWidgets.QAction(MainWindow)
        self.actionchexiao.setObjectName("actionchexiao")
        self.menu.addAction(self.actioncreate)
        self.menu.addAction(self.actiondiaodu)
        self.menu.addAction(self.actionzuse)
        self.menu.addAction(self.actionhuanxing)
        self.menu.addAction(self.actionchexiao)
        self.menubar.addAction(self.menu.menuAction())
        self.create = createWindow()  # 创建进程窗口的对象
        # 设置快捷键
        self.actioncreate.setShortcut('Ctrl+c')
        self.actiondiaodu.setShortcut('Ctrl+d')
        self.actionzuse.setShortcut('Ctrl+z')
        self.actionhuanxing.setShortcut('Ctrl+h')
        self.actionchexiao.setShortcut('Ctrl+x')
        self.actioncreate.triggered.connect(self.create.show)       # 创建按钮的信号与槽事件
        self.actiondiaodu.triggered.connect(self.diaodu)    # 调度按钮的信号与槽事件
        self.actionzuse.triggered.connect(self.zusePro)
        self.actionhuanxing.triggered.connect(self.huanxingPro)
        self.actionchexiao.triggered.connect(self.chexiaoPro)
        self.create.child_create.pushButton.clicked.connect(self.createPro)
        self.ready = {5: [], 4: [], 3: [], 2: [], 1: []}        # 就绪队列
        self.run = []           # 运行进程信息
        self.zuse = []
        self.finish = []
        self.kaishimoni = 0
        self.baocun = []
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "进程管理系统"))
        self.label.setText(_translate("MainWindow", "                                     进程列表"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "进程ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "优先级"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "运行时间"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "运行次数"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "状态"))
        self.menu.setTitle(_translate("MainWindow", "进程管理"))
        self.actioncreate.setText(_translate("MainWindow", "创建"))
        self.actiondiaodu.setText(_translate("MainWindow", "调度"))
        self.actionzuse.setText(_translate("MainWindow", "阻塞"))
        self.actionhuanxing.setText(_translate("MainWindow", "唤醒"))
        self.actionchexiao.setText(_translate("MainWindow", "撤销"))
        self.fileButton.setText(_translate("Dialog", "打开文件"))
        self.beginButton.setText(_translate("Dialog", "开始模拟"))
        self.baocunButton.setText(_translate("Dialog", "保存文件"))

    def createPro(self):
        try:
            time = int(self.create.child_create.lineEdit.text())
            if time<=0:
                QMessageBox.about(self, '错误提示', '时间应该为正整数!')
                return
        except:
            QMessageBox.about(self, '错误提示', '时间应该为正整数!')
            return
        else:
            cre_info = [self.create.child_create.comboBox.currentIndex(),
                        self.create.child_create.comboBox.currentText(),
                        self.create.child_create.comboBox_2.currentText(),
                        self.create.child_create.lineEdit.text()]


            for i in range(1, 4):
                newItem = QTableWidgetItem(cre_info[i])
                self.tableWidget.setItem(cre_info[0]+13, i - 1, newItem)
            newItem = QTableWidgetItem('0')
            self.create.close()  # 关闭创建窗口
            self.tableWidget.setItem(cre_info[0]+13, 3, newItem)
            newItem = QTableWidgetItem('就绪')
            self.tableWidget.setItem(cre_info[0]+13, 4, newItem)
    # 打开文件，加载初始化进程信息
    def openfile(self):
        fname = QFileDialog.getOpenFileName(self, '初始化进程', './')
        if fname[0]:
            with open(fname[0], 'r', encoding='gb18030', errors='ignore') as f:
                self.initPlist(f.readlines())

    def initPlist(self, s):
        for i in range(len(s)):
            cre_info = [x for x in s[i].strip().split(' ')]
            for j in range(1, len(cre_info)):
                newItem = QTableWidgetItem(cre_info[j])
                self.tableWidget.setItem(int(cre_info[0]), j - 1, newItem)

    # 开始模拟进程的实现
    # 0: 进程ID   1：优先级    2：运行时间    3： 运行次数    4： 状态
    def beginProcess(self):
        # 获取所有进程
        if self.kaishimoni>0:
            QMessageBox.about(self, '错误提示', '已经开始模拟!')
            return
        else:
            i = 0
            while self.tableWidget.item(i, 0):
                cur = []
                for j in range(5):
                    cur.append(self.tableWidget.item(i, j).text())
                self.ready[int(self.tableWidget.item(i, 1).text())].append(cur)
                i += 1
            pro = 5
            while pro > 0:
                if len(self.ready[pro]) != 0:
                    self.run = self.ready[pro].pop(0)
                    break
                else:
                    pro -= 1
            if pro == 0:
                if len(self.zuse) == 0:
                    QMessageBox.about(self, '进程调度', '所有进程已经完成!')
                    return
                else:
                    QMessageBox.about(self, '进程调度', '就绪队列已完成，请唤醒阻塞队列的进程!')
                    return
            i = 0
            while self.tableWidget.item(i, 0).text() != self.run[0]:
                i += 1
            newItem = QTableWidgetItem('运行')  # 改变表格中元素的值
            newItem.setBackground(QColor('Lime'))
            self.tableWidget.setItem(i, 4, newItem)
        self.kaishimoni += 1

    def diaodu(self):
        # 将当前运行的进程存放到就绪态
        self.baocun.append(self.run)
        self.baocun[-1][-1] = '运行'
        i = 0
        while self.tableWidget.item(i, 0).text() != self.run[0]:
            i += 1
        pro = int(self.tableWidget.item(i, 1).text()) - 1
        if pro < 1:
            # k  = 5
            # while len(self.ready[k])==0 and k>0:
            #     k-=1
            # if k==0:
            if len(self.ready[1]) == 0:  # 优先级为1的个数是否为0， 若为0，则退出
                newItem = QTableWidgetItem('完成')  # 改变进程的状态
                newItem.setBackground(QColor('red'))
                self.tableWidget.setItem(i, 4, newItem)
                newItem = QTableWidgetItem('5')  # 改变进程的状态
                self.tableWidget.setItem(i, 3, newItem)
                self.baocun.append(self.run)
                self.baocun[-1][-1] = '完成'
                if len(self.zuse) == 0:
                    QMessageBox.about(self, '进程调度', '所有进程已经完成!')
                    return
                else:
                    print(self.run)
                    QMessageBox.about(self, '进程调度', '就绪队列已完成，请唤醒阻塞队列的进程!')
                    return
            else:
                pro = 1
        newItem = QTableWidgetItem(str(pro))  # 改变进程的优先级
        self.tableWidget.setItem(i, 1, newItem)
        newItem = QTableWidgetItem(str(int(self.tableWidget.item(i, 3).text()) + 1))  # 改变进程的运行次数
        self.tableWidget.setItem(i, 3, newItem)

        if int(self.tableWidget.item(i, 3).text()) == int(self.tableWidget.item(i, 2).text()):
            newItem = QTableWidgetItem('完成')  # 改变进程的状态
            newItem.setBackground(QColor('red'))
            self.tableWidget.setItem(i, 4, newItem)
        else:
            newItem = QTableWidgetItem('就绪')  # 改变进程的状态
            self.tableWidget.setItem(i, 4, newItem)
            newItem.setBackground(QColor('white'))
            self.ready[pro].append(self.run)
        curMaxPro = 5
        while len(self.ready[curMaxPro]) == 0:
            curMaxPro -= 1
        if curMaxPro == 0:
            newItem = QTableWidgetItem('完成')  # 改变进程的状态
            newItem.setBackground(QColor('red'))
            self.tableWidget.setItem(i, 4, newItem)
            if len(self.zuse) == 0:
                QMessageBox.about(self, '进程调度', '所有进程已经完成!')
                return
            else:
                QMessageBox.about(self, '进程调度', '就绪队列已完成，请唤醒阻塞队列的进程!')
                return
        self.run = self.ready[curMaxPro].pop(0)
        i = 0
        while self.tableWidget.item(i, 0).text() != self.run[0]:
            i += 1
        newItem = QTableWidgetItem('运行')  # 改变表格中元素的值
        newItem.setBackground(QColor('Lime'))
        self.tableWidget.setItem(i, 4, newItem)

    def zusePro(self):
        i = 0
        while self.tableWidget.item(i, 0).text() != self.run[0]:
            i += 1
        newItem = QTableWidgetItem('阻塞')  # 改变表格中元素的值
        self.tableWidget.setItem(i, 4, newItem)
        newItem.setBackground(QColor('Blue'))
        self.zuse.append(self.run)
        self.baocun.append(self.zuse[-1])
        self.baocun[-1][-1] = '阻塞'
        pro = 5
        while pro > 0:
            if len(self.ready[pro]) != 0:
                self.run = self.ready[pro].pop(0)
                break
            else:
                pro -= 1
        if pro == 0:
            if len(self.zuse)==0:
                QMessageBox.about(self, '进程调度', '所有进程已经完成!')
                return
            else:
                QMessageBox.about(self, '进程调度', '就绪队列已完成，请唤醒阻塞队列的进程!')
                return
        i = 0
        while self.tableWidget.item(i, 0).text() != self.run[0]:
            i += 1
        newItem = QTableWidgetItem('运行')  # 改变表格中元素的值
        newItem.setBackground(QColor('Lime'))
        self.tableWidget.setItem(i, 4, newItem)

    def huanxingPro(self):
        try:
            p = self.zuse.pop(0)
        except:
            QMessageBox.about(self, '进程调度', '目前没有阻塞进程!')
        else:
            self.baocun.append(p)
            self.baocun[-1][-1] = '唤醒'
            self.ready[int(p[1])].append(p)
            i = 0
            while self.tableWidget.item(i, 0).text() != p[0]:
                i += 1
            newItem = QTableWidgetItem('就绪')  # 改变表格中元素的值
            self.tableWidget.setItem(i, 4, newItem)
            newItem.setBackground(QColor('white'))
            QMessageBox.about(self, '进程调度', '进程已被唤醒!')
    def huanxingPro(self):
        try:
            p = self.zuse.pop(0)
        except:
            QMessageBox.about(self, '进程调度', '目前没有阻塞进程!')
        else:
            self.baocun.append(p)
            self.baocun[-1][-1] = '唤醒'
            self.ready[int(p[1])].append(p)
            i = 0
            while self.tableWidget.item(i, 0).text() != p[0]:
                i += 1
            newItem = QTableWidgetItem('就绪')  # 改变表格中元素的值
            self.tableWidget.setItem(i, 4, newItem)
            newItem.setBackground(QColor('white'))
            QMessageBox.about(self, '进程调度', '进程已被唤醒!')

    def chexiaoPro(self):
        i = 0
        while self.tableWidget.item(i, 0).text() != self.run[0]:
            i += 1
        newItem = QTableWidgetItem('完成')  # 改变表格中元素的值
        self.tableWidget.setItem(i, 4, newItem)
        newItem.setBackground(QColor('red'))
        pro = 5
        while pro > 0:
            if len(self.ready[pro]) != 0:
                self.run = self.ready[pro].pop(0)
                break
            else:
                pro -= 1
        if pro == 0:
            if len(self.zuse) == 0:
                QMessageBox.about(self, '进程调度', '所有进程已经完成!')
                return
            else:
                QMessageBox.about(self, '进程调度', '就绪队列已完成，请唤醒阻塞队列的进程!')
                return
        i = 0
        while self.tableWidget.item(i, 0).text() != self.run[0]:
            i += 1
        newItem = QTableWidgetItem('运行')  # 改变表格中元素的值
        newItem.setBackground(QColor('Lime'))
        self.tableWidget.setItem(i, 4, newItem)

    def baocunwenjian(self):
        for i in range(len(self.baocun)):
            s = ''
            for j in range(len(self.baocun[i])):
                s += str(self.baocun[i][j])
                s += ' '
            s += '\n'
            with open('log.txt', 'a') as f:
                f.write(s)
        QMessageBox.about(self, '保存文件', '文件已保存到当前目录下!')
        return


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

