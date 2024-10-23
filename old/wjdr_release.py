# -*- encoding=utf8 -*-
__author__ = "猫耳小刻晴"

import logging
import subprocess
import threading
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from configparser import ConfigParser
from tkinter.scrolledtext import ScrolledText
from airtest.core.api import *
from airtest.core.android.android import *
from PIL import Image, ImageTk
import os
auto_setup(__file__)
logging.getLogger('airtest').setLevel(logging.ERROR)
'''模拟器点击变量'''
emulator_click = 0
number_brush = 0
number_meat = 0
number_wood = 0
number_coal = 0
number_iron = 0


# 获取当前文件的绝对路径(本地）
current_file_path = os.path.abspath(__file__)

# 获取当前文件夹的上一级目录的绝对路径(本地）
#parent_directory_path = os.path.dirname(os.path.dirname(current_file_path))
# 上一级文件夹中要删除的文件名
file_to_delete = 'jiaoben-1.2.2.exe'

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

'''打开模拟器'''

def start_exe():
    while True:
        try:
            print('开始启动雷电模拟器')
            #subprocess.Popen('E:\leidian\LDPlayer9\dnplayer.exe')
            subprocess.Popen('%s' % set_address.get())
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
            print('地址：android:// %s' % str(set_ip.get()))
            connect_device('android://%s'%set_ip.get())
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
            '''if exists(Template(r"icon\tpl1719196072757.png", threshold=0.8, record_pos=(0.112, -0.519),
                           resolution=(414, 780))):
            print('游戏未启动，点击启动')'''
            touch(Template(r"icon\tpl1719196072757.png", record_pos=(0.112, -0.519), resolution=(1080, 1920)))
            print_space("启动成功，等待30秒启动时间...")
            time.sleep(30)
            print_space('启动完成')
            break
        except:
            print('启动失败，再次尝试')
        '''else:
        print_space('游戏已启动!!!')'''


# 主页判断
def Homepage():
    a = 1
    try:
        while a < 4:
            if exists(Template(r"icon\tpl1719198809581.png", record_pos=(-0.441, -0.839), resolution=(1080, 1920))):
                print_space("在主页，准备执行任务")  # 在主界面，执行任务
                return
            else:
                a += 1
                print_space("不在主页，返回上一级")
                if exists(Template(r"icon\tpl1719198082012.png",rgb=True, record_pos=(-0.441, -0.839), resolution=(1080, 1920))):
                    print_space('点击黑色返回按钮')
                    touch(Template(r"icon\tpl1719198082012.png",rgb=True, record_pos=(-0.441, -0.839), resolution=(1080, 1920)))
                elif exists(Template(r'icon\return.png',rgb=True, record_pos=(-0.44, -0.783), resolution=(1080, 1920))):
                    print_space('点击白色返回按钮')
                    touch(Template(r"icon\return.png", threshold=0.8, record_pos=(-0.44, -0.783), resolution=(1080, 1920)))
                elif exists(Template(r"icon\tpl1719198103804.png", record_pos=(0.442, -0.35), resolution=(1080, 1920))):
                    print_space('点击关闭按钮')
                    touch(Template(r"icon\tpl1719198103804.png", record_pos=(0.442, -0.35), resolution=(1080, 1920)))
                else:
                    print_space('点击其他区域')
                    touch([500, 600])  # 不在主界面，返回到主页
            if stop_event.is_set():
                start_button_simple.configure(text='开始', command=save_simple_start_button)
                break
    except:
        print('执行错误')
    if a == 4:
        re_connet()


# 互助功能
def Help():
    result = exists(Template(r"icon\tpl1718936896202.png", record_pos=(0.248, 0.735), resolution=(1080, 1920)))
    if result:  # 判断是否有盟员求助
        print_space("有盟员求助，需点击援助按钮")
        #touch([800, 1700])
        touch(Template(r"icon\tpl1718936896202.png", record_pos=(0.248, 0.735), resolution=(1080, 1920)))
        #print_space("点击援助按钮成功，等待1s进行下一个任务")
        #time.sleep(1)
    else:
        print_space("无盟员求助，进行下一个任务")
        #time.sleep(1)


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
        lv_y = 10
        while lv_y > 0:
            if not exists(Template(r"icon\tpl17217845790633.png", rgb=True, threshold=0.8, record_pos=(0.22, 0.338), resolution=(1080, 1920))):
                lv_x = lv_x - 200
                touch([lv_x, 1225])  # 点击开始上一级士兵
                lv_y -= 1
                if lv_y == 5:
                    lv_x = 910
                    swipe([115, 1225], vector=[0.7397, 0.0009])  # 滑动训练兵种
                    touch([910, 1225])  # 点击五级兵
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
    elif exists(Template(r"icon/tpl1719478488283.png", threshold=0.9,rgb=True, record_pos=(-0.066, -0.111), resolution=(1080, 1920))):
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
    touch(Template(r"icon\tpl1719651083870.png", record_pos=(0.001, 0.731), resolution=(1080, 1920)))
    time.sleep(1)
    if exists(Template(r"icon\tpl1719817875178.png", record_pos=(-0.002, 0.683), resolution=(1080, 1920))):
        print_space('一键补齐资源不足，回到首页')
        touch(Template(r"icon\tpl1719198103804.png", record_pos=(0.442, -0.35), resolution=(1080, 1920)))
        touch(Template(r"icon\tpl1719198103804.png", record_pos=(0.442, -0.35), resolution=(1080, 1920)))
    else:
        touch(Template(r"icon\tpl1719651144335.png", record_pos=(0.224, 0.608), resolution=(1080, 1920)))
        touch(Template(r"icon\tpl1719578558005.png", record_pos=(0.003, -0.045), resolution=(1080, 1920)))  # 点击升级
        time.sleep(1)
        touch(Template(r"icon\tpl1719579273500.png", record_pos=(0.002, -0.08), resolution=(1080, 1920)))


# 自动建筑升级
def Build():
    touch([14, 823])
    time.sleep(1)
    touch([170, 400])
    if exists(Template(r"icon\tpl1719643933714.png",rgb=True, record_pos=(-0.311, -0.372), resolution=(1080, 1920))):
        print_space('有空闲队列，开始建造')
        touch(Template(r"icon\tpl1719643933714.png", record_pos=(-0.306, -0.318), resolution=(1080, 1920)))  # 点击跳转到需升级的建筑
        if exists(Template(r"icon\tpl1719580056417.png", record_pos=(-0.362, 0.238), resolution=(1080, 1920))):  # 判断是什么建筑升级升级
            print_space('升级资源建筑')
            time.sleep(5)  # 等待5s
            if not exists(Template(r"icon\tpl1719644932718.png", threshold=0.9, record_pos=(0.308, 0.056), resolution=(1080, 1920))):
                print_space('建筑设施未达到升级要求，升级设施')
                while not exists(Template(r"icon\tpl1719645172814.png", record_pos=(0.248, -0.102), resolution=(1080, 1920))):
                    touch([900, 1000])
                    if exists(Template(r"icon\tpl1719645172814.png", record_pos=(0.248, -0.102), resolution=(1080, 1920))):
                        print_space('达到升级条件，开始升级')
            touch([900, 800])  # 点击升级按钮
            touch([800, 1800])  # 点击升级
            if exists(Template(r"icon\tpl1719651083870.png", record_pos=(0.001, 0.731), resolution=(1080, 1920))):  # 判断资源是否充足
                print_space("/31资源不足，点击一键补齐")
                build_main()
            else:
                time.sleep(1)
                touch(Template(r"icon\tpl1719579273500.png", record_pos=(0.003, -0.045), resolution=(1080, 1920)))  # 点击求助
        else:
            print_space('升级功能建筑')
            touch([553, 1333])  # 点击升级按钮
            touch(Template(r"icon\tpl1719578558005.png", record_pos=(0.003, -0.045), resolution=(1080, 1920)))  # 点击升级
            if exists(Template(r"icon\tpl1719651083870.png", record_pos=(0.001, 0.731), resolution=(1080, 1920))):  # 判断资源是否充足
                print_space('资源不足，点击一键补齐')
                build_main()
            else:
                time.sleep(1)
                touch(Template(r"icon\tpl1719579273500.png", record_pos=(0.002, -0.08), resolution=(1080, 1920)))  # 点击求助
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
    if exists(Template(r"icon\tpl1719376487523.png", record_pos=(0.449, -0.78), resolution=(1080, 1920))):  # 判断背包是否打开成功
        touch([949, 171])  # 点击其他跳转至该页
        print_space('查看活动道具')
        if exists(Template(r"icon\tpl1719376586643.png", record_pos=(0.106, -0.476), resolution=(1080, 1920))):  # 判断是否有该道具
            print_space('使用活动道具')
            touch(Template(r"icon\tpl1719376586643.png", record_pos=(0.106, -0.476), resolution=(1080, 1920)))  # 点击道具
            touch(Template(r"icon\tpl1719376629723.png", record_pos=(0.0, 0.092), resolution=(1080, 1920)))  # 点击使用
            time.sleep(1)
            print_space('集结打怪')
            touch(Template(r"icon\tpl1719376765868.png", record_pos=(0.002, 0.705), resolution=(1080, 1920)))  # 寻找到怪物点击集结
            touch(Template(r"icon\tpl1719376776844.png", record_pos=(0.0, 0.326), resolution=(1080, 1920)))  # 点击发起集结
            print_space('兵力检查')
            if exists(Template(r"icon\tpl1721191349774.png", record_pos=(-0.118, 0.782), resolution=(1080, 1920))):
                touch(Template(r"icon\tpl1721191349774.png", record_pos=(-0.118, 0.782), resolution=(1080, 1920)))
                print_space('体力检查')
                if exists(Template(r"icon\tpl1719376787180.png", record_pos=(0.263, 0.773), resolution=(1080, 1920))):  # 判断体力是否充足
                    energy()
                else:
                    print_space("体力不足，暂停打怪")
            else:
                print_space('兵力不足，暂停打怪')
        else:
            print_space("未找到相关物品，退出任务")
            touch(Template(r"icon\tpl1719198082012.png", threshold=0.5, record_pos=(-0.44, -0.783), resolution=(
            1080, 1920))) or touch(Template(r"icon\tpl1719198103804.png", record_pos=(0.442, -0.35), resolution=(1080, 1920)))


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
    touch(Template(r"icon\tpl1721191349775.png", rgb=False, record_pos=(0.002, 0.705), resolution=(1080, 1920)))  # 点击出征怪物
    time.sleep(1)  # 等待1s
    if exists(Template(r"icon\tpl1721191349774.png", record_pos=(-0.118, 0.782), resolution=(1080, 1920))):  # 判断是否有兵力
        if exists(Template(r"icon\tpl1719376787180.png", record_pos=(0.263, 0.773), resolution=(1080, 1920))):  # 判断体力是否充足
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
            touch(Template(r"icon\tpl1721784579067.png", record_pos=(0.002, 0.705), resolution=(1080, 1920)))
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
    time.sleep(1)#等待1秒
    print_space('输入新的等级')
    text(set_WM_number.get())
    print_space('点击确定按钮')
    touch(Template(r"icon\sure_button.png", record_pos=(0.36, 0.806), resolution=(1080, 1920)))
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
    touch(Template(r"icon\tpl1719376765868.png", record_pos=(-0.003, -0.227), resolution=(1080, 1920)))  # 点击怪物集结
    time.sleep(1)  # 等待1s
    if exists(Template(r"icon\tpl1719376776844.png", record_pos=(0.0, 0.326), resolution=(1080, 1920))):
        print_space('点击发起集结')
        touch(Template(r"icon\tpl1719376776844.png", rgb=True, record_pos=(0.0, 0.326), resolution=(1080, 1920)))  # 点击发起集结
        time.sleep(1)  # 等待0.5s
        if exists(Template(r"icon\tpl1719376787180.png", record_pos=(0.263, 0.773), resolution=(1080, 1920))):  # 有兵力可出征
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
        touch(Template(r"icon\tpl1721191349776.png",rgb=True, record_pos=(0.26, 0.798), resolution=(1080, 1920)))  # 点击出征
        print_space('出征成功')
        time.sleep(1)
        touch([14, 823])
    else:  # 判断是否有多余兵力
        print_space('不满足条件，无兵力出征')


# 打怪出兵
def energy():
    touch(Template(r"icon\tpl1719376787180.png", record_pos=(0.263, 0.773), resolution=(1080, 1920)))  # 点击出征
    time.sleep(1)
    if exists(Template(r"icon\tpl1720264632282.png", record_pos=(0.301, -0.33), resolution=(1080, 1920))):  # 判断是否有体力
        print_space("体力不足，不满足出征条件，开始回到主页")
        print_space('关闭补充体力界面')
        touch(Template(r"icon\tpl1719198103804.png", record_pos=(0.442, -0.35), resolution=(1080, 1920)))
        print_space('关闭出征界面')
        touch(Template(r"icon\tpl1719198082012.png", threshold=0.5, record_pos=(-0.44, -0.783), resolution=(1080, 1920)))
    elif exists(Template(r"icon\tpl1719376787180.png", record_pos=(0.263, 0.773), resolution=(1080, 1920))):
        touch(Template(r"icon\tpl1719376787180.png", record_pos=(0.263, 0.773), resolution=(1080, 1920)))  # 点击出征
        print_space('出征成功')
    else:
        print_space("出征成功")


#采集等级设置
def collection_lv():
    print_space('首次启动或数据有更新，重新输入等级')
    print_space('点击等级输入框')
    touch([900, 1573])
    time.sleep(1)
    print_space('删除原本等级')
    keyevent('KEYCODE_DEL')
    time.sleep(1)#等待1秒
    print_space('输入新的等级')
    #print(set_collection_lv.get())
    text(set_collection_lv.get())
    print_space('点击确定按钮')
    touch(Template(r"icon\sure_button.png", record_pos=(0.404, 0.852), resolution=(1080, 1920)))
# 生肉
def Meat():
    global number_meat
    print_space('准备采集生肉资源')
    print_space('点击搜索图标')
    touch([63, 1314])  # 点击搜索图标
    time.sleep(1)  # 等待1s
    swipe([600, 1370], vector=[-0.4103, 0.0170])  # 滑动
    print_space('点击选择肉')
    touch([240, 1373])  # 点击选择肉
    time.sleep(1)  # 等待1s
    print_space('点击等级')
    '''判断本次是否需要执行选择等级'''
    if number_meat == 0:
        number_meat += 1
        collection_lv()
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
    global number_wood
    print_space('准备采集木材资源')
    print_space('点击搜索图标')
    touch([63, 1314])  # 点击搜索图标
    time.sleep(1)  # 等待1s
    swipe([600, 1370], vector=[-0.4103, 0.0170])  # 滑动
    print_space('点击选择木材资源')
    touch([476, 1373])  # 点击选择木材
    time.sleep(1)  # 等待1s
    print_space('点击等级')
    '''判断本次是否需要执行选择等级'''
    if number_wood == 0:
        number_wood += 1
        collection_lv()
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
    global number_coal
    print_space('准备采集煤矿资源')
    print_space('点击搜索图标')
    touch([63, 1314])  # 点击搜索图标
    time.sleep(1)  # 等待1s
    swipe([600, 1370], vector=[-0.4103, 0.0170])  # 滑动
    print_space('点击选择煤矿资源')
    touch([710, 1373])  # 点击选择煤矿
    time.sleep(1)  # 等待1s
    print_space('点击等级')
    '''判断本次是否需要执行选择等级'''
    if number_coal == 0:
        number_coal += 1
        collection_lv()
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
    global number_iron
    print_space('准备采集铁矿资源')
    print_space('点击搜索图标')
    touch([63, 1314])  # 点击搜索图标
    time.sleep(1)  # 等待1s
    swipe([600, 1370], vector=[-0.4103, 0.0170])  # 滑动
    print_space('点击选择铁矿资源')
    touch([950, 1373])  # 点击选择铁矿
    time.sleep(1)  # 等待1s
    print_space('点击等级')
    '''判断本次是否需要执行选择等级'''
    if number_iron == 0:
        number_iron += 1
        collection_lv()
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
        time.sleep(3)
    touch([14, 823])
    time.sleep(1)
    touch([500, 400])
    if not exists(Template(r"icon\tpl1720691682616.png", record_pos=(-0.188, -0.127), resolution=(1080, 1920))):
        print_space('有空闲队伍，执行采肉任务')
        time.sleep(1)
        Meat()
    else:
        print_space('已有采肉队伍')
    if not exists(Template(r"icon\tpl1720766916044.png",threshold=0.7, record_pos=(-0.438, -0.163), resolution=(1080, 1920))):
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
        touch(Template(r"icon\tpl1721191349779.png", threshold=0.8, record_pos=(0.29, 0.756), resolution=(1080, 1920)))
        print_space('点击联盟互助')
        touch(Template(r"icon\tpl1721191349780.png", threshold=0.8, record_pos=(0.142, -0.126), resolution=(1080, 1920)))
        print_space('点击返回按钮')
        touch(Template(r"icon\tpl1719198082012.png", threshold=0.8, record_pos=(-0.44, -0.783), resolution=(1080, 1920)))
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
            if not exists(Template(r"icon\tpl1721784579074.png", rgb=True, record_pos=(-0.44, -0.783), resolution=(1080, 1920))):
                print_space('点击捐献')
                touch(Template(r"icon\tpl1721784579073.png", record_pos=(-0.44, -0.783), resolution=(1080, 1920)),duration = 2)
            else:
                print_space('无捐献次数，结束任务')
                x = 0
    else:
        print_space('无大拇指指引，返回主页')
        touch(Template(r"icon\tpl1719198082012.png", threshold=0.8, record_pos=(-0.44, -0.783), resolution=(1080, 1920)))


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
            touch(Template(r"icon\return.png", threshold=0.8, record_pos=(-0.44, -0.783), resolution=(1080, 1920)))
            time.sleep(1)
        else:
            print_space('无免费招募次数')
        touch(Template(r"icon\return.png", threshold=0.8, record_pos=(-0.44, -0.783), resolution=(1080, 1920)))
        time.sleep(1)
        touch(Template(r"icon\tpl1719198082012.png", threshold=0.8, record_pos=(-0.44, -0.783), resolution=(1080, 1920)))

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
    while True:
        now = datetime.now()
        if now.second % 2 == 0:
            try:
                if int(option_help.get()) == 1:
                    print('\n' + '%d.开始执行互助任务' % run_number)
                    Homepage()  # 主页检查
                    Help()  # 互助模块
                    run_number += 1
                    if stop_event.is_set():
                        start_button.configure(text='开始', command=save_simple)  # 总功能
                        break
                    # else:  #     print_space('不执行互助任务')  #     if stop_event.is_set():  #         start_button.configure(text='开始', command=simle)  # 总功能  #         break
            except:
                print('程序执行异常，结束该任务，执行其他任务')
        if now.minute % 5 == 0 and now.second % 5 == 0 and now.hour != 21:
            try:
                if int(option_XG.get()) == 1:

                    print('\n' + '%d.开始执行野怪任务' % run_number)
                    Homepage()  # 主页检查
                    Brush_XG()  # 野怪
                    run_number += 1
                    if stop_event.is_set():
                        start_button.configure(text='开始', command=save_simple)  # 总功能
                        break
            except:
                print('程序执行异常，结束该任务，执行其他任务')
        if now.minute % 6 == 0 and 0 < now.second < 20 and now.hour != 21:
            try:
                if int(option_WM.get()) == 1:

                    print('\n' + '%d.开始执行冰原巨兽任务' % run_number)
                    Homepage()  # 主页检查
                    Brush_WM()  # 冰原巨兽
                    run_number += 1
                    if stop_event.is_set():
                        start_button.configure(text='开始', command=save_simple)  # 总功能
                        break
            except:
                print('程序执行异常，结束该任务，执行其他任务')
        if now.minute % 6 == 0 and now.hour != 21:
            try:
                if int(option_npc.get()) == 1:

                    print('\n' + '%d.开始执行活动雪怪任务' % run_number)
                    Homepage()  # 主页检查
                    NPC()  # 活动雪怪
                    run_number += 1
                    if stop_event.is_set():
                        start_button.configure(text='开始', command=save_simple)  # 总功能
                        break
            except:
                print('程序执行异常，结束该任务，执行其他任务')
        if now.minute % 5 == 0:
            try:
                if int(option_Production.get()) == 1:

                    print('\n' + '%d.开始执行训练任务' % run_number)
                    Homepage()  # 主页检查
                    Production_soldiers()  # 训练模块
                    run_number += 1
                    if stop_event.is_set():
                        start_button.configure(text='开始', command=save_simple)  # 总功能
                        break
            except:
                print('程序执行异常，结束该任务，执行其他任务')
        if now.minute % 2 == 0:
            try:
                if int(option_build.get()) == 1:
                    print('\n' + '%d.开始执行建造任务' % run_number)
                    Homepage()  # 主页检查
                    Build()  # 建造模块
                    run_number += 1
                    if stop_event.is_set():
                        start_button.configure(text='开始', command=save_simple)  # 总功能
                        break
            except:
                print('程序执行异常，结束该任务，执行其他任务')
        if now.hour == 3:
            try:
                if int(option_Collection.get()) == 1:

                    print('\n' + '%d.开始执行采集任务' % run_number)
                    Homepage()  # 主页检查
                    Collection()  # 采集资源模块
                    run_number += 1
                    if stop_event.is_set():
                        start_button.configure(text='开始', command=save_simple)  # 总功能
                        break
            except:
                print('程序执行异常，结束该任务，执行其他任务')
        if now.hour == 21:
            try:
                if int(option_bear.get()) == 1:

                    print_space('当前时间：%s,巨熊活动进行中' % now.strftime("%H:%M:%S"))
                    Homepage()  # 主页检查
                    bear()  # 巨熊模块
                    run_number += 1
                    if stop_event.is_set():
                        start_button.configure(text='开始', command=save_simple)  # 总功能
                        break
            except:
                print('程序执行异常，结束该任务，执行其他任务')
        if now.minute == 21:
            try:
                if int(option_treatment.get()) == 1:

                    print('\n' + '%d.开始执行治疗任务' % run_number)
                    Homepage()  # 主页检查
                    treatment()  # 治疗模块
                    run_number += 1
                    if stop_event.is_set():
                        start_button.configure(text='开始', command=save_simple)  # 总功能
                        break
            except:
                print('程序执行异常，结束该任务，执行其他任务')
        if now.minute == 25:
            try:
                if int(option_adventure.get()) == 1:

                    print('\n' + '%d.开始执行探险任务' % run_number)
                    Homepage()  # 主页检查
                    adventure()  # 探险
                    run_number += 1
                    if stop_event.is_set():
                        start_button.configure(text='开始', command=save_simple)  # 总功能
                        break
            except:
                print('程序执行异常，结束该任务，执行其他任务')
        if now.minute == 1:
            try:
                if int(option_donate.get()) == 1:
                    print('\n' + '%d.开始执行捐赠任务' % run_number)
                    Homepage()  # 主页检查
                    donate()  # 捐赠模块
                    run_number += 1
                    if stop_event.is_set():
                        start_button.configure(text='开始', command=save_simple)  # 总功能
                        break
            except:
                print('程序执行异常，结束该任务，执行其他任务')
        if now.hour == 1 and now.minute % 5 == 0:
            try:
                if int(option_donate.get()) == 1:
                    print('\n' + '%d.开始执行招募任务' % run_number)
                    Homepage()
                    recruit()
                    run_number += 1
                    if stop_event.is_set():
                        start_button.configure(text='开始', command=save_simple)  # 总功能
                        break
            except:
                print('程序执行异常，结束该任务，执行其他任务')
        if stop_event.is_set():
            start_button.configure(text='开始', command=save_simple)  # 总功能
            break
    print('结束任务')


def print_space(variable, spaces=4):
    print(' ' * spaces + str(variable))



'''-------------------------------------更新公告-----------------------------------------------'''
def gonggao():
    print('当前更新内容：')
    print_space('1.建筑升级优化')
    print_space('2.训练士兵优化')
    print_space('3.新增采集等级设置')
    print_space('4.其他优化')

'''-------------------------------------帮助说明-----------------------------------------------'''
def help_txt():
    print('模拟器路径：')
    print_space('电脑模拟器安装地址，以exe结尾，启动模拟器功能需要，地址错误时无法启动模拟器，只能手动启动')
    print('模拟器ip：')
    print_space('连接模拟器需要，由本地地址＋端口号组成，ip错误将无法连接模拟器，影响使用')
    print('启动游戏：')
    print_space('启动无尽冬日游戏')
    print('一键启动：')
    print_space('包含启动模拟器、连接模拟器、启动游戏功能')
    print('多选：')
    print_space('可一次性选择多选功能同时执行')
    print_space('互助：每2秒检测一次')
    print_space('野怪：分钟与秒是5的倍数是检测一次，21点不检测')
    print_space('冰原巨兽：分钟是6的倍数且秒数在0-20s时检查一次，21点不检测，等级可在单选内设置')
    print_space('活动雪怪：分钟是6的倍数时检测一次，21点不检测')
    print_space('训练士兵：分钟数是5的倍数时检测')
    print_space('建筑升级：分钟数是2的倍数时检测')
    print_space('采集资源：凌晨3点检测每一种资源是否有采集，每种只会采集一队')
    print_space('巨熊活动：21点时检测')
    print_space('治疗士兵：分钟数为21时检测，相当于每过一小时就检查')
    print_space('探险奖励：分钟数为25时检测，相当于每过一小时就检查')
    print_space('联盟捐赠：分钟数为1时检测，相当于每过一小时就检查')
    print_space('英雄招募：凌晨1点时分钟数为5的倍数时会检查')
    print('单选：')
    print_space('每次只能执行单个功能，可设置单个功能执行间隔，冰原巨兽可设置等级，设置的等级多选可用')
# --distpath

# pyinstaller  -w  --onefile --name "无尽冬日" --icon "E:\测试文件\测试工具\版本控制\Wjdr\main_icon.ico" --add-data "E:\测试文件\测试工具\AirtestIDE\airtest:airtest" --add-data "E:\测试文件\测试工具\版本控制\Wjdr\icon:icon" --add-data "E:\测试文件\测试工具\版本控制\Wjdr\wjdr.py:." E:\测试文件\测试工具\版本控制\Wjdr\wjdrwjdr_release.py
# pip install numpy==1.21.1
#pyi-makespec  -w  --hidden-import=six --name "main" --icon "E:\测试文件\测试工具\版本控制\Wjdr\old\icon\log.png" --add-data "E:\测试文件\测试工具\AirtestIDE\airtest:airtest"  E:\测试文件\测试工具\版本控制\Wjdr\old\wjdr_release.py

"""可视化界面代码"""


def start_simple(button_start_id):
    if button_start_id == 1:
        start_exe_button.configure(text='启动模拟器', command=lambda: start_simple(1))
        # start_exe()
        '''启动模拟器线程'''
        threading.Thread(target=start_exe).start()  # threading.Thread(target=start_exe).join()
    elif button_start_id == 2:
        '''连接模拟器线程'''
        threading.Thread(target=cnnect).start()  # threading.Thread(target=cnnect).join()
    elif button_start_id == 3:
        start_app_button.configure(text='再次启动app', command=lambda: start_simple(3))
        # start_app()
        '''启动app线程'''
        threading.Thread(target=start_app).start()  # threading.Thread(target=start_app).join()
    elif button_start_id == 4:
        '''一键启动线程'''
        threading.Thread(target=all_start).start()
    else:
        print_space('错误')


'''启动准备'''

'''一键启动'''
def all_start():
    start_exe()
    print('等待30s以完成模拟器的启动')
    time.sleep(30)
    cnnect()
    print('等待10s以确保系统加载完成')
    time.sleep(10)
    start_app()


'''启动复选功能主线程'''
def simple():
    # 点击后按钮变化
    start_button.configure(text='停止', command=stop_function)
    print("程序开始执行...")
    # 这里放置程序开始时需要执行的代码
    stop_event.clear()
    threading.Thread(target=subject).start()

'''保存选项'''
def save_simple():
    simple()
    save_options()

'''停止复选功能主线程'''
def stop_function():
    # 这里放置程序停止时需要执行的代码
    global stop_event
    stop_event.set()  # 设置事件，通知线程结束运行
    print("------------等待当前任务完成或10s左右结束任务------------")


stop_event = threading.Event()

'''------------------------------------窗口在电脑屏幕中的位置------------------------------------'''


def center_window(root, width, height):
    # 获取屏幕尺寸
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 计算窗口居中位置
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    # 设置窗口在屏幕上的位置
    root.geometry(f"{width}x{height}+{x}+{y}")

#控件隐藏
def hide_widgets():
    global label_2,version_label
    # 创建一个标签来显示图片
    label_2 = tk.Label(window, image=image)
    #label_2.image = image  # 防止图片被垃圾回收
    label_2.place(x=-2, y=-2)
    ttk.Button(window,text='显示UI',command=hide_widget,width=6).place(x=0, y=513)
    ttk.Label(window, text='版本:%s'%set_version.get()).place(x=901, y=518)
#控件显示
def hide_widget():
    global label_2,version_label
    label_2.place_forget()
    ttk.Button(window, text="隐藏UI",command=hide_widgets,width=6).place(x=0, y=513)
    ttk.Label(window, text='版本:%s'%set_version.get()).place(x=901, y=518)

'''------------------------------------创建主窗口------------------------------------'''
window = tk.Tk()
window.title("无尽冬日")  # 设置窗口标题
# window.geometry("500x600")  # 设置窗口大小
icon = tk.PhotoImage(file="icon/log.png")  # 设置窗口图标
window.iconphoto(True, icon)
#window.attributes("-transparent color", '')
#window.attributes("-topmost", True)
# 设置窗口不能调整大小
window.resizable(False, False)
window.resizable(False, False)
# 调用函数居中窗口
center_window(window, 960, 540)
#背景图判断
'''def background_
icon(evevt):
    global label_1
    if background_button.current() == 0:
        background_image = Image.open("icon/11.png")
        background_image = background_image.resize((960, 540))
        image = ImageTk.PhotoImage(background_image)
        window.mainloop()
    elif background_button.current() == 1:
        background_image = Image.open("icon/22.png")
        background_image = background_image.resize((960, 540))
        image = ImageTk.PhotoImage(background_image)
        window.mainloop()
    else:
        print_space('asda')'''
# 加载背景图片
background_image = Image.open("icon/11.png")
background_image = background_image.resize((960, 540))
image = ImageTk.PhotoImage(background_image)
label_1 = tk.Label(window, image=image)
label_1.place(x=-2, y=-2)
# 创建一个UI控制标签
ttk.Button(window, text="隐藏UI",command=hide_widgets,width=6).place(x=0, y=513)
ttk.Button(window,text='更新内容',command=gonggao,width=7).place(x=80,y=513)
ttk.Button(window,text='使用说明',command=help_txt,width=7).place(x=160,y=513)
#创建一个背景控制标签
'''background_button = ttk.Combobox(window,width=6,state='readonly')
background_button['value'] = ('背景1','背景2')
background_button.current(0)
background_button.bind('<<ComboboxSelected>>', background_icon)
background_button.place(x=50, y=513)'''

'''------------------------------------大标题------------------------------------'''
'''提示文本'''
#prompt_text = tkFont.Font(window,family="Helvetica", size=10, weight=tkFont.NORMAL)
#tk.Label(window,text='请等待程序停止后再设置相关参数', anchor='center', font=prompt_text).pack()
tk.Label(text='请等待程序停止后再设置相关参数').pack()
tk.Label(text='多选和单选不可同时执行').pack()
'''保存模拟器地址'''
def save_address():
    if emulator_entry.get() == '':
        print('输入框为空')
    else:
        if text_address.current() ==0:
            config.set('Options', '模拟器路径',emulator_entry.get())
        elif text_address.current() == 1:
            config.set('Options', '模拟器ip', emulator_entry.get())
        with open('set.ini', 'w') as configfile:
            config.write(configfile)
        load_options()
        print('保存成功！！！')
def on_select(event):
    if text_address.current() == 0:
        emulator_entry.delete(0, tk.END)
        emulator_entry.insert(0,set_address.get())  #获取配置文件内模拟器地址并放入输入框
    elif text_address.current() == 1:
        emulator_entry.delete(0, tk.END)
        emulator_entry.insert(0, set_ip.get())

#address = tk.Frame(window, width=400, height=27)
#address.place(x=5,y=30)
text_address = ttk.Combobox(window,width=9,state='readonly')
text_address['value'] = ('模拟器路径','模拟器ip')
text_address.current(0)
text_address.place(x=3,y=62)
text_address.bind('<<ComboboxSelected>>', on_select)
emulator_entry = tk.Entry(window ,width=30)
emulator_entry.place(x=91,y=62)
save_address_button = ttk.Button(window,text='保存',command=save_address)
save_address_button.place(x=310,y=60)
'''------------------------------------模拟器相关按钮------------------------------------'''
'''创建区域'''
frame_mumu = tk.Frame(window,width=400, height=27)
#frame_mumu.place(x=5,y=70)
'''创建按钮'''
start_exe_button = ttk.Button(window, text='启动模拟器', command=lambda: start_simple(1))
start_exe_button.place(x=6, y=110)
cnnect_button = ttk.Button(window, text='连接模拟器', command=lambda: start_simple(2))
cnnect_button.place(x=106,y=110)
start_app_button = ttk.Button(window, text='启动游戏', command=lambda: start_simple(3))
start_app_button.place(x=206,y=110)
all_button = ttk.Button(window, text='一键启动', command=lambda: start_simple(4))
all_button.place(x=306,y=110)


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
    global number_brush,number_meat,number_iron,number_wood,number_coal
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
            config.set('Options','冰原巨兽设置',WM_time)
            config.set('Options','冰原巨兽等级设置',WM_number)
            print('设置成功！！！')
        elif int(var.get()) == 3:
            npc_time = entry.get()
            config.set('Options','活动雪怪设置',npc_time)
            print('设置成功！！！')
        elif int(var.get()) == 4:
            Production_time = entry.get()
            config.set('Options','训练士兵设置',Production_time)
            print('设置成功！！！')
        elif int(var.get()) == 5:
            build_time = entry.get()
            config.set('Options', '建筑升级设置', build_time)
            print('设置成功！！！')
        elif int(var.get()) == 6:
            number_meat = 0
            number_wood = 0
            number_coal = 0
            number_iron = 0
            Collection_time = entry.get()
            collection_lv = entry_number.get()
            config.set('Options', '采集资源设置', Collection_time)
            config.set('Options', '采集等级设置', collection_lv)
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
            config.set('Options', '英雄招募设置',recruit_time)
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
    set_WM_time.set(config.get('Options','冰原巨兽设置'))
    set_npc_time.set(config.get('Options','活动雪怪设置'))
    set_Production_time.set(config.get('Options', '训练士兵设置'))
    set_build_time.set(config.get('Options', '建筑升级设置'))
    set_Collection_time.set(config.get('Options', '采集资源设置'))
    set_bear_time.set(config.get('Options', '巨熊活动设置'))
    set_treatment_time.set(config.get('Options', '治疗士兵设置'))
    set_adventure_time.set(config.get('Options', '探险奖励设置'))
    set_donate_time.set(config.get('Options', '联盟捐赠设置'))
    set_WM_number.set(config.get('Options', '冰原巨兽等级设置'))
    set_collection_lv.set(config.get('Options', '采集等级设置'))
    set_recruit_time.set(config.get('Options', '英雄招募设置'))
    set_version.set(config.get('Options', 'version'))
'''初始化配置解析器和选项变量'''
config = ConfigParser()
config['Options'] = {}
'''单选'''
var = tk.StringVar()
'''多选'''
set_ip = tk.StringVar()   #设置模拟器ip
set_address = tk.StringVar() #设置模拟器地址
option_help = tk.StringVar()  # 互助
option_XG = tk.StringVar()  # 野怪
option_WM = tk.StringVar()  # 巨兽
option_npc = tk.StringVar()  # 雪怪
option_Production = tk.StringVar()  # 士兵
option_build = tk.StringVar()  # 建筑
option_Collection = tk.StringVar()  # 采集
option_bear = tk.StringVar()  # 巨熊
option_treatment = tk.StringVar()  # 治疗
option_adventure = tk.StringVar()  # 探险
option_donate = tk.StringVar()  # 捐赠
option_recruit = tk.StringVar() #招募
set_help_time = tk.StringVar()#互助
set_XG_time = tk.StringVar()#野怪
set_WM_time = tk.StringVar()#巨兽
set_npc_time = tk.StringVar()#雪怪
set_Production_time = tk.StringVar()#士兵
set_build_time = tk.StringVar()#建筑
set_Collection_time = tk.StringVar()#采集
set_bear_time = tk.StringVar()#巨熊
set_treatment_time = tk.StringVar()#治疗
set_adventure_time = tk.StringVar()#探险
set_donate_time = tk.StringVar()#捐赠
set_WM_number = tk.StringVar()#冰原巨兽等级
set_collection_lv = tk.StringVar()#采集等级设置
set_recruit_time = tk.StringVar() #招募设置
set_version = tk.StringVar()#设置版本号
# 尝试加载先前保存的选项
def read_save():
    # 首次启动时默认选项
    if not config.read('set.ini'):
        config.set('Options','模拟器ip','127.0.0.1:5037')
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
        config.set('Options', '冰原巨兽等级设置', '6')
        config.set('Options', '采集等级设置', '7')
        config.set('Options', '英雄招募设置', '300')
        config.set('Options', 'version', '1.2.0')
        with open('set.ini', 'w') as configfile:
            config.write(configfile)
    try:
        with open('set.ini', 'r') as configfile:
            config.read_file(configfile)
        load_options()
    except IOError:
        print('No saved options found.')
read_save()
'''------------------------------------多选功能区功能------------------------------------'''
'''创建 frame(区域框)，设置宽度和高度'''
frame = tk.Frame(window, width=400, height=150)
#frame.place(x=5,y=120)

'''标签'''
title = tk.Label(window, text='功能选项(多选)：')
title.place(x=6,y=170)
#frame.create_window(55, 15, window=title)
'''全选'''

def select_all():
    for checkbox in checkboxes:
        checkbox.select()


'''取消全选'''

def deselect_all():
    for checkbox in checkboxes:
        checkbox.deselect()


'''保存全选'''


def save_select_all():
    select_all()
    save_options()


'''保存取消全选'''


def save_deselect_all():
    deselect_all()
    save_options()


checkboxes = []  # 创建11个复选框的状态变量

'''联盟互助'''
for i in range(1, 12):
    # option_help.set('1')  # 设置复选框的默认值为选中状态
    checkbox = tk.Checkbutton(window, text='联盟互助',width=6,height=1,  variable=option_help, command=save_options)
    #frame.create_window(88, 45, window=checkbox)
    checkbox.place(x=9,y=210)
    checkboxes.append(checkbox)
'''世界野怪'''
for i in range(1, 12):
    # option_XG.set(1)  # 设置复选框的默认值为选中状态
    checkbox = tk.Checkbutton(window, text='世界野怪',width=6,height=1, variable=option_XG, command=save_options)
    #frame.create_window(168, 45, window=checkbox)
    checkbox.place(x=89, y=210)
    checkboxes.append(checkbox)
'''冰原巨兽'''
for i in range(1, 12):
    # option_WM = tk.IntVar()
    # option_WM.set(1)  # 设置复选框的默认值为选中状态
    checkbox = tk.Checkbutton(window, text='冰原巨兽',width=6,height=1, variable=option_WM, command=save_options)
    #frame.create_window(248, 45, window=checkbox)
    checkbox.place(x=169, y=210)
    checkboxes.append(checkbox)
'''活动雪怪'''
for i in range(1, 12):
    # option_npc = tk.IntVar()
    # option_npc.set(1)  # 设置复选框的默认值为选中状态
    checkbox = tk.Checkbutton(window, text='活动雪怪',width=6,height=1, variable=option_npc, command=save_options)
    #frame.create_window(328, 45, window=checkbox)
    checkbox.place(x=249,y=210)
    checkboxes.append(checkbox)
'''训练士兵'''
for i in range(1, 12):
    # option_Production = tk.IntVar()
    # option_Production.set(1)  # 设置复选框的默认值为选中状态
    checkbox = tk.Checkbutton(window, text='训练士兵',width=6,height=1, variable=option_Production, command=save_options)
    #frame.create_window(88, 75, window=checkbox)
    checkbox.place(x=329, y=210)
    checkboxes.append(checkbox)
'''建筑升级'''
for i in range(1, 12):
    # option_build = tk.IntVar()
    # option_build.set(1)  # 设置复选框的默认值为选中状态
    checkbox = tk.Checkbutton(window, text='建筑升级',width=6,height=1, variable=option_build, command=save_options)
    #frame.create_window(168, 75, window=checkbox)
    checkbox.place(x=9, y=250)
    checkboxes.append(checkbox)
'''采集资源'''
for i in range(1, 12):
    # option_Collection = tk.IntVar()
    # option_Collection.set(1)  # 设置复选框的默认值为选中状态
    checkbox = tk.Checkbutton(window, text='采集资源',width=6,height=1, variable=option_Collection, command=save_options)
    #frame.create_window(248, 75, window=checkbox)
    checkbox.place(x=89, y=250)
    checkboxes.append(checkbox)
'''巨熊活动'''
for i in range(1, 12):
    # option_bear = tk.IntVar()
    # option_bear.set(1)  # 设置复选框的默认值为选中状态
    checkbox = tk.Checkbutton(window, text='巨熊活动',width=6,height=1, variable=option_bear, command=save_options)
    #frame.create_window(328, 75, window=checkbox)
    checkbox.place(x=169, y=250)
    checkboxes.append(checkbox)
'''治疗士兵'''
for i in range(1, 12):
    # option_treatment = tk.IntVar()
    # option_treatment.set(1)  # 设置复选框的默认值为选中状态
    checkbox = tk.Checkbutton(window, text='治疗士兵',width=6,height=1, variable=option_treatment, command=save_options)
    #frame.create_window(88, 105, window=checkbox)
    checkbox.place(x=249, y=250)
    checkboxes.append(checkbox)
'''探险奖励'''
for i in range(1, 12):
    # option_adventure = tk.IntVar()
    # option_adventure.set(1)  # 设置复选框的默认值为选中状态
    checkbox = tk.Checkbutton(window, text='探险奖励',width=6,height=1, variable=option_adventure, command=save_options)
    #frame.create_window(168, 105, window=checkbox)
    checkbox.place(x=329, y=250)
    checkboxes.append(checkbox)
'''联盟捐赠'''
for i in range(1, 12):
    # option_donate = tk.IntVar()
    # option_donate.set(1)  # 设置复选框的默认值为选中状态
    checkbox = tk.Checkbutton(window, text='联盟捐赠',width=6,height=1, variable=option_donate, command=save_options)
    #frame.create_window(248, 105, window=checkbox)
    checkbox.place(x=9, y=290)
    checkboxes.append(checkbox)
for i in range(1, 12):
    # option_donate = tk.IntVar()
    # option_donate.set(1)  # 设置复选框的默认值为选中状态
    checkbox = tk.Checkbutton(window, text='英雄招募',width=6,height=1, variable=option_recruit, command=save_options)
    #frame.create_window(328, 105, window=checkbox)
    checkbox.place(x=89, y=290)
    checkboxes.append(checkbox)

'''------------------------------------多选功能区功能按钮------------------------------------'''
'''创建按钮'''
select_button = ttk.Button(window, text="全选", command=save_select_all)
#frame.create_window(100, 135, window=select_button)
select_button.place(x=65, y = 330)
start_button = ttk.Button(window, text="开始", command=save_simple)
#frame.create_window(200, 135, window=start_button)
start_button.place(x=165, y=330)
select_all_button = ttk.Button(window, text="取消全选", command=save_deselect_all)
#frame.create_window(300, 135, window=select_button)
select_all_button.place(x=265, y = 330)

'''------------------------------------单选功能区功能------------------------------------'''

'''区域'''
frame_simple = tk.Frame(window, width=400, height=150)
# frame_simple.place(x=50,y=230)
#frame_simple.place(x=5,y=280)
#frame_simple.create_rectangle(1, 1, 400, 150, width=0)

'''标签'''
title = tk.Label(window, text='功能选项(单选):',width=12)
#frame_simple.create_window(55, 15, window=title)
title.place(x=470,y=60)
'''文本标题'''
imput_text = tk.Label(window,text='执行间隔(秒):',width=10)
#frame_simple.create_window(130, 15, window=imput_text)
imput_text.place(x=580,y=60)
'''输入框'''
entry = tk.Entry(window,width=4)
#frame_simple.create_window(180, 15, window=entry)
entry.place(x=655,y=60)
# 绑定一个点击事件到entry，当点击entry时，调用clear_entry函数
entry.bind("<Button-1>",entry.delete(0, tk.END))
time_unit = tk.Label(window,text='秒')
#frame_simple.create_window(200, 15, window=time_unit)
#time_unit.place(x=195,y=280)
WM_number = tk.Label(window, text='等级:',width=4)
entry_number = tk.Entry(window, width=4)


'''保存按钮'''
save_set_time_button = ttk.Button(window,text='设置',width=8,command=save_simple_set)
#frame_simple.create_window(340, 15, window=save_set_time_button)
save_set_time_button.place(x=810,y=60)
''''自定义单项功能的重新执行时间'''
'''选中选项时输入框获取对应选项的时间'''
def dropdown_changed():
    emulator_entry.delete(0, tk.END) #初始化模拟器地址输入框
    emulator_entry.insert(0,set_address.get())  #获取配置文件内模拟器地址并放入输入框
    WM_number.place_forget()   #隐藏冰原巨兽等级文本
    entry_number.place_forget()   #隐藏冰原巨兽等级输入框
    if int(var.get()) == 0:               #互助
        entry.delete(0,'end')
        entry.insert(0,set_help_time.get())
    elif int(var.get()) == 1:             #野怪
        entry.delete(0,'end')
        entry.insert(0,set_XG_time.get())
    elif int(var.get()) == 2:             #冰原巨兽
        WM_number.place(x=715,y=60)
        entry_number.place(x=750,y=60)
        entry.delete(0,'end')
        entry_number.delete(0,'end')
        entry.insert(0,set_WM_time.get())
        entry_number.insert(0,set_WM_number.get())
    elif int(var.get()) == 3:
        entry.delete(0,'end')
        entry.insert(0,set_npc_time.get())
    elif int(var.get()) == 4:
        entry.delete(0,'end')
        entry.insert(0,set_Production_time.get())
    elif int(var.get()) == 5:
        entry.delete(0,'end')
        entry.insert(0,set_build_time.get())
    elif int(var.get()) == 6:
        WM_number.place(x=715, y=60)
        entry_number.place(x=750, y=60)
        entry.delete(0,'end')
        entry_number.delete(0, 'end')
        entry.insert(0,set_Collection_time.get())
        entry_number.insert(0, set_collection_lv.get())
    elif int(var.get()) == 7:
        entry.delete(0,'end')
        entry.insert(0,set_bear_time.get())
    elif int(var.get()) == 8:
        entry.delete(0,'end')
        entry.insert(0,set_treatment_time.get())
    elif int(var.get()) == 9:
        entry.delete(0,'end')
        entry.insert(0,set_adventure_time.get())
    elif int(var.get()) == 10:
        entry.delete(0,'end')
        entry.insert(0,set_donate_time.get())
    elif int(var.get()) == 11:
        entry.delete(0,'end')
        entry.insert(0,set_recruit_time.get())
dropdown_changed()
'''下拉框'''
'''combo_box = ttk.Combobox(window,width=8,state='readonly')
combo_box['values'] = ['联盟互助', '世界野怪', '冰原巨兽','活动雪怪','训练士兵','建筑升级','采集资源','巨熊活动','治疗士兵','探险奖励','联盟捐赠']
combo_box.current(int(var.get()))  # 设置打开时默认选中
combo_box.bind("<<ComboboxSelected>>", dropdown_changed)
frame_simple.create_window(140, 15, window=combo_box)'''


def simple_start_button():
    start_button_simple.configure(text='停止', command=stop_function)
    print("程序开始执行...")
    stop_event.clear()
    threading.Thread(target=simple_select).start()


'''单项停止按钮'''


def simple_stop_button():
    global stop_event
    stop_event.set()  # 设置事件，通知线程结束运行


def save_simple_start_button():
    if entry.get() != '':
        simple_start_button()
        save_options()
    else:
        print('-------------间隔时间不能为空-------------')


'''单项运行函数'''


def simple_select():
    if emulator_click == 0:
        time.sleep(1)
        print('未连接模拟器')
        time.sleep(1)
        cnnect()
    var_value = int(var.get())
    execute = True
    if var_value == 0:
        while True:
            try:
                Homepage()
                Help()
                if stop_event.is_set():
                    start_button_simple.configure(text='开始', command=save_simple_start_button)  # 互助功能
                    break
                help_time = set_help_time.get()
                #print('%s'%help_time)
                print_space('等待%s秒后继续执行任务'%help_time+'\n')
                XG_number = int(help_time)
                time.sleep(XG_number)
            except:
                print('错误')
    elif var_value == 1:
        while execute:
            try:
                Homepage()
                Brush_XG()
                if stop_event.is_set():
                    start_button_simple.configure(text='开始', command=save_simple_start_button)  # 野怪功能
                    break
                XG_time = int(set_XG_time.get())
                print_space('等待%s秒后再次执行'%XG_time+'\n')
                number = 0
                XG_number = XG_time / 10
                while XG_number > number:
                    if stop_event.is_set():
                        execute = False
                        start_button_simple.configure(text='开始', command=save_simple_start_button)  # 野怪功能
                        break
                    else:
                        if XG_number < 1:
                            time.sleep(XG_time)
                            break
                        else:
                            number += 1
                            time.sleep(10)
            except:
                print('错误')
    elif var_value == 2:   #冰原巨兽
        while execute:
            try:
                Homepage()
                Brush_WM()
                if stop_event.is_set():
                    start_button_simple.configure(text='开始', command=save_simple_start_button)  # 停止后按钮变为开始
                    break
                WM_time = int(set_WM_time.get())
                print_space('等待%s秒后再次执行'%WM_time+'\n')
                number = 0
                WM_number = WM_time / 10
                while number < WM_number:
                    if stop_event.is_set():
                        execute = False
                        start_button_simple.configure(text='开始', command=save_simple_start_button)  # 野怪功能
                        break
                    else:
                        if WM_number < 1:
                            time.sleep(WM_time)
                            break
                        else:
                            number += 1
                            time.sleep(10)
            except:
                print('错误')
    elif var_value == 3:
        while execute:
            try:
                Homepage()
                NPC()
                if stop_event.is_set():
                    start_button_simple.configure(text='开始', command=save_simple_start_button)  # 停止后按钮变为开始
                    break
                npc_time = int(set_XG_time.get())
                print_space('等待%s秒后再次执行'%npc_time+'\n')
                number = 0
                npc_number = npc_time / 10
                while number < npc_number:
                    if stop_event.is_set():
                        execute = False
                        start_button_simple.configure(text='开始', command=save_simple_start_button)
                        break
                    else:
                        if npc_number < 1:
                            time.sleep(npc_time)
                            break
                        else:
                            number += 1
                            time.sleep(10)
            except:
                print('错误')
    elif var_value == 4:                             #训练士兵
        while execute:
            try:
                Homepage()
                Production_soldiers()
                if stop_event.is_set():
                    start_button_simple.configure(text='开始', command=save_simple_start_button)  # 停止后按钮变为开始
                    break
                Production_time = int(set_Production_time.get())
                print_space('等待%s秒后再次执行'%Production_time+'\n')
                Production_number = Production_time / 10
                number = 0
                while number < Production_number:
                    if stop_event.is_set():
                        execute = False
                        start_button_simple.configure(text='开始', command=save_simple_start_button)
                        break
                    else:
                        if Production_number < 1:
                            time.sleep(Production_time)
                            break
                        else:
                            number += 1
                            time.sleep(10)
            except:
                print('错误')
    elif var_value == 5:
        while execute:
            try:
                Homepage()
                Build()
                if stop_event.is_set():
                    start_button_simple.configure(text='开始', command=save_simple_start_button)  # 停止后按钮变为开始
                    break
                build_time = int(set_build_time.get())
                print_space('等待%s秒后再次执行' % build_time + '\n')
                build_number = build_time / 10
                number = 0
                while number < build_number:
                    if stop_event.is_set():
                        execute = False
                        start_button_simple.configure(text='开始', command=save_simple_start_button)
                        break
                    else:
                        if build_number < 1:
                            time.sleep(build_time)
                            break
                        else:
                            number += 1
                            time.sleep(10)
            except:
                print('错误')
    elif var_value == 6:
        while execute:
            try:
                Homepage()
                Collection()
                if stop_event.is_set():
                    start_button_simple.configure(text='开始', command=save_simple_start_button)  # 停止后按钮变为开始
                    break
                Collection_time = int(set_Collection_time.get())
                print_space('等待%s秒后再次执行' % Collection_time + '\n')
                number = 0
                Collection_number = Collection_time / 10
                while number < Collection_number:
                    if stop_event.is_set():
                        execute = False
                        start_button_simple.configure(text='开始', command=save_simple_start_button)  # 野怪功能
                        break
                    else:
                        if Collection_number < 1:
                            time.sleep(Collection_time)
                            break
                        else:
                            number += 1
                            time.sleep(10)
            except:
                print('错误')
    elif var_value == 7:
        while execute:
            try:
                Homepage()
                bear()
                if stop_event.is_set():
                    start_button_simple.configure(text='开始', command=save_simple_start_button)  # 停止后按钮变为开始
                    break
                bear_time = int(set_bear_time.get())
                print_space('等待%s秒后再次执行' % bear_time + '\n')
                number = 0
                bear_number = bear_time / 10
                while number < bear_number:
                    if stop_event.is_set():
                        execute = False
                        start_button_simple.configure(text='开始', command=save_simple_start_button)  # 野怪功能
                        break
                    else:
                        if bear_number < 1:
                            time.sleep(bear_time)
                            break
                        else:
                            number += 1
                            time.sleep(10)
            except:
                print('错误')
    elif var_value == 8:       #治疗
        while execute:
            try:
                Homepage()
                treatment()
                if stop_event.is_set():
                    start_button_simple.configure(text='开始', command=save_simple_start_button)  # 停止后按钮变为开始
                    break
                treatment_time = int(set_treatment_time.get())
                print_space('等待%s秒后再次执行' % treatment_time + '\n')
                number = 0
                treatment_number = treatment_time / 10
                while number < treatment_number:
                    if stop_event.is_set():
                        execute = False
                        start_button_simple.configure(text='开始', command=save_simple_start_button)
                        break
                    else:
                        if treatment_number < 1:
                            time.sleep(treatment_time)
                            break
                        else:
                            number += 1
                            time.sleep(10)
            except:
                print('错误')
    elif var_value == 9:
        while execute:
            try:
                Homepage()
                adventure()
                if stop_event.is_set():
                    start_button_simple.configure(text='开始', command=save_simple_start_button)  # 停止后按钮变为开始
                    break
                adventure_time = int(set_adventure_time.get())
                print_space('等待%s秒后再次执行' % adventure_time + '\n')
                number = 0
                adventure_number = adventure_time / 10
                while number < adventure_number:
                    if stop_event.is_set():
                        execute = False
                        start_button_simple.configure(text='开始', command=save_simple_start_button)  # 野怪功能
                        break
                    else:
                        if adventure_number < 1:
                            time.sleep(adventure_time)
                            break
                        else:
                            number += 1
                            time.sleep(10)
            except:
                print('错误')
    elif var_value == 10:
        while execute:
            try:
                Homepage()
                donate()
                if stop_event.is_set():
                    start_button_simple.configure(text='开始', command=save_simple_start_button)  # 停止后按钮变为开始
                    break
                donate_time = int(set_donate_time.get())
                print_space('等待%s秒后再次执行' % donate_time + '\n')
                number = 0
                donate_number = donate_time / 10
                while number < donate_number:
                    if stop_event.is_set():
                        execute = False
                        start_button_simple.configure(text='开始', command=save_simple_start_button)  # 野怪功能
                        break
                    else:
                        if donate_number < 1:
                            time.sleep(donate_time)
                            break
                        else:
                            number += 1
                            time.sleep(10)
            except:
                print('错误')
    elif var_value == 11:
        while execute:
            try:
                Homepage()
                recruit()
                if stop_event.is_set():
                    start_button_simple.configure(text='开始', command=save_simple_start_button)  # 停止后按钮变为开始
                    break
                recruit_time = int(set_recruit_time.get())
                print_space('等待%s秒后再次执行' % recruit_time + '\n')
                number = 0
                recruit_number = recruit_time / 10
                while number < recruit_number:
                    if stop_event.is_set():
                        execute = False
                        start_button_simple.configure(text='开始', command=save_simple_start_button)  # 野怪功能
                        break
                    else:
                        if recruit_number < 1:
                            time.sleep(recruit_time)
                            break
                        else:
                            number += 1
                            time.sleep(10)
            except:
                print('错误')
    print('任务已结束')
'''------------------------------------单选项选项------------------------------------'''
# 创建单选项并添加选项
'''联盟互助'''
select_help = tk.Radiobutton(window, text='联盟互助',width=6,height=1,  variable=var, value=0,command=dropdown_changed)
#frame_simple.create_window(88, 45, window=select_help)
select_help.place(x=480, y=100)
'''世界野怪'''
select_XG = tk.Radiobutton(window, text='世界野怪',width=6,height=1,  variable=var, value=1,command=dropdown_changed)
#frame_simple.create_window(168, 45, window=select_XG)
select_XG.place(x=560,y=100)
'''冰原巨兽'''
select_WM = tk.Radiobutton(window, text='冰原巨兽',width=6,height=1,  variable=var, value=2,command=dropdown_changed)
#frame_simple.create_window(248, 45, window=select_WM)
select_WM.place(x=640,y=100)
'''活动雪怪'''
select_npc = tk.Radiobutton(window, text='活动雪怪',width=6,height=1,  variable=var, value=3,command=dropdown_changed)
#frame_simple.create_window(328, 45, window=select_npc)
select_npc.place(x=720,y=100)
'''训练士兵'''
select_production = tk.Radiobutton(window, text='训练士兵',width=6,height=1,  variable=var, value=4,command=dropdown_changed)
#frame_simple.create_window(88, 75, window=select_production)
select_production.place(x=800,y=100)
'''建筑升级'''
select_build = tk.Radiobutton(window, text='建筑升级',width=6,height=1,  variable=var, value=5,command=dropdown_changed)
#frame_simple.create_window(168, 75, window=select_build)
select_build.place(x=480,y=140)
'''采集资源'''
select_collection = tk.Radiobutton(window, text='采集资源',width=6,height=1,  variable=var, value=6,command=dropdown_changed)
#frame_simple.create_window(248, 75, window=select_collection)
select_collection.place(x=560,y=140)
'''巨熊活动'''
select_bear = tk.Radiobutton(window, text='巨熊活动',width=6,height=1,  variable=var, value=7,command=dropdown_changed)
#frame_simple.create_window(328, 75, window=select_bear)
select_bear.place(x=640,y=140)
'''治疗士兵'''
select_treatment = tk.Radiobutton(window, text='治疗士兵',width=6,height=1,  variable=var, value=8,command=dropdown_changed)
#frame_simple.create_window(88, 105, window=select_treatment)
select_treatment.place(x=720,y=140)
'''探险奖励'''
select_adventure = tk.Radiobutton(window, text='探险奖励',width=6,height=1,  variable=var, value=9,command=dropdown_changed)
#frame_simple.create_window(168, 105, window=select_adventure)
select_adventure.place(x=800,y=140)
'''联盟捐赠'''
select_donate = tk.Radiobutton(window, text='联盟捐赠',width=6,height=1,  variable=var, value=10,command=dropdown_changed)
#frame_simple.create_window(248, 105, window=select_donate)
select_donate.place(x=480,y=180)
'''英雄招募'''
select_recruit = tk.Radiobutton(window,text='英雄招募',width=6,height=1, variable=var,value=11,command=dropdown_changed)
#frame_simple.create_window(328,105, window=select_recruit)
select_recruit.place(x=560,y=180)
'''开始按钮'''
start_button_simple = ttk.Button(window, text='开始', command=save_simple_start_button)
#frame_simple.create_window(200, 135, window=start_button_simple)
start_button_simple.place(x=640,y=220)
'''------------------------------------输出区域------------------------------------'''
'''区域'''
frame_output = tk.Frame(window,width=490,height=300)
#frame_output.place(x=450,y=30)
'''创建一个ScrolledText控件作为输出框'''
output_text = tk.Label(window, text='输出:')
output_text.place(x=450,y=270)
output_box = ScrolledText(window, width=65, height=16, takefocus=0)
output_box.place(x=450,y=300)
# sys.stdout.write = print(output_box)#写入输出框
'''------------------------------------版本号------------------------------------'''
ttk.Label(window, text='版本:%s'%set_version.get()).place(x=901,y=518)




def print(text_1):
    #    str_args = " ".join(str(arg) for arg in args)
    output_box.configure(state="normal")
    output_box.insert('end', text_1 + '\n')  # 换行显示
    output_box.see("end")  # 显示最底部内容
    output_box.configure(state="disabled")
# 开始Tkinter事件循环
tk.mainloop()

