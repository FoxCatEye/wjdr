# -*- encoding=utf8 -*-
__author__ = "猫耳小刻晴"

import logging
import subprocess
import threading
import time
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from configparser import ConfigParser
from tkinter import font as tkFont
from tkinter.scrolledtext import ScrolledText
from airtest.core.api import *
from airtest.core.android.android import *

auto_setup(__file__)
logging.getLogger('airtest').setLevel(logging.ERROR)
'''模拟器点击变量'''
emulator_click = 0

'''打开模拟器'''


def start_exe():
    try:
        print('开始启动雷电模拟器')
        subprocess.Popen('E:\leidian\LDPlayer9\dnplayer.exe')
        print('启动成功')
    except:
        print_space('未找到雷电模拟器')


# 连接模拟器
def cnnect():
    global emulator_click
    emulator_click = 1
    a = 1
    while a > 0:  # 连接模拟器
        try:
            print('%d.开始尝试连接模拟器' % a)
            subprocess.run(["adb", "connect", "127.0.0.1:5037"])
            connect_device("android://127.0.0.1:5037")
            time.sleep(5)
            print_space('连接模拟器成功!!!')
            a = 0
        except:
            a += 1
            print('未连接到模拟器，10s后重新执行')
            time.sleep(1)


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
            touch(Template(r"icon\tpl1719196072757.png", record_pos=(0.112, -0.519), resolution=(414, 780)))
            print_space("等待25秒启动时间...")
            time.sleep(25)
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
            if exists(Template(r"icon\tpl1719198809581.png", threshold=0.9, record_pos=(-0.398, 0.819), scale_max=800, resolution=(
            414, 780))):
                print_space("在主页，准备执行任务")  # 在主界面，执行任务
                return
            else:
                a += 1
                print_space("不在主页，返回上一级")
                if exists(Template(r"icon\tpl1719198082012.png", threshold=0.8, record_pos=(-0.44, -0.783), resolution=(414, 780))):
                    print_space('点击返回按钮')
                    touch(Template(r"icon\tpl1719198082012.png", threshold=0.8, record_pos=(-0.44, -0.783), resolution=(414, 780)))
                elif exists(Template(r"icon\tpl1719198103804.png", record_pos=(0.442, -0.35), resolution=(414, 780))):
                    print_space('点击关闭按钮')
                    touch(Template(r"icon\tpl1719198103804.png", record_pos=(0.442, -0.35), resolution=(414, 780)))
                else:
                    print_space('点击其他区域')
                    touch([500, 600])  # 不在主界面，返回到主页
            if stop_event.is_set():
                start_button_simple.configure(text='开始', command=save_simple_start_button)  # 野怪功能
                break

    except:
        print('执行错误')
    if a == 4:
        re_connet()


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
    time.sleep(3)  # 等待3秒
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
        touch(Template(r"icon\tpl1721784579063.png", rgb=True, record_pos=(0.22, 0.338), resolution=(1080, 1920)))
    elif exists(Template(r"icon\tpl1721784547262.png", rgb=True, record_pos=(0.399, 0.019), resolution=(1080, 1920))):
        print_space('点击晋升图标')
        touch(Template(r"icon\tpl1721784547262.png", record_pos=(0.399, 0.019), resolution=(1080, 1920)))
        print_space('点击开始晋升士兵')
        touch(Template(r"icon\tpl1721784579063.png", rgb=True, record_pos=(0.22, 0.338), resolution=(1080, 1920)))
    elif exists(Template(r"icon\tpl1721784547262.png", rgb=True, record_pos=(0.399, 0.019), resolution=(1080, 1920))):
        print_space('点击兵种')
        touch(Template(r"icon\tpl1721784547262.png", record_pos=(0.399, 0.019), resolution=(1080, 1920)))
        print_space('点击晋升图标')
        touch(Template(r"icon\tpl1721784547262.png", record_pos=(0.399, 0.019), resolution=(1080, 1920)))
        print_space('点击开始晋升士兵')
        touch(Template(r"icon\tpl1721784579063.png", rgb=True, record_pos=(0.22, 0.338), resolution=(1080, 1920)))
    else:
        print_space("没有可晋升士兵，训练最高级士兵")
        swipe([950, 1225], vector=[-0.4103, 0.0170])  # 滑动训练兵种
        touch([910, 1225])  # 点击十级兵
        lv_x = 910
        lv_y = 5
        while lv_y > 0:
            if not exists(Template(r"icon\tpl17217845790633.png", rgb=True, threshold=0.8, record_pos=(0.22, 0.338), resolution=(1080, 1920))):
                lv_x = lv_x - 200
                touch([lv_x, 1225])  # 点击开始上一级士兵
                lv_y -= 1
            else:
                break
        touch([800, 1800])  # 点击开始训练士兵
    time.sleep(1)  # 等待1秒
    print_space("返回上一级")
    if exists(Template(r"icon\tpl1719198082012.png", threshold=0.5, record_pos=(-0.44, -0.783), resolution=(414, 780))):
        touch(Template(r"icon\tpl1719198082012.png", threshold=0.5, record_pos=(-0.44, -0.783), resolution=(414, 780)))
    elif exists(Template(r"icon\tpl1719198103804.png", record_pos=(0.442, -0.35), resolution=(414, 780))):
        touch(Template(r"icon\tpl1719198103804.png", record_pos=(0.442, -0.35), resolution=(414, 780)))  # 关闭当前界面
    else:
        print_space('未找到对应图案')
    print_space('训练完成')
    time.sleep(1)
    touch([14, 823])
    time.sleep(1)  # 等待1秒


# 训练检查
def Production_soldiers():
    touch([14, 823])
    time.sleep(1)
    touch([170, 400])
    if exists(Template(r"icon\tpl1719478488282.png", threshold=0.9, rgb=True, record_pos=(-0.186, -0.058), resolution=(414, 780))):
        print_space("1跳转到盾兵兵营...")
        touch([600, 840])  # 点击索引到对应兵营
        train()
    elif exists(Template(r"icon\tpl1719478488283.png", threshold=0.95, record_pos=(-0.437, 0.046), resolution=(414, 780))):
        print_space("2跳转到盾兵兵营...")
        touch([600, 840])  # 点击索引到对应兵营
        train()
    if exists(Template(r"icon\tpl1719480722195.png", threshold=0.9, rgb=True, record_pos=(-0.437, 0.046), resolution=(414, 780))):
        print_space("跳转到矛兵兵营...")
        touch([600, 942])  # 点击索引到对应兵营
        train()
    elif exists(Template(r'icon\tpl1719480722196.png', threshold=0.95, record_pos=(-0.437, 0.046), resolution=(414, 780))):
        print_space("跳转到矛兵兵营...")
        touch([600, 942])  # 点击索引到对应兵营
        train()
    if exists(Template(r"icon\tpl1719480732965.png", threshold=0.9, rgb=True, record_pos=(-0.437, 0.145), resolution=(414, 780))):
        print_space("跳转到射手兵营...")
        touch([600, 1060])  # 点击索引到对应兵营
        train()
    elif exists(Template(r'icon\tpl1719480732966.png', threshold=0.95, record_pos=(-0.437, 0.046), resolution=(414, 780))):
        print_space("跳转到射手兵营...")
        touch([600, 1060])  # 点击索引到对应兵营
        train()
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
    print_space('点击等级')
    touch([651, 1573])  # 点击等级3
    time.sleep(1)  # 等待1s
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


# 冰原巨兽
def Brush_WM():
    search_main()
    swipe([600, 1370], vector=[0.4103, 0.0170])  # 滑动
    time.sleep(1)  # 等待1s
    print_space('点击选择冰原巨兽')
    touch([365, 1373])  # 点击冰原巨兽
    time.sleep(1)  # 等待1s
    print_space('点击等级')
    touch([500, 1573])  # 点击等级3
    time.sleep(1)  # 等待1s
    print_space('点击搜索按钮')
    touch([534, 1821])  # 点击搜索
    time.sleep(1)  # 等待1s
    print_space('点击集结按钮')
    touch(Template(r"icon\tpl1719376765868.png", record_pos=(0.002, 0.705), resolution=(414, 780)))  # 点击怪物集结
    time.sleep(1)  # 等待1s
    if exists(Template(r"icon\tpl1719376776844.png", rgb=True, record_pos=(0.0, 0.326), resolution=(414, 780))):
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
    if exists(Template(r"icon\tpl1721191349776.png", record_pos=(-0.168, -0.088), resolution=(1080, 1920))):  # 有兵力可出征
        print_space('点击出征按钮')
        touch(Template(r"icon\tpl1721191349776.png", record_pos=(-0.168, -0.088), resolution=(1080, 1920)))  # 点击出征
        print_space('出征成功')
        time.sleep(1)
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
        touch(Template(r"icon\tpl1720675061569.png", record_pos=(0.002, -0.015), resolution=(1080, 1920)))
        if not exists(Template(r"icon\tpl1720675170747.png", record_pos=(0.26, 0.795), resolution=(1080, 1920))):  # 判断是否有多余兵力
            print_space('不满足条件，无兵力出征')
        else:  # 有兵力可出征
            print_space('点击出征按钮')
            touch(Template(r"icon\tpl1720675170747.png", record_pos=(0.26, 0.795), resolution=(1080, 1920)))  # 点击出征
            print_space('出征成功')
    else:
        print_space('未搜索到铁矿资源，结束该任务')


# 自动采集
def Collection():
    if not exists(Template(r"icon\tpl1720145326019.png", record_pos=(0.404, 0.852), resolution=(1080, 1920))):
        print_space('不在世界，点击去往世界')
        touch([950, 1850])  # 点击野外
        time.sleep(5)  # 等待5秒
    else:
        print_space('在野外，执行采集任务')
        time, sleep(3)
    touch([14, 823])
    time.sleep(1)
    touch([500, 400])
    if not exists(Template(r"icon\tpl1720691682616.png", record_pos=(-0.168, -0.088), resolution=(1080, 1920))):
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
        touch(Template(r"icon\tpl1721191349779.png", threshold=0.8, record_pos=(0.142, -0.126), resolution=(1080, 1920)))
        print_space('点击联盟互助')
        touch(Template(r"icon\tpl1721191349780.png", threshold=0.8, record_pos=(0.142, -0.126), resolution=(1080, 1920)))
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
                touch(Template(r"icon\tpl1721784579073.png", record_pos=(-0.44, -0.783), resolution=(414, 780)))
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
        if now.minute % 5 == 0 and now.second % 5 == 0:
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
        if now.minute % 6 == 0:
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
        if now.minute % 6 == 0:
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
        if stop_event.is_set():
            start_button.configure(text='开始', command=save_simple)  # 总功能
            break
    print('结束任务')


'''def Subject():                                #老代码
    run_i = 1
    while True:
        if run_i % 10 == 0:
            Homepage()  # 主页检查
            try:
                if option_Production.get() == 1:
                    print('\n' + '%d.开始执行训练任务' % run_i)
                    Production_soldiers()  # 训练模块
                    if stop_event.is_set():
                        start_button.configure(text='开始', command=lambda: simle(0))  # 总功能
                        break
            except:
                print('程序执行异常，结束该任务，执行其他任务')
            run_i += 1
        if run_i % 14 == 0:
            Homepage()  # 主页检查
            try:
                if option_build.get() == 1:
                    print('\n' + '%d.开始执行建造任务' % run_i)
                    Build()  # 建造模块
                    if stop_event.is_set():
                        start_button.configure(text='开始', command=lambda: simle(0))  # 总功能
                        break
            except:
                print('程序执行异常，结束该任务，执行其他任务')
            run_i += 1
        if run_i % 19 == 0:
            Homepage()  # 主页检查
            try:
                now = datetime.now()
                if 17 <= now.hour <= 23:
                    if option_XG.get() == 1:
                        print('\n' + '%d.开始执行打野怪任务' % run_i)
                        Brush_XG()  # 打普通野怪
                        if stop_event.is_set():
                            start_button.configure(text='开始', command=lambda: simle(0))  # 总功能
                            break
                if now.hour == 0 or now.hour == 1:
                    if option_WM.get() == 1:
                        Brush_WM()  # 打巨兽模块
                        if stop_event.is_set():
                            start_button.configure(text='开始', command=lambda: simle(0))  # 总功能
                            break
                elif now.day == 24 or now.day == 25 or now.day == 26:
                    if option_npc.get() == 1:
                        NPC()
                        if stop_event.is_set():
                            start_button.configure(text='开始', command=lambda: simle(0))  # 总功能
                            break
            except:
                print('程序执行异常，结束该任务，执行其他任务')
            run_i += 1
        if run_i % 29 == 0:
            Homepage()  # 主页检查
            try:
                if option_Collection == 1:
                    print('\n' + '%d.开始执行采集任务' % run_i)
                    now = datetime.now().time()
                    if now.hour == 3:
                        Collection()  # 采集资源模块
                    else:
                        print_space('当前时间：%s,未到采集时间' % now.strftime("%H:%M"))
                    if stop_event.is_set():
                        start_button.configure(text='开始', command=lambda: simle(0))  # 总功能
                        break
            except:
                print('程序执行异常，结束该任务，执行其他任务')
            run_i = 1
            print('执行完成，结束该周期，开始新的周期')
        if not run_i==10 or not  run_i==14 or not  run_i==19 or not  run_i==29:
            Homepage()  # 主页检查
            try:
                if option_help.get() == 1:
                    print('\n' + '%d.开始执行互助任务' % run_i)
                    Help()  # 互助模块
                    if stop_event.is_set():
                        start_button.configure(text='开始', command=lambda: simle(0))  # 总功能
                        break
                elif option_help.get() == 0:
                    print_space('不执行互助任务')
                if option_bear.get() ==1:
                    now = datetime.now().time()
                    if now.hour == 21:
                        print_space('当前时间：%s,巨兽活动进行中' % now.strftime("%H:%M:%S"))
                        bear()  # 巨熊模块
                        if stop_event.is_set():
                            start_button.configure(text='开始', command=lambda: simle(0))  # 总功能
                            break
                if option_treatment.get() == 1:
                    now = datetime.now().time()
                    if now.minute == 21:
                        treatment()  # 治疗模块
                        if stop_event.is_set():
                            start_button.configure(text='开始', command=lambda: simle(0))  # 总功能
                            break
                if option_donate.get() == 1:
                    now = datetime.now().time()
                    if 0 < now.minute < 2:
                        donate()  # 捐赠模块
                        if stop_event.is_set():
                            start_button.configure(text='开始', command=lambda: simle(0))  # 总功能
                            break
                if option_adventure.get() == 1:
                    now = datetime.now().time()
                    if now.minute == 25:
                        adventure()
                        if stop_event.is_set():
                            start_button.configure(text='开始', command=lambda: simle(0))  # 总功能
                            break
                run_i += 1
            except:
                print('程序执行异常，结束该任务，执行其他任务')

    print('结束任务')'''


def print_space(variable, spaces=4):
    print(' ' * spaces + str(variable))


# --distpath

# pyinstaller  -w  --onefile --name "无尽冬日" --icon "E:\测试文件\测试工具\版本控制\Wjdr\main_icon.ico" --add-data "E:\测试文件\测试工具\AirtestIDE\airtest:airtest" --add-data "E:\测试文件\测试工具\版本控制\Wjdr\icon:icon" --add-data "E:\测试文件\测试工具\版本控制\Wjdr\wjdr.py:." E:\测试文件\测试工具\版本控制\Wjdr\wijd_release.py
# pip install numpy==1.21.1

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


'''------------------------------------创建主窗口------------------------------------'''
window = tk.Tk()
window.title("无尽冬日")  # 设置窗口标题
# window.geometry("500x600")  # 设置窗口大小
icon = tk.PhotoImage(file="icon\log.png")  # 设置窗口图标
window.iconphoto(True, icon)
# 调用函数居中窗口
center_window(window, 500, 600)
'''------------------------------------大标题------------------------------------'''
bt = tkFont.Font(family="Helvetica", size=17, weight=tkFont.BOLD)
tk.Label(window, text='无尽冬日', anchor='center', font=bt).pack()

'''------------------------------------模拟器相关按钮------------------------------------'''
'''创建区域'''
canvas_mumu = tk.Canvas(window, width=370, height=35)
# canvas_mumu.place(x=60, y=30)
canvas_mumu.pack()
canvas_mumu.create_rectangle(2, 2, 370, 35, width=0)
'''创建按钮'''
start_exe_button = ttk.Button(window, text='启动模拟器', command=lambda: start_simple(1))
canvas_mumu.create_window(50, 18, window=start_exe_button)
# start_exe_button.place(x=60, y=400)
cnnect_button = ttk.Button(window, text='连接模拟器', command=lambda: start_simple(2))
canvas_mumu.create_window(140, 18, window=cnnect_button)
# cnnect_button.place(x=150,y=400)
start_app_button = ttk.Button(window, text='启动游戏', command=lambda: start_simple(3))
canvas_mumu.create_window(230, 18, window=start_app_button)
# start_app_button.place(x=240,y=400)
all_button = ttk.Button(window, text='一键启动', command=lambda: start_simple(4))
canvas_mumu.create_window(320, 18, window=all_button)
# all_button.place(x=330,y=400)


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
    config.set('Options', '互助设置',str(help_time))
    with open('set.ini', 'w') as configfile:
        config.write(configfile)


'''读取设置'''

def load_options():
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
    help_time.set(config.get('Options', '互助设置'))




'''初始化配置解析器和选项变量'''
config = ConfigParser()
config['Options'] = {}
'''单选'''
var = tk.StringVar()
'''多选'''
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
help_time = tk.StringVar()

# 尝试加载先前保存的选项
if config.read('set.ini'):
    global input_time
    try:
        with open('set.ini', 'r') as configfile:
            config.read_file(configfile)
        load_options()
    except IOError:
        print('No saved options found.')
# 首次启动时默认选项
else:
    var.set('0')
    option_help.set('1')
    option_WM.set('1')
    option_npc.set('1')
    option_Production.set('1')
    option_build.set('1')
    option_Collection.set('1')
    option_bear.set('1')
    option_treatment.set('1')
    option_adventure.set('1')
    option_donate.set('1')
    help_time.set('10')
'''------------------------------------多选功能区功能------------------------------------'''
'''创建 Canvas(区域框)，设置宽度和高度'''
canvas = tk.Canvas(window, width=400, height=150)
# canvas.place(x=50,y=65)
canvas.pack()
canvas.create_rectangle(3, 3, 400, 150, width=0)

'''标签'''
title = tk.Label(window, text='功能选项(多选)：')
canvas.create_window(55, 15, window=title)
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
for i in range(1, 11):
    # option_help.set('1')  # 设置复选框的默认值为选中状态
    checkbox = tk.Checkbutton(window, text='联盟互助', variable=option_help, command=save_options)
    canvas.create_window(88, 45, window=checkbox)
    # checkbox.place(x=80,y=70)
    checkboxes.append(checkbox)
'''世界野怪'''
for i in range(1, 11):
    # option_XG.set(1)  # 设置复选框的默认值为选中状态
    checkbox = tk.Checkbutton(window, text='世界野怪', variable=option_XG, command=save_options)
    canvas.create_window(168, 45, window=checkbox)
    # checkbox.place(x=160, y=70)
    checkboxes.append(checkbox)
'''冰原巨兽'''
for i in range(1, 11):
    # option_WM = tk.IntVar()
    # option_WM.set(1)  # 设置复选框的默认值为选中状态
    checkbox = tk.Checkbutton(window, text='冰原巨兽', variable=option_WM, command=save_options)
    canvas.create_window(248, 45, window=checkbox)
    # checkbox.place(x=240, y=70)
    checkboxes.append(checkbox)
'''活动雪怪'''
for i in range(1, 11):
    # option_npc = tk.IntVar()
    # option_npc.set(1)  # 设置复选框的默认值为选中状态
    checkbox = tk.Checkbutton(window, text='活动雪怪', variable=option_npc, command=save_options)
    canvas.create_window(328, 45, window=checkbox)
    # checkbox.place(x=320,y=70)
    checkboxes.append(checkbox)
'''训练士兵'''
for i in range(1, 11):
    # option_Production = tk.IntVar()
    # option_Production.set(1)  # 设置复选框的默认值为选中状态
    checkbox = tk.Checkbutton(window, text='训练士兵', variable=option_Production, command=save_options)
    canvas.create_window(88, 75, window=checkbox)
    # checkbox.place(x=80, y=100)
    checkboxes.append(checkbox)
'''建筑升级'''
for i in range(1, 11):
    # option_build = tk.IntVar()
    # option_build.set(1)  # 设置复选框的默认值为选中状态
    checkbox = tk.Checkbutton(window, text='建筑升级', variable=option_build, command=save_options)
    canvas.create_window(168, 75, window=checkbox)
    # checkbox.place(x=160, y=100)
    checkboxes.append(checkbox)
'''采集资源'''
for i in range(1, 11):
    # option_Collection = tk.IntVar()
    # option_Collection.set(1)  # 设置复选框的默认值为选中状态
    checkbox = tk.Checkbutton(window, text='采集资源', variable=option_Collection, command=save_options)
    canvas.create_window(248, 75, window=checkbox)
    # checkbox.place(x=240, y=100)
    checkboxes.append(checkbox)
'''巨熊活动'''
for i in range(1, 11):
    # option_bear = tk.IntVar()
    # option_bear.set(1)  # 设置复选框的默认值为选中状态
    checkbox = tk.Checkbutton(window, text='巨熊活动', variable=option_bear, command=save_options)
    canvas.create_window(328, 75, window=checkbox)
    # checkbox.place(x=320, y=100)
    checkboxes.append(checkbox)
'''治疗士兵'''
for i in range(1, 11):
    # option_treatment = tk.IntVar()
    # option_treatment.set(1)  # 设置复选框的默认值为选中状态
    checkbox = tk.Checkbutton(window, text='治疗士兵', variable=option_treatment, command=save_options)
    canvas.create_window(88, 105, window=checkbox)
    # checkbox.place(x=80, y=130)
    checkboxes.append(checkbox)
'''探险奖励'''
for i in range(1, 11):
    # option_adventure = tk.IntVar()
    # option_adventure.set(1)  # 设置复选框的默认值为选中状态
    checkbox = tk.Checkbutton(window, text='探险奖励', variable=option_adventure, command=save_options)
    canvas.create_window(168, 105, window=checkbox)
    # checkbox.place(x=160, y=130)
    checkboxes.append(checkbox)
'''联盟捐赠'''
for i in range(1, 11):
    # option_donate = tk.IntVar()
    # option_donate.set(1)  # 设置复选框的默认值为选中状态
    checkbox = tk.Checkbutton(window, text='联盟捐赠', variable=option_donate, command=save_options)
    canvas.create_window(248, 105, window=checkbox)
    # checkbox.place(x=240, y=130)
    checkboxes.append(checkbox)

'''------------------------------------多选功能区功能按钮------------------------------------'''
'''创建按钮'''
select_button = ttk.Button(window, text="全选", command=save_select_all)
canvas.create_window(100, 135, window=select_button)
# select_button.place(x=100, y = 190)
start_button = ttk.Button(window, text="开始", command=save_simple)
canvas.create_window(200, 135, window=start_button)
# start_button.place(x=200, y=190)
select_button = ttk.Button(window, text="取消全选", command=save_deselect_all)
canvas.create_window(300, 135, window=select_button)
# select_button.place(x=300, y = 190)

'''------------------------------------单选功能区功能------------------------------------'''
'''区域'''
canvas_simple = tk.Canvas(window, width=400, height=150)
# canvas_simple.place(x=50,y=230)
canvas_simple.pack()
canvas_simple.create_rectangle(2, 2, 400, 150, width=1)

'''标签'''
title = tk.Label(window, text='功能选项(单选)：')
canvas_simple.create_window(55, 15, window=title)
'''单项开始按钮'''


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
    simple_start_button()
    save_options()


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
                print(int(input_value(0)))
                time.sleep(int(input_value(0)))
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
                print_space('等待1分钟后再次执行')
                number = 0
                while number < 6:
                    if stop_event.is_set():
                        execute = False
                        start_button_simple.configure(text='开始', command=save_simple_start_button)  # 野怪功能
                        break
                    else:
                        time.sleep(10)
            except:
                print('错误')
    elif var_value == 2:
        while execute:
            try:
                Homepage()
                Brush_WM()
                if stop_event.is_set():
                    start_button_simple.configure(text='开始', command=save_simple_start_button)  # 停止后按钮变为开始
                    break
                print_space('等待90s后再次执行')
                number = 0
                while number < 9:
                    if stop_event.is_set():
                        execute = False
                        start_button_simple.configure(text='开始', command=save_simple_start_button)  # 野怪功能
                        break
                    else:
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
                print_space('等待90s后再次执行')
                number = 0
                while number < 9:
                    if stop_event.is_set():
                        execute = False
                        start_button_simple.configure(text='开始', command=save_simple_start_button)  # 野怪功能
                        break
                    else:
                        time.sleep(10)
            except:
                print('错误')
    elif var_value == 4:
        while execute:
            try:
                Homepage()
                Production_soldiers()
                if stop_event.is_set():
                    start_button_simple.configure(text='开始', command=save_simple_start_button)  # 停止后按钮变为开始
                    break
                print_space('等待1小时后再次执行')
                number = 0
                while number < 360:
                    if stop_event.is_set():
                        execute = False
                        start_button_simple.configure(text='开始', command=save_simple_start_button)  # 野怪功能
                        break
                    else:
                        time.sleep(10)
            except:
                print('错误')
    elif var_value == 5:
        while True:
            try:
                Homepage()
                Build()
                if stop_event.is_set():
                    start_button_simple.configure(text='开始', command=save_simple_start_button)  # 停止后按钮变为开始
                    break
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
                print_space('等待1分钟后再次执行')
                number = 0
                while number < 6:
                    if stop_event.is_set():
                        execute = False
                        start_button_simple.configure(text='开始', command=save_simple_start_button)  # 野怪功能
                        break
                    else:
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
                print_space('等待1分钟')
                number = 0
                while number < 6:
                    execute = False
                    if stop_event.is_set():
                        start_button_simple.configure(text='开始', command=save_simple_start_button)  # 野怪功能
                        break
                    else:
                        time.sleep(10)
            except:
                print('错误')
    elif var_value == 8:
        while True:
            try:
                Homepage()
                treatment()
                if stop_event.is_set():
                    start_button_simple.configure(text='开始', command=save_simple_start_button)  # 停止后按钮变为开始
                    break
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
                print_space('等待1小时后再次执行')
                number = 0
                while number < 360:
                    if stop_event.is_set():
                        execute = False
                        start_button_simple.configure(text='开始', command=save_simple_start_button)  # 野怪功能
                        break
                    else:
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
                print_space('等待5分钟后再次执行')
                number = 0
                while number < 30:
                    execute = False
                    if stop_event.is_set():
                        start_button_simple.configure(text='开始', command=save_simple_start_button)  # 野怪功能
                        break
                    else:
                        time.sleep(10)
            except:
                print('错误')
    print('任务已结束')


'''获取输入框的值'''
def input_value(value):
    if value == 0 :
        help_time = input_time.get()
        return help_time
    if value == 1 :
        return input_time.get()
'''------------------------------------单选项选项------------------------------------'''
# 创建单选项并添加选项
'''联盟互助'''
select_help = tk.Radiobutton(window, text='联盟互助', variable=var, value=0)
canvas_simple.create_window(88, 45, window=select_help)
'''世界野怪'''
select_XG = tk.Radiobutton(window, text='世界野怪', variable=var, value=1)
canvas_simple.create_window(168, 45, window=select_XG)
'''冰原巨兽'''
select_WM = tk.Radiobutton(window, text='冰原巨兽', variable=var, value=2)
canvas_simple.create_window(248, 45, window=select_WM)
'''活动雪怪'''
select_npc = tk.Radiobutton(window, text='活动雪怪', variable=var, value='3')
canvas_simple.create_window(328, 45, window=select_npc)
'''训练士兵'''
select_production = tk.Radiobutton(window, text='训练士兵', variable=var, value='4')
canvas_simple.create_window(88, 75, window=select_production)
'''建筑升级'''
select_build = tk.Radiobutton(window, text='建筑升级', variable=var, value='5')
canvas_simple.create_window(168, 75, window=select_build)
'''采集资源'''
select_collection = tk.Radiobutton(window, text='采集资源', variable=var, value='6')
canvas_simple.create_window(248, 75, window=select_collection)
'''巨熊活动'''
select_bear = tk.Radiobutton(window, text='巨熊活动', variable=var, value='7')
canvas_simple.create_window(328, 75, window=select_bear)
'''治疗士兵'''
select_treatment = tk.Radiobutton(window, text='治疗士兵', variable=var, value='8')
canvas_simple.create_window(88, 105, window=select_treatment)
'''探险奖励'''
select_adventure = tk.Radiobutton(window, text='探险奖励', variable=var, value='9')
canvas_simple.create_window(168, 105, window=select_adventure)
'''联盟捐赠'''
select_donate = tk.Radiobutton(window, text='联盟捐赠', variable=var, value='10')
canvas_simple.create_window(248, 105, window=select_donate)

'''开始按钮'''
start_button_simple = ttk.Button(window, text='开始', command=save_simple_start_button)
canvas_simple.create_window(300, 135, window=start_button_simple)

''''自定义单项功能的重新执行时间'''
imput_text = tk.Label(canvas_simple,text='等待时间:')
canvas_simple.create_window(80, 135, window=imput_text)
input_time = tk.Entry(window)
canvas_simple.create_window(165, 135, window=input_time)


'''------------------------------------输出区域------------------------------------'''
'''区域'''
canvas_output = tk.Canvas(window, width=490, height=200)
# canvas_output.place(x=5, y=390)
canvas_output.pack()
canvas_output.create_rectangle(2, 2, 490, 200, width=0)
'''创建一个ScrolledText控件作为输出框'''
output_text = tk.Label(window, text='输出:')
canvas_output.create_window(25, 15, window=output_text)
output_box = ScrolledText(window, width=65, height=13)
canvas_output.create_window(250, 110, window=output_box)
# output_box.pack(side=tk.BOTTOM,padx=10,pady=10)
# sys.stdout.write = print(output_box)#写入输出框

'''------------------------------------输出框输出内容------------------------------------'''


def print(text_1):
    #    str_args = " ".join(str(arg) for arg in args)
    output_box.configure(state="normal")
    output_box.insert('end', text_1 + '\n')  # 换行显示
    output_box.see("end")  # 显示最底部内容
    output_box.configure(state="disabled")


# 开始Tkinter事件循环
tk.mainloop()

# 窗口线程
thread_window = threading.Thread(target=window.mainloop).start()
