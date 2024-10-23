import logging
from PyQt5 import QtCore, QtGui, QtWidgets
import threading
import time
from datetime import datetime
import subprocess
import os
import sys
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from configparser import ConfigParser
from PyQt5.QtCore import QTimer
from airtest.core.api import *
from airtest.core.android.android import *

logging.getLogger('airtest').setLevel(logging.ERROR)
'''模拟器点击变量'''
emulator_click = 0
number_brush = 0

# 获取当前文件的绝对路径(本地）
current_file_path = os.path.abspath(__file__)

# 获取当前文件夹的上一级目录的绝对路径(本地）
#parent_directory_path = os.path.dirname(os.path.dirname(current_file_path))
# 上一级文件夹中要删除的文件名
file_to_delete = 'jiaoben-1.2.1.exe'

# 构建要删除的文件的绝对路径(本地）
#file_path_to_delete = os.path.join(current_file_path, file_to_delete)

# 删除文件
#os.remove(file_path_to_delete)
if os.path.isfile(file_to_delete):
    # 删除文件
    time.sleep(2)
    os.remove(file_to_delete)
    print(f"文件 已被删除。")
else:
    print(f"文件 不存在。")

# 假设配置文件为config.ini，且其中的选项在[Options]部分
import configparser

config = configparser.ConfigParser()
config.read('set.ini')
# 假设需要读取的选项变量名为'my_option'
option_help = config.get('Options', '联盟互助')
option_XG = config.get('Options', '世界野怪')
option_WM = config.get('Options', '冰原巨兽')
option_npc = config.get('Options', '活动雪怪')
option_Production = config.get('Options', '训练士兵')
option_build = config.get('Options', '建筑升级')
option_Collection = config.get('Options', '采集资源')
option_bear = config.get('Options', '巨熊活动')
option_treatment = config.get('Options', '治疗士兵')
option_adventure = config.get('Options', '探险奖励')
option_donate = config.get('Options', '联盟捐赠')
option_recruit = config.get('Options', '英雄招募')


#重写打印
def print_space(variable, spaces=4):
    print(' ' * spaces + str(variable))


'''打开模拟器'''


def start_exe():
    while True:
        try:
            print('开始启动雷电模拟器')
            subprocess.Popen('E:\leidian\LDPlayer9\dnplayer.exe')
            #subprocess.Popen('%s' % set_address.get())
            print('启动成功')
            break
        except:
            print_space('未找到模拟器，5s后重新尝试启动')
            time.sleep(5)


# 连接模拟器
def cnnect():
    global emulator_click
    emulator_click = 1
    a = 1
    while a > 0:  # 连接模拟器
        try:
            print('%d.开始尝试连接模拟器' % a)
            os.popen('adb start-server')
            #print('地址：android:// %s' % str(set_ip.get()))
            print('地址：android://127.0.0.1:5037')
            #connect_device('android://%s'%set_ip.get())
            connect_device('android://127.0.0.1:5037')
            #subprocess.run(['adb', '-s', '127.0.0.1:21503', 'shell'])
            time.sleep(5)
            print('连接模拟器成功!!!')
            a = 0
        except:
            a += 1
            print('未连接到模拟器，5s后尝试重新连接')
            time.sleep(5)


# 启动APP
def start_app():
    global emulator_click
    if emulator_click == 0:
        print('未连接模拟器')
        time.sleep(1)
        cnnect()
    while True:
        try:
            print_space('开始尝试启动游戏')
            touch(Template(r"icon\tpl1719196072757.png", record_pos=(0.112, -0.519), resolution=(414, 780)))
            print_space("启动成功，等待30秒启动时间...")
            time.sleep(30)
            print_space('启动完成')
            break
        except:
            print('启动失败，再次尝试')
        '''else:
        print_space('游戏已启动!!!')'''


def all_start():  #一键启动
    start_exe()
    print('等待30s以完成模拟器的启动')
    time.sleep(30)
    cnnect()
    print('等待10s以确保系统加载完成')
    time.sleep(10)
    start_app()


def start_simple(button_start_id):  #模拟器启动相关
    if button_start_id == 1:
        #start_exe_button.configure(text='启动模拟器', command=lambda: start_simple(1))
        # start_exe()
        '''启动模拟器线程'''
        threading.Thread(target=start_exe).start()  # threading.Thread(target=start_exe).join()
    elif button_start_id == 2:
        '''连接模拟器线程'''
        threading.Thread(target=cnnect).start()  # threading.Thread(target=cnnect).join()
    elif button_start_id == 3:
        #start_app_button.configure(text='再次启动app', command=lambda: start_simple(3))
        # start_app()
        '''启动app线程'''
        threading.Thread(target=start_app).start()  # threading.Thread(target=start_app).join()
    elif button_start_id == 4:
        '''一键启动线程'''
        threading.Thread(target=all_start).start()
    else:
        print_space('错误')


# 主页判断
def Homepage():
    a = 1
    #try:
    while a < 4:
        if exists(Template(r"icon\tpl1719198809581.png", threshold=0.9, record_pos=(-0.398, 0.819), scale_max=800, resolution=(414, 780))):
            print_space("在主页，准备执行任务")  # 在主界面，执行任务
            return
        else:
            a += 1
            print_space("不在主页，返回上一级")
            if exists(Template(r"icon\tpl1719198082012.png", threshold=0.8, record_pos=(-0.44, -0.783), resolution=(414, 780))):
                print_space('点击返回按钮')
                touch(Template(r"icon\tpl1719198082012.png", threshold=0.8, record_pos=(-0.44, -0.783), resolution=(414, 780)))
            elif exists(Template(r'icon\return.png', threshold=0.8, record_pos=(-0.44, -0.783), resolution=(414, 780))):
                print_space('点击返回按钮')
                touch(Template(r"icon\return.png", threshold=0.8, record_pos=(-0.44, -0.783), resolution=(414, 780)))
            elif exists(Template(r"icon\tpl1719198103804.png", record_pos=(0.442, -0.35), resolution=(414, 780))):
                print_space('点击关闭按钮')
                touch(Template(r"icon\tpl1719198103804.png", record_pos=(0.442, -0.35), resolution=(414, 780)))
            else:
                print_space('点击其他区域')
                touch([500, 600])  # 不在主界面，返回到主页
        if stop_event.is_set():
            main_class = Ui_MainWindow()
            main_class.stop_button()
    '''except:
        print('执行错误')
    if a == 4:
        re_connet()'''


# 互助功能
def Help():
    result = exists(Template(r"icon\tpl1718936896202.png", record_pos=(0.248, 0.735), resolution=(449, 842)))
    if result:  # 判断是否有盟员求助
        print_space("有盟员求助，需点击援助按钮")
        touch([800, 1700])
        print_space("点击援助按钮成功，等待1s进行下一个任务")
        time.sleep(1)
    else:
        print_space("无盟员求助，等待1s进行下一个任务")
        time.sleep(1)


# 生产士兵
def train():
    time.sleep(5)  # 等待3秒
    print_space("收取已生产士兵...")
    touch([500, 950])  # 收取已生产的兵
    time.sleep(1)  # 等待1秒
    print_space("点击兵营")
    touch([500, 950])  # 点击兵营
    time.sleep(1)  # 等待1秒
    print_space("点击训练")
    touch([786, 1221])  # 点击训练按钮
    time.sleep(1)  # 等待1秒
    print_space('检查是否有可晋升士兵')
    if exists(Template(r"icon\tpl1721784527077.png", record_pos=(-0.439, 0.078), resolution=(1080, 1920))):
        print_space('点击前往可晋升士兵')
        touch(Template(r"icon\tpl1721784527077.png", record_pos=(-0.439, 0.078), resolution=(1080, 1920)))
        print_space('点击晋升图标')
        touch(Template(r"icon\tpl1721784547262.png", record_pos=(0.399, 0.019), resolution=(1080, 1920)))
        print_space('点击开始晋升士兵')
        touch(Template(r"icon\tpl1727422988298.png", record_pos=(0.216, 0.339), resolution=(1080, 1920)))
    elif exists(Template(r"icon\tpl1721784547262.png", rgb=True, record_pos=(0.399, 0.019), resolution=(1080, 1920))):
        print_space('点击晋升图标')
        touch(Template(r"icon\tpl1721784547262.png", record_pos=(0.399, 0.019), resolution=(1080, 1920)))
        print_space('点击开始晋升士兵')
        touch(Template(r"icon\tpl1727422988298.png", record_pos=(0.216, 0.339), resolution=(1080, 1920)))
    elif exists(Template(r"icon\tpl1721784547262.png", rgb=True, record_pos=(0.399, 0.019), resolution=(1080, 1920))):
        print_space('点击兵种')
        touch(Template(r"icon\tpl1721784547262.png", record_pos=(0.399, 0.019), resolution=(1080, 1920)))
        print_space('点击晋升图标')
        touch(Template(r"icon\tpl1721784547262.png", record_pos=(0.399, 0.019), resolution=(1080, 1920)))
        print_space('点击开始晋升士兵')
        touch(Template(r"icon\tpl1727422988298.png", record_pos=(0.216, 0.339), resolution=(1080, 1920)))
    else:
        print_space("没有可晋升士兵，训练最高级士兵")
        swipe([950, 1225], vector=[-0.8, 0.0170])  # 滑动训练兵种
        touch([910, 1225])  # 点击十级兵
        lv_x = 910
        lv_y = 5
        while lv_y > 0:
            if not exists(Template(r"icon\tpl17217845790633.png", rgb=True, threshold=0.8, record_pos=(0.22, 0.338), resolution=(
                    1080, 1920))):
                lv_x = lv_x - 200
                touch([lv_x, 1225])  # 点击开始上一级士兵
                lv_y -= 1
            else:
                break
        touch([800, 1800])  # 点击开始训练士兵
    time.sleep(2)  # 等待2秒
    print_space("返回上一级")
    if exists(Template(r"icon\tpl1719198082013.png", threshold=0.8, record_pos=(-0.439, -0.835), resolution=(1080, 1920))):
        touch(Template(r"icon\tpl1719198082013.png", threshold=0.8, record_pos=(-0.439, -0.835), resolution=(1080, 1920)))
    elif exists(Template(r"icon\tpl1719198103804.png", record_pos=(0.442, -0.35), resolution=(1080, 1920))):
        touch(Template(r"icon\tpl1719198103804.png", record_pos=(0.442, -0.35), resolution=(1080, 1920)))  # 关闭当前界面
    else:
        print_space('未找到对应图案')
    print_space('训练完成')


# 训练检查
def Production_soldiers():
    touch([14, 823])
    time.sleep(1)
    touch([170, 400])
    print('检查盾兵训练是否完成')
    if exists(Template(r"icon\tpl1719478488282.png", threshold=0.8, rgb=True, record_pos=(-0.189, -0.009), resolution=(1080, 1920))):
        print_space("1跳转到盾兵兵营...")
        touch([600, 840])  # 点击索引到对应兵营
        train()
    elif exists(Template(r"icon/tpl1719478488283.png", threshold=0.9, rgb=True, record_pos=(-0.066, -0.111), resolution=(1080, 1920))):
        print_space("跳转到盾兵兵营...")
        touch([600, 840])  # 点击索引到对应兵营
        train()
        time.sleep(1)  # 等待1秒
        touch([14, 823])
    print('检查矛兵训练是否完成')
    if exists(Template(r"icon\tpl1719480722195.png", threshold=0.8, rgb=True, record_pos=(-0.189, -0.009), resolution=(1080, 1920))):
        print_space("1跳转到矛兵兵营...")
        touch([600, 942])  # 点击索引到对应兵营
        train()
        time.sleep(1)  # 等待1秒
        touch([14, 823])
    elif exists(Template(r"icon/tpl1719480722196.png", threshold=0.8, rgb=True, record_pos=(-0.314, -0.01), resolution=(1080, 1920))):
        print_space("跳转到矛兵兵营...")
        touch([600, 942])  # 点击索引到对应兵营
        train()
        time.sleep(1)  # 等待1秒
        touch([14, 823])
    print('检查射手训练是否完成')
    if exists(Template(r"icon/tpl1719480732965.png", threshold=0.8, rgb=True, record_pos=(-0.192, 0.087), resolution=(1080, 1920))):
        print_space("1跳转到射手兵营...")
        touch([600, 1060])  # 点击索引到对应兵营
        train()
        time.sleep(1)  # 等待1秒
        touch([14, 823])
    elif exists(Template(r'icon\tpl1719480732966.png', threshold=0.9, rgb=True, record_pos=(-0.021, -0.003), resolution=(1080, 1920))):
        print_space("跳转到射手兵营...")
        touch([600, 1060])  # 点击索引到对应兵营
        train()
        time.sleep(1)  # 等待1秒
        touch([14, 823])
    else:
        print_space("没有兵营已完成生产，结束该任务")
        touch(Template(r"icon\tpl1719552273333.png", threshold=0.9, record_pos=(0.142, -0.126), resolution=(1080, 1920)))


# 升级资源检查
def build_main():
    touch(Template(r"icon\tpl1719651083870.png", record_pos=(0.001, 0.731), resolution=(449, 842)))
    time.sleep(1)
    if exists(Template(r"icon\tpl1719817875178.png", record_pos=(-0.002, 0.683), resolution=(1080, 1920))):
        print_space('一键补齐资源不足，回到首页')
        touch(Template(r"icon\tpl1719198103804.png", record_pos=(0.442, -0.35), resolution=(414, 780)))
        touch(Template(r"icon\tpl1719198103804.png", record_pos=(0.442, -0.35), resolution=(414, 780)))
    else:
        touch(Template(r"icon\tpl1719651144335.png", record_pos=(0.224, 0.608), resolution=(449, 842)))
        touch(Template(r"icon\tpl1719578558005.png", record_pos=(0.003, -0.045), resolution=(449, 842)))  # 点击升级
        time.sleep(1)
        touch(Template(r"icon\tpl1719579273500.png", record_pos=(0.003, -0.045), resolution=(449, 842)))


# 自动建筑升级
def Build():
    touch([14, 823])
    time.sleep(1)
    touch([170, 400])
    if exists(Template(r"icon\tpl1719643933714.png", threshold=0.95, record_pos=(-0.306, -0.318), resolution=(449, 842))):
        print_space('有空闲队列，开始建造')
        touch(Template(r"icon\tpl1719643933714.png", record_pos=(-0.306, -0.318), resolution=(449, 842)))  # 点击跳转到需升级的建筑
        if exists(Template(r"icon\tpl1719580056417.png", record_pos=(-0.362, 0.238), resolution=(449, 842))):  # 判断是什么建筑升级升级
            print_space('升级资源建筑')
            time.sleep(5)  # 等待5s
            if not exists(Template(r"icon\tpl1719644932718.png", threshold=0.9, record_pos=(0.308, 0.056), resolution=(449, 842))):
                print_space('建筑设施未达到升级要求，升级设施')
                while not exists(Template(r"icon\tpl1719645172814.png", record_pos=(0.248, -0.102), resolution=(449, 842))):
                    touch([900, 1000])
                    if exists(Template(r"icon\tpl1719645172814.png", record_pos=(0.248, -0.102), resolution=(449, 842))):
                        print_space('达到升级条件，开始升级')
            touch([900, 800])  # 点击升级按钮
            touch([800, 1800])  # 点击升级
            if exists(Template(r"icon\tpl1719651083870.png", record_pos=(0.001, 0.731), resolution=(449, 842))):  # 判断资源是否充足
                print_space("/31资源不足，点击一键补齐")
                build_main()
            else:
                time.sleep(1)
                touch(Template(r"icon\tpl1719579273500.png", record_pos=(0.003, -0.045), resolution=(449, 842)))  # 点击求助
        else:
            print_space('升级功能建筑')
            touch([553, 1333])  # 点击升级按钮
            touch(Template(r"icon\tpl1719578558005.png", record_pos=(0.003, -0.045), resolution=(449, 842)))  # 点击升级
            if exists(Template(r"icon\tpl1719651083870.png", record_pos=(0.001, 0.731), resolution=(449, 842))):  # 判断资源是否充足
                print_space('资源不足，点击一键补齐')
                build_main()
            else:
                time.sleep(1)
                touch(Template(r"icon\tpl1719579273500.png", record_pos=(0.003, -0.045), resolution=(449, 842)))  # 点击求助
    else:
        print_space("没有空闲建筑队列")
        touch(Template(r"icon\tpl1719552273333.png", threshold=0.9, record_pos=(0.142, -0.126), resolution=(1080, 1920)))


# 搜索资源
def search_main():
    if not exists(Template(r"icon\tpl1720145326019.png", record_pos=(0.404, 0.852), resolution=(1080, 1920))):
        print_space('不在世界，点击去往世界')
        touch([950, 1850])  # 点击野外
        time.sleep(5)
    print_space('点击搜索图标')
    touch([63, 1314])  # 点击搜索图标
    time.sleep(1)  # 等待1s


# 打雪怪功能
def NPC():
    print_space('打雪怪时间，开始集结雪怪')
    print_space('打开背包')
    touch([460, 1836])  # 点击打开背包
    time.sleep(1)
    if exists(Template(r"icon\tpl1719376487523.png", record_pos=(0.449, -0.78), resolution=(414, 780))):  # 判断背包是否打开成功
        touch([949, 171])  # 点击其他跳转至该页
        print_space('查看活动道具')
        if exists(Template(r"icon\tpl1719376586643.png", record_pos=(0.106, -0.476), resolution=(414, 780))):  # 判断是否有该道具
            print_space('使用活动道具')
            touch(Template(r"icon\tpl1719376586643.png", record_pos=(0.106, -0.476), resolution=(414, 780)))  # 点击道具
            touch(Template(r"icon\tpl1719376629723.png", record_pos=(0.0, 0.092), resolution=(414, 780)))  # 点击使用
            time.sleep(1)
            print_space('集结打怪')
            touch(Template(r"icon\tpl1719376765868.png", record_pos=(0.002, 0.705), resolution=(414, 780)))  # 寻找到怪物点击集结
            touch(Template(r"icon\tpl1719376776844.png", record_pos=(0.0, 0.326), resolution=(414, 780)))  # 点击发起集结
            print_space('兵力检查')
            if exists(Template(r"icon\tpl1721191349774.png", record_pos=(-0.118, 0.782), resolution=(1080, 1920))):
                touch(Template(r"icon\tpl1721191349774.png", record_pos=(-0.118, 0.782), resolution=(1080, 1920)))
                print_space('体力检查')
                if exists(Template(r"icon\tpl1719376787180.png", record_pos=(0.268, 0.824), resolution=(414, 780))):  # 判断体力是否充足
                    energy()
                else:
                    print_space("体力不足，暂停打怪")
            else:
                print_space('兵力不足，暂停打怪')
        else:
            print_space("未找到相关物品，退出任务")
            touch(Template(r"icon\tpl1719198082012.png", threshold=0.5, record_pos=(-0.44, -0.783), resolution=(
                414, 780))) or touch(Template(r"icon\tpl1719198103804.png", record_pos=(0.442, -0.35), resolution=(414, 780)))


# 野兽
def Brush_XG():
    print_space('打野怪时间，开始出征')
    search_main()
    print_space('点击选择普通野兽')
    touch([120, 1373])  # 点击普通野兽
    time.sleep(1)  # 等待1s
    '''print_space('点击等级')
    touch([651, 1573])  # 点击等级3
    time.sleep(1)  # 等待1s'''
    print_space('点击搜索按钮')
    touch([534, 1821])  # 点击搜索
    time.sleep(1)  # 等待1s
    print_space('点击攻击按钮')
    touch(Template(r"icon\tpl1721191349775.png", rgb=False, record_pos=(0.002, 0.705), resolution=(414, 780)))  # 点击出征怪物
    time.sleep(1)  # 等待1s
    if exists(Template(r"icon\tpl1721191349774.png", record_pos=(-0.118, 0.782), resolution=(1080, 1920))):  # 判断是否有兵力
        # touch(Template(r"icon\tpl1721191349774.png", record_pos=(-0.118, 0.782), resolution=(1080, 1920)))
        if exists(Template(r"icon\tpl1719376787180.png", record_pos=(0.268, 0.824), resolution=(414, 780))):  # 判断体力是否充足
            energy()
        else:
            print_space("体力不足，暂停打野怪")
    else:
        print_space('兵力不足，暂停打野怪')


# 巨熊活动
def bear():
    if exists(Template(r"icon\tpl1721191349777.png", record_pos=(0.26, 0.795), resolution=(1080, 1920))):
        print_space('点击活动按钮')
        touch(Template(r"icon\tpl1721191349777.png", record_pos=(0.26, 0.795), resolution=(1080, 1920)))
        time.sleep(2)
        print_space('点击集结按钮')
        touch(Template(r'icon\tpl1721784579065.png', record_pos=(0.26, 0.795), resolution=(1080, 1920)))
        if exists(Template(r"icon\tpl1721784579066.png", record_pos=(0.26, 0.795), resolution=(1080, 1920))):
            print_space('发起集结')
            touch(Template(r"icon\tpl1721784579066.png", record_pos=(0.26, 0.795), resolution=(1080, 1920)))
            print_space('点击出征')
            touch(Template(r"icon\tpl1721784579067.png", record_pos=(0.002, 0.705), resolution=(414, 780)))
            print_space('出征成功')
        else:
            print_space('集结中')
    else:
        print_space('未找到活动图标')


def WM_lv():
    print_space('首次启动或数据有更新，重新输入等级')
    print_space('点击等级输入框')
    touch([900, 1573])
    time.sleep(1)
    print_space('删除原本等级')
    keyevent('KEYCODE_DEL')
    time.sleep(1)  #等待1秒
    print_space('输入新的等级')
    text('5')
    #text(set_WM_number.get())
    print_space('点击确定按钮')
    touch(Template(r"icon\sure_button.png", record_pos=(0.404, 0.852), resolution=(1080, 1920)))


# 冰原巨兽
def Brush_WM():
    global number_brush
    search_main()
    swipe([600, 1370], vector=[0.4103, 0.0170])  # 滑动
    time.sleep(1)  # 等待1s
    print_space('点击选择冰原巨兽')
    touch([365, 1373])  # 点击冰原巨兽
    time.sleep(1)  # 等待1s
    '''判断本次是否需要执行选择等级'''
    if number_brush == 0:
        number_brush += 1
        WM_lv()
        time.sleep(1)  # 等待1s
    print_space('点击搜索按钮')
    touch([534, 1821])  # 点击搜索
    time.sleep(1)  # 等待1s
    print_space('点击集结按钮')
    touch(Template(r"icon\tpl1719376765868.png", record_pos=(0.002, 0.705), resolution=(414, 780)))  # 点击怪物集结
    time.sleep(1)  # 等待1s
    if exists(Template(r"icon\tpl1719376776844.png", record_pos=(0.0, 0.326), resolution=(414, 780))):
        print_space('点击发起集结')
        touch(Template(r"icon\tpl1719376776844.png", rgb=True, record_pos=(0.0, 0.326), resolution=(414, 780)))  # 点击发起集结
        time.sleep(1)  # 等待0.5s
        if exists(Template(r"icon\tpl1719376787180.png", record_pos=(0.268, 0.824), resolution=(414, 780))):  # 有兵力可出征
            print_space('点击出征按钮')
            energy()
        else:  # 判断是否有多余兵力
            print_space('不满足条件，无兵力出征')
    else:
        print_space('队伍数不足，无法出征')


# 采集出兵
def gather():
    print_space('点击采集按钮')
    touch(Template(r"icon\tpl1720675061569.png", record_pos=(0.002, -0.015), resolution=(1080, 1920)))
    if exists(Template(r"icon\tpl1721191349776.png", record_pos=(0.26, 0.798), resolution=(1080, 1920))):  # 有兵力可出征
        print_space('点击出征按钮')
        touch(Template(r"icon\tpl1721191349776.png", rgb=True, record_pos=(0.26, 0.798), resolution=(1080, 1920)))  # 点击出征
        print_space('出征成功')
        time.sleep(1)
        touch([14, 823])
    else:  # 判断是否有多余兵力
        print_space('不满足条件，无兵力出征')


# 打怪出兵
def energy():
    touch(Template(r"icon\tpl1719376787180.png", record_pos=(0.268, 0.824), resolution=(414, 780)))  # 点击出征
    time.sleep(1)
    if exists(Template(r"icon\tpl1720264632282.png", record_pos=(0.301, -0.33), resolution=(1080, 1920))):  # 判断是否有体力
        print_space("体力不足，不满足出征条件，开始回到主页")
        print_space('关闭补充体力界面')
        touch(Template(r"icon\tpl1719198103804.png", record_pos=(0.442, -0.35), resolution=(414, 780)))
        print_space('关闭出征界面')
        touch(Template(r"icon\tpl1719198082012.png", threshold=0.5, record_pos=(-0.44, -0.783), resolution=(414, 780)))
    elif exists(Template(r"icon\tpl1719376787180.png", record_pos=(0.268, 0.824), resolution=(414, 780))):
        touch(Template(r"icon\tpl1719376787180.png", record_pos=(0.268, 0.824), resolution=(414, 780)))  # 点击出征
        print_space('出征成功')
    else:
        print_space("出征成功")


# 生肉
def Meat():
    print_space('准备采集生肉资源')
    print_space('点击搜索图标')
    touch([63, 1314])  # 点击搜索图标
    time.sleep(1)  # 等待1s
    swipe([600, 1370], vector=[-0.4103, 0.0170])  # 滑动
    print_space('点击选择肉')
    touch([240, 1373])  # 点击选择肉
    time.sleep(1)  # 等待1s
    print_space('点击等级')
    touch([570, 1573])  # 点击等级
    time.sleep(1)  # 等待1s
    print_space('点击搜索按钮')
    touch([534, 1821])  # 点击搜索
    time.sleep(3)  # 等待1s
    if exists(Template(r"icon\tpl1720675061569.png", rgb=True, record_pos=(0.002, -0.015), resolution=(1080, 1920))):
        gather()
    else:
        print_space('未搜索到生肉资源，结束该任务')


# 木材
def Wood():
    print_space('准备采集木材资源')
    print_space('点击搜索图标')
    touch([63, 1314])  # 点击搜索图标
    time.sleep(1)  # 等待1s
    swipe([600, 1370], vector=[-0.4103, 0.0170])  # 滑动
    print_space('点击选择木材资源')
    touch([476, 1373])  # 点击选择木材
    time.sleep(1)  # 等待1s
    print_space('点击等级')
    touch([570, 1573])  # 点击等级
    time.sleep(1)  # 等待1s
    print_space('点击搜索按钮')
    touch([534, 1821])  # 点击搜索
    time.sleep(1)  # 等待1s
    if exists(Template(r"icon\tpl1720675061569.png", record_pos=(0.002, -0.015), resolution=(1080, 1920))):
        gather()
    else:
        print_space('未搜索到对应资源，结束该任务')


# 煤矿
def Coal():
    print_space('准备采集煤矿资源')
    print_space('点击搜索图标')
    touch([63, 1314])  # 点击搜索图标
    time.sleep(1)  # 等待1s
    swipe([600, 1370], vector=[-0.4103, 0.0170])  # 滑动
    print_space('点击选择煤矿资源')
    touch([710, 1373])  # 点击选择煤矿
    time.sleep(1)  # 等待1s
    print_space('点击等级')
    touch([570, 1573])  # 点击等级
    time.sleep(1)  # 等待1s
    print_space('点击搜索按钮')
    touch([534, 1821])  # 点击搜索
    time.sleep(1)  # 等待1s
    if exists(Template(r"icon\tpl1720675061569.png", record_pos=(0.002, -0.015), resolution=(1080, 1920))):
        gather()
    else:
        print_space('未搜索到煤矿资源，结束该任务')


# 铁矿
def Iron():
    print_space('准备采集铁矿资源')
    print_space('点击搜索图标')
    touch([63, 1314])  # 点击搜索图标
    time.sleep(1)  # 等待1s
    swipe([600, 1370], vector=[-0.4103, 0.0170])  # 滑动
    print_space('点击选择铁矿资源')
    touch([950, 1373])  # 点击选择铁矿
    time.sleep(1)  # 等待1s
    print_space('点击等级')
    touch([570, 1573])  # 点击等级
    time.sleep(1)  # 等待1s
    print_space('点击搜索按钮')
    touch([534, 1821])  # 点击搜索
    time.sleep(1)  # 等待1s
    if exists(Template(r"icon\tpl1720675061569.png", record_pos=(0.002, -0.015), resolution=(1080, 1920))):
        gather()
    else:
        print_space('未搜索到铁矿资源，结束该任务')

# 自动采集
def Collection():
    if not exists(Template(r"icon\tpl1720145326019.png", record_pos=(-0.191, -0.169), resolution=(1080, 1920))):
        print_space('不在世界，点击去往世界')
        touch([950, 1850])  # 点击野外
        time.sleep(5)  # 等待5秒
    else:
        print_space('在野外，执行采集任务')
        time, sleep(3)
    touch([14, 823])
    time.sleep(1)
    touch([500, 400])
    if not exists(Template(r"icon\tpl1720691682616.png", record_pos=(-0.191, -0.169), resolution=(1080, 1920))):
        print_space('有空闲队伍，执行采肉任务')
        time.sleep(1)
        Meat()
    else:
        print_space('已有采肉队伍')
    if not exists(Template(r"icon\tpl1720766916044.png", record_pos=(-0.168, -0.088), resolution=(1080, 1920))):
        print_space('有空闲队伍，执行采木头任务')
        time.sleep(1)
        Wood()
    else:
        print_space('已有采木材队伍')
    if not exists(Template(r"icon\tpl1720766916045.png", record_pos=(-0.168, -0.088), resolution=(1080, 1920))):
        print_space('有空闲队伍，执行采煤任务')
        time.sleep(1)
        Coal()
    else:
        print_space('已有采煤队伍')
    if not exists(Template(r"icon\tpl1720766916046.png", rgb=True, record_pos=(-0.168, -0.088), resolution=(1080, 1920))):
        print_space('有空闲队伍，执行采铁任务')
        time.sleep(1)
        Iron()
    else:
        print_space('已有采铁队伍')
    touch(Template(r"icon\tpl1719552273333.png", threshold=0.9, record_pos=(0.142, -0.126), resolution=(1080, 1920)))


# 治疗
def treatment():
    if exists(Template(r"icon\tpl1721191349778.png", record_pos=(-0.168, -0.088), resolution=(1080, 1920))):
        print_space("点击治疗图标")
        touch(Template(r"icon\tpl1721191349778.png", threshold=0.8, record_pos=(-0.168, -0.088), resolution=(1080, 1920)))
        print_space('点击治疗按钮')
        touch(Template(r"icon\tpl1721191349779.png", threshold=0.8, record_pos=(0.29, 0.756), resolution=(461, 851)))
        print_space('点击联盟互助')
        touch(Template(r"icon\tpl1721191349780.png", threshold=0.8, record_pos=(0.142, -0.126), resolution=(1080, 1920)))
        print_space('点击返回按钮')
        touch(Template(r"icon\tpl1719198082012.png", threshold=0.8, record_pos=(-0.44, -0.783), resolution=(414, 780)))
    else:
        print_space('没有需要治疗的士兵')


# 联盟捐赠
def donate():
    print_space('开始执行联盟捐献任务')
    print_space('点击联盟图案')
    touch(Template(r"icon\tpl1721784579070.png", record_pos=(-0.168, -0.088), resolution=(1080, 1920)))
    print_space('点击联盟科技')
    touch(Template(r"icon\tpl1721784579071.png", record_pos=(-0.168, -0.088), resolution=(1080, 1920)))
    if exists(Template(r"icon\tpl1721784579072.png", record_pos=(-0.168, -0.088), resolution=(1080, 1920))):
        print_space('点击大拇指科技')
        touch(Template(r"icon\tpl1721784579072.png", record_pos=(-0.168, -0.088), resolution=(1080, 1920)))
        x = 1
        while x > 0:
            if not exists(Template(r"icon\tpl1721784579074.png", rgb=True, record_pos=(-0.44, -0.783), resolution=(414, 780))):
                print_space('点击捐献')
                touch(Template(r"icon\tpl1721784579073.png", record_pos=(-0.44, -0.783), resolution=(414, 780)), duration=2)
            else:
                print_space('无捐献次数，结束任务')
                x = 0
    else:
        print_space('无大拇指指引，返回主页')
        touch(Template(r"icon\tpl1719198082012.png", threshold=0.8, record_pos=(-0.44, -0.783), resolution=(414, 780)))


# 探险
def adventure():
    print_space('点击探险')
    touch(Template(r"icon\tpl1719198809581.png", threshold=0.9, record_pos=(-0.398, 0.819), scale_max=800, resolution=(1080, 1920)))
    time.sleep(1)
    print_space('点击宝箱')
    touch([910, 1250])
    if exists(Template(r'icon\tpl1721784579076.png', threshold=0.8, record_pos=(-0.398, 0.819), resolution=(1080, 1920))):
        print_space('点击领取奖励')
        touch(Template(r'icon\tpl1721784579076.png', threshold=0.8, record_pos=(-0.398, 0.819), resolution=(1080, 1920)))
        time.sleep(1)
        print_space('回到主页')
        touch([500, 500])
        touch(Template(r"icon\tpl1719198082012.png", threshold=0.8, record_pos=(-0.44, -0.783), resolution=(1080, 1920)))
    else:
        print_space('没有可领取奖励')


'''招募英雄'''


def recruit():
    if exists(Template(r"icon\hero.png", threshold=0.9, record_pos=(-0.398, 0.819), scale_max=800, resolution=(1080, 1920))):
        print_space('点击英雄')
        touch(Template(r"icon\hero.png", threshold=0.9, record_pos=(-0.398, 0.819), scale_max=800, resolution=(1080, 1920)))
        print_space('点击英雄招募')
        touch(Template(r"icon\hero_recruit.png", threshold=0.8, record_pos=(-0.398, 0.819), scale_max=800, resolution=(1080, 1920)))
        if exists(Template(r"icon\free_recruit.png", threshold=0.8, record_pos=(-0.398, 0.819), scale_max=800, resolution=(1080, 1920))):
            print_space('点击免费招募')
            touch(Template(r"icon\free_recruit.png", threshold=0.8, record_pos=(-0.398, 0.819), scale_max=800, resolution=(1080, 1920)))
            time.sleep(1)
            touch(Template(r"icon\return.png", threshold=0.8, record_pos=(-0.44, -0.783), resolution=(414, 780)))
            time.sleep(1)
        else:
            print_space('无免费招募次数')
        touch(Template(r"icon\return.png", threshold=0.8, record_pos=(-0.44, -0.783), resolution=(414, 780)))
        time.sleep(1)
        touch(Template(r"icon\tpl1719198082012.png", threshold=0.8, record_pos=(-0.44, -0.783), resolution=(414, 780)))


# 设备顶号重连
def re_connet():
    if exists(Template(r"icon\tpl1720766916047.png", rgb=False, record_pos=(-0.168, -0.088), resolution=(1080, 1920))):
        print('在其他设备登录，等待5分钟后重新连接')
        time.sleep(300)
        try:
            print_space('点击重新连接')
            re = 1
            while re > 0:
                touch(Template(r"icon\tpl1720766916047.png", record_pos=(-0.168, -0.088), resolution=(1080, 1920)))
                time.sleep(10)
                if exists(Template(r"icon\tpl1720766916047.png", rgb=False, record_pos=(-0.168, -0.088), resolution=(1080, 1920))):
                    print('重新连接失败，等待1分钟继续尝试')
                    time.sleep(60)
                else:
                    print_space('重新连接成功')
                    re = 0
        except:
            print('重新连接失败，稍后尝试')
    else:
        print_space('连接正常')


# 主体代码
def subject():
    if emulator_click == 0:
        time.sleep(1)
        print('未连接模拟器')
        time.sleep(1)
        cnnect()
    run_number = 1
    global option_help
    while True:
        now = datetime.now()
        if now.second % 2 == 0:
            try:
                if option_help.lower() == '1':
                    print('\n' + '%d.开始执行互助任务' % run_number)
                    Homepage()  # 主页检查
                    Help()  # 互助模块
                    run_number += 1
                    if stop_event.is_set():
                        main_class = Ui_MainWindow()
                        main_class.stop_button()
                        break
            except:
                print('程序执行异常，结束该任务，执行其他任务')
        if now.minute % 5 == 0 and now.second % 5 == 0 and now.hour != 21:
            try:
                if int(option_XG.lower()) == 1:

                    print('\n' + '%d.开始执行野怪任务' % run_number)
                    Homepage()  # 主页检查
                    Brush_XG()  # 野怪
                    run_number += 1
                    if stop_event.is_set():
                        main_class = Ui_MainWindow()
                        main_class.stop_button()  # 总功能
                        break
            except:
                print('程序执行异常，结束该任务，执行其他任务')
        if now.minute % 6 == 0 and 0 < now.second < 20 and now.hour != 21:
            try:
                if int(option_WM.lower()) == 1:

                    print('\n' + '%d.开始执行冰原巨兽任务' % run_number)
                    Homepage()  # 主页检查
                    Brush_WM()  # 冰原巨兽
                    run_number += 1
                    if stop_event.is_set():
                        main_class = Ui_MainWindow()
                        main_class.stop_button()
                        break
            except:
                print('程序执行异常，结束该任务，执行其他任务')
        if now.minute % 6 == 0 and now.hour != 21:
            try:
                if int(option_npc.lower()) == 1:

                    print('\n' + '%d.开始执行活动雪怪任务' % run_number)
                    Homepage()  # 主页检查
                    NPC()  # 活动雪怪
                    run_number += 1
                    if stop_event.is_set():
                        main_class = Ui_MainWindow()
                        main_class.stop_button()
                        break
            except:
                print('程序执行异常，结束该任务，执行其他任务')
        if now.minute % 5 == 0:
            try:
                if int(option_Production.lower()) == 1:

                    print('\n' + '%d.开始执行训练任务' % run_number)
                    Homepage()  # 主页检查
                    Production_soldiers()  # 训练模块
                    run_number += 1
                    if stop_event.is_set():
                        main_class = Ui_MainWindow()
                        main_class.stop_button()  # 总功能
                        break
            except:
                print('程序执行异常，结束该任务，执行其他任务')
        if now.minute % 2 == 0:
            try:
                if int(option_build.lower()) == 1:

                    print('\n' + '%d.开始执行建造任务' % run_number)
                    Homepage()  # 主页检查
                    Build()  # 建造模块
                    run_number += 1
                    if stop_event.is_set():
                        main_class = Ui_MainWindow()
                        main_class.stop_button()  # 总功能
                        break
            except:
                print('程序执行异常，结束该任务，执行其他任务')
        if now.hour == 3:
            try:
                if int(option_Collection.lower()) == 1:

                    print('\n' + '%d.开始执行采集任务' % run_number)
                    Homepage()  # 主页检查
                    Collection()  # 采集资源模块
                    run_number += 1
                    if stop_event.is_set():
                        main_class = Ui_MainWindow()
                        main_class.stop_button()  # 总功能
                        break
            except:
                print('程序执行异常，结束该任务，执行其他任务')
        if now.hour == 21:
            try:
                if int(option_bear.lower()) == 1:

                    print_space('当前时间：%s,巨熊活动进行中' % now.strftime("%H:%M:%S"))
                    Homepage()  # 主页检查
                    bear()  # 巨熊模块
                    run_number += 1
                    if stop_event.is_set():
                        main_class = Ui_MainWindow()
                        main_class.stop_button()  # 总功能
                        break
            except:
                print('程序执行异常，结束该任务，执行其他任务')
        if now.minute == 21:
            try:
                if int(option_treatment.lower()) == 1:

                    print('\n' + '%d.开始执行治疗任务' % run_number)
                    Homepage()  # 主页检查
                    treatment()  # 治疗模块
                    run_number += 1
                    if stop_event.is_set():
                        main_class = Ui_MainWindow()
                        main_class.stop_button()  # 总功能
                        break
            except:
                print('程序执行异常，结束该任务，执行其他任务')
        if now.minute == 25:
            try:
                if int(option_adventure.lower()) == 1:

                    print('\n' + '%d.开始执行探险任务' % run_number)
                    Homepage()  # 主页检查
                    adventure()  # 探险
                    run_number += 1
                    if stop_event.is_set():
                        main_class = Ui_MainWindow()
                        main_class.stop_button()  # 总功能
                        break
            except:
                print('程序执行异常，结束该任务，执行其他任务')
        if now.minute == 1:
            try:
                if int(option_donate.lower()) == 1:
                    print('\n' + '%d.开始执行捐赠任务' % run_number)
                    Homepage()  # 主页检查
                    donate()  # 捐赠模块
                    run_number += 1
                    if stop_event.is_set():
                        main_class = Ui_MainWindow()
                        main_class.stop_button()  # 总功能
                        break
            except:
                print('程序执行异常，结束该任务，执行其他任务')
        if now.hour == 1 and now.minute % 5 == 0:
            try:
                if int(option_donate.lower()) == 1:
                    print('\n' + '%d.开始执行招募任务' % run_number)
                    Homepage()
                    recruit()
                    run_number += 1
                    if stop_event.is_set():
                        main_class = Ui_MainWindow()
                        main_class.stop_button()  # 总功能
                        break
            except:
                print('程序执行异常，结束该任务，执行其他任务')
        if stop_event.is_set():
            main_class = Ui_MainWindow()
            main_class.stop_button()  # 总功能
            break
    print('结束任务')


'''-------------------------------------更新公告-----------------------------------------------'''

class Ui_NoticeWindow(object):
    def setupUi(self, noticewindow):
        noticewindow.setObjectName("helpWindow")
        noticewindow.resize(371, 262)
        noticewindow.setFixedSize(noticewindow.width(), noticewindow.height())  # 设置窗口大小固定
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
        NoticeWindow.setWindowTitle(_translate("NoticeWindow", "更新公告"))
        self.textEdit.setHtml(_translate("NoticeWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                         "p, li { white-space: pre-wrap; }\n"
                                                         "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px;\">更新公告</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\">1.UI界面重构</p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\"></p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\"></p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\"></p>\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px;\"></p></body></html>"))
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
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">多选：</p>\n"
                                                       "<p style=\" margin-top:0px; margin-bottom:0px;\">    可一次性选择多选功能同时执行</p>\n"
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


'''------------------------------------保存设置区域------------------------------------'''

'''保存设置'''


def save_options():
    config.set('Options', '单项', var.get())
    config.set('Options', '联盟互助', option_help.get())
    config.set('Options', '世界野怪', option_XG.get())
    config.set('Options', '冰原巨兽', option_WM.get())
    config.set('Options', '活动雪怪', option_npc.get())
    config.set('Options', '训练士兵', option_Production.get())
    config.set('Options', '建筑升级', option_build.get())
    config.set('Options', '采集资源', option_Collection.get())
    config.set('Options', '巨熊活动', option_bear.get())
    config.set('Options', '治疗士兵', option_treatment.get())
    config.set('Options', '探险奖励', option_adventure.get())
    config.set('Options', '联盟捐赠', option_donate.get())
    config.set('Options', '英雄招募', option_recruit.get())
    with open('set.ini', 'w') as configfile:
        config.write(configfile)


def save_simple_set():
    global number_brush
    if entry.get() != '':
        config.set('Options', '单项', var.get())
        if int(var.get()) == 0:
            help_time = entry.get()
            config.set('Options', '联盟互助设置', help_time)
            print('设置成功！！！')
        elif int(var.get()) == 1:
            XG_time = entry.get()
            config.set('Options', '世界野怪设置', XG_time)
            print('设置成功！！！')
        elif int(var.get()) == 2:
            number_brush = 0
            WM_time = entry.get()
            WM_number = entry_number.get()
            config.set('Options', '冰原巨兽设置', WM_time)
            config.set('Options', '冰原巨兽等级设置', WM_number)
            print('设置成功！！！')
        elif int(var.get()) == 3:
            npc_time = entry.get()
            config.set('Options', '活动雪怪设置', npc_time)
            print('设置成功！！！')
        elif int(var.get()) == 4:
            Production_time = entry.get()
            config.set('Options', '训练士兵设置', Production_time)
            print('设置成功！！！')
        elif int(var.get()) == 5:
            build_time = entry.get()
            config.set('Options', '建筑升级设置', build_time)
            print('设置成功！！！')
        elif int(var.get()) == 6:
            Collection_time = entry.get()
            config.set('Options', '采集资源设置', Collection_time)
            print('设置成功！！！')
        elif int(var.get()) == 7:
            bear_time = entry.get()
            config.set('Options', '巨熊活动设置', bear_time)
            print('设置成功！！！')
        elif int(var.get()) == 8:
            treatment_time = entry.get()
            config.set('Options', '治疗士兵设置', treatment_time)
            print('设置成功！！！')
        elif int(var.get()) == 9:
            adventure_time = entry.get()
            config.set('Options', '探险奖励设置', adventure_time)
            print('设置成功！！！')
        elif int(var.get()) == 10:
            donate_time = entry.get()
            config.set('Options', '联盟捐赠设置', donate_time)
            print('设置成功！！！')
        elif int(var.get()) == 11:
            recruit_time = entry.get()
            config.set('Options', '英雄招募设置', recruit_time)
            print('设置成功！！！')
        with open('set.ini', 'w') as configfile:
            config.write(configfile)
        load_options()
    else:
        print('-------------间隔时间不能为空-------------')


'''读取设置'''


def load_options():
    set_ip.set(config.get('Options', '模拟器ip'))
    set_address.set(config.get('Options', '模拟器路径'))
    var.set(config.get('Options', '单项'))
    option_help.set(config.get('Options', '联盟互助'))
    option_XG.set(config.get('Options', '世界野怪'))
    option_WM.set(config.get('Options', '冰原巨兽'))
    option_npc.set(config.get('Options', '活动雪怪'))
    option_Production.set(config.get('Options', '训练士兵'))
    option_build.set(config.get('Options', '建筑升级'))
    option_Collection.set(config.get('Options', '采集资源'))
    option_bear.set(config.get('Options', '巨熊活动'))
    option_treatment.set(config.get('Options', '治疗士兵'))
    option_adventure.set(config.get('Options', '探险奖励'))
    option_donate.set(config.get('Options', '联盟捐赠'))
    option_recruit.set(config.get('Options', '英雄招募'))
    set_help_time.set(config.get('Options', '联盟互助设置'))
    set_XG_time.set(config.get('Options', '世界野怪设置'))
    set_WM_time.set(config.get('Options', '冰原巨兽设置'))
    set_npc_time.set(config.get('Options', '活动雪怪设置'))
    set_Production_time.set(config.get('Options', '训练士兵设置'))
    set_build_time.set(config.get('Options', '建筑升级设置'))
    set_Collection_time.set(config.get('Options', '采集资源设置'))
    set_bear_time.set(config.get('Options', '巨熊活动设置'))
    set_treatment_time.set(config.get('Options', '治疗士兵设置'))
    set_adventure_time.set(config.get('Options', '探险奖励设置'))
    set_donate_time.set(config.get('Options', '联盟捐赠设置'))
    set_WM_number.set(config.get('Options', '冰原巨兽等级设置'))
    set_recruit_time.set(config.get('Options', '英雄招募设置'))
    set_version.set(config.get('Options', 'version'))


'''初始化配置解析器和选项变量'''
config = ConfigParser()
config['Options'] = {}
'''单选'''
var = QSettings()
'''多选'''
set_ip = QSettings()  #设置模拟器ip
set_address = QSettings()  #设置模拟器地址
set_help_time = QSettings()  #互助
set_XG_time = QSettings()  #野怪
set_WM_time = QSettings()  #巨兽
set_npc_time = QSettings()  #雪怪
set_Production_time = QSettings()  #士兵
set_build_time = QSettings()  #建筑
set_Collection_time = QSettings()  #采集
set_bear_time = QSettings()  #巨熊
set_treatment_time = QSettings()  #治疗
set_adventure_time = QSettings()  #探险
set_donate_time = QSettings()  #捐赠
set_WM_number = QSettings()  #冰原巨兽等级
set_recruit_time = QSettings()  #招募设置
set_version = QSettings()  #设置版本号


# 尝试加载先前保存的选项
def read_save():
    # 首次启动时默认选项
    if not config.read('set.ini'):
        config.set('Options', '模拟器ip', '127.0.0.1:5037')
        config.set('Options', '模拟器路径', 'E:\leidian\LDPlayer9\dnplayer.exe')
        config.set('Options', '单项', '0')
        config.set('Options', '联盟互助', '1')
        config.set('Options', '世界野怪', '1')
        config.set('Options', '冰原巨兽', '1')
        config.set('Options', '活动雪怪', '1')
        config.set('Options', '训练士兵', '1')
        config.set('Options', '建筑升级', '1')
        config.set('Options', '采集资源', '1')
        config.set('Options', '巨熊活动', '1')
        config.set('Options', '治疗士兵', '1')
        config.set('Options', '探险奖励', '1')
        config.set('Options', '联盟捐赠', '1')
        config.set('Options', '英雄招募', '1')
        config.set('Options', '联盟互助设置', '2')
        config.set('Options', '世界野怪设置', '60')
        config.set('Options', '冰原巨兽设置', '180')
        config.set('Options', '活动雪怪设置', '90')
        config.set('Options', '训练士兵设置', '3600')
        config.set('Options', '建筑升级设置', '1')
        config.set('Options', '采集资源设置', '60')
        config.set('Options', '巨熊活动设置', '60')
        config.set('Options', '治疗士兵设置', '1')
        config.set('Options', '探险奖励设置', '3600')
        config.set('Options', '联盟捐赠设置', '300')
        config.set('Options', '冰原巨兽等级设置', '4')
        config.set('Options', '英雄招募设置', '300')
        config.set('Options', 'version', '1.2.0')
        with open('set.ini', 'w') as configfile:
            config.write(configfile)
    try:
        with open('set.ini', 'r') as configfile:
            config.read_file(configfile)  #load_options()
    except IOError:
        print('No saved options found.')


read_save()


def stop_function():
    # 这里放置程序停止时需要执行的代码
    global stop_event
    stop_event.set()  # 设置事件，通知线程结束运行
    print("------------等待当前任务完成或10s左右结束任务------------")
stop_event = threading.Event()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(960, 540)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())  # 设置窗口大小固定
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"icon\log.png"))
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        MainWindow.setAnimated(False)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        #模拟器参数设置区域
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 60, 461, 41))
        #self.frame.setStyleSheet("#frame{border:1px solid rgb(0,255,0)}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        #下拉框
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 91, 22))
        self.comboBox.setAutoFillBackground(False)
        #self.comboBox.setStyleSheet("background: transparent;")
        self.comboBox.setStyleSheet("QComboBox {\n"
                                    "    background-color: rgba(0, 0, 0, 0); /* 白色背景，150为透明度 */\n"
                                    "    border: 1px solid rgba(0, 255, 0); /* 边框样式 */\n"
                                    "}\n"
                                    "QComboBox QAbstractItemView {\n"
                                    "    background-color: transparent; /* 下拉列表背景透明度 */\n"
                                    "    border: 1px solid rgb(0,255,0); /* 下拉列表边框样式 */\n"
                                    "}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.lineEdit = QtWidgets.QLineEdit(self.frame)  #模拟器地址输入框
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
        '''模拟器区域'''
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 160, 461, 41))
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.frame_2.setBaseSize(QtCore.QSize(0, 0))
        self.frame_2.setMouseTracking(False)
        self.frame_2.setTabletTracking(False)
        self.frame_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frame_2.setAcceptDrops(False)
        self.frame_2.setAutoFillBackground(False)
        #self.frame_2.setStyleSheet("#frame_2{border:1px solid rgb(0,255,0)}")
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
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 270, 461, 191))
        #self.frame_3.setStyleSheet("#frame_3{border:1px solid rgb(0,255,0)}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.select_text = QtWidgets.QLabel(self.frame_3)
        self.select_text.setGeometry(QtCore.QRect(10, 0, 81, 16))
        self.select_text.setObjectName("select_text")
        self.checkBox_help = QtWidgets.QCheckBox(self.frame_3)  #互助
        self.checkBox_help.setGeometry(QtCore.QRect(20, 30, 71, 16))
        self.checkBox_help.setAutoFillBackground(False)
        '''self.checkBox_help.setStyleSheet("QCheckBox:indicator:checked {background-color: transparent;border:1px solid rgb(0,255,0)}"
        "QCheckBox:indicator {background-color: transparent;border:1px solid rgb(0,0,0)}")'''
        self.checkBox_help.setAutoRepeat(False)
        self.checkBox_help.setAutoExclusive(False)
        self.checkBox_help.setTristate(False)
        self.checkBox_help.setObjectName("checkBox_help")
        self.checkBox_XG = QtWidgets.QCheckBox(self.frame_3)  #野怪
        self.checkBox_XG.setGeometry(QtCore.QRect(110, 30, 71, 16))
        self.checkBox_XG.setObjectName("checkBox_XG")
        self.checkBox_XG.setStyleSheet("background-color: transparent")
        self.checkBox_WM = QtWidgets.QCheckBox(self.frame_3)  #冰原巨兽
        self.checkBox_WM.setGeometry(QtCore.QRect(200, 30, 71, 16))
        self.checkBox_WM.setObjectName("checkBox_WM")
        self.checkBox_npc = QtWidgets.QCheckBox(self.frame_3)  #活动雪怪
        self.checkBox_npc.setGeometry(QtCore.QRect(290, 30, 71, 16))
        self.checkBox_npc.setObjectName("checkBox_npc")
        self.checkBox_Production = QtWidgets.QCheckBox(self.frame_3)  #训练士兵
        self.checkBox_Production.setGeometry(QtCore.QRect(380, 30, 71, 16))
        self.checkBox_Production.setObjectName("checkBox_Production")
        self.checkBox_adventure = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_adventure.setGeometry(QtCore.QRect(380, 70, 71, 16))
        self.checkBox_adventure.setObjectName("checkBox_adventure")
        self.checkBox_treatment = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_treatment.setGeometry(QtCore.QRect(290, 70, 71, 16))
        self.checkBox_treatment.setMouseTracking(True)
        self.checkBox_treatment.setTabletTracking(False)
        self.checkBox_treatment.setFocusPolicy(QtCore.Qt.StrongFocus)
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
        self.checkBox_recruit.setObjectName("checkBox_recruit")
        #全选
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
        #开始按钮
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
        self.listView.setStyleSheet("background-image: url(./icon/11.png)")
        self.listView.setObjectName("listView")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(490, 60, 461, 191))
        #self.frame_4.setStyleSheet("#frame_4{border:1px solid rgb(0,255,0)}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.simple_title = QtWidgets.QLabel(self.frame_4)
        self.simple_title.setGeometry(QtCore.QRect(10, 0, 81, 21))
        self.simple_title.setObjectName("simple_title")
        self.radioButton_help = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_help.setGeometry(QtCore.QRect(20, 30, 71, 16))
        self.radioButton_help.setAutoFillBackground(False)
        self.radioButton_help.setStyleSheet("")
        self.radioButton_help.setCheckable(True)
        self.radioButton_help.setChecked(False)
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
        self.radioButton_11 = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_11.setGeometry(QtCore.QRect(380, 70, 71, 16))
        self.radioButton_11.setObjectName("radioButton_11")
        self.radioButton_12 = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_12.setGeometry(QtCore.QRect(290, 70, 71, 16))
        self.radioButton_12.setMouseTracking(True)
        self.radioButton_12.setTabletTracking(False)
        self.radioButton_12.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.radioButton_12.setStyleSheet("")
        self.radioButton_12.setCheckable(False)
        self.radioButton_12.setChecked(False)
        self.radioButton_12.setObjectName("radioButton_12")
        self.radioButton_build = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_build.setGeometry(QtCore.QRect(20, 70, 71, 16))
        self.radioButton_build.setObjectName("radioButton_build")
        self.radioButton_16 = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_16.setGeometry(QtCore.QRect(110, 70, 71, 16))
        self.radioButton_16.setObjectName("radioButton_16")
        self.radioButton_17 = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_17.setGeometry(QtCore.QRect(200, 70, 71, 16))
        self.radioButton_17.setObjectName("radioButton_17")
        self.radioButton_18 = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_18.setGeometry(QtCore.QRect(20, 110, 71, 16))
        self.radioButton_18.setObjectName("radioButton_18")
        self.radioButton_ = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_.setGeometry(QtCore.QRect(110, 110, 71, 16))
        self.radioButton_.setObjectName("radioButton_")
        #单项停止
        self.simple_stop = QtWidgets.QPushButton(self.frame_4)
        self.simple_stop.setEnabled(True)
        self.simple_stop.setVisible(False)
        self.simple_stop.setGeometry(QtCore.QRect(190, 150, 75, 23))
        self.simple_stop.setAutoExclusive(False)
        self.simple_stop.setDefault(False)
        self.simple_stop.setFlat(True)
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
        self.simple_start.setEnabled(True)
        self.simple_start.setGeometry(QtCore.QRect(190, 150, 75, 23))
        self.simple_start.setAutoDefault(False)
        self.simple_start.setDefault(False)
        self.simple_start.setFlat(True)
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
        #等级文本
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(270, 0, 54, 21))
        self.label_4.setObjectName("label_4")
        #等级输入
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(300, 1, 31, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
                                      "background: transparent;\n"
                                      "border: 1px solid rgba(0, 255, 0)"
                                      "}")
        #单项保存按钮
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_9.setGeometry(QtCore.QRect(380, 0, 75, 21))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setFlat(True)
        self.pushButton_9.setStyleSheet("QPushButton {\n""border: 1px solid rgb(0,255,0); /* 边框样式 */\n"
                                        "}"
                                        "QPushButton:hover {\n"
                                        "background-color: rgba(0, 0, 0, 15); /* 编辑状态下的背景透明度 */\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "background-color: rgba(0, 0, 0, 80); /* 编辑状态下的背景透明度 */\n"
                                        "}\n")
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
        self.textEdit_out.setTabChangesFocus(False)
        self.textEdit_out.setUndoRedoEnabled(False)
        self.textEdit_out.setReadOnly(True)
        self.textEdit_out.setOverwriteMode(False)
        self.textEdit_out.setAcceptRichText(True)
        #self.textEdit_out.setLineSpacing(1)
        self.textEdit_out.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(890, 520, 71, 20))
        self.label_2.setObjectName("label_2")
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
        self.textEdit.setGeometry(QtCore.QRect(370, 10, 231, 41))
        self.textEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
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
        self.hide_UI = QtWidgets.QPushButton(self.centralwidget)
        self.hide_UI.setGeometry(QtCore.QRect(5, 520, 51, 23))
        self.hide_UI.setFlat(True)
        self.hide_UI.setObjectName("hide_UI")
        self.listView.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
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
        MainWindow.setCentralWidget(self.centralwidget)
        #按钮点击触发响应
        self.retranslateUi(MainWindow)
        self.select_start.clicked.connect(self.save_simple)  # type: ignore
        self.select_stop.clicked.connect(stop_function)  # type: ignore
        self.simple_start.clicked.connect(self.simple_start.hide)  # type: ignore
        self.simple_start.clicked.connect(self.simple_stop.show)  # type: ignore
        self.simple_stop.clicked.connect(self.simple_start.show)  # type: ignore
        self.simple_stop.clicked.connect(self.simple_stop.hide)  # type: ignore
        self.hide_UI.clicked.connect(self.hide_ui)  # type: ignore
        self.show_UI.clicked.connect(self.show_ui)  # type: ignore
        self.start_simulator.clicked.connect(lambda: start_simple(1))
        self.connect_simulator.clicked.connect(lambda: start_simple(2))
        self.start_game.clicked.connect(lambda: start_simple(3))
        self.simulator_start_all.clicked.connect(lambda: start_simple(4))
        self.select_all.clicked.connect(self.toggle_checkbox)
        self.select_unall.clicked.connect(self.untoggle_checkbox)
        self.comboBox.currentIndexChanged.connect(self.on_combobox_changed)
        self.notice_button.clicked.connect(self.open_noticeable)
        self.notice = noticelog()
        self.help_button.clicked.connect(self.open_helpline)
        self.help = helplog()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 根据读取的配置值来更新界面元素
        # 假设界面上有一个QCheckBox名为self.checkBox_help
        if option_help.lower() == '1':
            self.checkBox_help.setChecked(True)
        else:
            self.checkBox_help.setChecked(False)

        if option_XG.lower() == '1':
            self.checkBox_XG.setChecked(True)
        else:
            self.checkBox_XG.setChecked(False)

        if option_WM.lower() == '1':
            self.checkBox_WM.setChecked(True)
        else:
            self.checkBox_WM.setChecked(False)

        if option_npc.lower() == '1':
            self.checkBox_npc.setChecked(True)
        else:
            self.checkBox_npc.setChecked(False)

        if option_Production.lower() == '1':
            self.checkBox_Production.setChecked(True)
        else:
            self.checkBox_Production.setChecked(False)

        if option_build.lower() == '1':
            self.checkBox_build.setChecked(True)
        else:
            self.checkBox_build.setChecked(False)

        if option_Collection.lower() == '1':
            self.checkBox_Collection.setChecked(True)
        else:
            self.checkBox_Collection.setChecked(False)

        if option_bear.lower() == '1':
            self.checkBox_bear.setChecked(True)
        else:
            self.checkBox_bear.setChecked(False)

        if option_treatment.lower() == '1':
            self.checkBox_treatment.setChecked(True)
        else:
            self.checkBox_treatment.setChecked(False)

        if option_adventure.lower() == '1':
            self.checkBox_adventure.setChecked(True)
        else:
            self.checkBox_adventure.setChecked(False)

        if option_donate.lower() == '1':
            self.checkBox_donate.setChecked(True)
        else:
            self.checkBox_donate.setChecked(False)

        if option_recruit.lower() == '1':
            self.checkBox_recruit.setChecked(True)
        else:
            self.checkBox_recruit.setChecked(False)

    def save_simple(self):
        self.select_stop.show()  # type: ignore
        self.select_start.hide()  # type: ignore
        print("程序开始执行...")
        # 这里放置程序开始时需要执行的代码
        #stop_event.clear()
        threading.Thread(target=subject).start()  #save_options()

    def stop_button(self):
        self.select_start.show()
        self.select_stop.hide()

    def open_noticeable(self):
        self.notice.show()

    def open_helpline(self):
        self.help.show()

    def on_combobox_changed(self, index):
        if index == 0:
            self.lineEdit.setText('模拟器地址')
        if index == 1:
            self.lineEdit.setText('模拟器ip')

    def hide_ui(self):
        self.frame.setVisible(False)
        self.frame_2.setVisible(False)
        self.frame_3.setVisible(False)
        self.frame_4.setVisible(False)
        self.frame_5.setVisible(False)
        self.hide_UI.setVisible(False)
        self.show_UI.setVisible(True)
        self.textEdit.setVisible(False)

    def show_ui(self):
        self.frame.setVisible(True)
        self.frame_2.setVisible(True)
        self.frame_3.setVisible(True)
        self.frame_4.setVisible(True)
        self.frame_5.setVisible(True)
        self.hide_UI.setVisible(True)
        self.show_UI.setVisible(False)
        self.textEdit.setVisible(True)

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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "无尽冬日"))
        self.comboBox.setItemText(0, _translate("MainWindow", "模拟器路径"))
        self.comboBox.setItemText(1, _translate("MainWindow", "模拟器ip"))
        self.save_simulator.setText(_translate("MainWindow", "保存"))
        self.start_simulator.setText(_translate("MainWindow", "启动模拟器"))
        self.connect_simulator.setText(_translate("MainWindow", "连接模拟器"))
        self.start_game.setText(_translate("MainWindow", "启动游戏"))
        self.simulator_start_all.setText(_translate("MainWindow", "一键启动"))
        self.select_text.setText(_translate("MainWindow", "复选项（多选）"))
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
        self.radioButton_11.setText(_translate("MainWindow", "探险奖励"))
        self.radioButton_12.setText(_translate("MainWindow", "治疗士兵"))
        self.radioButton_build.setText(_translate("MainWindow", "建筑升级"))
        self.radioButton_16.setText(_translate("MainWindow", "采集资源"))
        self.radioButton_17.setText(_translate("MainWindow", "巨熊活动"))
        self.radioButton_18.setText(_translate("MainWindow", "联盟捐赠"))
        self.radioButton_.setText(_translate("MainWindow", "英雄招募"))
        self.simple_stop.setText(_translate("MainWindow", "停止"))
        self.simple_start.setText(_translate("MainWindow", "开始"))
        self.label_3.setText(_translate("MainWindow", "执行间隔(秒):"))
        self.label_4.setText(_translate("MainWindow", "等级:"))
        self.pushButton_9.setText(_translate("MainWindow", "设置"))
        self.label.setText(_translate("MainWindow", "输出："))
        self.label_2.setText(_translate("MainWindow", "版本:1.2.2"))
        self.show_UI.setText(_translate("MainWindow", "显示UI"))
        self.notice_button.setText(_translate("MainWindow", "更新公告"))
        self.help_button.setText(_translate("MainWindow", "帮助文档"))
        self.textEdit.setHtml(_translate("MainWindow", "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; \">请等待程序停止后再设置相关参数</span></p>\n"
                                                       "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; \">多选和单选不可同时执行</span></p></body>"))
        self.textEdit.setReadOnly(True)
        self.hide_UI.setText(_translate("MainWindow", "隐藏UI"))

    def write(self, text):
        # 将text写入textEdit
        self.textEdit_out.insertPlainText(text)
        self.textEdit_out.moveCursor(self.textEdit_out.textCursor().End)  # 移动光标到文本末尾


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MyApp()
    # 重定向stdout和stderr
    #sys.stdout = mainWindow
    #sys.stderr = mainWindow
    mainWindow.show()
    sys.exit(app.exec_())
