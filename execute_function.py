'''模拟器点击变量'''
import os
import subprocess
import threading
import time
from datetime import datetime
from airtest.core.api import connect_device
from main_function import *

'''打开模拟器'''
emulator_click = 0


def start_exe():
    while True:
        try:
            print('开始启动模拟器')
            # subprocess.Popen('E:\leidian\LDPlayer9\dnplayer.exe')
            subprocess.Popen(settings.value('模拟器地址', 'E:\leidian\LDPlayer9\dnplayer.exe', type=str))
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
            connect_ip = settings.value('模拟器ip', '127.0.0.1:5037', type=str)
            print('地址：android:// %s' % connect_ip)
            # print('地址：android://127.0.0.1:5037')
            connect_device('android://%s' % connect_ip)
            # connect_device('android://127.0.0.1:5037')
            # subprocess.run(['adb', '-s', '127.0.0.1:21503', 'shell'])
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
            touch(Template(r"icon/tpl1719196072757.png", record_pos=(0.112, -0.519), resolution=(414, 780)))
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
        # start_exe_button.configure(text='启动模拟器', command=lambda: start_simple(1))
        # start_exe()
        '''启动模拟器线程'''
        threading.Thread(target=start_exe).start()  # threading.Thread(target=start_exe).join()
    elif button_start_id == 2:
        '''连接模拟器线程'''
        threading.Thread(target=cnnect).start()  # threading.Thread(target=cnnect).join()
    elif button_start_id == 3:
        # start_app_button.configure(text='再次启动app', command=lambda: start_simple(3))
        # start_app()
        '''启动app线程'''
        threading.Thread(target=start_app).start()  # threading.Thread(target=start_app).join()
    elif button_start_id == 4:
        '''一键启动线程'''
        threading.Thread(target=all_start).start()
    else:
        print_space('错误')


def stop_function():
    # 这里放置停止需要的代码
    global stop_event
    stop_event.set()  # 设置事件，通知线程结束
    print('-------------当前任务结束或10s后结束任务-------------')


stop_event = threading.Event()


# 多选主体代码
def subject(self):
    global emulator_click, stop_event
    if emulator_click == 0:
        time.sleep(1)
        print('未连接模拟器')
        time.sleep(1)
        cnnect()
    run_number = 1
    if self.select_time.isChecked():
        while True:
            now = datetime.now()
            if self.checkBox_help.isChecked() and now.second % 2 == 0:
                try:
                    print('%d.开始执行互助任务' % run_number)
                    Homepage()  # 主页检查
                    Help()  # 互助模块
                    run_number += 1
                    if stop_event.is_set():
                        self.select_stop_button()
                        break
                except:
                    print('程序执行异常，结束该任务，执行其他任务')
            if self.checkBox_XG.isChecked() and now.minute % 5 == 0 and now.second % 5 == 0 and now.hour != 21:
                try:
                    print('%d.开始执行野怪任务' % run_number)
                    Homepage()  # 主页检查
                    Brush_XG(self)  # 野怪
                    run_number += 1
                    if stop_event.is_set():
                        self.select_stop_button()  # 总功能
                        break
                except:
                    print('程序执行异常，结束该任务，执行其他任务')
            if self.checkBox_WM.isChecked() and now.minute % 6 == 0 and 0 < now.second < 20 and now.hour != 21:
                try:
                    print('%d.开始执行冰原巨兽任务' % run_number)
                    Homepage()  # 主页检查
                    Brush_WM(self)  # 冰原巨兽
                    run_number += 1
                    if stop_event.is_set():
                        self.select_stop_button()
                        break
                except:
                    print('程序执行异常，结束该任务，执行其他任务')
            if self.checkBox_npc.isChecked() and now.minute % 6 == 0 and now.hour != 21:
                try:
                    print('%d.开始执行活动雪怪任务' % run_number)
                    Homepage()  # 主页检查
                    NPC()  # 活动雪怪
                    run_number += 1
                    if stop_event.is_set():
                        self.select_stop_button()
                        break
                except:
                    print('程序执行异常，结束该任务，执行其他任务')
            if self.checkBox_Production.isChecked() and now.minute % 5 == 0:
                try:
                    print('%d.开始执行训练任务' % run_number)
                    Homepage()  # 主页检查
                    Production_soldiers(self)  # 训练模块
                    run_number += 1
                    if stop_event.is_set():
                        self.select_stop_button()  # 总功能
                        break
                except:
                    print('程序执行异常，结束该任务，执行其他任务')
            if self.checkBox_build.isChecked() and now.minute % 10 == 2:
                try:
                    print('%d.开始执行建造任务' % run_number)
                    Homepage()  # 主页检查
                    Build()  # 建造模块
                    run_number += 1
                    if stop_event.is_set():
                        self.select_stop_button()  # 总功能
                        break
                except:
                    print('程序执行异常，结束该任务，执行其他任务')
            if self.checkBox_Collection.isChecked() and now.minute % 10 == 3:
                try:
                    print('%d.开始执行采集任务' % run_number)
                    Homepage()  # 主页检查
                    Collection(self)  # 采集资源模块
                    run_number += 1
                    if stop_event.is_set():
                        self.select_stop_button()  # 总功能
                        break
                except:
                    print('程序执行异常，结束该任务，执行其他任务')
            if self.checkBox_bear.isChecked() and now.hour == 21:
                try:
                    print_space('当前时间：%s,巨熊活动进行中' % now.strftime("%H:%M:%S"))
                    Homepage()  # 主页检查
                    bear()  # 巨熊模块
                    run_number += 1
                    if stop_event.is_set():
                        self.select_stop_button()  # 总功能
                        break
                except:
                    print('程序执行异常，结束该任务，执行其他任务')
            if self.checkBox_treatment.isChecked() and now.minute % 10 == 5:
                try:
                    print('%d.开始执行治疗任务' % run_number)
                    Homepage()  # 主页检查
                    treatment()  # 治疗模块
                    run_number += 1
                    if stop_event.is_set():
                        self.select_stop_button()  # 总功能
                        break
                except:
                    print('程序执行异常，结束该任务，执行其他任务')
            if self.checkBox_adventure.isChecked() and now.minute == 25:
                try:
                    print('%d.开始执行探险任务' % run_number)
                    Homepage()  # 主页检查
                    adventure()  # 探险
                    run_number += 1
                    if stop_event.is_set():
                        self.select_stop_button()  # 总功能
                        break
                except:
                    print('程序执行异常，结束该任务，执行其他任务')
            if self.checkBox_donate.isChecked() and now.minute == 1:
                try:
                    print('%d.开始执行捐赠任务' % run_number)
                    Homepage()  # 主页检查
                    donate()  # 捐赠模块
                    run_number += 1
                    if stop_event.is_set():
                        self.select_stop_button()  # 总功能
                        break
                except:
                    print('程序执行异常，结束该任务，执行其他任务')
            if self.checkBox_recruit.isChecked() and now.hour == 1 and now.minute % 5 == 0:
                try:
                    print('%d.开始执行招募任务' % run_number)
                    Homepage()
                    recruit()  # 英雄招募
                    run_number += 1
                    if stop_event.is_set():
                        self.select_stop_button()  # 停止
                        break
                except:
                    print('程序执行异常，结束该任务，执行其他任务')
            if self.checkBox_collision.isChecked():
                try:
                    print('%d.开始执行攻击检测任务' % run_number)
                    Homepage()
                    mining_collision()  #攻击检测
                    run_number += 1
                    if stop_event.is_set():
                        self.select_stop_button()  # 停止
                        break
                except:
                    print('程序执行异常，结束该任务，执行其他任务')
            if self.checkBox_mail.isChecked() and now.minute == 30 and now.second % 20 == 0:
                try:
                    print('%d.开始执行邮件领取任务' % run_number)
                    Homepage()
                    mail_function()    # 邮件领取
                    run_number += 1
                    if stop_event.is_set():
                        self.select_stop_button()  # 停止
                        break
                except:
                    print('程序执行异常，结束该任务，执行其他任务')
            if self.checkBox_Treasure_Chest.isChecked() and now.minute == 50 and now.second % 20 == 0:
                try:
                    print('%d.开始执行联盟宝箱领取任务' % run_number)
                    Homepage()
                    union_Treasure_Chest()    # 联盟宝箱
                    run_number += 1
                    if stop_event.is_set():
                        self.select_stop_button()  # 停止
                        break
                except:
                    print('程序执行异常，结束该任务，执行其他任务')
            if stop_event.is_set():
                self.select_stop_button()  # 总功能
                break
    else:
        while True:
            now = datetime.now()
            if self.checkBox_help.isChecked():
                try:
                    print('%d.开始执行互助任务' % run_number)
                    Homepage()  # 主页检查
                    Help()  # 互助模块
                    run_number += 1
                    if stop_event.is_set():
                        self.select_stop_button()
                        break
                except:
                    print('程序执行异常，结束该任务，执行其他任务')
            if self.checkBox_XG.isChecked() and now.hour != 21:
                try:
                    print('%d.开始执行野怪任务' % run_number)
                    Homepage()  # 主页检查
                    Brush_XG(self)  # 野怪
                    run_number += 1
                    if stop_event.is_set():
                        self.select_stop_button()  # 总功能
                        break
                except:
                    print('程序执行异常，结束该任务，执行其他任务')
            if self.checkBox_WM.isChecked() and now.hour != 21:
                try:
                    print('%d.开始执行冰原巨兽任务' % run_number)
                    Homepage()  # 主页检查
                    Brush_WM(self)  # 冰原巨兽
                    run_number += 1
                    if stop_event.is_set():
                        self.select_stop_button()
                        break
                except:
                    print('程序执行异常，结束该任务，执行其他任务')
            if self.checkBox_npc.isChecked() and now.hour != 21:
                try:
                    print('%d.开始执行活动雪怪任务' % run_number)
                    Homepage()  # 主页检查
                    NPC()  # 活动雪怪
                    run_number += 1
                    if stop_event.is_set():
                        self.select_stop_button()
                        break
                except:
                    print('程序执行异常，结束该任务，执行其他任务')
            if self.checkBox_Production.isChecked():
                try:
                    print('%d.开始执行训练任务' % run_number)
                    Homepage()  # 主页检查
                    Production_soldiers(self)  # 训练模块
                    run_number += 1
                    if stop_event.is_set():
                        self.select_stop_button()  # 总功能
                        break
                except:
                    print('程序执行异常，结束该任务，执行其他任务')
            if self.checkBox_build.isChecked():
                try:
                    print('%d.开始执行建造任务' % run_number)
                    Homepage()  # 主页检查
                    Build()  # 建造模块
                    run_number += 1
                    if stop_event.is_set():
                        self.select_stop_button()  # 总功能
                        break
                except:
                    print('程序执行异常，结束该任务，执行其他任务')
            if self.checkBox_Collection.isChecked():
                try:
                    print('%d.开始执行采集任务' % run_number)
                    Homepage()  # 主页检查
                    Collection(self)  # 采集资源模块
                    run_number += 1
                    if stop_event.is_set():
                        self.select_stop_button()  # 总功能
                        break
                except:
                    print('程序执行异常，结束该任务，执行其他任务')
            if self.checkBox_bear.isChecked():
                try:
                    print_space('当前时间：%s,巨熊活动进行中' % now.strftime("%H:%M:%S"))
                    Homepage()  # 主页检查
                    bear()  # 巨熊模块
                    run_number += 1
                    if stop_event.is_set():
                        self.select_stop_button()  # 总功能
                        break
                except:
                    print('程序执行异常，结束该任务，执行其他任务')
            if self.checkBox_treatment.isChecked():
                try:
                    print('%d.开始执行治疗任务' % run_number)
                    Homepage()  # 主页检查
                    treatment()  # 治疗模块
                    run_number += 1
                    if stop_event.is_set():
                        self.select_stop_button()  # 总功能
                        break
                except:
                    print('程序执行异常，结束该任务，执行其他任务')
            if self.checkBox_adventure.isChecked():
                try:
                    print('%d.开始执行探险任务' % run_number)
                    Homepage()  # 主页检查
                    adventure()  # 探险
                    run_number += 1
                    if stop_event.is_set():
                        self.select_stop_button()  # 总功能
                        break
                except:
                    print('程序执行异常，结束该任务，执行其他任务')
            if self.checkBox_donate.isChecked():
                try:
                    print('%d.开始执行捐赠任务' % run_number)
                    Homepage()  # 主页检查
                    donate()  # 捐赠模块
                    run_number += 1
                    if stop_event.is_set():
                        self.select_stop_button()  # 总功能
                        break
                except:
                    print('程序执行异常，结束该任务，执行其他任务')
            if self.checkBox_recruit.isChecked():
                try:
                    print('%d.开始执行招募任务' % run_number)
                    Homepage()
                    recruit()  #英雄招募
                    run_number += 1
                    if stop_event.is_set():
                        self.select_stop_button()  # 总功能
                        break
                except:
                    print('程序执行异常，结束该任务，执行其他任务')
            if self.checkBox_collision.isChecked():
                try:
                    print('%d.开始执行攻击检测任务' % run_number)
                    Homepage()
                    mining_collision()  #攻击检测
                    run_number += 1
                    if stop_event.is_set():
                        self.select_stop_button()  # 总功能
                        break
                except:
                    print('程序执行异常，结束该任务，执行其他任务')
            if self.checkBox_mail.isChecked():
                try:
                    print('%d.开始执行邮件领取任务' % run_number)
                    Homepage()
                    mail_function()    # 邮件领取
                    run_number += 1
                    if stop_event.is_set():
                        self.select_stop_button()  # 停止
                        break
                except:
                    print('程序执行异常，结束该任务，执行其他任务')
            if self.checkBox_Treasure_Chest.isChecked():
                try:
                    print('%d.开始执行联盟宝箱领取任务' % run_number)
                    Homepage()
                    union_Treasure_Chest()    # 联盟宝箱
                    run_number += 1
                    if stop_event.is_set():
                        self.select_stop_button()  # 停止
                        break
                except:
                    print('程序执行异常，结束该任务，执行其他任务')
            if stop_event.is_set():
                self.select_stop_button()  # 总功能
                break
    print('结束任务')


# 单选主体代码
def simple_select(self):
    global emulator_click, stop_event
    if emulator_click == 0:
        time.sleep(1)
        print('未连接模拟器')
        time.sleep(1)
        cnnect()
    execute = True
    if self.radioButton_help.isChecked():
        while True:
            try:
                Homepage()
                Help()
                if stop_event.is_set():
                    self.simple_stop_button()  # 互助功能
                    break
                help_time = settings.value('联盟互助设置', 20, type=str)
                print_space('等待%s秒后继续执行任务' % help_time)
                XG_number = int(help_time)
                time.sleep(XG_number)
            except:
                print('错误')
    elif self.radioButton_XG.isChecked():
        while execute:
            try:
                Homepage()
                Brush_XG(self)
                if stop_event.is_set():
                    execute = False
                    self.simple_stop_button()  # 野怪功能
                    break
                XG_time = int(settings.value('世界野怪设置', 20, type=str))
                print_space('等待%s秒后再次执行' % XG_time)
                number = 0
                XG_number = XG_time / 10
                while XG_number > number:
                    if stop_event.is_set():
                        execute = False
                        self.simple_stop_button()  # 野怪功能
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
    elif self.radioButton_WM.isChecked():  #冰原巨兽
        while execute:
            try:
                Homepage()
                Brush_WM(self)
                if stop_event.is_set():
                    execute = False
                    self.simple_stop_button()  # 停止后按钮变为开始
                    break
                WM_time = int(settings.value('冰原巨兽设置', 20, type=str))
                print_space('等待%s秒后再次执行' % WM_time)
                number = 0
                WM_number = WM_time / 10
                while number < WM_number:
                    if stop_event.is_set():
                        execute = False
                        self.simple_stop_button()  # 野怪功能
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
    elif self.radioButton_npc.isChecked():
        while execute:
            try:
                Homepage()
                NPC()
                if stop_event.is_set():
                    execute = False
                    self.simple_stop_button()  # 停止后按钮变为开始
                    break
                npc_time = int(settings.value('活动雪怪设置', 20, type=str))
                print_space('等待%s秒后再次执行' % npc_time)
                number = 0
                npc_number = npc_time / 10
                while number < npc_number:
                    if stop_event.is_set():
                        execute = False
                        self.simple_stop_button()
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
    elif self.radioButton_Production.isChecked():  # 训练士兵
        while execute:
            try:
                Homepage()
                Production_soldiers(self)
                if stop_event.is_set():
                    execute = False
                    self.simple_stop_button()  # 停止后按钮变为开始
                    break
                production_time = int(settings.value('训练士兵设置', 20, type=str))
                print_space('等待%s秒后再次执行' % production_time)
                production_number = production_time / 10
                number = 0
                while number < production_number:
                    if stop_event.is_set():
                        execute = False
                        self.simple_stop_button()
                        break
                    else:
                        if production_number < 1:
                            time.sleep(production_time)
                            break
                        else:
                            number += 1
                            time.sleep(10)
            except:
                print('错误')
    elif self.radioButton_build.isChecked():
        while execute:
            try:
                Homepage()
                Build()
                if stop_event.is_set():
                    execute = False
                    self.simple_stop_button()  # 停止后按钮变为开始
                    break
                build_time = int(settings.value('建筑升级设置', 20, type=str))
                print_space('等待%s秒后再次执行' % build_time)
                build_number = build_time / 10
                number = 0
                while number < build_number:
                    if stop_event.is_set():
                        execute = False
                        self.simple_stop_button()
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
    elif self.radioButton_Collection.isChecked():
        while execute:
            try:
                Homepage()
                Collection(self)
                if stop_event.is_set():
                    execute = False
                    self.simple_stop_button()  # 停止后按钮变为开始
                    break
                Collection_time = int(settings.value('采集资源设置', 20, type=str))
                print_space('等待%s秒后再次执行' % Collection_time)
                number = 0
                Collection_number = Collection_time / 10
                while number < Collection_number:
                    if stop_event.is_set():
                        execute = False
                        self.simple_stop_button()
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
    elif self.radioButton_bear.isChecked():
        while execute:
            try:
                Homepage()
                bear()
                if stop_event.is_set():
                    execute = False
                    self.simple_stop_button()  # 停止后按钮变为开始
                    break
                bear_time = int(settings.value('巨熊活动设置', 20, type=str))
                print_space('等待%s秒后再次执行' % bear_time)
                number = 0
                bear_number = bear_time / 10
                while number < bear_number:
                    if stop_event.is_set():
                        execute = False
                        self.simple_stop_button()  # 野怪功能
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
    elif self.radioButton_treatment.isChecked():  #治疗
        while execute:
            try:
                Homepage()
                treatment()
                if stop_event.is_set():
                    execute = False
                    self.simple_stop_button()  # 停止后按钮变为开始
                    break
                treatment_time = int(settings.value('治疗士兵设置', 20, type=str))
                print_space('等待%s秒后再次执行' % treatment_time)
                number = 0
                treatment_number = treatment_time / 10
                while number < treatment_number:
                    if stop_event.is_set():
                        execute = False
                        self.simple_stop_button()
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
    elif self.radioButton_adventure.isChecked():
        while execute:
            try:
                Homepage()
                adventure()
                if stop_event.is_set():
                    execute = False
                    self.simple_stop_button()  # 停止后按钮变为开始
                    break
                adventure_time = int(settings.value('探险奖励设置', 20, type=str))
                print_space('等待%s秒后再次执行' % adventure_time)
                number = 0
                adventure_number = adventure_time / 10
                while number < adventure_number:
                    if stop_event.is_set():
                        execute = False
                        self.simple_stop_button()  # 野怪功能
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
    elif self.radioButton_donate.isChecked():
        while execute:
            try:
                Homepage()
                donate()
                if stop_event.is_set():
                    execute = False
                    self.simple_stop_button()  # 停止后按钮变为开始
                    break
                donate_time = int(settings.value('联盟捐赠设置', 20, type=str))
                print_space('等待%s秒后再次执行' % donate_time)
                number = 0
                donate_number = donate_time / 10
                while number < donate_number:
                    if stop_event.is_set():
                        execute = False
                        self.simple_stop_button()  # 野怪功能
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
    elif self.radioButton_recruit.isChecked():
        while execute:
            try:
                Homepage()
                recruit()
                if stop_event.is_set():
                    execute = False
                    self.simple_stop_button()  # 停止后按钮变为开始
                    break
                recruit_time = int(settings.value('英雄招募设置', 20, type=str))
                print_space('等待%s秒后再次执行' % recruit_time)
                number = 0
                recruit_number = recruit_time / 10
                while number < recruit_number:
                    if stop_event.is_set():
                        execute = False
                        self.simple_stop_button()  # 停止后按钮变为开始
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
    elif self.radioButton_collision.isChecked():  # 攻击检测
        while execute:
            try:
                Homepage()
                mining_collision()
                if stop_event.is_set():
                    execute = False
                    self.simple_stop_button()  # 停止后按钮变为开始
                    break
                mining_collision_time1 = int(settings.value('攻击检测设置', 20, type=str))
                print_space('等待%s秒后再次执行' % mining_collision_time1)
                number = 0
                mining_collision_number = mining_collision_time1 / 10
                while number < mining_collision_number:
                    if stop_event.is_set():
                        execute = False
                        self.simple_stop_button()  # 停止后按钮变为开始
                        break
                    else:
                        if mining_collision_number < 1:
                            time.sleep(mining_collision_number)
                            break
                        else:
                            number += 1
                            time.sleep(10)
                if stop_event.is_set():
                    execute = False
                    self.simple_stop_button()  # 停止后按钮变为开始
            except:
                print('错误')
    elif self.radioButton_mail.isChecked():  # 邮件领取
        while execute:
            try:
                Homepage()
                mail_function()
                if stop_event.is_set():
                    execute = False
                    self.simple_stop_button()  # 停止后按钮变为开始
                    break
                mail_function_time = int(settings.value('邮件领取设置', 20, type=str))
                print_space('等待%s秒后再次执行' % mail_function_time)
                number = 0
                mail_function_number = mail_function_time / 10
                while number < mail_function_number:
                    if stop_event.is_set():
                        execute = False
                        self.simple_stop_button()  # 停止后按钮变为开始
                        break
                    else:
                        if mail_function_number < 1:
                            time.sleep(mail_function_number)
                            break
                        else:
                            number += 1
                            time.sleep(10)
                if stop_event.is_set():
                    execute = False
                    self.simple_stop_button()  # 停止后按钮变为开始
            except:
                print('错误')
    elif self.radioButton_Treasure_Chest.isChecked():  # 联盟宝箱
        while execute:
            try:
                Homepage()
                union_Treasure_Chest()
                if stop_event.is_set():
                    execute = False
                    self.simple_stop_button()  # 停止后按钮变为开始
                    break
                Treasure_Chest_time = int(settings.value('联盟宝箱设置', 20, type=str))
                print_space('等待%s秒后再次执行' % Treasure_Chest_time)
                number = 0
                Treasure_Chest_number = Treasure_Chest_time / 10
                while number < Treasure_Chest_number:
                    if stop_event.is_set():
                        execute = False
                        self.simple_stop_button()  # 停止后按钮变为开始
                        break
                    else:
                        if Treasure_Chest_number < 1:
                            time.sleep(Treasure_Chest_number)
                            break
                        else:
                            number += 1
                            time.sleep(10)
                if stop_event.is_set():
                    execute = False
                    self.simple_stop_button()  # 停止后按钮变为开始
            except:
                print('错误')
    print('任务已结束')
