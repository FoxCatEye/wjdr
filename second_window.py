from Window_UI import QtCore, QtGui, QtWidgets, QMainWindow
from PyQt5.QtWidgets import QApplication, QTextEdit
from PyQt5.QtCore import QTimer

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
                                                         "<p style=\" margin-bottom:0px;\">V2.3.0</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.UI调整：</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">        ①去除单项功能</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">        ②多选功能区和通用功能区合并</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    2.优化训练单种完成后返回逻辑</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    3.添加仓库补给领取功能</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    4.修复冰原巨兽，采集资源选项报错</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    5.更新治疗功能</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    6.更新版本日志</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    7.更新使用说明</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    8.优化循环逻辑</p>\n"
                                                         "<p style=\" margin-bottom:0px;\">V2.3.1</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.bug修复：循环时间等待中停止不生效</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    2.bug修复：体力概率未领取</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    3.bug修复：隐藏UI崩溃问题</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    4.优化：野怪，联盟宝箱，仓库执行时间优化（重复）</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    5.优化：仓库未检查到时未关闭左侧弹窗</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    6.优化：主页检查逻辑</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    7.优化：英雄招募检查逻辑</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    8.优化：仓库补给\n检查逻辑</p>\n"
                                                         "<p style=\" margin-bottom:0px;\">V2.3.2</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.修复：将驻防识别成攻击</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    2.bug修复：单项停止后再次开始任务未执行并提示结束的bug</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    3.尝试修复招募消耗钻石bug</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    4.修复更新后导致的采集英雄失效问题</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    5.修复设置等级等参数后执行失败问题</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    6.新增情报:高品质，十次情报</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    7.优化：体力补给晚上领取时间检查优化及自定义领取</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    8.优化：兵营空闲中状态识别优化</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    9.优化：循环时间等待</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    10.优化：互助点击</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    11.优化：巨熊新增队列选项</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    12.代码优化：主体代码优化</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    13.优化：建筑升级（补充资源未完善）</p>\n"
                                                         "<p style=\" margin-bottom:0px;\">V2.3.3</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.bug修复：巨兽单兵集结输入数量失效（更新后新增增益导致坐标失效）</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    2.优化：攻击检测频率优化（更多检测）</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    3.增加系统托盘（可隐藏程序窗口）</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    4.巨熊任务时间自定义</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    5.优化情报奖励领取逻辑及修复输出代码问题</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    6.修复十次情报跨天未重置</p>\n"
                                                         "<p style=\" margin-bottom:0px;\">V2.3.4</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.bug修复：十次情报跨天未重置</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    2.bug修复：部分用户巨兽-单兵集结，采集-采集英雄功能失效</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    3.bug修复：尝试修复情报出征失败</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    4.优化：配置文件汉化</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    5.新增：重启游戏功能</p>\n"
                                                         "<p style=\" margin-bottom:0px;\">V2.3.5</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.bug修复：部分配置需重启脚本才生效</p>\n"
                                                         "<p style=\" margin-bottom:0px;\">V2.3.6</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.重构:服务器通信，新版本提醒</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    2.新增：炼金实验室领取功能</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    3.新增：每日任务奖励领取</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    4.新增：晨曦岛回礼领取</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    5.新增：晨曦岛水晶领取</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    6.优化：巨兽-平均兵力改为队列选项</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    7.优化：攻击检测逻辑（战争增益开盾增加点击战争页签）</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    8.优化：主页检查增加颜色识别</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    9.优化：巨兽执行时间优化</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    10.优化：取消情报-金紫品质、十次情报功能、悬赏情报，增加火晶版本选项</p>\n"
                                                         "<p style=\" margin-bottom:0px;\">V2.3.7</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.bug修复-保存参数导致勾选项失效</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    2.新增-满级兵营勾选项</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    3.优化-采集队伍识别-尝试修复重复识别已采集矿种</p>\n"
                                                         "<p style=\" margin-bottom:0px;\">V2.3.8</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.优化-采集资源检查</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    2.优化-搜索野怪/矿物等逻辑</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    3.优化-模拟器地址/ip显示</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    4.优化-联盟宝箱，每日任务，生命之树，晨曦回礼定时逻辑</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    5.代码优化删除</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    6.优化-输入逻辑</p>\n"
                                                         "<p style=\" margin-bottom:0px;\">V2.3.9</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.bug修复-模拟器安装地址/IP地址修改后不生效</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    2.优化-采铁识别逻辑</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    3.优化-采集结束逻辑</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    4.新增-活动雪怪新增英雄使命选项</p>\n"
                                                         "<p style=\" margin-bottom:0px;\">V2.3.10</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.新增-采集自定义采集资源种类</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    2.优化采集：取消采集英雄选项，默认只有采集英雄出征，以识别采集英雄判断是否有队伍出征</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    3.优化训练：取消满级兵营选项，脚本识别是否满级兵营</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    4.新增-功能旁增加功能介绍</p>\n"
                                                         "<p style=\" margin-bottom:0px;\"></p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">    </p>\n"))
        self.textEdit.setReadOnly(True)  # 设置文本不可编辑状态


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
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.模拟器安装路径：电脑模拟器安装地址，以exe结尾，启动模拟器功能需要，地址错误时无法启动模拟器，只能手动启动</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    2.模拟器ip地址：连接模拟器需要，由本地地址＋端口号组成，ip错误将无法连接模拟器，影响使用</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\"> </p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">二.模拟器按钮：</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.启动模拟器：启动模拟器路径内设置的模拟器</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    2.连接模拟器：使用adb连接模拟器IP地址对应的模拟器</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    3.启动游戏：启动无尽冬日游戏</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    4.一键启动：包含启动模拟器、连接模拟器、启动游戏功能</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\"> </p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">三.其他设置：</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.开启定时：勾选后多选项功能只会在特定时间（下面介绍的时间）执行，未勾选，不会有时间判定，执行完一个功能立马执行下一个</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ①.互助：每2秒检测一次</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ②.野怪：分钟是4的倍数，秒数是10的倍数时检测一次，巨熊功能开启且在活动时间不检测</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ③.冰原巨兽：分钟是6的倍数且秒数在0-20s时检查一次，巨熊功能开启且在活动时间不检测，等级可在单选内设置</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ④.活动雪怪：分钟是6的倍数时检测一次，巨熊功能开启且在活动时间不检测</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ⑤.训练士兵：分钟数是5的倍数时检测</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ⑥.建筑升级（已删除）：分钟个位数是2时检测</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ⑦.采集资源：分钟个位数为3时检测每一种资源是否有采集，每种只会采集一队</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ⑧.巨熊活动：21点时检测</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ⑨.治疗士兵：分钟个位数为5时检测，相当于每过一小时就检查</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ⑩.探险奖励：分钟数为14时检测，每小时分钟数为14，28,42，56检查</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ⑩①.联盟捐赠：分钟数为1时检测，相当于每过一小时就检查</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ⑩②.英雄招募：凌晨1点时分钟数为5的倍数时会检查是否有免费次数</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ⑩③.攻击检测：开启后轮到就检测，检测城堡和撞矿攻击</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ⑩④.邮件领取：分钟数为30时领取邮件内联盟，系统，报告的奖励（5次领取）</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ⑩⑤.联盟宝箱：分钟数为49分且秒数是20的倍数时就检测联盟宝箱内的战利品宝箱和盟友赠礼是否有一键领取（5次）</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ⑩⑥.仓库补给：分钟数是5的倍数时检测，体力检测会在首次启动或体力刷新时间内进行</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ⑩⑦.情报灯塔：12点或19点时进行</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ⑩⑧.炼金实验室：首次启动或凌晨1时及23时分钟数为12的倍数时检查（4次）</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ⑩⑧.每日任务：首次启动或凌晨23时，早上8时检查</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ⑩⑧.生命之树：首次启动或凌晨23时，早上8时检查</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ⑩⑧.晨曦回礼：首次启动或凌晨23时，早上8时检查</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    2.循环间隔：关闭定时时使用，当前列表内任务完成一次循环，下一次循环开始的间隔时间</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    3.增益已解锁：如果巨兽/采集出征界面有显示增益一项，需要勾选该选项，否则部分功能选项（出征）会受到影响，未显示增益一项不需要勾选，否则部分功能选项会受到影响</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">四.功能介绍：</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    1.联盟互助：</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ①.随机时间：识别到互助按钮后随机时间点击（防系统检测）</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    2.世界野怪：</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ①.平均兵力：设置全局集结冰原巨兽时平均兵力出征</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ②.等级设置：设置全局攻击世界野怪的等级</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    3.冰原巨兽：</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ①.单兵集结：集结巨兽时只上一个兵（英雄正常上）</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ②.巨兽队列：选择预设好的第二序列的队伍</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ③.等级设置：设置全局集结冰原巨兽的等级</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    4.训练士兵：</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ①.优先晋升：训练士兵时，有低级兵优先晋升低级兵</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ②.满级兵营：兵营没有升级按钮时，需要勾选此选项才能正常执行训练任务</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    5.资源采集：</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ①.采集英雄：采集队伍出发时只带第一个英雄</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ②.等级设置：设置全局采集资源的等级</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    6.情报灯塔：</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ①.火晶版本：未勾选，识别30级前的情报图案，勾选后，识别火晶版本的情报图案</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    7.巨熊活动：</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ①.巨熊队列：选择预设好的第一序列的队伍</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ①.时间/时：自定义巨熊活动时间，24小时制</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    8.仓库补给：</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ②.仓库体力：检查是否有体力可领取</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    9.活动雪怪：</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">        ②.英雄使命：吉娜版本已过，道具为散落的零件时勾选该选项</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\"> </p></body></html>"))
        self.textEdit.setReadOnly(True)


# "<p style=\" margin-top:0px; margin-bottom:0px;\">        ②.十次情报：每天只执行10次情报</p>\n"
# "<p style=\" margin-top:0px; margin-bottom:0px;\">        ③.悬赏情报：执行悬赏任务</p>\n"
class helplog(QMainWindow, Ui_helpWindow):
    def __init__(self, parent=None):
        super(helplog, self).__init__(parent)
        self.setupUi(self)
