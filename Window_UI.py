import logging
import os
import sys
import threading
import subprocess
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup, QMessageBox, QVBoxLayout
from PyQt5.QtCore import QSettings, QTextStream, pyqtSlot, pyqtSignal, Qt
from execute_function import *
from main_function import *
from configparser import ConfigParser
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QFont, QGuiApplication
from second_window import *
import requests
import socket

logging.getLogger('airtest').setLevel(logging.ERROR)
settings = QSettings("set.ini", QSettings.IniFormat)
settings.setIniCodec('UTF-8')  # 设置ini文件编码为 UTF-8

close_number = 1
version = '2.2.3'  # 当前版本


def get_ip_address():
    try:
        # 获取本地主机名
        hostname = socket.gethostname()
        # 获取本地IP
        ip_address = socket.gethostbyname(hostname)
        return ip_address  # 返回IP地址
    except socket.error as e:
        print(f"Unable to get IP Address: {e}")


def check_update():
    global version
    # 首次启动时默认选项
    version_url = "http://fukesihu.gnway.cc:80/version.txt"
    response = requests.get(version_url)
    # print(response)
    get_version = response.text.strip()
    # print(get_version)
    last_version = get_version.replace('version = ', '')
    # print(last_version)
    body = '</body>'
    if response.status_code == 200:  # 如果连接到服务器
        if last_version != version:  # 如果版本不一致，返回1
            # print('当前版本:%s' % version)
            #print("有新版本:%s" % last_version)
            # print('5555555555555')
            return 1
        else:  # 否则返回0
            # print('4444444444444')
            return 0
    elif body in get_version:  # 如果没连接到服务器，返回0
        # print('1')
        return 0


# check_update()


def send_address():
    send_number = 4  # 设置发送次数
    while close_number == 1 and send_number > 0:
        try:
            update_url = "http://fukesihu.gnway.cc:80"  # 连接服务器
            requests.post(update_url, data={'key': get_ip_address()})  # 将唯一IP发送给服务器（统计连接数使用）
            wait_time = 600  # 设置发送时间，每10分钟发送一次
            send_number -= 1  # 发送一次后，次数减1
            while wait_time > 0:
                time.sleep(2)
                wait_time -= 2
                # print(wait_time)
                if close_number == 0:
                    break
        except:
            time.sleep(5)


thread1 = threading.Thread(target=send_address)  # save_options()
thread1.start()

# 获取当前文件的绝对路径(本地）
# current_file_path = os.path.abspath(__file__)

# 获取当前文件夹的上一级目录的绝对路径(本地）
# parent_directory_path = os.path.dirname(os.path.dirname(current_file_path))
# 上一级文件夹中要删除的文件名
# file_to_delete = 'jiaoben-1.2.1.exe'

# 构建要删除的文件的绝对路径(本地）
# file_path_to_delete = os.path.join(current_file_path, file_to_delete)

# 删除文件
# os.remove(file_path_to_delete)
'''if os.path.isfile(file_to_delete):
    # 删除文件
    time.sleep(2)
    os.remove(file_to_delete)
    print(f"文件 已被删除。")
else:
    print(f"文件 不存在。")'''

'''class RedirectText():
    def __init__(self, textEdit_out):
        self.textEdit_out = textEdit_out

    def write(self, message):
        #self.text_edit.append(message)
        self.textEdit_out.insertPlainText(message)
        self.textEdit_out.moveCursor(self.textEdit_out.textCursor().End)  # 移动光标到文本末尾'''


class Ui_MainWindow(object):
    textSignal = pyqtSignal(str)

    def setupUi(self, MainWindow):
        super().__init__()
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(960, 540)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())  # 设置窗口大小固定
        MainWindow.setAcceptDrops(True)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/log.png"))
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)  # type: ignore
        MainWindow.setAutoFillBackground(False)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(True)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        #模拟器参数设置区域
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 40, 461, 41))
        #self.frame.setStyleSheet("#frame{border:1px solid rgb(0,255,0)}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        #下拉框
        # noinspection PyAttributeOutsideInit
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 91, 22))
        #self.comboBox.setAutoFillBackground(False)
        #self.comboBox.setStyleSheet("background: transparent;")
        self.comboBox.setStyleSheet("QComboBox {\n"
                                    "    background-color: rgba(0, 0, 0, 0); /* 白色背景，150为透明度 */\n"
                                    "    border: 1px solid rgba(0, 255, 0); /* 边框样式 */\n"
                                    "}\n")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("模拟器地址", 0)
        self.comboBox.addItem("模拟器ip", 1)

        self.comboBox.currentIndexChanged[int].connect(self.updateLineEdit)  #下拉框信号槽

        self.lineEdit = QtWidgets.QLineEdit(self.frame)  # 模拟器地址输入框
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(130, 10, 221, 21))
        self.lineEdit.setMouseTracking(True)
        self.lineEdit.setAcceptDrops(True)
        self.lineEdit.setToolTip("")
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("QLineEdit {\n""    background: transparent;\n""    border: 1px solid rgba(0, 255, 0); /* 边框样式 */\n""}")
        self.lineEdit.setFrame(True)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        #模拟器地址/ip保存按钮
        self.save_simulator = QtWidgets.QPushButton(self.frame)
        self.save_simulator.setEnabled(True)
        self.save_simulator.setGeometry(QtCore.QRect(380, 10, 75, 23))
        self.save_simulator.setMouseTracking(False)
        self.save_simulator.setTabletTracking(False)
        self.save_simulator.setAcceptDrops(False)
        self.save_simulator.setToolTip("")
        self.save_simulator.setAutoFillBackground(False)
        self.save_simulator.setCheckable(False)
        self.save_simulator.setChecked(False)
        self.save_simulator.setAutoRepeat(False)
        self.save_simulator.setAutoExclusive(False)
        self.save_simulator.setAutoDefault(False)
        self.save_simulator.setDefault(False)
        self.save_simulator.setFlat(True)
        self.save_simulator.setStyleSheet("QPushButton {\n""border: 1px solid rgb(0,255,0); /* 边框样式 */\n"
                                          "}"
                                          "QPushButton:hover {\n"
                                          "background-color: rgba(0, 0, 0, 15); /* 编辑状态下的背景透明度 */\n"
                                          "}\n"
                                          "QPushButton:pressed {\n"
                                          "background-color: rgba(0, 0, 0, 80); /* 编辑状态下的背景透明度 */\n"
                                          "}\n")
        self.save_simulator.setObjectName("pushButton")
        self.save_simulator.clicked.connect(self.save_simulator_settings)  #type: ignore
        '''模拟器区域'''
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 90, 461, 41))
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.frame_2.setBaseSize(QtCore.QSize(0, 0))
        self.frame_2.setMouseTracking(False)
        self.frame_2.setTabletTracking(False)
        self.frame_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)  #type: ignore
        self.frame_2.setAcceptDrops(False)
        self.frame_2.setAutoFillBackground(False)
        # self.frame_2.setStyleSheet("#frame_2{border:1px solid rgb(0,255,0)}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(1)
        self.frame_2.setMidLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        #启动模拟器
        self.start_simulator = QtWidgets.QPushButton(self.frame_2)
        self.start_simulator.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.start_simulator.setFlat(True)
        self.start_simulator.setStyleSheet("QPushButton {\n""border: 1px solid rgb(0,255,0); /* 边框样式 */\n"
                                           "}"
                                           "QPushButton:hover {\n"
                                           "background-color: rgba(0, 0, 0, 15); /* 编辑状态下的背景透明度 */\n"
                                           "}\n"
                                           "QPushButton:pressed {\n"
                                           "background-color: rgba(0, 0, 0, 80); /* 编辑状态下的背景透明度 */\n"
                                           "}\n")
        self.start_simulator.setObjectName("start_simulator")
        #连接模拟器
        self.connect_simulator = QtWidgets.QPushButton(self.frame_2)
        self.connect_simulator.setGeometry(QtCore.QRect(130, 10, 75, 23))
        self.connect_simulator.setFlat(True)
        self.connect_simulator.setStyleSheet("QPushButton {\n""border: 1px solid rgb(0,255,0); /* 边框样式 */\n"
                                             "}"
                                             "QPushButton:hover {\n"
                                             "background-color: rgba(0, 0, 0, 15); /* 编辑状态下的背景透明度 */\n"
                                             "}\n"
                                             "QPushButton:pressed {\n"
                                             "background-color: rgba(0, 0, 0, 80); /* 编辑状态下的背景透明度 */\n"
                                             "}\n")
        self.connect_simulator.setObjectName("connect_simulator")
        #启动游戏
        self.start_game = QtWidgets.QPushButton(self.frame_2)
        self.start_game.setGeometry(QtCore.QRect(260, 10, 75, 23))
        self.start_game.setAutoDefault(False)
        self.start_game.setDefault(False)
        self.start_game.setFlat(True)
        self.start_game.setStyleSheet("QPushButton {\n""border: 1px solid rgb(0,255,0); /* 边框样式 */\n"
                                      "}"
                                      "QPushButton:hover {\n"
                                      "background-color: rgba(0, 0, 0, 15); /* 编辑状态下的背景透明度 */\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "background-color: rgba(0, 0, 0, 80); /* 编辑状态下的背景透明度 */\n"
                                      "}\n")
        self.start_game.setObjectName("start_game")
        #一键启动
        self.simulator_start_all = QtWidgets.QPushButton(self.frame_2)
        self.simulator_start_all.setGeometry(QtCore.QRect(380, 10, 75, 23))
        self.simulator_start_all.setAutoDefault(False)
        self.simulator_start_all.setDefault(False)
        self.simulator_start_all.setFlat(True)
        self.simulator_start_all.setStyleSheet("QPushButton {\n""border: 1px solid rgb(0,255,0); /* 边框样式 */\n"
                                               "}"
                                               "QPushButton:hover {\n"
                                               "background-color: rgba(0, 0, 0, 15); /* 编辑状态下的背景透明度 */\n"
                                               "}\n"
                                               "QPushButton:pressed {\n"
                                               "background-color: rgba(0, 0, 0, 80); /* 编辑状态下的背景透明度 */\n"
                                               "}\n")
        self.simulator_start_all.setObjectName("simulator_start_all")
        # 功能区
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 140, 461, 181))
        # self.frame_3.setStyleSheet("#frame_3{border:1px solid rgb(0,255,0)}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.select_text = QtWidgets.QLabel(self.frame_3)
        self.select_text.setGeometry(QtCore.QRect(10, 5, 81, 16))
        self.select_text.setObjectName("select_text")
        self.select_time = QtWidgets.QCheckBox(self.frame_3)  # 固定时间选项
        self.select_time.setGeometry(QtCore.QRect(110, 5, 100, 16))
        self.select_time.setObjectName("select_time")
        self.select_time.setStyleSheet("background-color: transparent")
        self.checkBox_help = QtWidgets.QCheckBox(self.frame_3)  #互助
        self.checkBox_help.setGeometry(QtCore.QRect(20, 30, 71, 16))
        self.checkBox_help.setAutoFillBackground(False)
        '''self.checkBox_help.setStyleSheet("QCheckBox:indicator:checked {background-color: transparent;border:1px solid rgb(0,255,0)}"
        "QCheckBox:indicator {background-color: transparent;border:1px solid rgb(0,0,0)}")'''
        self.checkBox_help.setAutoRepeat(False)
        self.checkBox_help.setAutoExclusive(False)
        self.checkBox_help.setTristate(False)
        self.checkBox_help.setObjectName("checkBox_help")
        self.checkBox_XG = QtWidgets.QCheckBox(self.frame_3)  # 野怪
        self.checkBox_XG.setGeometry(QtCore.QRect(110, 30, 71, 16))
        self.checkBox_XG.setObjectName("checkBox_XG")
        self.checkBox_XG.setStyleSheet("background-color: transparent")
        self.checkBox_WM = QtWidgets.QCheckBox(self.frame_3)  # 冰原巨兽
        self.checkBox_WM.setGeometry(QtCore.QRect(200, 30, 71, 16))
        self.checkBox_WM.setObjectName("checkBox_WM")
        self.checkBox_npc = QtWidgets.QCheckBox(self.frame_3)  # 活动雪怪
        self.checkBox_npc.setGeometry(QtCore.QRect(290, 30, 71, 16))
        self.checkBox_npc.setObjectName("checkBox_npc")
        self.checkBox_Production = QtWidgets.QCheckBox(self.frame_3)  # 训练士兵
        self.checkBox_Production.setGeometry(QtCore.QRect(380, 30, 71, 16))
        self.checkBox_Production.setObjectName("checkBox_Production")
        self.checkBox_adventure = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_adventure.setGeometry(QtCore.QRect(380, 70, 71, 16))
        self.checkBox_adventure.setObjectName("checkBox_adventure")
        self.checkBox_treatment = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_treatment.setGeometry(QtCore.QRect(290, 70, 71, 16))
        self.checkBox_treatment.setMouseTracking(True)
        self.checkBox_treatment.setTabletTracking(False)
        self.checkBox_treatment.setFocusPolicy(QtCore.Qt.StrongFocus)  # type: ignore
        self.checkBox_treatment.setStyleSheet("")
        self.checkBox_treatment.setTristate(False)
        self.checkBox_treatment.setObjectName("checkBox_treatment")
        self.checkBox_build = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_build.setGeometry(QtCore.QRect(20, 70, 71, 16))
        self.checkBox_build.setObjectName("checkBox_build")
        self.checkBox_Collection = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_Collection.setGeometry(QtCore.QRect(110, 70, 71, 16))
        self.checkBox_Collection.setObjectName("checkBox_Collection")
        self.checkBox_bear = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_bear.setGeometry(QtCore.QRect(200, 70, 71, 16))
        self.checkBox_bear.setObjectName("checkBox_bear")
        self.checkBox_donate = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_donate.setGeometry(QtCore.QRect(20, 110, 71, 16))
        self.checkBox_donate.setObjectName("checkBox_donate")
        self.checkBox_recruit = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_recruit.setGeometry(QtCore.QRect(110, 110, 71, 16))
        self.checkBox_recruit.setObjectName("checkBox_collision")
        self.checkBox_collision = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_collision.setGeometry(QtCore.QRect(200, 110, 71, 16))
        self.checkBox_collision.setObjectName("checkBox_collision")
        self.checkBox_mail = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_mail.setGeometry(QtCore.QRect(290, 110, 71, 16))
        self.checkBox_mail.setObjectName("checkBox_mail")
        self.checkBox_Treasure_Chest = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_Treasure_Chest.setGeometry(QtCore.QRect(380, 110, 71, 16))
        self.checkBox_Treasure_Chest.setObjectName("checkBox_Treasure_Chest")
        # 全选
        self.select_all = QtWidgets.QPushButton(self.frame_3)
        self.select_all.setGeometry(QtCore.QRect(90, 150, 75, 23))
        self.select_all.setFlat(True)
        self.select_all.setObjectName("select_all")
        self.select_all.setStyleSheet("QPushButton {\n""border: 1px solid rgb(0,255,0); /* 边框样式 */\n"
                                      "}"
                                      "QPushButton:hover {\n"
                                      "background-color: rgba(0, 0, 0, 15); /* 编辑状态下的背景透明度 */\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "background-color: rgba(0, 0, 0, 80); /* 编辑状态下的背景透明度 */\n"
                                      "}\n")
        #取消全选
        self.select_unall = QtWidgets.QPushButton(self.frame_3)
        self.select_unall.setGeometry(QtCore.QRect(290, 150, 75, 23))
        self.select_unall.setFlat(True)
        self.select_unall.setObjectName("select_unall")
        self.select_unall.setStyleSheet("QPushButton {\n""border: 1px solid rgb(0,255,0); /* 边框样式 */\n"
                                        "}"
                                        "QPushButton:hover {\n"
                                        "background-color: rgba(0, 0, 0, 15); /* 编辑状态下的背景透明度 */\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "background-color: rgba(0, 0, 0, 80); /* 编辑状态下的背景透明度 */\n"
                                        "}\n")
        #停止按钮
        self.select_stop = QtWidgets.QPushButton(self.frame_3)
        self.select_stop.setEnabled(True)
        self.select_stop.setGeometry(QtCore.QRect(190, 150, 75, 23))
        self.select_stop.setFlat(True)
        self.select_stop.setVisible(False)
        self.select_stop.setObjectName("select_stop")
        self.select_stop.setStyleSheet("QPushButton {\n""border: 1px solid rgb(0,255,0); /* 边框样式 */\n"
                                       "}"
                                       "QPushButton:hover {\n"
                                       "background-color: rgba(0, 0, 0, 15); /* 编辑状态下的背景透明度 */\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "background-color: rgba(0, 0, 0, 80); /* 编辑状态下的背景透明度 */\n"
                                       "}\n")
        #多选开始按钮
        self.select_start = QtWidgets.QPushButton(self.frame_3)
        self.select_start.setEnabled(True)
        self.select_start.setGeometry(QtCore.QRect(190, 150, 75, 23))
        self.select_start.setWhatsThis("")
        self.select_start.setAutoFillBackground(False)
        self.select_start.setCheckable(False)
        self.select_start.setChecked(False)
        self.select_start.setFlat(True)
        self.select_start.setObjectName("select_start")
        self.select_start.setStyleSheet("QPushButton {\n""border: 1px solid rgb(0,255,0); /* 边框样式 */\n"
                                        "}"
                                        "QPushButton:hover {\n"
                                        "background-color: rgba(0, 0, 0, 15); /* 编辑状态下的背景透明度 */\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "background-color: rgba(0, 0, 0, 80); /* 编辑状态下的背景透明度 */\n"
                                        "}\n")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setEnabled(False)
        self.listView.setGeometry(QtCore.QRect(-2, -1, 971, 553))
        self.listView.setAutoFillBackground(False)
        self.listView.setStyleSheet("background-image: url(icon/11.png)")
        self.listView.setObjectName("listView")
        # 通用区域
        self.frame_ty = QtWidgets.QFrame(self.centralwidget)
        self.frame_ty.setGeometry(QtCore.QRect(10, 330, 461, 190))
        # self.frame_ty.setStyleSheet("#frame_ty{border:1px solid rgb(0,255,0)}")
        self.frame_ty.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_ty.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ty.setObjectName("frame_ty")
        self.ty_title = QtWidgets.QLabel(self.frame_ty)
        self.ty_title.setGeometry(QtCore.QRect(10, 0, 81, 21))
        self.ty_title.setObjectName("simple_title")
        # 互助文本
        self.label_help = QtWidgets.QLabel(self.frame_ty)
        self.label_help.setGeometry(QtCore.QRect(20, 20, 54, 21))  # 显示等级文本
        self.label_help.setObjectName("联盟互助")
        # 互助随机时间选项
        self.checkBox_Random_time = QtWidgets.QCheckBox(self.frame_ty)
        self.checkBox_Random_time.setGeometry(QtCore.QRect(110, 23, 71, 16))
        self.checkBox_Random_time.setObjectName("随机时间")
        # 训练文本
        self.label_xunlian = QtWidgets.QLabel(self.frame_ty)
        self.label_xunlian.setGeometry(QtCore.QRect(20, 50, 54, 21))  # 显示等级文本
        self.label_xunlian.setObjectName("训练士兵")
        # 训练晋升选项
        self.checkBox_jinshen = QtWidgets.QCheckBox(self.frame_ty)
        self.checkBox_jinshen.setGeometry(QtCore.QRect(110, 53, 71, 16))
        self.checkBox_jinshen.setObjectName("优先晋升")
        # 采集文本
        self.label_caiji = QtWidgets.QLabel(self.frame_ty)
        self.label_caiji.setGeometry(QtCore.QRect(20, 80, 54, 21))  # 显示等级文本
        self.label_caiji.setObjectName("资源采集")
        # 采集英雄选项
        self.checkBox_ty_un = QtWidgets.QCheckBox(self.frame_ty)
        self.checkBox_ty_un.setGeometry(QtCore.QRect(110, 83, 71, 16))
        self.checkBox_ty_un.setObjectName("采集英雄")
        # 采集平均兵力选项
        #self.checkBox_ty_caiji_average = QtWidgets.QCheckBox(self.frame_ty)
        #self.checkBox_ty_caiji_average.setGeometry(QtCore.QRect(200, 53, 71, 16))
        #self.checkBox_ty_caiji_average.setObjectName("平均兵力")
        # 采集等级文本
        self.label_4 = QtWidgets.QLabel(self.frame_ty)
        self.label_4.setGeometry(QtCore.QRect(290, 80, 54, 21))  # 显示等级文本
        self.label_4.setObjectName("label_4")
        #self.label_4.setVisible(False)
        # 采集等级输入
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_ty)
        self.lineEdit_3.setGeometry(QtCore.QRect(350, 80, 31, 21))  # 显示等级输入框
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
                                      "background: transparent;\n"
                                      "border: 1px solid rgba(0, 255, 0)"
                                      "}")
        # 冰原巨兽文本
        self.label_WM = QtWidgets.QLabel(self.frame_ty)
        self.label_WM.setGeometry(QtCore.QRect(20, 110, 54, 21))  # 显示等级文本
        self.label_WM.setObjectName("冰原巨兽文本")
        # 冰原巨兽单兵选项
        self.checkBox_ty_simple = QtWidgets.QCheckBox(self.frame_ty)
        self.checkBox_ty_simple.setGeometry(QtCore.QRect(110, 113, 71, 16))
        self.checkBox_ty_simple.setObjectName("checkBox_ty_simple")
        # 冰原巨兽平均兵力选项
        self.checkBox_ty_WM_average = QtWidgets.QCheckBox(self.frame_ty)
        self.checkBox_ty_WM_average.setGeometry(QtCore.QRect(200, 113, 71, 16))
        self.checkBox_ty_WM_average.setObjectName("平均兵力")
        # 冰原巨兽等级文本
        self.label_WM_lv = QtWidgets.QLabel(self.frame_ty)
        self.label_WM_lv.setGeometry(QtCore.QRect(290, 110, 54, 21))  # 显示等级文本
        self.label_WM_lv.setObjectName("label_WM_lv")
        # 冰原巨兽输入
        self.lineEdit_WM = QtWidgets.QLineEdit(self.frame_ty)
        self.lineEdit_WM.setGeometry(QtCore.QRect(350, 110, 31, 21))  # 显示等级输入框
        self.lineEdit_WM.setObjectName("lineEdit_WM")
        self.lineEdit_WM.setStyleSheet("QLineEdit {\n"
                                       "background: transparent;\n"
                                       "border: 1px solid rgba(0, 255, 0)"
                                       "}")
        # 世界野怪文本
        self.label_XG = QtWidgets.QLabel(self.frame_ty)
        self.label_XG.setGeometry(QtCore.QRect(20, 140, 54, 21))  # 显示等级文本
        self.label_XG.setObjectName("世界野怪文本")
        # 世界野怪平均兵力选项
        self.checkBox_XG_average = QtWidgets.QCheckBox(self.frame_ty)
        self.checkBox_XG_average.setGeometry(QtCore.QRect(110, 140, 71, 16))
        self.checkBox_XG_average.setObjectName("平均兵力")
        # 世界野怪文本
        self.label_XG_lv = QtWidgets.QLabel(self.frame_ty)
        self.label_XG_lv.setGeometry(QtCore.QRect(290, 140, 54, 21))  # 显示等级文本
        self.label_XG_lv.setObjectName("label_XG_lv")
        # 世界野怪输入
        self.lineEdit_XG = QtWidgets.QLineEdit(self.frame_ty)
        self.lineEdit_XG.setGeometry(QtCore.QRect(350, 140, 31, 21))  # 显示等级输入框
        self.lineEdit_XG.setObjectName("lineEdit_XG")
        self.lineEdit_XG.setStyleSheet("QLineEdit {\n"
                                       "background: transparent;\n"
                                       "border: 1px solid rgba(0, 255, 0)"
                                       "}")
        # 通用设置按钮
        self.ty_set = QtWidgets.QPushButton(self.frame_ty)
        self.ty_set.setGeometry(QtCore.QRect(190, 160, 75, 21))
        self.ty_set.setObjectName("ty_set")
        self.ty_set.setFlat(True)
        self.ty_set.setStyleSheet("QPushButton {\n""border: 1px solid rgb(0,255,0); /* 边框样式 */\n"
                                  "}"
                                  "QPushButton:hover {\n"
                                  "background-color: rgba(0, 0, 0, 15); /* 编辑状态下的背景透明度 */\n"
                                  "}\n"
                                  "QPushButton:pressed {\n"
                                  "background-color: rgba(0, 0, 0, 80); /* 编辑状态下的背景透明度 */\n"
                                  "}\n")
        # 单项内容
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(490, 60, 461, 191))
        #self.frame_4.setStyleSheet("#frame_4{border:1px solid rgb(0,255,0)}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.simple_title = QtWidgets.QLabel(self.frame_4)
        self.simple_title.setGeometry(QtCore.QRect(10, 0, 81, 21))
        self.simple_title.setObjectName("simple_title")
        # 单项设置按钮
        self.simple_set = QtWidgets.QPushButton(self.frame_4)
        self.simple_set.setGeometry(QtCore.QRect(350, 0, 75, 21))
        self.simple_set.setObjectName("simple_set")
        self.simple_set.setFlat(True)
        self.simple_set.setStyleSheet("QPushButton {\n""border: 1px solid rgb(0,255,0); /* 边框样式 */\n"
                                      "}"
                                      "QPushButton:hover {\n"
                                      "background-color: rgba(0, 0, 0, 15); /* 编辑状态下的背景透明度 */\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "background-color: rgba(0, 0, 0, 80); /* 编辑状态下的背景透明度 */\n"
                                      "}\n")
        self.radioButton_help = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_help.setGeometry(QtCore.QRect(20, 30, 71, 16))
        self.radioButton_help.setAutoFillBackground(False)
        self.radioButton_help.setStyleSheet("")
        self.radioButton_help.setAutoRepeat(False)
        self.radioButton_help.setAutoExclusive(True)
        self.radioButton_help.setObjectName("radioButton_help")
        self.radioButton_XG = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_XG.setGeometry(QtCore.QRect(110, 30, 71, 16))
        self.radioButton_XG.setObjectName("radioButton_XG")
        self.radioButton_WM = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_WM.setGeometry(QtCore.QRect(200, 30, 71, 16))
        self.radioButton_WM.setObjectName("radioButton_WM")
        self.radioButton_npc = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_npc.setGeometry(QtCore.QRect(290, 30, 71, 16))
        self.radioButton_npc.setObjectName("radioButton_npc")
        self.radioButton_Production = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_Production.setGeometry(QtCore.QRect(380, 30, 71, 16))
        self.radioButton_Production.setObjectName("radioButton_Production")
        self.radioButton_adventure = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_adventure.setGeometry(QtCore.QRect(380, 70, 71, 16))
        self.radioButton_adventure.setObjectName("radioButton_adventure")
        self.radioButton_treatment = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_treatment.setGeometry(QtCore.QRect(290, 70, 71, 16))
        self.radioButton_treatment.setMouseTracking(True)
        self.radioButton_treatment.setTabletTracking(False)
        self.radioButton_treatment.setFocusPolicy(QtCore.Qt.StrongFocus)  #type: ignore
        self.radioButton_treatment.setStyleSheet("")
        self.radioButton_treatment.setObjectName("radioButton_treatment")
        self.radioButton_build = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_build.setGeometry(QtCore.QRect(20, 70, 71, 16))
        self.radioButton_build.setObjectName("radioButton_build")
        self.radioButton_Collection = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_Collection.setGeometry(QtCore.QRect(110, 70, 71, 16))
        self.radioButton_Collection.setObjectName("radioButton_Collection")
        self.radioButton_bear = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_bear.setGeometry(QtCore.QRect(200, 70, 71, 16))
        self.radioButton_bear.setObjectName("radioButton_bear")
        self.radioButton_donate = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_donate.setGeometry(QtCore.QRect(20, 110, 71, 16))
        self.radioButton_donate.setObjectName("radioButton_18")
        self.radioButton_recruit = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_recruit.setGeometry(QtCore.QRect(110, 110, 71, 16))
        self.radioButton_recruit.setObjectName("radioButton_recruit")
        self.radioButton_collision = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_collision.setGeometry(QtCore.QRect(200, 110, 71, 16))
        self.radioButton_collision.setObjectName("radioButton_collision")
        self.radioButton_mail = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_mail.setGeometry(QtCore.QRect(290, 110, 71, 16))
        self.radioButton_mail.setObjectName("radioButton_mail")
        self.radioButton_Treasure_Chest = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_Treasure_Chest.setGeometry(QtCore.QRect(380, 110, 71, 16))
        self.radioButton_Treasure_Chest.setObjectName("radioButton_Treasure_Chest")
        #将单选按钮添加至组
        self.radioButton_group = QButtonGroup(self.frame_4)  #创建按钮组
        self.radioButton_group.addButton(self.radioButton_help, 1)  #将单选项加入到按钮组
        self.radioButton_group.addButton(self.radioButton_XG, 2)
        self.radioButton_group.addButton(self.radioButton_WM, 3)
        self.radioButton_group.addButton(self.radioButton_npc, 4)
        self.radioButton_group.addButton(self.radioButton_Production, 5)
        self.radioButton_group.addButton(self.radioButton_build, 6)
        self.radioButton_group.addButton(self.radioButton_Collection, 7)
        self.radioButton_group.addButton(self.radioButton_bear, 8)
        self.radioButton_group.addButton(self.radioButton_treatment, 9)
        self.radioButton_group.addButton(self.radioButton_adventure, 10)
        self.radioButton_group.addButton(self.radioButton_donate, 11)
        self.radioButton_group.addButton(self.radioButton_recruit, 12)
        self.radioButton_group.addButton(self.radioButton_collision, 13)
        self.radioButton_group.addButton(self.radioButton_mail, 14)
        self.radioButton_group.addButton(self.radioButton_Treasure_Chest, 15)
        self.radioButton_group.buttonClicked.connect(self.read_simple_set)  #type: ignore #监听按钮点击事件
        #单项停止
        self.simple_stop = QtWidgets.QPushButton(self.frame_4)
        #self.simple_stop.setEnabled(True)
        self.simple_stop.setVisible(False)
        self.simple_stop.setGeometry(QtCore.QRect(190, 150, 75, 23))
        #self.simple_stop.setAutoExclusive(False)
        #self.simple_stop.setDefault(False)
        #self.simple_stop.setFlat(True)
        self.simple_stop.setObjectName("simple_stop")
        self.simple_stop.setStyleSheet("QPushButton {\n""border: 1px solid rgb(0,255,0); /* 边框样式 */\n"
                                       "}"
                                       "QPushButton:hover {\n"
                                       "background-color: rgba(0, 0, 0, 15); /* 编辑状态下的背景透明度 */\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "background-color: rgba(0, 0, 0, 80); /* 编辑状态下的背景透明度 */\n"
                                       "}\n")
        #单项开始
        self.simple_start = QtWidgets.QPushButton(self.frame_4)
        #self.simple_start.setEnabled(True)
        self.simple_start.setGeometry(QtCore.QRect(190, 150, 75, 23))
        #self.simple_start.setAutoDefault(False)
        #self.simple_start.setDefault(False)
        #self.simple_start.setFlat(True)
        self.simple_start.setObjectName("simple_start")
        self.simple_start.setStyleSheet("QPushButton {\n""border: 1px solid rgb(0,255,0); /* 边框样式 */\n"
                                        "}"
                                        "QPushButton:hover {\n"
                                        "background-color: rgba(0, 0, 0, 15); /* 编辑状态下的背景透明度 */\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "background-color: rgba(0, 0, 0, 80); /* 编辑状态下的背景透明度 */\n"
                                        "}\n")
        #执行间隔文本
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(110, 0, 81, 21))
        self.label_3.setObjectName("label_3")
        #间隔时间输入
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 1, 51, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
                                      "background: transparent;\n"
                                      "border: 1px solid rgba(0, 255, 0)"
                                      "}")

        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(490, 270, 461, 241))
        #self.frame_5.setStyleSheet("#frame_5{border:1px solid rgb(0,255,0)}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setGeometry(QtCore.QRect(10, 10, 54, 12))
        self.label.setObjectName("label")
        self.textEdit_out = QtWidgets.QTextEdit(self.frame_5)
        self.textEdit_out.setEnabled(True)
        self.textEdit_out.setGeometry(QtCore.QRect(10, 30, 441, 201))
        self.textEdit_out.setMouseTracking(True)
        self.textEdit_out.setTabletTracking(False)
        self.textEdit_out.setAcceptDrops(True)
        self.textEdit_out.setToolTip("")
        self.textEdit_out.setAutoFillBackground(False)
        self.textEdit_out.setStyleSheet("background: transparent;border:1px solid rgb(0,255,0)")
        self.textEdit_out.setReadOnly(True)

        #self.textEdit_out.ensureCursorVisible()
        #self.textEdit_out.setOverwriteMode(False)
        #self.textEdit_out.ensureCursorVisible()
        self.textEdit_out.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(890, 520, 71, 20))
        self.label_2.setObjectName("label_2")
        self.label_Version_prompt = QtWidgets.QLabel(self.centralwidget)  # 版本提示
        self.label_Version_prompt.setGeometry(QtCore.QRect(700, 520, 300, 20))
        return_value = check_update()
        if return_value == 1:
            self.label_Version_prompt.setVisible(True)
        elif return_value == 0:
            self.label_Version_prompt.setVisible(False)
        self.label_Version_prompt.setObjectName("label_Version_prompt")
        self.show_UI = QtWidgets.QPushButton(self.centralwidget)
        self.show_UI.setGeometry(QtCore.QRect(190, 520, 51, 23))
        self.show_UI.setFlat(True)
        self.show_UI.setObjectName("show_UI")
        self.notice_button = QtWidgets.QPushButton(self.centralwidget)
        self.notice_button.setGeometry(QtCore.QRect(60, 520, 61, 23))
        self.notice_button.setFlat(True)
        self.notice_button.setObjectName("notice_button")
        self.help_button = QtWidgets.QPushButton(self.centralwidget)
        self.help_button.setGeometry(QtCore.QRect(130, 520, 70, 23))
        self.help_button.setFlat(True)
        self.help_button.setObjectName("help_button")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(370, 5, 231, 50))
        self.textEdit.setLayoutDirection(QtCore.Qt.RightToLeft)  #type: ignore
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setStyleSheet("QTextEdit {\n"
                                    "    background: transparent;\n"
                                    "    color: rgb(0, 0, 0);\n"
                                    "}")
        self.textEdit.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit.setTabChangesFocus(False)
        self.textEdit.setUndoRedoEnabled(False)
        self.textEdit.setOverwriteMode(False)
        self.textEdit.setAcceptRichText(False)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        self.hide_UI = QtWidgets.QPushButton(self.centralwidget)
        self.hide_UI.setGeometry(QtCore.QRect(5, 520, 51, 23))
        self.hide_UI.setFlat(True)
        self.hide_UI.setObjectName("hide_UI")
        self.listView.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.frame_ty.raise_()
        self.checkBox_ty_simple.raise_()
        self.checkBox_ty_WM_average.raise_()
        self.checkBox_ty_un.raise_()
        #self.checkBox_ty_caiji_average.raise_()
        self.label_xunlian.raise_()
        self.checkBox_jinshen.raise_()
        self.frame_4.raise_()
        self.frame_5.raise_()
        self.label_2.raise_()
        self.show_UI.raise_()
        self.show_UI.setVisible(False)
        self.show_UI.setGeometry(QtCore.QRect(5, 520, 51, 23))
        self.notice_button.raise_()
        self.help_button.raise_()
        self.textEdit.raise_()
        self.hide_UI.raise_()
        self.label_Version_prompt.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        #按钮点击触发响应
        self.retranslateUi(MainWindow)
        # 多选开始
        self.select_start.clicked.connect(self.select_start_button)  # type: ignore
        self.select_stop.clicked.connect(stop_function)  #type: ignore# 多选停止
        self.ty_set.clicked.connect(self.save_ty_setting)  # type: ignore#通用设置
        self.simple_set.clicked.connect(self.save_simple_set)  # type: ignore#单选设置
        self.simple_start.clicked.connect(self.simple_start_button)  #type: ignore# 单选开始
        self.simple_stop.clicked.connect(stop_function)  #type: ignore# 单选停止
        self.hide_UI.clicked.connect(self.hide_ui)  # type: ignore
        self.show_UI.clicked.connect(self.show_ui)  # type: ignore
        self.start_simulator.clicked.connect(lambda: start_simple(1))  #type: ignore
        self.connect_simulator.clicked.connect(lambda: start_simple(2))  #type: ignore
        self.start_game.clicked.connect(lambda: start_simple(3))  #type: ignore
        self.simulator_start_all.clicked.connect(lambda: start_simple(4))  #type: ignore
        self.select_all.clicked.connect(self.toggle_checkbox)  #type: ignore
        self.select_unall.clicked.connect(self.untoggle_checkbox)  #type: ignore
        self.notice_button.clicked.connect(self.open_noticeable)  #type: ignore
        self.notice = noticelog()
        self.help_button.clicked.connect(self.open_helpline)  #type: ignore
        self.help = helplog()
        #sys.stdout = RedirectText(self.textEdit_out)
        # 捕获标准输出和错误
        sys.stdout = self

        def insert_text(text):
            self.textEdit_out.insertPlainText(text)  # 将打印的内容插入到textEdit中
            self.textEdit_out.ensureCursorVisible()  # 将光标移动到可见区域（底部）

        # 连接textSignal到insert_text方法
        self.textSignal.connect(insert_text)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def set_font(self):  #设置界面文本大小，保证不同分辨率情况下显示正常
        font = QFont("Arial", 7)
        #font.setPointSize(10)
        self.save_simulator.setFont(font)
        self.start_simulator.setFont(font)
        self.connect_simulator.setFont(font)
        self.start_game.setFont(font)
        self.simulator_start_all.setFont(font)
        self.select_text.setFont(font)
        self.select_time.setFont(font)
        self.checkBox_help.setFont(font)
        self.checkBox_XG.setFont(font)
        self.checkBox_WM.setFont(font)
        self.checkBox_npc.setFont(font)
        self.checkBox_Production.setFont(font)
        self.checkBox_adventure.setFont(font)
        self.checkBox_treatment.setFont(font)
        self.checkBox_build.setFont(font)
        self.checkBox_Collection.setFont(font)
        self.checkBox_bear.setFont(font)
        self.checkBox_donate.setFont(font)
        self.checkBox_recruit.setFont(font)
        self.checkBox_collision.setFont(font)
        self.checkBox_mail.setFont(font)
        self.checkBox_Treasure_Chest.setFont(font)
        self.select_all.setFont(font)
        self.select_unall.setFont(font)
        self.select_stop.setFont(font)
        self.select_start.setFont(font)
        self.radioButton_help.setFont(font)
        self.radioButton_XG.setFont(font)
        self.radioButton_WM.setFont(font)
        self.radioButton_npc.setFont(font)
        self.radioButton_Production.setFont(font)
        self.radioButton_adventure.setFont(font)
        self.radioButton_treatment.setFont(font)
        self.radioButton_build.setFont(font)
        self.radioButton_Collection.setFont(font)
        self.radioButton_bear.setFont(font)
        self.radioButton_donate.setFont(font)
        self.radioButton_recruit.setFont(font)
        self.radioButton_collision.setFont(font)
        self.radioButton_mail.setFont(font)
        self.radioButton_Treasure_Chest.setFont(font)
        self.simple_stop.setFont(font)
        self.simple_start.setFont(font)
        self.label_3.setFont(font)
        self.label_4.setFont(font)
        self.label_caiji.setFont(font)
        self.label_WM.setFont(font)
        self.ty_set.setFont(font)
        self.label_help.setFont(font)
        self.checkBox_Random_time.setFont(font)
        self.label_xunlian.setFont(font)
        self.checkBox_jinshen.setFont(font)
        self.checkBox_ty_simple.setFont(font)
        self.checkBox_ty_WM_average.setFont(font)
        self.checkBox_ty_un.setFont(font)
        self.label_XG.setFont(font)
        self.checkBox_XG_average.setFont(font)
        self.label_XG_lv.setFont(font)
        self.lineEdit_XG.setFont(font)
        #self.checkBox_ty_caiji_average.setFont(font)
        self.simple_set.setFont(font)
        self.label.setFont(font)
        self.label_Version_prompt.setFont(font)
        self.label_2.setFont(font)
        self.show_UI.setFont(font)
        self.notice_button.setFont(font)
        self.help_button.setFont(font)
        self.textEdit.setFont(font)
        self.hide_UI.setFont(font)

    def retranslateUi(self, MainWindow):  #将按钮文本等显示到窗口
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "无尽冬日"))
        self.save_simulator.setText(_translate("MainWindow", "保存"))
        self.start_simulator.setText(_translate("MainWindow", "启动模拟器"))
        self.connect_simulator.setText(_translate("MainWindow", "连接模拟器"))
        self.start_game.setText(_translate("MainWindow", "启动游戏"))
        self.simulator_start_all.setText(_translate("MainWindow", "一键启动"))
        self.select_text.setText(_translate("MainWindow", "复选项（多选）"))
        self.select_time.setText(_translate("MainWindow", "是否固定时间"))
        self.checkBox_help.setText(_translate("MainWindow", "联盟互助"))
        self.checkBox_XG.setText(_translate("MainWindow", "世界野怪"))
        self.checkBox_WM.setText(_translate("MainWindow", "冰原巨兽"))
        self.checkBox_npc.setText(_translate("MainWindow", "活动雪怪"))
        self.checkBox_Production.setText(_translate("MainWindow", "训练士兵"))
        self.checkBox_adventure.setText(_translate("MainWindow", "探险奖励"))
        self.checkBox_treatment.setText(_translate("MainWindow", "治疗士兵"))
        self.checkBox_build.setText(_translate("MainWindow", "建筑升级"))
        self.checkBox_Collection.setText(_translate("MainWindow", "采集资源"))
        self.checkBox_bear.setText(_translate("MainWindow", "巨熊活动"))
        self.checkBox_donate.setText(_translate("MainWindow", "联盟捐赠"))
        self.checkBox_recruit.setText(_translate("MainWindow", "英雄招募"))
        self.checkBox_collision.setText(_translate("MainWindow", "攻击检测"))
        self.checkBox_mail.setText(_translate("MainWindow", "邮件领取"))
        self.checkBox_Treasure_Chest.setText(_translate("MainWindow", "联盟宝箱"))
        self.select_all.setText(_translate("MainWindow", "全选"))
        self.select_unall.setText(_translate("MainWindow", "取消全选"))
        self.select_stop.setText(_translate("MainWindow", "停止"))
        self.select_start.setText(_translate("MainWindow", "开始"))
        self.simple_title.setText(_translate("MainWindow", "单选项（单选）"))
        self.radioButton_help.setText(_translate("MainWindow", "联盟互助"))
        self.radioButton_XG.setText(_translate("MainWindow", "世界野怪"))
        self.radioButton_WM.setText(_translate("MainWindow", "冰原巨兽"))
        self.radioButton_npc.setText(_translate("MainWindow", "活动雪怪"))
        self.radioButton_Production.setText(_translate("MainWindow", "训练士兵"))
        self.radioButton_adventure.setText(_translate("MainWindow", "探险奖励"))
        self.radioButton_treatment.setText(_translate("MainWindow", "治疗士兵"))
        self.radioButton_build.setText(_translate("MainWindow", "建筑升级"))
        self.radioButton_Collection.setText(_translate("MainWindow", "采集资源"))
        self.radioButton_bear.setText(_translate("MainWindow", "巨熊活动"))
        self.radioButton_donate.setText(_translate("MainWindow", "联盟捐赠"))
        self.radioButton_recruit.setText(_translate("MainWindow", "英雄招募"))
        self.radioButton_collision.setText(_translate("MainWindow", "攻击检测"))
        self.radioButton_mail.setText(_translate("MainWindow", "邮件领取"))
        self.radioButton_Treasure_Chest.setText(_translate("MainWindow", "联盟宝箱"))
        self.simple_stop.setText(_translate("MainWindow", "停止"))
        self.simple_start.setText(_translate("MainWindow", "开始"))
        self.label_3.setText(_translate("MainWindow", "执行间隔(秒):"))
        self.ty_title.setText(_translate("MainWindow", "通用"))
        self.label_help.setText(_translate("MainWindow", "联盟互助："))
        self.checkBox_Random_time.setText(_translate("MainWindow", "随机时间"))
        self.label_xunlian.setText(_translate("MainWindow", "训练士兵:"))
        self.checkBox_jinshen.setText(_translate("MainWindow", "优先晋升"))
        self.label_caiji.setText(_translate("MainWindow", "资源采集:"))
        self.checkBox_ty_un.setText(_translate("MainWindow", "采集英雄"))
        #self.checkBox_ty_caiji_average.setText(_translate("MainWindow", "平均兵力"))
        self.label_4.setText(_translate("MainWindow", "等级设置:"))
        self.label_WM.setText(_translate("MainWindow", "冰原巨兽:"))
        self.checkBox_ty_simple.setText(_translate("MainWindow", "单兵集结"))
        self.checkBox_ty_WM_average.setText(_translate("MainWindow", "平均兵力"))
        self.label_WM_lv.setText(_translate("MainWindow", "等级设置:"))
        self.label_XG.setText(_translate("MainWindow", "世界野怪:"))
        self.checkBox_XG_average.setText(_translate("MainWindow", "平均兵力"))
        self.label_XG_lv.setText(_translate("MainWindow", "等级设置:"))
        self.ty_set.setText(_translate("MainWindow", "设置"))
        self.simple_set.setText(_translate("MainWindow", "设置"))
        self.label.setText(_translate("MainWindow", "输出："))
        self.label_Version_prompt.setText(_translate("MainWindow", "<font color=\"#FF0000\" ><p>有新版本，请于群内下载新版本</p></font>"))
        self.label_2.setText(_translate("MainWindow", "版本:" + version))
        self.show_UI.setText(_translate("MainWindow", "显示UI"))
        self.notice_button.setText(_translate("MainWindow", "版本日志"))
        self.help_button.setText(_translate("MainWindow", "帮助文档"))
        self.textEdit.setText(_translate("MainWindow", "<font color=\"#FF0000\" size=4><p align=\"center\"  style=\" margin-top:0px; "
                                                       "margin-bottom:5px; \">请等待程序停止后再设置相关参数</p>"
                                                       "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px\" >多选和单选不可同时执行</p></font>"))
        self.hide_UI.setText(_translate("MainWindow", "隐藏UI"))

    @pyqtSlot()
    def load_settings(self):  # 读取设置
        simulator_settings = settings.value('下拉框', 1, type=int)
        option_time = settings.value('固定时间', 1, type=bool)
        option1 = settings.value('联盟互助', 1, type=bool)
        option2 = settings.value('世界野怪', 1, type=bool)
        option3 = settings.value('冰原巨兽', 1, type=bool)
        option4 = settings.value('活动雪怪', 1, type=bool)
        option5 = settings.value('训练士兵', 1, type=bool)
        option6 = settings.value('建筑升级', 1, type=bool)
        option7 = settings.value('采集资源', 1, type=bool)
        option8 = settings.value('巨熊活动', 1, type=bool)
        option9 = settings.value('治疗士兵', 1, type=bool)
        option10 = settings.value('探险奖励', 1, type=bool)
        option11 = settings.value('联盟捐赠', 1, type=bool)
        option12 = settings.value('英雄招募', 1, type=bool)
        option13 = settings.value('攻击检测', 1, type=bool)
        option14 = settings.value('邮件领取', 1, type=bool)
        option15 = settings.value('联盟宝箱', 1, type=bool)
        option = settings.value('单选选择', 1, type=int)
        self.comboBox.setCurrentIndex(simulator_settings)
        self.radioButton_group.button(option).setChecked(True)
        self.select_time.setChecked(option_time)
        self.checkBox_help.setChecked(option1)
        self.checkBox_XG.setChecked(option2)
        self.checkBox_WM.setChecked(option3)
        self.checkBox_npc.setChecked(option4)
        self.checkBox_Production.setChecked(option5)
        self.checkBox_build.setChecked(option6)
        self.checkBox_Collection.setChecked(option7)
        self.checkBox_bear.setChecked(option8)
        self.checkBox_treatment.setChecked(option9)
        self.checkBox_adventure.setChecked(option10)
        self.checkBox_donate.setChecked(option11)
        self.checkBox_recruit.setChecked(option12)
        self.checkBox_collision.setChecked(option13)
        self.checkBox_mail.setChecked(option14)
        self.checkBox_Treasure_Chest.setChecked(option15)

    def read_ty_setting(self):  # 读取通用设置
        global number_brush, number_iron, number_wood, number_meat, number_coal
        option_Random_time = settings.value('随机时间', 1, type=bool)
        option_jinshen = settings.value('优先晋升', 1, type=bool)
        option_WM = settings.value('冰原巨兽等级设置', 5, type=str)
        option_lv = settings.value('采集资源等级设置', 7, type=str)
        option_XG_lv = settings.value('世界野怪等级设置', 10, type=str)
        option_ty_un = settings.value('采集英雄', 1, type=bool)
        option_ty_sim = settings.value('单兵集结', 1, type=bool)
        option_ty_WM_average = settings.value('冰原巨兽平均兵力', 0, type=bool)
        option_ty_XG_average = settings.value('世界野怪平均兵力', 0, type=bool)
        settings.setValue('冰原巨兽等级设置更新', 1)
        settings.setValue('肉采集等级设置更新', 1)
        settings.setValue('木头采集等级设置更新', 1)
        settings.setValue('煤矿采集等级设置更新', 1)
        settings.setValue('铁矿采集等级设置更新', 1)
        settings.setValue('世界野怪等级设置更新', 1)
        self.checkBox_Random_time.setChecked(option_Random_time)
        self.checkBox_jinshen.setChecked(option_jinshen)
        self.lineEdit_3.setText(option_lv)
        self.lineEdit_WM.setText(option_WM)
        self.lineEdit_XG.setText(option_XG_lv)
        self.checkBox_ty_un.setChecked(option_ty_un)
        self.checkBox_ty_simple.setChecked(option_ty_sim)
        self.checkBox_ty_WM_average.setChecked(option_ty_WM_average)
        self.checkBox_XG_average.setChecked(option_ty_XG_average)

    def save_ty_setting(self):  # 保存通用设置
        option_WM = self.lineEdit_WM.text()
        option_lv = self.lineEdit_3.text()
        option_XG_lv = self.lineEdit_XG.text()
        settings.setValue('随机时间', self.checkBox_Random_time.isChecked())
        settings.setValue('优先晋升', self.checkBox_jinshen.isChecked())
        settings.setValue('冰原巨兽等级设置', option_WM)
        settings.setValue('采集资源等级设置', option_lv)
        settings.setValue('世界野怪等级设置', option_XG_lv)
        settings.setValue('采集英雄', self.checkBox_ty_un.isChecked())
        settings.setValue('单兵集结', self.checkBox_ty_simple.isChecked())
        settings.setValue('冰原巨兽平均兵力', self.checkBox_ty_WM_average.isChecked())
        settings.setValue('世界野怪平均兵力', self.checkBox_XG_average.isChecked())
        print_space('通用设置成功！！！')
        self.read_ty_setting()

    @pyqtSlot()
    def save_simulator_settings(self):  # 保存模拟器设置
        value = self.lineEdit.text()
        index = self.comboBox.currentIndex()
        settings.setValue('下拉框', index)
        if index == 0:
            settings.setValue('模拟器地址', value)
            print('模拟器安装地址：%s' % value)
        elif index == 1:
            settings.setValue('模拟器ip', value)
            print('模拟器ip地址：%s' % value)

    @pyqtSlot()
    def updateLineEdit(self):  # 读取保存的模拟器设置
        # 获取下拉框当前选中的值
        currentText = self.comboBox.currentIndex()
        if currentText == 0:
            itemData_1 = settings.value('模拟器地址', 'E:\leidian\LDPlayer9\dnplayer.exe', type=str)
            self.lineEdit.setText(itemData_1)
        elif currentText == 1:
            itemData_2 = settings.value('模拟器ip', '127.0.0.1:5037', type=str)
            self.lineEdit.setText(itemData_2)  # 获取当前选中项的数据  itemData = self.comboBox.itemData(index)   在输入框中显示内容  self.lineEdit.setText(itemData)

    @pyqtSlot()
    def read_simple_set(self):  # 读取单项设置
        settings.setValue('单选选择', self.radioButton_group.checkedId())
        simple_index = self.radioButton_group.checkedId()
        if simple_index == 1:
            option = settings.value('联盟互助设置', 20, type=str)
            self.lineEdit_2.setText(option)
        elif simple_index == 2:
            option = settings.value('世界野怪设置', 20, type=str)
            self.lineEdit_2.setText(option)
        elif simple_index == 3:
            option = settings.value('冰原巨兽设置', 20, type=str)
            self.lineEdit_2.setText(option)
        elif simple_index == 4:
            option = settings.value('活动雪怪设置', 20, type=str)
            self.lineEdit_2.setText(option)
        elif simple_index == 5:
            option = settings.value('训练士兵设置', 20, type=str)
            self.lineEdit_2.setText(option)
        elif simple_index == 6:
            option = settings.value('建筑升级设置', 20, type=str)
            self.lineEdit_2.setText(option)
        elif simple_index == 7:
            option = settings.value('采集资源设置', 20, type=str)
            self.lineEdit_2.setText(option)
        elif simple_index == 8:
            option = settings.value('巨熊活动设置', 20, type=str)
            self.lineEdit_2.setText(option)
        elif simple_index == 9:
            option = settings.value('治疗士兵设置', 20, type=str)
            self.lineEdit_2.setText(option)
        elif simple_index == 10:
            option = settings.value('探险奖励设置', 20, type=str)
            self.lineEdit_2.setText(option)
        elif simple_index == 11:
            option = settings.value('联盟捐赠设置', 20, type=str)
            self.lineEdit_2.setText(option)
        elif simple_index == 12:
            option = settings.value('英雄招募设置', 20, type=str)
            self.lineEdit_2.setText(option)
        elif simple_index == 13:
            option = settings.value('攻击检测设置', 20, type=str)
            self.lineEdit_2.setText(option)
        elif simple_index == 14:
            option = settings.value('邮件领取设置', 20, type=str)
            self.lineEdit_2.setText(option)
        elif simple_index == 15:
            option = settings.value('联盟宝箱设置', 20, type=str)
            self.lineEdit_2.setText(option)

    @pyqtSlot()
    def save_simple_set(self):  # 保存单项时间设置
        global number_brush, number_iron, number_wood, number_meat, number_coal
        simple_set_time_value = self.lineEdit_2.text()
        simple_index = self.radioButton_group.checkedId()
        if simple_index == 1:
            settings.setValue('联盟互助设置', simple_set_time_value)
            print('间隔时间设置成功！！！')
        elif simple_index == 2:
            settings.setValue('世界野怪设置', simple_set_time_value)
            print('间隔时间设置成功！！！')
        elif simple_index == 3:
            # brush_lv_set_value = self.lineEdit_3.text()
            settings.setValue('冰原巨兽设置', simple_set_time_value)
            # settings.setValue('冰原巨兽等级设置', brush_lv_set_value)
            # number_brush = 0  # 重置该功能运行次数，下次运行走输入等级流程
            print('间隔时间设置成功！！！')
        elif simple_index == 4:
            settings.setValue('活动雪怪设置', simple_set_time_value)
            print('间隔时间设置成功！！！')
        elif simple_index == 5:
            settings.setValue('训练士兵设置', simple_set_time_value)
            print('间隔时间设置成功！！！')
        elif simple_index == 6:
            settings.setValue('建筑升级设置', simple_set_time_value)
            print('间隔时间设置成功！！！')
        elif simple_index == 7:
            # collection_lv_set_value = self.lineEdit_3.text()
            settings.setValue('采集资源设置', simple_set_time_value)
            # settings.setValue('采集资源等级设置', collection_lv_set_value)
            # number_meat = 0  # 重置该功能运行次数，下次运行走输入等级流程
            # number_wood = 0
            # number_coal = 0
            # number_iron = 0
            print('间隔时间设置成功！！！')
        elif simple_index == 8:
            settings.setValue('巨熊活动设置', simple_set_time_value)
            print('间隔时间设置成功！！！')
        elif simple_index == 9:
            settings.setValue('治疗士兵设置', simple_set_time_value)
            print('间隔时间设置成功！！！')
        elif simple_index == 10:
            settings.setValue('探险奖励设置', simple_set_time_value)
            print('间隔时间设置成功！！！')
        elif simple_index == 11:
            settings.setValue('联盟捐赠设置', simple_set_time_value)
            print('间隔时间设置成功！！！')
        elif simple_index == 12:
            settings.setValue('英雄招募设置', simple_set_time_value)
            print('间隔时间设置成功！！！')
        elif simple_index == 13:
            settings.setValue('攻击检测设置', simple_set_time_value)
            print('间隔时间设置成功！！！')
        elif simple_index == 14:
            settings.setValue('邮件领取设置', simple_set_time_value)
            print('间隔时间设置成功！！！')
        elif simple_index == 15:
            settings.setValue('联盟宝箱设置', simple_set_time_value)
            print('间隔时间设置成功！！！')
        # settings.setValue('单选选择', self.radioButton_group.checkedId())
        self.read_simple_set()

    @pyqtSlot()
    def save_settings(self):  # 保存多项设置
        # settings.setValue('下拉框', self.comboBox.index())
        settings.setValue('固定时间', self.select_time.isChecked())
        settings.setValue('联盟互助', self.checkBox_help.isChecked())
        settings.setValue('世界野怪', self.checkBox_XG.isChecked())
        settings.setValue('冰原巨兽', self.checkBox_WM.isChecked())
        settings.setValue('活动雪怪', self.checkBox_npc.isChecked())
        settings.setValue('训练士兵', self.checkBox_Production.isChecked())
        settings.setValue('建筑升级', self.checkBox_build.isChecked())
        settings.setValue('采集资源', self.checkBox_Collection.isChecked())
        settings.setValue('巨熊活动', self.checkBox_bear.isChecked())
        settings.setValue('治疗士兵', self.checkBox_treatment.isChecked())
        settings.setValue('探险奖励', self.checkBox_adventure.isChecked())
        settings.setValue('联盟捐赠', self.checkBox_donate.isChecked())
        settings.setValue('英雄招募', self.checkBox_recruit.isChecked())
        settings.setValue('攻击检测', self.checkBox_collision.isChecked())
        settings.setValue('邮件领取', self.checkBox_mail.isChecked())
        settings.setValue('联盟宝箱', self.checkBox_Treasure_Chest.isChecked())

    @pyqtSlot()
    def select_start_button(self):  # 多选开始按钮
        self.save_settings()
        self.select_stop.show()  # type: ignore
        self.select_start.hide()  # type: ignore
        print("程序开始执行...")
        # 这里放置程序开始时需要执行的代码
        stop_event.clear()
        threading.Thread(target=lambda: subject(self)).start()  # save_options()

    @pyqtSlot()
    def select_stop_button(self):  # 多选停止程序
        self.select_start.show()
        self.select_stop.hide()

    @pyqtSlot()
    def simple_start_button(self):  # 单选开始按钮
        settings.setValue('单选选择', self.radioButton_group.checkedId())
        self.simple_stop.show()  # type: ignore
        self.simple_start.hide()  # type: ignore
        print("程序开始执行...")
        stop_event.clear()
        threading.Thread(target=lambda: simple_select(self)).start()

    @pyqtSlot()
    def simple_stop_button(self):  # 单选停止程序
        self.simple_start.show()
        self.simple_stop.hide()

    @pyqtSlot()
    def open_noticeable(self):
        self.notice.show()

    @pyqtSlot()
    def open_helpline(self):
        self.help.show()

    @pyqtSlot()
    def hide_ui(self):  # 隐藏界面
        self.frame_ty.setVisible(False)
        self.frame.setVisible(False)
        self.frame_2.setVisible(False)
        self.frame_3.setVisible(False)
        self.frame_4.setVisible(False)
        self.frame_5.setVisible(False)
        self.hide_UI.setVisible(False)
        self.show_UI.setVisible(True)
        self.textEdit.setVisible(False)

    @pyqtSlot()
    def show_ui(self):  # 显示界面
        self.frame_ty.setVisible(True)
        self.frame.setVisible(True)
        self.frame_2.setVisible(True)
        self.frame_3.setVisible(True)
        self.frame_4.setVisible(True)
        self.frame_5.setVisible(True)
        self.hide_UI.setVisible(True)
        self.show_UI.setVisible(False)
        self.textEdit.setVisible(True)

    @pyqtSlot()  # 全选
    def toggle_checkbox(self):
        self.checkBox_help.setChecked(True)
        self.checkBox_XG.setChecked(True)
        self.checkBox_WM.setChecked(True)
        self.checkBox_npc.setChecked(True)
        self.checkBox_Production.setChecked(True)
        self.checkBox_build.setChecked(True)
        self.checkBox_Collection.setChecked(True)
        self.checkBox_bear.setChecked(True)
        self.checkBox_treatment.setChecked(True)
        self.checkBox_adventure.setChecked(True)
        self.checkBox_donate.setChecked(True)
        self.checkBox_recruit.setChecked(True)
        self.checkBox_collision.setChecked(True)
        self.checkBox_mail.setChecked(True)
        self.checkBox_Treasure_Chest.setChecked(True)
        self.save_settings()

    @pyqtSlot()  # 取消全选
    def untoggle_checkbox(self):
        self.checkBox_help.setChecked(False)
        self.checkBox_XG.setChecked(False)
        self.checkBox_WM.setChecked(False)
        self.checkBox_npc.setChecked(False)
        self.checkBox_Production.setChecked(False)
        self.checkBox_build.setChecked(False)
        self.checkBox_Collection.setChecked(False)
        self.checkBox_bear.setChecked(False)
        self.checkBox_treatment.setChecked(False)
        self.checkBox_adventure.setChecked(False)
        self.checkBox_donate.setChecked(False)
        self.checkBox_recruit.setChecked(False)
        self.checkBox_collision.setChecked(False)
        self.checkBox_mail.setChecked(False)
        self.checkBox_Treasure_Chest.setChecked(False)
        self.save_settings()

    #@pyqtSlot()
    def write(self, text):
        # 将text写入textEdit
        #self.textEdit_out.insertPlainText(text)
        self.textSignal.emit(text)  #type: ignore#self.textEdit_out.moveCursor(self.textEdit_out.textCursor().End)  # 移动光标到文本末尾  # 当写入时触发信号

    def closeEvent(self, event):
        # 当窗口关闭时调用
        global close_number
        close_number = 0  # 通知发送信息函数程序已停止，终止发送连接请求
        event.accept()


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)
        self.setupUi(self)
        self.load_settings()  # 读取所有设置
        self.read_simple_set()  # 读取单项设置
        self.read_ty_setting()  # 读取通用设置  #self.updateLineEdit()  # 读取模拟器设置  # 重定向print函数到text_edit  #sys.stdout = RedirectText(self.textEdit_out)  #sys.stderr = RedirectText(self.textEdit_out)


if __name__ == '__main__':

    # 解决不同电脑不同缩放比例问题
    QGuiApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)  #type: ignore
    app = QApplication(sys.argv)
    mainWindow = MyApp()
    # 重定向stdout和stderr
    #sys.stdout = mainWindow
    #sys.stderr = mainWindow
    mainWindow.show()
    sys.exit(app.exec_())
