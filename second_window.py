from Window_UI import QtCore, QtGui, QtWidgets, QMainWindow



'''-------------------------------------更新公告-----------------------------------------------'''

class Ui_NoticeWindow(object):
    def setupUi(self, noticewindow):
        noticewindow.setObjectName("helpWindow")
        noticewindow.resize(371, 262)
        noticewindow.setFixedSize(noticewindow.width(), noticewindow.height())  # 设置窗口大小固定
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("log.png"))
        noticewindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(noticewindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 371, 262))
        self.textEdit.setObjectName("textEdit")
        noticewindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(noticewindow)
        QtCore.QMetaObject.connectSlotsByName(noticewindow)

    def retranslateUi(self, NoticeWindow):
        _translate = QtCore.QCoreApplication.translate
        NoticeWindow.setWindowTitle(_translate("NoticeWindow", "版本日志"))
        self.textEdit.setHtml(_translate("NoticeWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                         "p, li { white-space: pre-wrap; }\n"
                                                         "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; "
                                                         "font-weight:400; font-style:normal;\">\n"
                                                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px;\">版本日志</p>\n"
                                                         "<p style=\" margin-bottom:0px;\">V2.0.0</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.UI界面重构</p>\n"
                                                         "<p style=\" margin-bottom:0px;\">V2.0.1</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.修复模拟器设置保存导致崩溃问题</p>\n"
                                                         "<p style=\" margin-bottom:0px;\">V2.0.2</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.更新帮助文档</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    2.修复冰原巨兽等级设置失败bug</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    3.修复采集资源等级设置失败bug</p>\n"
                                                         "<p style=\" margin-bottom:0px;\">V2.0.3</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.增加不同显示缩放适配</p>\n"
                                                         "<p style=\" margin-bottom:0px;\">V2.0.4</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.单项非等待时间停止不生效bug</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    2.尝试修复只训练6级兵bug</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    3.优化：训练增加识别当前界面可晋升士兵逻辑</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    4.优化：采集部队不派遣英雄</p>\n"
                                                         "<p style=\" margin-bottom:0px;\"></p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    </p>\n"
                                                         ))
        self.textEdit.setReadOnly(True)


class noticelog(QMainWindow, Ui_NoticeWindow):
    def __init__(self, parent=None):
        super(noticelog, self).__init__(parent)
        self.setupUi(self)


'''-------------------------------------帮助说明-----------------------------------------------'''


class Ui_helpWindow(object):
    def setupUi(self, helpwindow):
        helpwindow.setObjectName("helpWindow")
        helpwindow.resize(371, 262)
        helpwindow.setFixedSize(helpwindow.width(), helpwindow.height())  # 设置窗口大小固定
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("log.png"))
        helpwindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(helpwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 371, 262))
        self.textEdit.setObjectName("textEdit")
        helpwindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(helpwindow)
        QtCore.QMetaObject.connectSlotsByName(helpwindow)

    def retranslateUi(self, helpWindow):
        _translate = QtCore.QCoreApplication.translate
        helpWindow.setWindowTitle(_translate("helpWindow", "帮助文档"))
        self.textEdit.setHtml(_translate("helpWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">模拟器路径：</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    电脑模拟器安装地址，以exe结尾，启动模拟器功能需要，地址错误时无法启动模拟器，只能手动启动</p>\n\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">模拟器ip：</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    连接模拟器需要，由本地地址＋端口号组成，ip错误将无法连接模拟器，影响使用</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">启动游戏：</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    启动无尽冬日游戏</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">一键启动：</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    包含启动模拟器、连接模拟器、启动游戏功能</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">多选：可一次性选择多选功能同时执行</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    固定时间：勾选后多选项功能只会在特定时间执行，未勾选，不会有时间判定，执行完一个功能立马执行下一个</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    互助：每2秒检测一次</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    野怪：分钟与秒是5的倍数是检测一次，21点不检测</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    冰原巨兽：分钟是6的倍数且秒数在0-20s时检查一次，21点不检测，等级可在单选内设置</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    活动雪怪：分钟是6的倍数时检测一次，21点不检测</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    训练士兵：分钟数是5的倍数时检测</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    建筑升级：分钟数是2的倍数时检测</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    采集资源：凌晨3点检测每一种资源是否有采集，每种只会采集一队</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    巨熊活动：21点时检测</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    治疗士兵：分钟数为21时检测，相当于每过一小时就检查</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    探险奖励：分钟数为25时检测，相当于每过一小时就检查</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    联盟捐赠：分钟数为1时检测，相当于每过一小时就检查</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    英雄招募：凌晨1点时分钟数为5的倍数时会检查</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">单选：</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    每次只能执行单个功能，可设置单个功能执行间隔，冰原巨兽可设置等级，设置的等级多选可用</p></body></html>"))
        self.textEdit.setReadOnly(True)


class helplog(QMainWindow, Ui_helpWindow):
    def __init__(self, parent=None):
        super(helplog, self).__init__(parent)
        self.setupUi(self)