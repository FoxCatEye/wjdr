from Window_UI import QtCore, QtGui, QtWidgets, QMainWindow



'''-------------------------------------更新公告-----------------------------------------------'''

class Ui_NoticeWindow(object):
    def setupUi(self, noticewindow):
        noticewindow.setObjectName("helpWindow")
        noticewindow.resize(371, 262)
        noticewindow.setFixedSize(noticewindow.width(), noticewindow.height())  # 设置窗口大小固定
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/log.png"))
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
                                                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px;\">版本日志</p>"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">V2.0.0</p>\n"
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
                                                         "<p style=\" margin-bottom:0px;\">V2.0.5（2.1.0-2.1.1）</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.修复设置冰原巨兽、采集等级后，设置未立即生效</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    2.修复日志输出空白行问题</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    3.修复配置文件无法找到</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    4.新增采集队自由选择是否带英雄（带默认英雄）</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    5.新增巨兽单兵集结功能</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    6.训练逻辑优化：完成一个兵种训练后回到下一个兵种检查界面</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    7.训练检查本页时一直卡在检查</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    8.攻击检测优化（优化多个攻击时无法检测）</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    9.优化英雄招募招募到英雄后返回逻辑</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    10.修复单项训练检查非等待时间停止失败问题</p>\n"
                                                         "<p style=\" margin-bottom:0px;\">V2.2.0</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.训练升级晋升士兵变为勾选项</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    2.训练升级逻辑优化</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    3.调整采集无英雄功能为采集英雄功能</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    4.巨兽平均兵力出征</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    5.领取邮件（联盟，系统，报告邮件）</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    6.联盟宝箱领取</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    7.野怪等级设置</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    8.野怪平均兵力出征</p>\n"
                                                         "<p style=\" margin-bottom:0px;\">V2.2.1</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.修复采集出征时报错导致无法出征</p>\n"
                                                         "<p style=\" margin-bottom:0px;\">V2.2.2</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.优化：捐献无次数时返回到主页</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    2.优化：互助随机等待时间改为配置项及使用说明更新</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    3.优化：攻击检测使用帮助更新</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    4.优化：调整红色提示字体大小</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    5.新版本提醒功能</p>\n"
                                                         "<p style=\" margin-bottom:0px;\">V2.2.3</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.修复主页检查报错</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    2.优化：捐献结束返回主页逻辑</p>\n"
                                                         "<p style=\" margin-bottom:0px;\">V2.2.4</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.新版本提醒优化：增加连接不上服务器判断</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    2.主页检查优化：注释测试代码及取消主页检查时停止判断（无用）</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    3.基础功能优化：程序关闭时终止线程信号</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    4.训练优化：检查前回到城镇</p>\n"
                                                         "<p style=\" margin-bottom:0px;\">V2.2.5</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.优化版本提醒：服务器本地未开启时，不会有新版本提醒</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    2.修复联盟宝箱-盟友赠礼报错</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    3.优化联盟捐赠：时间修改为2小时检查一次</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    4.优化：补充未检测到图案时打印提示</p>\n"
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
        helpwindow.resize(400, 300)
        helpwindow.setFixedSize(helpwindow.width(), helpwindow.height())  # 设置窗口大小固定
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/log.png"))
        helpwindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(helpwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 400, 300))
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
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">一.模拟器设置：</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.模拟器路径：电脑模拟器安装地址，以exe结尾，启动模拟器功能需要，地址错误时无法启动模拟器，只能手动启动</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    2.模拟器ip：连接模拟器需要，由本地地址＋端口号组成，ip错误将无法连接模拟器，影响使用</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\"> </p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">二.模拟器按钮：</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.启动模拟器：启动模拟器路径内设置的模拟器</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    2.连接模拟器：使用adb连接模拟器IP地址对应的模拟器</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    3.启动游戏：启动无尽冬日游戏</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    4.一键启动：包含启动模拟器、连接模拟器、启动游戏功能</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\"> </p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">三.多选：</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    介绍：可一次性选择多选功能同时执行</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.固定时间：勾选后多选项功能只会在特定时间（下面介绍的时间）执行，未勾选，不会有时间判定，执行完一个功能立马执行下一个</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    2.互助：每2秒检测一次</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    3.野怪：分钟与秒是5的倍数是检测一次，21点不检测</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    4.冰原巨兽：分钟是6的倍数且秒数在0-20s时检查一次，21点不检测，等级可在单选内设置</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    5.活动雪怪：分钟是6的倍数时检测一次，21点不检测</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    6.训练士兵：分钟数是5的倍数时检测</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    7.建筑升级：分钟个位数是2时检测</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    8.采集资源：分钟个位数为3时检测每一种资源是否有采集，每种只会采集一队</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    9.巨熊活动：21点时检测</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    10.治疗士兵：分钟个位数为5时检测，相当于每过一小时就检查</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    11.探险奖励：分钟数为25时检测，相当于每过一小时就检查</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    12.联盟捐赠：分钟数为1时检测，相当于每过一小时就检查</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    13.英雄招募：凌晨1点时分钟数为5的倍数时会检查是否有免费次数</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    14.攻击检测：开启后轮到就检测，检测城堡和撞矿攻击</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    14.邮件领取：分钟数为30时领取邮件内联盟，系统，报告的奖励（5次领取）</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    14.联盟宝箱：分钟数为50时就检测联盟宝箱内的战利品宝箱和盟友赠礼是否有一键领取（5次）</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\"> </p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">四.通用：</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    介绍：通用设置内的设置同时适用于单项和多选</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.联盟互助：</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ①.随机时间：识别到互助按钮后随机时间点击（防系统检测）</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    2.资源采集：</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ①.采集英雄：采集队伍出发时只带第一个英雄</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ②.等级设置：设置全局采集资源的等级</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    3.冰原巨兽：</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ①.单兵集结：集结巨兽时只上一个兵（英雄正常上）</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ②.平均兵力：设置全局集结冰原巨兽时平均兵力出征</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ③.等级设置：设置全局集结冰原巨兽的等级</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    4.训练士兵：</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ①.优先晋升：训练士兵时，有低级兵优先晋升低级兵</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    5.世界野怪：</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ①.平均兵力：设置全局集结冰原巨兽时平均兵力出征</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ②.等级设置：设置全局攻击世界野怪的等级</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\"> </p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">五.单选：</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    每次只能执行单个功能，可设置单个功能执行完成后下一次执行的间隔时间</p></body></html>"))
        self.textEdit.setReadOnly(True)


class helplog(QMainWindow, Ui_helpWindow):
    def __init__(self, parent=None):
        super(helplog, self).__init__(parent)
        self.setupUi(self)