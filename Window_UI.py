# -*- coding: utf-8 -*-
import logging
import os
import sys
import threading
import subprocess
import time
import socket
import requests
from configparser import ConfigParser
import ctypes
# 新版本检查及人数统计
import requests
from requests.exceptions import RequestException
from datetime import datetime

# 合并PyQt5相关的导入语句
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSettings, pyqtSlot, pyqtSignal, Qt, QRect, QLocale, QMetaObject, QCoreApplication
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QFont, QGuiApplication, QPainter, QPainterPath, QPen, QIcon, QTextCursor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QButtonGroup, QMessageBox, QVBoxLayout, QWidget, QPushButton, QFrame, QComboBox,
    QLineEdit, QLabel, QCheckBox, QListView, QTextEdit, QSystemTrayIcon, QMenu, QAction
)

from execute_function import *
from main_function import *
from second_window import *

logging.getLogger('airtest').setLevel(logging.ERROR)
close_number = 1
local_version = "2.3.8"  # 当前版本
network_address = "http://fukesihu.gnway.cc:80"  # 服务器地址1
network_address1 = "https://fukesihu.iepose.cn"  # 服务器地址2


# 旧版本的 PyQt5 中使用 QSettings.IniFormat 来指定配置文件格式，而在新版本中可以直接省略该参数
# settings = QSettings("set.ini", QSettings.IniFormat)   # 该代码可以让配置生成一个可见的配置文件,多开需要不同的配置
# QTextCodec.codecForName("UTF-8")   # 设置ini文件编码为中文

# 转换配置文件为中文
class ConfigSettings:
    def __init__(self, filename, section="配置", encoding="utf-8"):
        self.filename = filename
        self.section = section
        self.encoding = encoding
        self.config = ConfigParser()

        if os.path.exists(filename):
            self.config.read(filename, encoding=encoding)
        else:
            self.config.add_section(section)

    def setValue(self, key, value):
        self.config.read(self.filename, encoding=self.encoding)
        if not self.config.has_section(self.section):
            self.config.add_section(self.section)

        self.config.set(self.section, key, str(value))
        with open(self.filename, "w", encoding=self.encoding) as f:
            self.config.write(f)

    def value(self, key, default=None, type=None):
        """获取值，并支持指定类型转换"""
        self.config.read(self.filename, encoding=self.encoding)
        if not self.config.has_option(self.section, key):
            if type:
                return type(self.convert_string_to_type(default))
            return default

        raw = self.convert_string_to_type(self.config.get(self.section, key))
        try:
            # 尝试将字符串转换为浮动数
            if type:
                return type(raw)
            return raw
        except ValueError:
            pass

    def convert_string_to_type(self, newValue):
        """
        将字符串转换为对应的实际类型，如 int, float, bool
        """
        value = str(newValue)
        if value.isdigit():  # 如果字符串只包含数字
            return int(value)
        try:
            # 尝试将字符串转换为浮动数
            return float(value)
        except ValueError:
            pass

        if value.lower() in ['true', 'false']:  # 如果是布尔值
            return value.lower() == 'true'
        return value

    def _to_bool(self, val: str):
        val = str(val).strip().lower()
        if val in ("true", "yes", "1"):
            return True
        elif val in ("false", "no", "0"):
            return False
        raise ValueError("Not a boolean value")

    def setSection(self, section):
        """切换 section（组）"""
        self.config.read(self.filename, encoding=self.encoding)
        self.section = section
        if not self.config.has_section(section):
            self.config.add_section(section)

    def allValues(self):
        """获取当前 section 所有键值对（会自动转换类型）"""
        self.config.read(self.filename, encoding=self.encoding)
        if not self.config.has_section(self.section):
            return {}
        return {k: self.value(k) for k, _ in self.config.items(self.section)}

    def removeValue(self, key):
        self.config.read(self.filename, encoding=self.encoding)
        self.config.remove_option(self.section, key)
        with open(self.filename, "w", encoding=self.encoding) as f:
            self.config.write(f)


settings = ConfigSettings("set.ini")  # 生成配置文件

class ClientManager:
    def __init__(self, server_url):
        self.server_url = server_url
        self.session = requests.Session()  # 使用会话保持连接

    def get_public_ip(self):
        """获取公网IP地址"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))  # 使用标准DNS服务器
            client_address = s.getsockname()[0]
            s.close()
            return client_address
        except Exception:
            return '127.0.0.1'

    def register(self):
        """注册客户端到服务器"""
        try:
            headers = {'Content-Type': 'application/json'}
            data = {'client_address': self.get_public_ip(), 'timestamp': datetime.now().isoformat()}
            #response = requests.post("http://fukesihu.gnway.cc:80", data={'key': self.get_public_ip()})
            response = self.session.post(f"{self.server_url}/register", json=data, headers=headers, timeout=1)
            return response.status_code == 200
        except RequestException as e:
            print(f"注册异常: {e}")
            return False

    def check_version(self):
        """检查服务器版本"""
        try:
            response = self.session.get(f"{self.server_url}/version", timeout=3)
            if response.json().get('version') != local_version:  # 如果有版本信息且版本不一致，返回1
                version_status = 1
                return (version_status, response.json().get('version'))
            else:  # 否则返回0
                version_status = 0
                return (version_status, response.json().get('version'))
        except RequestException as e:
            version_status = 0
            # print(f"版本检查失败: {e}")
            return (version_status, 0)


'''def get_ip_address():
    try:
        # 获取本地主机名
        hostname = socket.gethostname()
        # 获取本地IP
        ip_address = socket.gethostbyname(hostname)
        return ip_address  # 返回IP地址
    except socket.error as e:
        print(f"Unable to get IP Address: {e}")
        return None  # 添加默认返回值


def check_update():
    global version
    # 首次启动时默认选项
    version_url = "http://fukesihu.gnway.cc:80/version.txt"
    try:
        response = requests.get(version_url)
        get_version = response.text.strip()
        last_version = get_version.replace('version = ', '')
        if response.status_code == 200:  # 如果连接到服务器
            if 'version' in get_version and last_version != version:  # 如果有版本信息且版本不一致，返回1
                return 1
            else:  # 否则返回0
                return 0
        else:  # 如果没连接到服务器，返回0
            return 0
    except requests.RequestException as e:
        print(f"Error checking update: {e}")
        return 0'''


# check_update()


'''def send_address():
    send_number = 3  # 设置发送次数
    while close_number == 1 and send_number > 0:
        try:
            update_url = "http://fukesihu.gnway.cc:80"  # 连接服务器
            requests.post(update_url, data={'key': get_ip_address()})  # 将唯一IP发送给服务器（统计连接数使用）
            wait_time = 300  # 设置发送时间，每5分钟发送一次
            send_number -= 1  # 发送一次后，次数减1
            while wait_time > 0:
                time.sleep(2)
                wait_time -= 2
                # print(wait_time)
                if close_number == 0:
                    break
        except requests.RequestException:
            time.sleep(5)
            send_number = 0  # print('连接服务器失败')


thread1 = threading.Thread(target=send_address)  # save_options()
thread1.start()'''

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

'''def closeEvent(event):
    # 当窗口关闭时调用
    global close_number, thread1
    close_number = 0  # 通知发送信息函数程序已停止，终止发送连接请求
    # event.accept()
    thread1.join()  # 等待线程结束
    stop_event.set()  # 通知所有线程停止'''


class Ui_MainWindow(object):
    textSignal = pyqtSignal(str)


    def setupUi(self, MainWindow):

        #super().__init__()
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(960, 540)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())  # 设置窗口大小固定
        MainWindow.setAcceptDrops(True)

        # 修正导入，确保从正确的模块导入 QIcon
        icon = QIcon()
        # 修正导入问题，确保从正确的模块导入 QPixmap
        icon.addPixmap(QPixmap("icon/log.png"))
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)  # type: ignore
        MainWindow.setAutoFillBackground(False)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(True)

        # Windows 应用标识设置（Win11必须）
        self.appid = '无尽冬日' + str(local_version)   # 需要唯一标识
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(self.appid)

        # 主窗口初始化
        #self.setWindowTitle('Win11 托盘演示')
        #self.setGeometry(300, 300, 400, 200)

        # 系统托盘初始化
        self.init_tray()

        # 初始显示
        #self.show()

        # 确保导入了QWidget类
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        # 背景
        self.listView = QListView(self.centralwidget)
        self.listView.setEnabled(False)
        self.listView.setGeometry(QRect(-2, -1, 971, 553))
        self.listView.setAutoFillBackground(False)
        self.listView.setStyleSheet("background-image: url(icon/11.png)")
        self.listView.setObjectName("listView")
        # 模拟器参数设置区域
        # 确保导入了QFrame类
        self.frame = QFrame(self.centralwidget)
        # 问题在于代码中使用了 QRect，但没有确保正确导入 QtCore 模块。
        self.frame.setGeometry(QRect(490, 40, 461, 230))
        # self.frame.setStyleSheet("#frame{border:1px solid rgb(0,255,0)}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        # 下拉框
        # noinspection PyAttributeOutsideInit
        # 模拟器安装地址
        self.select_address = QLabel(self.frame)
        self.select_address.setGeometry(QRect(20, 10, 90, 21))
        self.select_address.setObjectName("select_text")
        '''self.comboBox = QComboBox(self.frame)
        self.comboBox.setGeometry(QRect(10, 10, 91, 22))
        # self.comboBox.setAutoFillBackground(False)
        # self.comboBox.setStyleSheet("background: transparent;")
        self.comboBox.setStyleSheet("QComboBox {\n"
                                    "    background-color: rgba(0, 0, 0, 0); /* 白色背景，150为透明度 */\n"
                                    "    border: 1px solid rgba(0, 255, 0); /* 边框样式 */\n"
                                    "}\n")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("模拟器地址", 1)
        self.comboBox.addItem("模拟器ip", 2)
        self.comboBox.currentIndexChanged[int].connect(self.updateLineEdit)  # 下拉框信号槽'''
        self.lineEdit_address = QLineEdit(self.frame)  # 模拟器地址输入框
        self.lineEdit_address.setEnabled(True)
        self.lineEdit_address.setGeometry(QRect(130, 10, 221, 21))
        self.lineEdit_address.setMouseTracking(True)
        self.lineEdit_address.setAcceptDrops(True)
        # self.lineEdit.setText(self.updateLineEdit())
        self.lineEdit_address.setAutoFillBackground(False)
        self.lineEdit_address.setStyleSheet("QLineEdit {\n""    background: transparent;\n""    border: 1px solid rgba(0, 255, 0); /* 边框样式 */\n""}")
        self.lineEdit_address.setFrame(True)
        self.lineEdit_address.setDragEnabled(False)
        self.lineEdit_address.setReadOnly(False)
        self.lineEdit_address.setClearButtonEnabled(False)
        self.lineEdit_address.setObjectName("lineEdit")
        # 模拟器ip地址
        self.select_ip_address = QLabel(self.frame)
        self.select_ip_address.setGeometry(QRect(20, 40, 90, 21))
        self.select_ip_address.setObjectName("select_text")
        # 模拟器ip地址输入框
        self.lineEdit_ip_address = QLineEdit(self.frame)
        self.lineEdit_ip_address.setEnabled(True)
        self.lineEdit_ip_address.setGeometry(QRect(130, 40, 221, 21))
        self.lineEdit_ip_address.setMouseTracking(True)
        self.lineEdit_ip_address.setAcceptDrops(True)
        self.lineEdit_ip_address.setAutoFillBackground(False)
        self.lineEdit_ip_address.setStyleSheet("QLineEdit {\n""    background: transparent;\n""    border: 1px solid rgba(0, 255, 0); /* 边框样式 */\n""}")
        self.lineEdit_ip_address.setFrame(True)
        self.lineEdit_ip_address.setDragEnabled(False)
        self.lineEdit_ip_address.setReadOnly(False)
        self.lineEdit_ip_address.setClearButtonEnabled(False)
        self.lineEdit_ip_address.setObjectName("lineEdit")
        # 模拟器地址/ip保存按钮
        self.save_simulator = QPushButton(self.frame)
        self.save_simulator.setEnabled(True)
        self.save_simulator.setGeometry(QRect(380, 10, 75, 23))
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
        self.save_simulator.setVisible(False)  # 隐藏显示该功能（已弃用该功能）
        self.save_simulator.setStyleSheet("QPushButton {\n""border: 1px solid rgb(0,255,0); /* 边框样式 */\n"
                                          "}"
                                          "QPushButton:hover {\n"
                                          "background-color: rgba(0, 0, 0, 15); /* 编辑状态下的背景透明度 */\n"
                                          "}\n"
                                          "QPushButton:pressed {\n"
                                          "background-color: rgba(0, 0, 0, 80); /* 编辑状态下的背景透明度 */\n"
                                          "}\n")
        self.save_simulator.setObjectName("pushButton")
        # self.save_simulator.clicked.connect(self.save_simulator_settings)  # type: ignore
        '''模拟器区域'''
        '''self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setGeometry(QRect(490, 90, 461, 41))
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.frame_2.setBaseSize(QtCore.QSize(0, 0))
        self.frame_2.setMouseTracking(False)
        self.frame_2.setTabletTracking(False)
        self.frame_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)  #type: ignore
        self.frame_2.setAcceptDrops(False)
        self.frame_2.setAutoFillBackground(False)
        # self.frame_2.setStyleSheet("#frame_2{border:1px solid rgb(0,255,0)}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(1)
        self.frame_2.setMidLineWidth(0)
        self.frame_2.setObjectName("frame_2")'''
        # 启动模拟器
        self.start_simulator = QPushButton(self.frame)
        # self.start_simulator = StyledButton(self.frame)
        self.start_simulator.setGeometry(QRect(10, 70, 75, 23))
        self.start_simulator.setFlat(True)
        # self.start_simulator.setFont(QFont("Arial", 20))
        self.start_simulator.setStyleSheet("QPushButton {\n""border: 1px solid rgb(0,255,0); /* 边框样式 */\n"
                                           "}"
                                           "QPushButton:hover {\n"
                                           "background-color: rgba(0, 0, 0, 15); /* 编辑状态下的背景透明度 */\n"
                                           "}\n"
                                           "QPushButton:pressed {\n"
                                           "background-color: rgba(0, 0, 0, 80); /* 编辑状态下的背景透明度 */\n"
                                           "}\n")
        self.start_simulator.setObjectName("start_simulator")
        # 连接模拟器
        self.connect_simulator = QPushButton(self.frame)
        self.connect_simulator.setGeometry(QRect(130, 70, 75, 23))
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
        # 启动游戏
        self.start_game = QPushButton(self.frame)
        self.start_game.setGeometry(QRect(260, 70, 75, 23))
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
        # 一键启动
        self.simulator_start_all = QPushButton(self.frame)
        self.simulator_start_all.setGeometry(QRect(380, 70, 75, 23))
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
        # 其他设置
        self.select_text = QLabel(self.frame)
        self.select_text.setGeometry(QRect(10, 100, 81, 21))
        self.select_text.setObjectName("select_text")
        # 开启定时
        self.select_time = QCheckBox(self.frame)
        self.select_time.setGeometry(QRect(20, 130, 100, 21))
        self.select_time.setObjectName("开启定时")
        self.select_time.setStyleSheet("background-color: transparent")
        # 循环间隔文本
        self.label_3 = QLabel(self.frame)
        self.label_3.setGeometry(QRect(120, 130, 81, 21))
        self.label_3.setObjectName("label_3")
        # 间隔时间输入
        self.lineEdit_cycle_time = QLineEdit(self.frame)
        self.lineEdit_cycle_time.setGeometry(QRect(200, 131, 31, 21))
        self.lineEdit_cycle_time.setObjectName("lineEdit_cycle_time")
        self.lineEdit_cycle_time.setStyleSheet("QLineEdit {\n"
                                               "background: transparent;\n"
                                               "border: 1px solid rgba(0, 255, 0)"
                                               "}")
        # 增益已解锁
        self.checkBox_pet_Unlock = QCheckBox(self.frame)
        self.checkBox_pet_Unlock.setGeometry(QRect(300, 130, 100, 21))
        self.checkBox_pet_Unlock.setObjectName("增益已解锁")
        self.checkBox_pet_Unlock.setStyleSheet("background-color: transparent")
        # 保存参数按钮
        self.ty_set = QPushButton(self.frame)
        self.ty_set.setGeometry(QRect(190, 160, 75, 21))
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
        # 全选
        self.select_all = QPushButton(self.frame)
        self.select_all.setGeometry(QRect(90, 190, 75, 23))
        self.select_all.setFlat(True)
        self.select_all.setObjectName("select_all")
        self.select_all.setStyleSheet("QPushButton {\n""border: 1px solid rgb(0,255,0); /* 边框样式 */\n"
                                      "}"

                                      "QPushButton:hover {\n"
                                      "background-color: rgba(0, 0, 0, 15); /* 鼠标悬停时的背景透明度 */\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "background-color: rgba(0, 0, 0, 80); /* 按钮按下时的背景透明度 */\n"
                                      "}\n")
        # 取消全选
        self.select_unall = QPushButton(self.frame)
        self.select_unall.setGeometry(QRect(290, 190, 75, 23))
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
        # 停止按钮
        self.select_stop = QPushButton(self.frame)
        self.select_stop.setEnabled(True)
        self.select_stop.setGeometry(QRect(190, 190, 75, 23))
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
        # 多选开始按钮
        self.select_start = QPushButton(self.frame)
        self.select_start.setEnabled(True)
        self.select_start.setGeometry(QRect(190, 190, 75, 23))
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

        # 功能区
        ''' self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setGeometry(QRect(10, 40, 461, 181))
        # self.frame_3.setStyleSheet("#frame_3{border:1px solid rgb(0,255,0)}")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setObjectName("frame_3")'''

        # 任务区域
        self.frame_task = QFrame(self.centralwidget)
        self.frame_task.setGeometry(QRect(10, 40, 461, 470))
        # self.frame_task.setStyleSheet("#frame_task{border:1px solid rgb(0,255,0)}")
        self.frame_task.setFrameShape(QFrame.NoFrame)
        self.frame_task.setFrameShadow(QFrame.Raised)
        self.frame_task.setObjectName("frame_task")
        self.ty_title = QLabel(self.frame_task)
        self.ty_title.setGeometry(QRect(10, 0, 81, 21))
        self.ty_title.setObjectName("simple_title")

        # 互助文本
        self.label_help = QLabel(self.frame_task)
        self.label_help.setGeometry(QRect(20, 20, 54, 21))  # 显示文本
        self.label_help.setObjectName("联盟互助")
        # 开关选项
        self.checkBox_help = QCheckBox(self.frame_task)  # 互助
        self.checkBox_help.setGeometry(QRect(80, 20, 71, 21))
        self.checkBox_help.setObjectName("checkBox_help")
        # 互助随机时间选项
        self.checkBox_Random_time = QCheckBox(self.frame_task)
        self.checkBox_Random_time.setGeometry(QRect(170, 20, 71, 21))
        self.checkBox_Random_time.setObjectName("随机时间")
        # 世界野怪文本
        self.label_XG = QLabel(self.frame_task)
        self.label_XG.setGeometry(QRect(20, 50, 54, 21))  # 显示等级文本
        self.label_XG.setObjectName("世界野怪文本")
        # 开关选项
        self.checkBox_XG = QCheckBox(self.frame_task)  # 野怪
        self.checkBox_XG.setGeometry(QRect(80, 50, 71, 21))
        self.checkBox_XG.setObjectName("checkBox_XG")
        self.checkBox_XG.setStyleSheet("background-color: transparent")
        # 世界野怪平均兵力选项
        self.checkBox_XG_average = QCheckBox(self.frame_task)
        self.checkBox_XG_average.setGeometry(QRect(170, 50, 71, 21))
        self.checkBox_XG_average.setObjectName("平均兵力")
        # 世界野怪等级文本
        self.label_XG_lv = QLabel(self.frame_task)
        self.label_XG_lv.setGeometry(QRect(350, 50, 54, 21))  # 显示等级文本
        self.label_XG_lv.setObjectName("label_XG_lv")
        # 世界野怪输入
        self.lineEdit_XG = QLineEdit(self.frame_task)
        self.lineEdit_XG.setGeometry(QRect(400, 50, 31, 21))  # 显示等级输入框
        self.lineEdit_XG.setObjectName("lineEdit_XG")
        self.lineEdit_XG.setStyleSheet("QLineEdit {\n"
                                       "background: transparent;\n"
                                       "border: 1px solid rgba(0, 255, 0)"
                                       "}")
        # 冰原巨兽文本
        self.label_WM = QLabel(self.frame_task)
        self.label_WM.setGeometry(QRect(20, 80, 54, 21))  # 显示文本
        self.label_WM.setObjectName("冰原巨兽文本")
        # 开关选项
        self.checkBox_WM = QCheckBox(self.frame_task)  # 冰原巨兽
        self.checkBox_WM.setGeometry(QRect(80, 80, 71, 21))
        self.checkBox_WM.setObjectName("checkBox_WM")
        # 冰原巨兽单兵选项
        self.checkBox_WM_simple = QCheckBox(self.frame_task)
        self.checkBox_WM_simple.setGeometry(QRect(170, 80, 71, 21))
        self.checkBox_WM_simple.setObjectName("checkBox_ty_simple")
        # 冰原巨兽巨兽队列选项
        self.checkBox_WM_average = QCheckBox(self.frame_task)
        self.checkBox_WM_average.setGeometry(QRect(260, 80, 71, 21))
        self.checkBox_WM_average.setObjectName("巨兽队列")
        # 冰原巨兽等级文本
        self.label_WM_lv = QLabel(self.frame_task)
        self.label_WM_lv.setGeometry(QRect(350, 80, 54, 21))  # 显示等级文本
        self.label_WM_lv.setObjectName("label_WM_lv")
        # 冰原巨兽输入
        self.lineEdit_WM = QLineEdit(self.frame_task)
        self.lineEdit_WM.setGeometry(QRect(400, 80, 31, 21))  # 显示等级输入框
        self.lineEdit_WM.setObjectName("lineEdit_WM")
        self.lineEdit_WM.setStyleSheet("QLineEdit {\n"
                                       "background: transparent;\n"
                                       "border: 1px solid rgba(0, 255, 0)"
                                       "}")
        

        # 训练士兵文本
        self.label_Production = QLabel(self.frame_task)
        self.label_Production.setGeometry(QRect(20, 110, 54, 21))  # 显示等级文本
        self.label_Production.setObjectName("训练士兵")
        # 开关选项
        self.checkBox_Production = QCheckBox(self.frame_task)  # 训练士兵
        self.checkBox_Production.setGeometry(QRect(80, 110, 71, 21))
        self.checkBox_Production.setObjectName("checkBox_Production")

        # 训练晋升选项
        self.checkBox_jinshen = QCheckBox(self.frame_task)
        self.checkBox_jinshen.setGeometry(QRect(170, 113, 71, 21))
        self.checkBox_jinshen.setObjectName("优先晋升")

        # 训练晋升选项
        self.checkBox_maxed_barracks = QCheckBox(self.frame_task)
        self.checkBox_maxed_barracks.setGeometry(QRect(260, 110, 71, 21))
        self.checkBox_maxed_barracks.setObjectName("满级兵营")
        

        # 采集文本
        self.label_Collection = QLabel(self.frame_task)
        self.label_Collection.setGeometry(QRect(20, 140, 54, 21))  # 显示等级文本
        self.label_Collection.setObjectName("资源采集")
        # 开关选项
        self.checkBox_Collection = QCheckBox(self.frame_task)  # 采集资源
        self.checkBox_Collection.setGeometry(QRect(80, 140, 71, 21))
        self.checkBox_Collection.setObjectName("checkBox_Collection")

        # 采集英雄选项
        self.checkBox_Collection_hero = QCheckBox(self.frame_task)
        self.checkBox_Collection_hero.setGeometry(QRect(170, 140, 71, 21))
        self.checkBox_Collection_hero.setObjectName("采集英雄")
        # 采集平均兵力选项
        # self.checkBox_ty_caiji_average = QCheckBox(self.frame_task)
        # self.checkBox_ty_caiji_average.setGeometry(QRect(200, 53, 71, 21))
        # self.checkBox_ty_caiji_average.setObjectName("平均兵力")
        # 采集等级文本
        self.label_Collection_lv = QLabel(self.frame_task)
        self.label_Collection_lv.setGeometry(QRect(350, 140, 54, 21))  # 显示等级文本
        self.label_Collection_lv.setObjectName("label_4")
        #self.label_4.setVisible(False)
        # 采集等级输入
        self.lineEdit_Collection = QLineEdit(self.frame_task)
        self.lineEdit_Collection.setGeometry(QRect(400, 140, 31, 21))  # 显示等级输入框
        self.lineEdit_Collection.setObjectName("lineEdit_3")
        self.lineEdit_Collection.setStyleSheet("QLineEdit {\n"
                                               "background: transparent;\n"
                                               "border: 1px solid rgba(0, 255, 0)"
                                               "}")

        # 情报文本
        self.label_intelligence = QLabel(self.frame_task)
        self.label_intelligence.setGeometry(QRect(20, 170, 54, 21))  # 显示文本
        self.label_intelligence.setObjectName("情报文本")
        # 情报开关选项
        self.checkBox_intelligence = QCheckBox(self.frame_task)
        self.checkBox_intelligence.setGeometry(QRect(80, 170, 71, 21))
        self.checkBox_intelligence.setObjectName("情报开关")
        # 情报版本选项
        self.checkBox_intelligence_version = QCheckBox(self.frame_task)
        self.checkBox_intelligence_version.setGeometry(QRect(170, 170, 71, 21))
        self.checkBox_intelligence_version.setObjectName("情报版本")
        # self.checkBox_intelligence_version.setVisible(False)
        # 情报品质选项
        self.checkBox_intelligence_high_quality = QCheckBox(self.frame_task)
        self.checkBox_intelligence_high_quality.setGeometry(QRect(170, 170, 71, 21))
        self.checkBox_intelligence_high_quality.setObjectName("情报品质")
        self.checkBox_intelligence_high_quality.setVisible(False)
        # 十次情报选项
        self.checkBox_intelligence_number = QCheckBox(self.frame_task)
        self.checkBox_intelligence_number.setGeometry(QRect(260, 170, 71, 21))
        self.checkBox_intelligence_number.setObjectName("十次情报")
        self.checkBox_intelligence_number.setVisible(False)
        # 十次情报选项
        self.checkBox_intelligence_offer_a_reward = QCheckBox(self.frame_task)
        self.checkBox_intelligence_offer_a_reward.setGeometry(QRect(350, 170, 71, 21))
        self.checkBox_intelligence_offer_a_reward.setObjectName("悬赏情报")
        self.checkBox_intelligence_offer_a_reward.setVisible(False)
        # 仓库补给文本
        self.label_warehouse = QLabel(self.frame_task)
        self.label_warehouse.setGeometry(QRect(20, 200, 54, 21))  # 显示文本
        self.label_warehouse.setObjectName("仓库补给")
        # 仓库补给开关选项
        self.checkBox_warehouse = QCheckBox(self.frame_task)
        self.checkBox_warehouse.setGeometry(QRect(80, 200, 71, 21))
        self.checkBox_warehouse.setObjectName("仓库补给")
        # 仓库体力补给开关选项
        self.checkBox_warehouse_physical_strength = QCheckBox(self.frame_task)
        self.checkBox_warehouse_physical_strength.setGeometry(QRect(170, 200, 71, 21))
        self.checkBox_warehouse_physical_strength.setObjectName("仓库体力")
        # 巨熊活动文本
        self.label_bear = QLabel(self.frame_task)
        self.label_bear.setGeometry(QRect(20, 230, 54, 21))  # 显示文本
        self.label_bear.setObjectName("巨熊活动")
        # 开关选项
        self.checkBox_bear = QCheckBox(self.frame_task)  # 巨熊活动
        self.checkBox_bear.setGeometry(QRect(80, 230, 71, 21))
        self.checkBox_bear.setObjectName("checkBox_bear")
        # 巨熊队列开关选项
        self.checkBox_bear_queue = QCheckBox(self.frame_task)  # 巨熊活动
        self.checkBox_bear_queue.setGeometry(QRect(170, 230, 71, 21))
        self.checkBox_bear_queue.setObjectName("队列开关")
        # 巨熊时间文本
        self.label_bear_time = QLabel(self.frame_task)
        self.label_bear_time.setGeometry(QRect(350, 230, 54, 21))  # 显示时间文本
        self.label_bear_time.setObjectName("label_4")
        # self.label_4.setVisible(False)
        # 巨熊时间输入
        self.lineEdit_bear_time = QLineEdit(self.frame_task)
        self.lineEdit_bear_time.setGeometry(QRect(400, 230, 31, 21))  # 显示时间输入框
        self.lineEdit_bear_time.setObjectName("lineEdit_3")
        self.lineEdit_bear_time.setStyleSheet("QLineEdit {\n"
                                              "background: transparent;\n"
                                              "border: 1px solid rgba(0, 255, 0)"
                                              "}")
        # 活动雪怪文本
        self.label_npc = QLabel(self.frame_task)
        self.label_npc.setGeometry(QRect(20, 260, 54, 21))  # 显示文本
        self.label_npc.setObjectName("活动雪怪")
        # 开关选项
        self.checkBox_npc = QCheckBox(self.frame_task)  # 活动雪怪
        self.checkBox_npc.setGeometry(QRect(80, 260, 71, 21))
        self.checkBox_npc.setObjectName("checkBox_npc")

        # 建筑升级文本
        self.label_build = QLabel(self.frame_task)
        self.label_build.setGeometry(QRect(170, 260, 54, 21))  # 显示文本
        self.label_build.setObjectName("XXXX")
        self.label_build.setVisible(False)
        # 开关选项
        self.checkBox_build = QCheckBox(self.frame_task)  # 建筑升级
        self.checkBox_build.setGeometry(QRect(230, 260, 200, 21))
        self.checkBox_build.setObjectName("checkBox_build")
        self.checkBox_build.setVisible(False)
        # 治疗士兵文本
        self.label_treatment = QLabel(self.frame_task)
        self.label_treatment.setGeometry(QRect(20, 320, 54, 21))  # 显示文本
        self.label_treatment.setObjectName("XXXX")
        # 开关选项
        self.checkBox_treatment = QCheckBox(self.frame_task)  # 治疗士兵
        self.checkBox_treatment.setGeometry(QRect(80, 320, 71, 21))
        self.checkBox_treatment.setObjectName("checkBox_treatment")


        # 联盟捐赠文本
        self.label_donate = QLabel(self.frame_task)
        self.label_donate.setGeometry(QRect(170, 320, 54, 21))  # 显示文本
        self.label_donate.setObjectName("XXXX")
        # 开关选项
        self.checkBox_donate = QCheckBox(self.frame_task)  # 联盟捐赠
        self.checkBox_donate.setGeometry(QRect(230, 320, 71, 21))
        self.checkBox_donate.setObjectName("checkBox_donate")

        # 英雄招募文本
        self.label_recruit = QLabel(self.frame_task)
        self.label_recruit.setGeometry(QRect(320, 320, 54, 21))  # 显示文本
        self.label_recruit.setObjectName("XXXX")
        # 开关选项
        self.checkBox_recruit = QCheckBox(self.frame_task)  # 英雄招募
        self.checkBox_recruit.setGeometry(QRect(380, 320, 71, 21))
        self.checkBox_recruit.setObjectName("checkBox_collision")
        # 炼金实验室文本
        self.label_alchemical_Laboratory = QLabel(self.frame_task)
        self.label_alchemical_Laboratory.setGeometry(QRect(20, 350, 65, 21))  # 显示文本
        self.label_alchemical_Laboratory.setObjectName("XXXX")
        # 开关选项
        self.checkBox_alchemical_Laboratory = QCheckBox(self.frame_task)  # 炼金实验室
        self.checkBox_alchemical_Laboratory.setGeometry(QRect(80, 350, 71, 21))
        self.checkBox_alchemical_Laboratory.setObjectName("checkBox_collision")

        # 攻击检测文本
        self.label_collision = QLabel(self.frame_task)
        self.label_collision.setGeometry(QRect(170, 350, 54, 21))  # 显示文本
        self.label_collision.setObjectName("XXXX")
        # 开关选项
        self.checkBox_collision = QCheckBox(self.frame_task)  # 攻击检测
        self.checkBox_collision.setGeometry(QRect(230, 350, 71, 21))
        self.checkBox_collision.setObjectName("checkBox_collision")

        # 邮件领取文本
        self.label_mail = QLabel(self.frame_task)
        self.label_mail.setGeometry(QRect(320, 350, 54, 21))  # 显示文本
        self.label_mail.setObjectName("XXXX")
        # 开关选项
        self.checkBox_mail = QCheckBox(self.frame_task)  # 邮件领取
        self.checkBox_mail.setGeometry(QRect(380, 350, 71, 21))
        self.checkBox_mail.setObjectName("checkBox_mail")

        # 联盟宝箱文本
        self.label_Treasure_Chest = QLabel(self.frame_task)
        self.label_Treasure_Chest.setGeometry(QRect(20, 380, 54, 21))  # 显示文本
        self.label_Treasure_Chest.setObjectName("XXXX")
        # 开关选项
        self.checkBox_Treasure_Chest = QCheckBox(self.frame_task)  # 联盟宝箱
        self.checkBox_Treasure_Chest.setGeometry(QRect(80, 380, 71, 21))
        self.checkBox_Treasure_Chest.setObjectName("checkBox_Treasure_Chest")

        # 探险奖励文本
        self.label_adventure = QLabel(self.frame_task)
        self.label_adventure.setGeometry(QRect(170, 380, 54, 21))  # 显示文本
        self.label_adventure.setObjectName("XXXX")
        # 开关选项
        self.checkBox_adventure = QCheckBox(self.frame_task)  # 探险奖励
        self.checkBox_adventure.setGeometry(QRect(230, 380, 71, 21))
        self.checkBox_adventure.setObjectName("checkBox_adventure")

        # 每日任务文本
        self.label_daily_task = QLabel(self.frame_task)
        self.label_daily_task.setGeometry(QRect(320, 380, 54, 21))  # 显示文本
        self.label_daily_task.setObjectName("XXXX")
        # 开关选项
        self.checkBox_daily_task = QCheckBox(self.frame_task)  # 每日任务
        self.checkBox_daily_task.setGeometry(QRect(380, 380, 71, 21))
        self.checkBox_daily_task.setObjectName("checkBox_adventure")

        # 生命之树文本
        self.label_tree_of_life = QLabel(self.frame_task)
        self.label_tree_of_life.setGeometry(QRect(20, 410, 54, 21))  # 显示文本
        self.label_tree_of_life.setObjectName("XXXX")
        # 开关选项
        self.checkBox_tree_of_life = QCheckBox(self.frame_task)  # 生命之树
        self.checkBox_tree_of_life.setGeometry(QRect(80, 410, 71, 21))
        self.checkBox_tree_of_life.setObjectName("checkBox_adventure")

        # 晨曦回礼文本
        self.label_morning_light_returns_gift = QLabel(self.frame_task)
        self.label_morning_light_returns_gift.setGeometry(QRect(170, 410, 54, 21))  # 显示文本
        self.label_morning_light_returns_gift.setObjectName("XXXX")
        # 开关选项
        self.checkBox_morning_light_returns_gift = QCheckBox(self.frame_task)  # 晨曦回礼
        self.checkBox_morning_light_returns_gift.setGeometry(QRect(230, 410, 71, 21))
        self.checkBox_morning_light_returns_gift.setObjectName("checkBox_adventure")

        # 单项内容
        '''
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setGeometry(QRect(490, 60, 461, 191))
        #self.frame_4.setStyleSheet("#frame_4{border:1px solid rgb(0,255,0)}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.simple_title = QLabel(self.frame_4)
        self.simple_title.setGeometry(QRect(10, 0, 81, 21))
        self.simple_title.setObjectName("simple_title")
        # 单项设置按钮
        self.simple_set = QPushButton(self.frame)
        self.simple_set.setGeometry(QRect(350, 0, 75, 21))
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
        self.radioButton_help.setGeometry(QRect(20, 30, 71, 16))
        self.radioButton_help.setAutoFillBackground(False)
        self.radioButton_help.setStyleSheet("")
        self.radioButton_help.setAutoRepeat(False)
        self.radioButton_help.setAutoExclusive(True)
        self.radioButton_help.setObjectName("radioButton_help")
        self.radioButton_XG = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_XG.setGeometry(QRect(110, 30, 71, 16))
        self.radioButton_XG.setObjectName("radioButton_XG")
        self.radioButton_WM = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_WM.setGeometry(QRect(200, 30, 71, 16))
        self.radioButton_WM.setObjectName("radioButton_WM")
        self.radioButton_npc = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_npc.setGeometry(QRect(290, 30, 71, 16))
        self.radioButton_npc.setObjectName("radioButton_npc")
        self.radioButton_Production = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_Production.setGeometry(QRect(380, 30, 71, 16))
        self.radioButton_Production.setObjectName("radioButton_Production")
        self.radioButton_adventure = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_adventure.setGeometry(QRect(380, 70, 71, 16))
        self.radioButton_adventure.setObjectName("radioButton_adventure")
        self.radioButton_treatment = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_treatment.setGeometry(QRect(290, 70, 71, 16))
        self.radioButton_treatment.setMouseTracking(True)
        self.radioButton_treatment.setTabletTracking(False)
        self.radioButton_treatment.setFocusPolicy(QtCore.Qt.StrongFocus)  #type: ignore
        self.radioButton_treatment.setStyleSheet("")
        self.radioButton_treatment.setObjectName("radioButton_treatment")
        self.radioButton_build = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_build.setGeometry(QRect(20, 70, 71, 16))
        self.radioButton_build.setObjectName("radioButton_build")
        self.radioButton_Collection = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_Collection.setGeometry(QRect(110, 70, 71, 16))
        self.radioButton_Collection.setObjectName("radioButton_Collection")
        self.radioButton_bear = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_bear.setGeometry(QRect(200, 70, 71, 16))
        self.radioButton_bear.setObjectName("radioButton_bear")
        self.radioButton_donate = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_donate.setGeometry(QRect(20, 110, 71, 16))
        self.radioButton_donate.setObjectName("radioButton_18")
        self.radioButton_recruit = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_recruit.setGeometry(QRect(110, 110, 71, 16))
        self.radioButton_recruit.setObjectName("radioButton_recruit")
        self.radioButton_collision = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_collision.setGeometry(QRect(200, 110, 71, 16))
        self.radioButton_collision.setObjectName("radioButton_collision")
        self.radioButton_mail = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_mail.setGeometry(QRect(290, 110, 71, 16))
        self.radioButton_mail.setObjectName("radioButton_mail")
        self.radioButton_Treasure_Chest = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_Treasure_Chest.setGeometry(QRect(380, 110, 71, 16))
        self.radioButton_Treasure_Chest.setObjectName("radioButton_Treasure_Chest")
        #将单选按钮添加至组
        self.radioButton_group = QButtonGroup(self.frame_4)  # 创建按钮组
        self.radioButton_group.addButton(self.radioButton_help, 1)  # 将单选项加入到按钮组
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
        self.simple_stop = QPushButton(self.frame_4)
        #self.simple_stop.setEnabled(True)
        self.simple_stop.setVisible(False)
        self.simple_stop.setGeometry(QRect(190, 150, 75, 23))
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
        self.simple_start = QPushButton(self.frame_4)
        #self.simple_start.setEnabled(True)
        self.simple_start.setGeometry(QRect(190, 150, 75, 23))
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
        '''
        # 输出区域
        self.frame_out = QFrame(self.centralwidget)
        self.frame_out.setGeometry(QRect(490, 270, 461, 241))
        # self.frame_out.setStyleSheet("#frame_out{border:1px solid rgb(0,255,0)}")
        self.frame_out.setFrameShape(QFrame.StyledPanel)
        self.frame_out.setFrameShadow(QFrame.Raised)
        self.frame_out.setObjectName("frame_out")
        self.label = QLabel(self.frame_out)
        self.label.setGeometry(QRect(10, 10, 54, 12))
        self.label.setObjectName("label")
        self.textEdit_out = QTextEdit(self.frame_out)
        self.textEdit_out.setEnabled(True)
        self.textEdit_out.setGeometry(QRect(10, 30, 441, 201))
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
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setGeometry(QRect(890, 520, 71, 20))
        self.label_2.setObjectName("label_2")
        self.label_Version_prompt = QLabel(self.centralwidget)  # 版本提示
        self.label_Version_prompt.setGeometry(QRect(650, 520, 300, 20))
        clientManager = ClientManager(network_address)
        return_value = clientManager.check_version()[0]
        clientManager1 = ClientManager(network_address1)
        return_value1 = clientManager1.check_version()[0]
        if return_value == 1:
            self.label_Version_prompt.setVisible(True)
        elif return_value == 0:
            if return_value1 == 1:
                self.label_Version_prompt.setVisible(True)
            elif return_value1 == 0:
                self.label_Version_prompt.setVisible(False)
        self.label_Version_prompt.setObjectName("label_Version_prompt")
        self.show_UI = QPushButton(self.centralwidget)
        self.show_UI.setGeometry(QRect(190, 520, 51, 23))
        self.show_UI.setFlat(True)
        self.show_UI.setObjectName("show_UI")
        self.notice_button = QPushButton(self.centralwidget)
        self.notice_button.setGeometry(QRect(60, 520, 61, 23))
        self.notice_button.setFlat(True)
        self.notice_button.setObjectName("notice_button")
        self.help_button = QPushButton(self.centralwidget)
        self.help_button.setGeometry(QRect(130, 520, 70, 23))
        self.help_button.setFlat(True)
        self.help_button.setObjectName("help_button")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QRect(70, 0, 850, 45))
        self.textEdit.setLayoutDirection(QtCore.Qt.RightToLeft)  #type: ignore
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setStyleSheet("QTextEdit {\n"
                                    "    background: transparent;\n"
                                    "    color: rgb(0, 0, 0);\n"
                                    "}")
        self.textEdit.setLocale(QLocale(QLocale.Chinese, QLocale.China))
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setFrameShadow(QFrame.Plain)
        self.textEdit.setTabChangesFocus(False)
        self.textEdit.setUndoRedoEnabled(False)
        self.textEdit.setOverwriteMode(False)
        self.textEdit.setAcceptRichText(False)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        self.hide_UI = QPushButton(self.centralwidget)
        self.hide_UI.setGeometry(QRect(5, 520, 51, 23))
        self.hide_UI.setFlat(True)
        self.hide_UI.setObjectName("hide_UI")
        self.listView.raise_()
        self.frame.raise_()
        # 2.3.0版本取消单项功能区
        # self.frame_2.raise_()
        # self.frame_3.raise_()
        self.frame_task.raise_()
        self.checkBox_WM_simple.raise_()
        self.checkBox_WM_average.raise_()
        self.checkBox_Collection_hero.raise_()
        #self.checkBox_ty_caiji_average.raise_()
        self.label_Collection.raise_()
        self.checkBox_jinshen.raise_()
        self.checkBox_maxed_barracks.raise_()
        # self.frame_4.raise_()
        self.frame_out.raise_()
        self.label_2.raise_()
        self.show_UI.raise_()
        self.show_UI.setVisible(False)
        self.show_UI.setGeometry(QRect(5, 520, 51, 23))
        self.notice_button.raise_()
        self.help_button.raise_()
        self.textEdit.raise_()
        self.hide_UI.raise_()
        self.label_Version_prompt.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        # 按钮点击触发响应
        self.retranslateUi(MainWindow)
        # 多选开始
        self.select_start.clicked.connect(self.select_start_button)  # type: ignore
        self.select_stop.clicked.connect(stop_function)  # type: ignore  # 多选停止
        self.ty_set.clicked.connect(self.save_ty_setting)  # type: ignore#保存参数
        # self.simple_set.clicked.connect(self.save_simple_set)  # type: ignore#单选设置
        # self.simple_start.clicked.connect(self.simple_start_button)  #type: ignore# 单选开始
        # self.simple_stop.clicked.connect(stop_function)  #type: ignore# 单选停止
        self.hide_UI.clicked.connect(self.hide_ui)  # type: ignore
        self.show_UI.clicked.connect(self.show_ui)  # type: ignore
        self.start_simulator.clicked.connect(lambda: start_simple(1))  # type: ignore
        self.connect_simulator.clicked.connect(lambda: start_simple(2))  # type: ignore
        self.start_game.clicked.connect(lambda: start_simple(3))  # type: ignore
        self.simulator_start_all.clicked.connect(lambda: start_simple(4))  # type: ignore
        self.select_all.clicked.connect(self.toggle_checkbox)  # type: ignore
        self.select_unall.clicked.connect(self.untoggle_checkbox)  # type: ignore
        self.notice_button.clicked.connect(self.open_noticeable)  # type: ignore
        self.notice = noticelog()
        self.help_button.clicked.connect(self.open_helpline)  # type: ignore
        self.help = helplog()
        # sys.stdout = RedirectText(self.textEdit_out）
        # 捕获标准输出和错误
        sys.stdout = self

        def insert_text(text):
            self.textEdit_out.insertPlainText(text)  # 将打印的内容插入到textEdit中
            self.textEdit_out.ensureCursorVisible()  # 将光标移动到可见区域（底部）

        # 连接textSignal到insert_text方法
        self.textSignal.connect(insert_text)  # type: ignore
        QMetaObject.connectSlotsByName(MainWindow)

    def set_font(self):  # 界面兼容设置，设置界面文本大小，保证不同分辨率情况下显示正常
        font = QFont("Arial", 7)
        # font.setPointSize(10)
        self.select_address.setFont(font)
        self.select_ip_address.setFont(font)
        self.save_simulator.setFont(font)
        self.start_simulator.setFont(font)
        self.connect_simulator.setFont(font)
        self.start_game.setFont(font)
        self.simulator_start_all.setFont(font)
        self.select_text.setFont(font)
        self.select_time.setFont(font)
        self.checkBox_pet_Unlock.setFont(font)
        self.label_help.setFont(font)
        self.checkBox_help.setFont(font)
        self.label_XG.setFont(font)
        self.checkBox_XG.setFont(font)
        self.label_WM.setFont(font)
        self.checkBox_WM.setFont(font)
        self.label_npc.setFont(font)
        self.checkBox_npc.setFont(font)
        self.label_Production.setFont(font)
        self.checkBox_Production.setFont(font)
        self.label_adventure.setFont(font)
        self.checkBox_adventure.setFont(font)
        self.label_daily_task.setFont(font)
        self.checkBox_daily_task.setFont(font)
        self.label_tree_of_life.setFont(font)
        self.checkBox_tree_of_life.setFont(font)
        self.label_morning_light_returns_gift.setFont(font)
        self.checkBox_morning_light_returns_gift.setFont(font)
        self.label_treatment.setFont(font)
        self.checkBox_treatment.setFont(font)
        self.label_build.setFont(font)
        self.checkBox_build.setFont(font)
        self.label_Collection.setFont(font)
        self.label_Collection_lv.setFont(font)
        self.checkBox_Collection.setFont(font)
        self.label_bear.setFont(font)
        self.checkBox_bear.setFont(font)
        self.label_bear_time.setFont(font)
        self.label_donate.setFont(font)
        self.checkBox_donate.setFont(font)
        self.label_recruit.setFont(font)
        self.checkBox_recruit.setFont(font)
        self.label_alchemical_Laboratory.setFont(font)
        self.checkBox_alchemical_Laboratory.setFont(font)
        self.label_collision.setFont(font)
        self.checkBox_collision.setFont(font)
        self.label_mail.setFont(font)
        self.checkBox_mail.setFont(font)
        self.label_Treasure_Chest.setFont(font)
        self.checkBox_Treasure_Chest.setFont(font)
        self.label_warehouse.setFont(font)
        self.checkBox_warehouse.setFont(font)
        self.select_all.setFont(font)
        self.select_unall.setFont(font)
        self.select_stop.setFont(font)
        self.select_start.setFont(font)
        self.label_intelligence.setFont(font)
        self.checkBox_intelligence.setFont(font)
        self.checkBox_intelligence_version.setFont(font)
        self.checkBox_intelligence_number.setFont(font)
        self.checkBox_intelligence_offer_a_reward.setFont(font)
        self.checkBox_intelligence_high_quality.setFont(font)
        self.checkBox_warehouse_physical_strength.setFont(font)
        '''self.radioButton_help.setFont(font)
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
        self.radioButton_Treasure_Chest.setFont(font)'''
        #self.simple_stop.setFont(font)
        #self.simple_start.setFont(font)
        self.label_3.setFont(font)
        #self.label_4.setFont(font)
        self.label_Collection.setFont(font)
        self.label_WM.setFont(font)
        self.ty_set.setFont(font)
        self.checkBox_Random_time.setFont(font)
        self.checkBox_jinshen.setFont(font)
        self.checkBox_maxed_barracks.setFont(font)
        self.checkBox_WM_simple.setFont(font)
        self.checkBox_WM_average.setFont(font)
        self.checkBox_Collection_hero.setFont(font)
        self.checkBox_XG_average.setFont(font)
        self.label_XG_lv.setFont(font)
        self.lineEdit_XG.setFont(font)
        # self.checkBox_ty_caiji_average.setFont(font)
        # self.simple_set.setFont(font)
        self.label.setFont(font)
        self.label_Version_prompt.setFont(font)
        self.label_2.setFont(font)
        self.show_UI.setFont(font)
        self.notice_button.setFont(font)
        self.help_button.setFont(font)
        self.textEdit.setFont(font)
        self.hide_UI.setFont(font)

    def retranslateUi(self, MainWindow):  # 将按钮文本等显示到窗口
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "无尽冬日（个人练习使用，请勿商用）"))
        self.textEdit.setText(_translate("MainWindow", "<font color=\"#FF0000\" size=4><p align=\"center\"  style=\" margin-top:0px; "
                                                       "margin-bottom:5px; \">注意事项：①模拟器分辨率：手机（1080*1920）____②游戏设置：画质高级，关闭雪花和昼夜</p>"
                                                       "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px\" >③请停止执行任务后再关闭脚本____④请等待程序停止后再设置相关参数____⑤设置相关参数后点击保存参数并请重新开始执行任务</p></font>"))
        self.save_simulator.setText(_translate("MainWindow", "保存"))
        self.select_address.setText(_translate("MainWindow", "模拟器安装路径："))
        self.select_ip_address.setText(_translate("MainWindow", "模拟器IP地址："))
        self.start_simulator.setText(_translate("MainWindow", "启动模拟器"))
        self.connect_simulator.setText(_translate("MainWindow", "连接模拟器"))
        self.start_game.setText(_translate("MainWindow", "启动游戏"))
        self.simulator_start_all.setText(_translate("MainWindow", "一键启动"))
        self.select_text.setText(_translate("MainWindow", "其他设置"))
        self.select_time.setText(_translate("MainWindow", "开启定时"))
        self.label_3.setText(_translate("MainWindow", "循环间隔(秒):"))
        self.checkBox_pet_Unlock.setText(_translate("MainWindow", "增益已解锁"))
        self.ty_set.setText(_translate("MainWindow", "保存参数"))
        self.ty_title.setText(_translate("MainWindow", "任务选项"))
        self.label_help.setText(_translate("MainWindow", "联盟互助："))
        self.checkBox_help.setText(_translate("MainWindow", "启用"))
        self.checkBox_Random_time.setText(_translate("MainWindow", "随机时间"))
        self.label_XG.setText(_translate("MainWindow", "世界野怪："))
        self.checkBox_XG.setText(_translate("MainWindow", "启用"))
        self.checkBox_XG_average.setText(_translate("MainWindow", "平均兵力"))
        self.label_XG_lv.setText(_translate("MainWindow", "等级设置:"))
        self.label_WM.setText(_translate("MainWindow", "冰原巨兽："))
        self.checkBox_WM.setText(_translate("MainWindow", "启用"))
        self.checkBox_WM_simple.setText(_translate("MainWindow", "单兵集结"))
        self.checkBox_WM_average.setText(_translate("MainWindow", "巨兽队列"))
        self.label_WM_lv.setText(_translate("MainWindow", "等级设置:"))
        self.label_npc.setText(_translate("MainWindow", "活动雪怪："))
        self.checkBox_npc.setText(_translate("MainWindow", "启用"))
        self.label_Production.setText(_translate("MainWindow", "训练士兵："))
        self.checkBox_Production.setText(_translate("MainWindow", "启用"))
        self.checkBox_jinshen.setText(_translate("MainWindow", "优先晋升"))
        self.checkBox_maxed_barracks.setText(_translate("MainWindow", "满级兵营"))
        self.label_adventure.setText(_translate("MainWindow", "探险奖励："))
        self.checkBox_adventure.setText(_translate("MainWindow", "启用"))
        self.label_daily_task.setText(_translate("MainWindow", "每日任务："))
        self.checkBox_daily_task.setText(_translate("MainWindow", "启用"))
        self.label_tree_of_life.setText(_translate("MainWindow", "生命之树："))
        self.checkBox_tree_of_life.setText(_translate("MainWindow", "启用"))
        self.label_morning_light_returns_gift.setText(_translate("MainWindow", "晨曦回礼："))
        self.checkBox_morning_light_returns_gift.setText(_translate("MainWindow", "启用"))
        self.label_treatment.setText(_translate("MainWindow", "治疗士兵："))
        self.checkBox_treatment.setText(_translate("MainWindow", "启用"))
        self.label_build.setText(_translate("MainWindow", "建筑升级："))
        self.checkBox_build.setText(_translate("MainWindow", "启用"))
        self.label_Collection.setText(_translate("MainWindow", "采集资源："))
        self.checkBox_Collection.setText(_translate("MainWindow", "启用"))
        self.checkBox_Collection_hero.setText(_translate("MainWindow", "采集英雄"))
        # self.checkBox_ty_caiji_average.setText(_translate("MainWindow", "平均兵力"))
        self.label_Collection_lv.setText(_translate("MainWindow", "等级设置:"))
        self.label_bear.setText(_translate("MainWindow", "巨熊活动："))
        self.checkBox_bear.setText(_translate("MainWindow", "启用"))
        self.checkBox_bear_queue.setText(_translate("MainWindow", "巨熊队列"))
        self.label_bear_time.setText(_translate("MainWindow", "时间/时："))
        self.label_intelligence.setText(_translate("MainWindow", "情报灯塔："))
        self.checkBox_intelligence.setText(_translate("MainWindow", "启用"))
        self.checkBox_intelligence_version.setText(_translate("MainWindow", "火晶版本"))
        self.checkBox_intelligence_high_quality.setText(_translate("MainWindow", "金紫品质"))
        self.checkBox_intelligence_number.setText(_translate("MainWindow", "十次情报"))
        self.checkBox_intelligence_offer_a_reward.setText(_translate("MainWindow", "悬赏情报"))
        self.label_donate.setText(_translate("MainWindow", "联盟捐赠："))
        self.checkBox_donate.setText(_translate("MainWindow", "启用"))
        self.label_recruit.setText(_translate("MainWindow", "英雄招募："))
        self.checkBox_recruit.setText(_translate("MainWindow", "启用"))
        self.label_alchemical_Laboratory.setText(_translate("MainWindow", "炼金实验："))
        self.checkBox_alchemical_Laboratory.setText(_translate("MainWindow", "启用"))
        self.label_collision.setText(_translate("MainWindow", "攻击检测："))
        self.checkBox_collision.setText(_translate("MainWindow", "启用"))
        self.label_mail.setText(_translate("MainWindow", "邮件领取："))
        self.checkBox_mail.setText(_translate("MainWindow", "启用"))
        self.label_Treasure_Chest.setText(_translate("MainWindow", "联盟宝箱："))
        self.checkBox_Treasure_Chest.setText(_translate("MainWindow", "启用"))
        self.label_warehouse.setText(_translate("MainWindow", "仓库补给："))
        self.checkBox_warehouse.setText(_translate("MainWindow", "启用"))
        self.checkBox_warehouse_physical_strength.setText(_translate("MainWindow", "仓库体力"))
        self.select_all.setText(_translate("MainWindow", "全选"))
        self.select_unall.setText(_translate("MainWindow", "取消全选"))
        self.select_stop.setText(_translate("MainWindow", "停止"))
        self.select_start.setText(_translate("MainWindow", "开始"))
        # 2.3.0版本取消单项功能区
        '''self.simple_title.setText(_translate("MainWindow", "单选项（单选）"))
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
        self.simple_start.setText(_translate("MainWindow", "开始"))'''

        # self.simple_set.setText(_translate("MainWindow", "设置"))
        self.label.setText(_translate("MainWindow", "输出："))
        self.label_Version_prompt.setText(_translate("MainWindow", "<font color=\"#FF0000\" ><p>检查到新版本，请于群内下载最新版本</p></font>"))
        self.label_2.setText(_translate("MainWindow", "版本:" + str(local_version)))
        self.show_UI.setText(_translate("MainWindow", "显示UI"))
        self.notice_button.setText(_translate("MainWindow", "版本日志"))
        self.help_button.setText(_translate("MainWindow", "功能说明"))
        self.hide_UI.setText(_translate("MainWindow", "隐藏UI"))

    @pyqtSlot()
    def load_settings(self):  # 读取设置
        # global settings
        simulator_address = settings.value('模拟器安装地址', r'E:\leidian\LDPlayer9\dnplayer.exe', type=str)
        simulator_ip_address = settings.value('模拟器ip地址', '127.0.0.1:5037/emulator-5554', type=str)
        option_time = settings.value('开启定时', 1, type=bool)
        option_pet_Unlock = settings.value("增益已解锁", 1, type=bool)
        option1 = settings.value('联盟互助', 0, type=bool)
        option2 = settings.value('世界野怪', 0, type=bool)
        option3 = settings.value('冰原巨兽', 0, type=bool)
        option4 = settings.value('活动雪怪', 0, type=bool)
        option5 = settings.value('训练士兵', 0, type=bool)
        option6 = settings.value('建筑升级', 0, type=bool)
        option7 = settings.value("采集资源", 0, type=bool)
        option8 = settings.value('巨熊活动', 0, type=bool)
        option9 = settings.value('治疗士兵', 0, type=bool)
        option10 = settings.value('探险奖励', 0, type=bool)
        option11 = settings.value('联盟捐赠', 0, type=bool)
        option12 = settings.value('英雄招募', 0, type=bool)
        option13 = settings.value('攻击检测', 0, type=bool)
        option14 = settings.value('邮件领取', 0, type=bool)
        option15 = settings.value('联盟宝箱', 0, type=bool)
        option16 = settings.value('仓库补给', 0, type=bool)
        option17 = settings.value('情报灯塔', 0, type=bool)
        option18 = settings.value('炼金实验室', 0, type=bool)
        option19 = settings.value('每日任务', 0, type=bool)
        option20 = settings.value('生命之树', 0, type=bool)
        option21 = settings.value('晨曦回礼', 0, type=bool)
        # 2.3.0版本取消单项功能区
        # option = settings.value('单选选择', 1, type=int)
        # self.comboBox.setCurrentIndex(simulator_settings)
        # 2.3.0版本取消单项功能区
        # self.radioButton_group.button(option).setChecked(True)
        self.lineEdit_address.setText(simulator_address)
        self.lineEdit_ip_address.setText(simulator_ip_address)
        self.select_time.setChecked(option_time)
        self.checkBox_pet_Unlock.setChecked(option_pet_Unlock)
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
        self.checkBox_alchemical_Laboratory.setChecked(option18)
        self.checkBox_collision.setChecked(option13)
        self.checkBox_mail.setChecked(option14)
        self.checkBox_Treasure_Chest.setChecked(option15)
        self.checkBox_warehouse.setChecked(option16)
        self.checkBox_intelligence.setChecked(option17)
        self.checkBox_daily_task.setChecked(option19)
        self.checkBox_tree_of_life.setChecked(option20)
        self.checkBox_morning_light_returns_gift.setChecked(option21)
        self.read_ty_setting()

    def read_ty_setting(self):  # 读取通用设置
        # global settings
        option_Random_time = settings.value("随机时间", 1, type=bool)
        option_jinshen = settings.value('优先晋升', 1, type=bool)
        option_maxed_barracks = settings.value('满级兵营', 0, type=bool)
        option_WM = settings.value('冰原巨兽等级设置', 7, type=str)
        option_lv = settings.value('采集资源等级设置', 7, type=str)
        option_XG_lv = settings.value('世界野怪等级设置', 20, type=str)
        option_ty_un = settings.value('采集英雄', 1, type=bool)
        option_ty_sim = settings.value('单兵集结', 0, type=bool)
        option_ty_WM_average = settings.value('冰原巨兽平均兵力', 0, type=bool)
        option_ty_XG_average = settings.value('世界野怪平均兵力', 0, type=bool)
        option_cycle_time = settings.value('循环时间设置', 10, type=str)
        option_intelligence_version = settings.value('火晶版本', 1, type=bool)
        option_intelligence_number = settings.value('十次情报', 0, type=bool)
        option_intelligence_offer_a_reward = settings.value('悬赏情报', 0, type=bool)
        option_intelligence_high_quality = settings.value('金紫品质', 0, type=bool)
        option_physical_strength = settings.value('仓库体力', 1, type=bool)
        option_bear_queue = settings.value('巨熊队列', 0, type=bool)
        option_bear_time = settings.value('巨熊执行时间设置', "21", type=str)
        self.lineEdit_cycle_time.setText(option_cycle_time)
        settings.setValue('冰原巨兽等级设置更新', 1)
        settings.setValue('肉采集等级设置更新', 1)
        settings.setValue('木头采集等级设置更新', 1)
        settings.setValue('煤矿采集等级设置更新', 1)
        settings.setValue('铁矿采集等级设置更新', 1)
        settings.setValue('世界野怪等级设置更新', 1)
        settings.setValue('十次情报状态', 0)
        settings.setValue('炼金实验室初始化', 0)
        self.checkBox_Random_time.setChecked(option_Random_time)
        self.checkBox_jinshen.setChecked(option_jinshen)
        self.checkBox_maxed_barracks.setChecked(option_maxed_barracks)
        self.lineEdit_Collection.setText(option_lv)
        self.lineEdit_WM.setText(option_WM)
        self.lineEdit_XG.setText(option_XG_lv)
        self.checkBox_Collection_hero.setChecked(option_ty_un)
        self.checkBox_WM_simple.setChecked(option_ty_sim)
        self.checkBox_WM_average.setChecked(option_ty_WM_average)
        self.checkBox_XG_average.setChecked(option_ty_XG_average)
        self.checkBox_intelligence_version.setChecked(option_intelligence_version)
        self.checkBox_intelligence_number.setChecked(option_intelligence_number)
        self.checkBox_intelligence_offer_a_reward.setChecked(option_intelligence_offer_a_reward)
        self.checkBox_intelligence_high_quality.setChecked(option_intelligence_high_quality)
        self.checkBox_warehouse_physical_strength.setChecked(option_physical_strength)
        self.checkBox_bear_queue.setChecked(option_bear_queue)
        self.lineEdit_bear_time.setText(option_bear_time)

    def save_ty_setting(self):  # 保存通用设置
        option_WM = self.lineEdit_WM.text()
        option_lv = self.lineEdit_Collection.text()
        option_XG_lv = self.lineEdit_XG.text()
        option_bear_time = self.lineEdit_bear_time.text()
        option_cycle_time = self.lineEdit_cycle_time.text()
        option_lineEdit_address = self.lineEdit_address.text()
        option_lineEdit_ip_address = self.lineEdit_ip_address.text()
        settings.setValue('模拟器安装地址', option_lineEdit_address)
        settings.setValue('模拟器ip地址', option_lineEdit_ip_address)
        settings.setValue('随机时间', self.checkBox_Random_time.isChecked())
        settings.setValue('世界野怪平均兵力', self.checkBox_XG_average.isChecked())
        settings.setValue('世界野怪等级设置', option_XG_lv)
        settings.setValue('单兵集结', self.checkBox_WM_simple.isChecked())
        settings.setValue('冰原巨兽平均兵力', self.checkBox_WM_average.isChecked())
        settings.setValue('冰原巨兽等级设置', option_WM)
        settings.setValue('优先晋升', self.checkBox_jinshen.isChecked())
        settings.setValue('满级兵营', self.checkBox_maxed_barracks.isChecked())
        settings.setValue('采集英雄', self.checkBox_Collection_hero.isChecked())
        settings.setValue('采集资源等级设置', option_lv)
        settings.setValue('循环时间设置', option_cycle_time)
        settings.setValue('火晶版本', self.checkBox_intelligence_version.isChecked())
        settings.setValue('十次情报', self.checkBox_intelligence_number.isChecked())
        settings.setValue('悬赏情报', self.checkBox_intelligence_offer_a_reward.isChecked())
        settings.setValue('金紫品质', self.checkBox_intelligence_high_quality.isChecked())
        settings.setValue('仓库体力', self.checkBox_warehouse_physical_strength.isChecked())
        settings.setValue('巨熊队列', self.checkBox_bear_queue.isChecked())
        settings.setValue('巨熊执行时间设置', option_bear_time)
        print_space('通用设置成功！！！')
        self.save_settings()  # 保存功能选项

    '''@pyqtSlot()
    def save_simulator_settings(self):  # 保存模拟器设置（已弃用）
        value = self.lineEdit.text()
        index = self.comboBox.currentIndex()
        settings.setValue('下拉框', index)
        if index == 0:
            settings.setValue('模拟器地址', value)
            print('模拟器安装地址：%s' % value)
        elif index == 1:
            settings.setValue('模拟器ip', value)
            print('模拟器ip地址：%s' % value)

    @pyqtSlot(int)
    def updateLineEdit(self, index):  # 读取保存的模拟器设置
        # 获取下拉框当前选中的值
        # Bug 修复：`currentIndex` 方法不需要参数，因此删除 `index`
        currentText = self.comboBox.currentIndex()
        if currentText == 0:
            itemData_1 = settings.value('模拟器地址', r'E:\leidian\LDPlayer9\dnplayer.exe', type=str)
            self.lineEdit.setText(itemData_1)
        elif currentText == 1:
            itemData_2 = settings.value('模拟器ip', '127.0.0.1:5037/emulator-5554', type=str)
            self.lineEdit.setText(itemData_2)  # 获取当前选中项的数据  itemData = self.comboBox.itemData(index)   在输入框中显示内容  self.lineEdit.setText(itemData)'''

    '''@pyqtSlot()
    def read_simple_set(self):  # 读取单项设置  （已废弃）
        settings.setValue('单选选择', self.radioButton_group.checkedId())
        simple_index = self.radioButton_group.checkedId()
        if simple_index == 1:
            option = settings.value('联盟互助设置', 20, type=str)
            self.lineEdit_cycle_time.setText(option)
        elif simple_index == 2:
            option = settings.value('世界野怪设置', 20, type=str)
            self.lineEdit_cycle_time.setText(option)
        elif simple_index == 3:
            option = settings.value('冰原巨兽设置', 20, type=str)
            self.lineEdit_cycle_time.setText(option)
        elif simple_index == 4:
            option = settings.value('活动雪怪设置', 20, type=str)
            self.lineEdit_cycle_time.setText(option)
        elif simple_index == 5:
            option = settings.value('训练士兵设置', 20, type=str)
            self.lineEdit_cycle_time.setText(option)
        elif simple_index == 6:
            option = settings.value('建筑升级设置', 20, type=str)
            self.lineEdit_cycle_time.setText(option)
        elif simple_index == 7:
            option = settings.value('采集资源设置', 20, type=str)
            self.lineEdit_cycle_time.setText(option)
        elif simple_index == 8:
            option = settings.value('巨熊活动设置', 20, type=str)
            self.lineEdit_cycle_time.setText(option)
        elif simple_index == 9:
            option = settings.value('治疗士兵设置', 20, type=str)
            self.lineEdit_cycle_time.setText(option)
        elif simple_index == 10:
            option = settings.value('探险奖励设置', 20, type=str)
            self.lineEdit_cycle_time.setText(option)
        elif simple_index == 11:
            option = settings.value('联盟捐赠设置', 20, type=str)
            self.lineEdit_cycle_time.setText(option)
        elif simple_index == 12:
            option = settings.value('英雄招募设置', 20, type=str)
            self.lineEdit_cycle_time.setText(option)
        elif simple_index == 13:
            option = settings.value('攻击检测设置', 20, type=str)
            self.lineEdit_cycle_time.setText(option)
        elif simple_index == 14:
            option = settings.value('邮件领取设置', 20, type=str)
            self.lineEdit_cycle_time.setText(option)
        elif simple_index == 15:
            option = settings.value('联盟宝箱设置', 20, type=str)
            self.lineEdit_cycle_time.setText(option)

    @pyqtSlot()
    def save_simple_set(self):  # 保存单项时间设置  （已废弃）
        simple_set_time_value = self.lineEdit_cycle_time.text()
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
        self.read_simple_set()'''

    @pyqtSlot()
    def save_settings(self):  # 保存功能选项设置
        # settings.setValue('下拉框', self.comboBox.index())
        settings.setValue('开启定时', self.select_time.isChecked())
        settings.setValue('增益已解锁', self.checkBox_pet_Unlock.isChecked())
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
        settings.setValue('炼金实验室', self.checkBox_alchemical_Laboratory.isChecked())
        settings.setValue('攻击检测', self.checkBox_collision.isChecked())
        settings.setValue('邮件领取', self.checkBox_mail.isChecked())
        settings.setValue('联盟宝箱', self.checkBox_Treasure_Chest.isChecked())
        settings.setValue('仓库补给', self.checkBox_warehouse.isChecked())
        settings.setValue('情报灯塔', self.checkBox_intelligence.isChecked())
        settings.setValue('每日任务', self.checkBox_daily_task.isChecked())
        settings.setValue('生命之树', self.checkBox_tree_of_life.isChecked())
        settings.setValue('晨曦回礼', self.checkBox_morning_light_returns_gift.isChecked())

    @pyqtSlot()
    def select_start_button(self):  # 多选开始按钮
        self.save_settings()  # type: ignore
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

    '''def simple_start_button(self):  # 单选开始按钮（已废弃）
        settings.setValue('单选选择', self.radioButton_group.checkedId())
        self.simple_stop.show()  # type: ignore
        self.simple_start.hide()  # type: ignore
        print("程序开始执行...")
        stop_event.clear()
        threading.Thread(target=lambda: simple_select(self)).start()'''

    '''@pyqtSlot()
    def simple_stop_button(self):  # 单选停止程序  （已废弃）
        self.simple_start.show()
        self.simple_stop.hide()'''

    @pyqtSlot()
    def open_noticeable(self):  # 打开公告
        self.notice.show()
        self.notice.textEdit.moveCursor(QtGui.QTextCursor.End)  # 确保窗口打开后处于最底部

    @pyqtSlot()
    def open_helpline(self):  # 打开帮助
        self.help.show()

    @pyqtSlot()
    def hide_ui(self):  # 隐藏界面
        self.frame_task.setVisible(False)
        self.frame.setVisible(False)
        # self.frame_2.setVisible(False)
        # self.frame_3.setVisible(False)
        # self.frame_4.setVisible(False)
        self.frame_out.setVisible(False)
        self.hide_UI.setVisible(False)
        self.show_UI.setVisible(True)
        self.textEdit.setVisible(False)

    @pyqtSlot()
    def show_ui(self):  # 显示界面
        self.frame_task.setVisible(True)
        self.frame.setVisible(True)
        # self.frame_2.setVisible(True)
        # self.frame_3.setVisible(True)
        # self.frame_4.setVisible(True)
        self.frame_out.setVisible(True)
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
        # self.checkBox_build.setChecked(True)
        self.checkBox_Collection.setChecked(True)
        self.checkBox_bear.setChecked(True)
        self.checkBox_treatment.setChecked(True)
        self.checkBox_adventure.setChecked(True)
        self.checkBox_donate.setChecked(True)
        self.checkBox_recruit.setChecked(True)
        self.checkBox_alchemical_Laboratory.setChecked(True)
        self.checkBox_collision.setChecked(True)
        self.checkBox_mail.setChecked(True)
        self.checkBox_Treasure_Chest.setChecked(True)
        self.checkBox_warehouse.setChecked(True)
        self.checkBox_intelligence.setChecked(True)
        self.checkBox_daily_task.setChecked(True)
        self.checkBox_tree_of_life.setChecked(True)
        self.checkBox_morning_light_returns_gift.setChecked(True)
        self.save_settings()  # type: ignore

    @pyqtSlot()  # 取消全选
    def untoggle_checkbox(self):
        self.checkBox_help.setChecked(False)
        self.checkBox_XG.setChecked(False)
        self.checkBox_WM.setChecked(False)
        self.checkBox_npc.setChecked(False)
        self.checkBox_Production.setChecked(False)
        # self.checkBox_build.setChecked(False)
        self.checkBox_Collection.setChecked(False)
        self.checkBox_bear.setChecked(False)
        self.checkBox_treatment.setChecked(False)
        self.checkBox_adventure.setChecked(False)
        self.checkBox_donate.setChecked(False)
        self.checkBox_recruit.setChecked(False)
        self.checkBox_alchemical_Laboratory.setChecked(False)
        self.checkBox_collision.setChecked(False)
        self.checkBox_mail.setChecked(False)
        self.checkBox_Treasure_Chest.setChecked(False)
        self.checkBox_warehouse.setChecked(False)
        self.checkBox_intelligence.setChecked(False)
        self.checkBox_daily_task.setChecked(False)
        self.checkBox_tree_of_life.setChecked(False)
        self.checkBox_morning_light_returns_gift.setChecked(False)
        self.save_settings()  # type: ignore

    #@pyqtSlot()
    def write(self, text):
        # 将text写入textEdit
        # self.textEdit_out.insertPlainText(text)
        self.textSignal.emit(text)  # type: ignore #self.textEdit_out.moveCursor(self.textEdit_out.textCursor().End)  # 移动光标到文本末尾  # 当写入时触发信号

    def init_tray(self):
        """初始化系统托盘组件"""
        # 加载图标（推荐使用ICO格式）
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("icon/log.png"))  # 准备一个Win11风格的ico文件

        # 创建上下文菜单（适配Win11圆角风格）
        self.tray_menu = QMenu()
        '''self.tray_menu.setStyleSheet("""
            QMenu {
                background-color: #f3f3f3;
                border-radius: 6px;
                padding: 8px;
                border: 1px solid #e0e0e0;
            }
            QMenu::item {
                padding: 8px 24px 8px 16px;
                color: #202020;
            }
            QMenu::item:selected {
                background-color: #e8f0fe;
                border-radius: 4px;
                color: #1967d2;
            }
        """)'''

        # 菜单项
        show_action = QAction("显示主窗口", self)
        exit_action = QAction("退出程序", self)

        # 连接信号
        show_action.triggered.connect(self.show_normal)
        exit_action.triggered.connect(self.clean_exit)

        # 构建菜单
        self.tray_menu.addAction(show_action)
        self.tray_menu.addSeparator()
        self.tray_menu.addAction(exit_action)

        # 设置托盘属性
        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.activated.connect(self.tray_activated)
        self.tray_icon.show()

    def tray_activated(self, reason):
        """处理托盘交互（适配Win11点击行为）"""
        if reason == QSystemTrayIcon.DoubleClick:
            self.show_normal()
        elif reason == QSystemTrayIcon.Trigger:
            pass  # Win11单击通常不处理，保持与系统一致

    def show_normal(self):
        """Win11风格窗口显示"""
        if self.isMinimized():
            self.showNormal()
        self.show()
        self.activateWindow()
        self.raise_()

    def clean_exit(self):
        """安全退出"""
        # 当窗口关闭时调用
        global close_number
        close_number = 0  # 通知发送信息函数程序已停止，终止发送连接请求
        # event.accept()
        # thread1.join()  # 等待线程结束
        stop_event.set()  # 通知所有线程停止
        self.tray_icon.hide()
        self.close()
        QApplication.quit()

    '''def closeEvent(event):
        # 当窗口关闭时调用
        global close_number, thread1
        close_number = 0  # 通知发送信息函数程序已停止，终止发送连接请求
        # event.accept()
        thread1.join()  # 等待线程结束
        stop_event.set()  # 通知所有线程停止'''

    def closeEvent(self, event):
        """Win11关闭处理（最小化到托盘）"""
        event.ignore()
        self.hide()
        # Win11风格通知
        self.tray_icon.showMessage("后台运行中", "程序仍在系统托盘继续运行", QSystemTrayIcon.Information, 2000)


# 确保基类正确，这里使用了正确的基类
class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)
        self.setupUi(self)
        self.load_settings()  # type: ignore # 读取所有设置
        self.session = requests.Session()  # 使用会话保持连接
        # 2.3.0版本取消单项功能区
        # self.read_simple_set()  # 读取单项设置
        # self.read_ty_setting()  # 读取通用设置  #self.updateLineEdit()  # 读取模拟器设置  # 重定向print函数到text_edit  #sys.stdout = RedirectText(self.textEdit_out)  #sys.stderr = RedirectText(self.textEdit_out)


if __name__ == '__main__':
    client = ClientManager(network_address)
    client1 = ClientManager(network_address1)
    if client.register():
        print("注册成功")
        version = client.check_version()[1]
        if version:
            print(f"服务器版本: {version}")
    elif client1.register():
        print("注册成功")
        version = client1.check_version()[1]
        if version:
            print(f"服务器版本: {version}")
    # 解决不同电脑不同缩放比例问题
    QGuiApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)  # type: ignore
    app = QApplication(sys.argv)
    # app.setQuitOnLastWindowClosed(False)   # 重要：避免关闭最后一个窗口退出程序
    mainWindow = MyApp()
    # 重定向stdout和stderr
    # sys.stdout = mainWindow
    # sys.stderr = mainWindow
    mainWindow.show()
    mainWindow.open_noticeable()
    sys.exit(app.exec_())
