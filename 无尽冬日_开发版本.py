# -*- encoding=utf8 -*-
__author__ = "猫耳小刻晴"

import logging
from datetime import datetime

from airtest.core.api import *

auto_setup(__file__)
logging.getLogger('airtest').setLevel(logging.ERROR)


# 连接模拟器
def Cnnect():
    a = 1
    while True:  # 连接模拟器
        try:
            print('%d.开始连接模拟器' % a)
            connect_device("android://127.0.0.1:5037/emulator-5570")
            print_with_space('连接模拟器成功，准备启动游戏')
            start()  # 首次运行
            break
        except:
            a += 1
            print_with_space('未连接到模拟器，10s后重新执行')
            time.sleep(10)


# 启动APP
def start():
    if exists(Template(r"icon\tpl1719196072757.png", threshold=0.8, record_pos=(0.112, -0.519), resolution=(414, 780))):
        print_with_space('游戏未启动，点击启动')
        touch(Template(r"icon\tpl1719196072757.png", record_pos=(0.112, -0.519), resolution=(414, 780)))
        print_with_space("等待25秒启动时间...")
        time.sleep(25)
        Homepage()
    else:
        print_with_space('游戏已启动，开始执行游戏任务')


# 主页判断
def Homepage():
    a = 1
    while a < 3:
        if exists(Template(r"icon\tpl1719198809581.png", threshold=0.9, record_pos=(-0.398, 0.819), scale_max=800,
                           resolution=(414, 780))):
            print_with_space("在主页，准备执行任务")  # 在主界面，执行任务
            break
        else:
            a += 1
            print_with_space("不在主页，返回上一级")
            if exists(Template(r"icon\tpl1719198082012.png", threshold=0.8, record_pos=(-0.44, -0.783),
                               resolution=(414, 780))):
                print_with_space('点击返回按钮')
                touch(
                    Template(r"icon\tpl1719198082012.png", threshold=0.8, record_pos=(-0.44, -0.783),
                             resolution=(414, 780)))
            elif exists(Template(r"icon\tpl1719198103804.png", record_pos=(0.442, -0.35), resolution=(414, 780))):
                print_with_space('点击关闭按钮')
                touch(Template(r"icon\tpl1719198103804.png", record_pos=(0.442, -0.35), resolution=(414, 780)))
            else:
                print_with_space('点击其他区域')
                touch([500, 600])  # 不在主界面，返回到主页
    if a == 3:
        re_connet()


# 互助功能
def Help():
    result = exists(Template(r"icon\tpl1718936896202.png", record_pos=(0.248, 0.735), resolution=(449, 842)))
    if result:  # 判断是否有盟员求助
        print_with_space("有盟员求助，需点击援助按钮")
        touch([800, 1700])
        print_with_space("点击援助按钮成功，等待10s进行下一个任务")
        time.sleep(10)
    else:
        print_with_space("无盟员求助，等待10s进行下一个任务")
        time.sleep(10)


# 生产士兵
def train():
    time.sleep(3)  # 等待3秒
    print_with_space("收取已生产士兵...")
    touch([500, 950])  # 收取已生产的兵
    time.sleep(1)  # 等待1秒
    print_with_space("点击兵营")
    touch([500, 950])  # 点击兵营
    time.sleep(1)  # 等待1秒
    print_with_space("点击训练")
    touch([786, 1221])  # 点击训练按钮
    time.sleep(1)  # 等待1秒
    print_with_space('检查是否有可晋升士兵')
    if exists(Template(r"icon\tpl1721784527077.png", record_pos=(-0.439, 0.078), resolution=(1080, 1920))):
        print_with_space('点击前往可晋升士兵')
        touch(Template(r"icon\tpl1721784527077.png", record_pos=(-0.439, 0.078), resolution=(1080, 1920)))
        print_with_space('点击晋升图标')
        touch(Template(r"icon\tpl1721784547262.png", record_pos=(0.399, 0.019), resolution=(1080, 1920)))
        print_with_space('点击开始晋升士兵')
        touch(Template(r"icon\tpl1721784579063.png", rgb=True, record_pos=(0.22, 0.338), resolution=(1080, 1920)))
    elif exists(Template(r"icon\tpl1721784547262.png",rgb=True, record_pos=(0.399, 0.019), resolution=(1080, 1920))):
        print_with_space('点击晋升图标')
        touch(Template(r"icon\tpl1721784547262.png", record_pos=(0.399, 0.019), resolution=(1080, 1920)))
        print_with_space('点击开始晋升士兵')
        touch(Template(r"icon\tpl1721784579063.png", rgb=True, record_pos=(0.22, 0.338), resolution=(1080, 1920)))
    elif exists(Template(r"icon\tpl1721784547262.png",rgb=True, record_pos=(0.399, 0.019), resolution=(1080, 1920))):
        print_with_space('点击兵种')
        touch(Template(r"icon\tpl1721784547262.png", record_pos=(0.399, 0.019), resolution=(1080, 1920)))
        print_with_space('点击晋升图标')
        touch(Template(r"icon\tpl1721784547262.png", record_pos=(0.399, 0.019), resolution=(1080, 1920)))
        print_with_space('点击开始晋升士兵')
        touch(Template(r"icon\tpl1721784579063.png", rgb=True, record_pos=(0.22, 0.338), resolution=(1080, 1920)))
    else:
        print_with_space("没有可晋升士兵，点击训练士兵")
        touch([800, 1800])  # 点击开始训练士兵
    time.sleep(1)  # 等待1秒
    print_with_space("返回上一级")
    if exists(Template(r"icon\tpl1719198082012.png", threshold=0.5, record_pos=(-0.44, -0.783), resolution=(414, 780))):
        touch(Template(r"icon\tpl1719198082012.png", threshold=0.5, record_pos=(-0.44, -0.783), resolution=(414, 780)))
    elif exists(Template(r"icon\tpl1719198103804.png", record_pos=(0.442, -0.35), resolution=(414, 780))):
        touch(Template(r"icon\tpl1719198103804.png", record_pos=(0.442, -0.35), resolution=(414, 780)))  # 关闭当前界面
    else:
        print('\033[31m未找到对应图案\033[0m')
    print_with_space('训练完成')
    time.sleep(1)
    touch([14, 823])
    time.sleep(1)  # 等待1秒


# 训练检查
def Production_soldiers():
    touch([14, 823])
    time.sleep(1)
    touch([170, 400])
    if exists(Template(r"icon\tpl1719478488282.png",rgb=True, threshold=0.9, record_pos=(-0.186, -0.058),
                       resolution=(414, 780))):
        print_with_space("跳转到盾兵兵营...")
        touch([600, 840])  # 点击索引到对应兵营
        train()
    if exists(Template(r"icon\tpl1719480722195.png", threshold=0.9, record_pos=(-0.437, 0.046), resolution=(414, 780))):
        print_with_space("跳转到矛兵兵营...")
        touch([600, 942])  # 点击索引到对应兵营
        train()
    if exists(Template(r"icon\tpl1719480732965.png", threshold=0.9, record_pos=(-0.437, 0.145), resolution=(414, 780))):
        print_with_space("跳转到射手兵营...")
        touch([600, 1060])  # 点击索引到对应兵营
        train()
    else:
        print_with_space("没有兵营已完成生产，结束该任务")
        touch(
            Template(r"icon\tpl1719552273333.png", threshold=0.9, record_pos=(0.142, -0.126), resolution=(1080, 1920)))


def clear_python_caches():
    os.system('python -m py_compile -c .')  # 清理解释器代码缓存
    os.system('python -m compileall -c .')  # 清理解释器编译后的代码缓存


# 升级资源检查
def build_main():
    touch(Template(r"icon\tpl1719651083870.png", record_pos=(0.001, 0.731), resolution=(449, 842)))
    time.sleep(1)
    if exists(Template(r"icon\tpl1719817875178.png", record_pos=(-0.002, 0.683), resolution=(1080, 1920))):
        print_with_space('一键补齐资源不足，回到首页')
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
    if exists(
            Template(r"icon\tpl1719643933714.png", threshold=0.95, record_pos=(-0.306, -0.318), resolution=(449, 842))):
        print_with_space('有空闲队列，开始建造')
        touch(Template(r"icon\tpl1719643933714.png", record_pos=(-0.306, -0.318), resolution=(449, 842)))  # 点击跳转到需升级的建筑
        if exists(Template(r"icon\tpl1719580056417.png", record_pos=(-0.362, 0.238),
                           resolution=(449, 842))):  # 判断是什么建筑升级升级
            print_with_space('升级资源建筑')
            time.sleep(5)  # 等待5s
            if not exists(
                    Template(r"icon\tpl1719644932718.png", threshold=0.9, record_pos=(0.308, 0.056),
                             resolution=(449, 842))):
                print_with_space('建筑设施未达到升级要求，升级设施')
                while not exists(
                        Template(r"icon\tpl1719645172814.png", record_pos=(0.248, -0.102), resolution=(449, 842))):
                    touch([900, 1000])
                    if exists(
                            Template(r"icon\tpl1719645172814.png", record_pos=(0.248, -0.102), resolution=(449, 842))):
                        print_with_space('达到升级条件，开始升级')
            touch([900, 800])  # 点击升级按钮
            touch([800, 1800])  # 点击升级
            if exists(Template(r"icon\tpl1719651083870.png", record_pos=(0.001, 0.731),
                               resolution=(449, 842))):  # 判断资源是否充足
                print_with_space("/31资源不足，点击一键补齐")
                build_main()
            else:
                time.sleep(1)
                touch(Template(r"icon\tpl1719579273500.png", record_pos=(0.003, -0.045), resolution=(449, 842)))  # 点击求助
        else:
            print_with_space('升级功能建筑')
            touch([553, 1333])  # 点击升级按钮
            touch(Template(r"icon\tpl1719578558005.png", record_pos=(0.003, -0.045), resolution=(449, 842)))  # 点击升级
            if exists(Template(r"icon\tpl1719651083870.png", record_pos=(0.001, 0.731),
                               resolution=(449, 842))):  # 判断资源是否充足
                print_with_space('资源不足，点击一键补齐')
                build_main()
            else:
                time.sleep(1)
                touch(Template(r"icon\tpl1719579273500.png", record_pos=(0.003, -0.045), resolution=(449, 842)))  # 点击求助
    else:
        print_with_space("没有空闲建筑队列")
        touch(
            Template(r"icon\tpl1719552273333.png", threshold=0.9, record_pos=(0.142, -0.126), resolution=(1080, 1920)))


# 搜索资源
def search_main():
    if not exists(Template(r"icon\tpl1720145326019.png", record_pos=(0.404, 0.852), resolution=(1080, 1920))):
        print_with_space('不在世界，点击去往世界')
        touch([950, 1850])  # 点击野外
        time.sleep(5)
    print_with_space('点击搜索图标')
    touch([63, 1314])  # 点击搜索图标
    time.sleep(1)  # 等待1s
# 打雪怪功能
def NPC():
    now = datetime.now().date()
    if now.day == 24 or now.day == 25 or now.day == 26:
        print_with_space('打雪怪时间，开始集结雪怪')
        print_with_space('打开背包')
        touch([460, 1836])  # 点击打开背包
        time.sleep(1)
        if exists(
                Template(r"icon\tpl1719376487523.png", record_pos=(0.449, -0.78), resolution=(414, 780))):  # 判断背包是否打开成功
            touch([949, 171])  # 点击其他跳转至该页
            print_with_space('查看活动道具')
            if exists(Template(r"icon\tpl1719376586643.png", record_pos=(0.106, -0.476),
                               resolution=(414, 780))):  # 判断是否有该道具
                print_with_space('使用活动道具')
                touch(Template(r"icon\tpl1719376586643.png", record_pos=(0.106, -0.476), resolution=(414, 780)))  # 点击道具
                touch(Template(r"icon\tpl1719376629723.png", record_pos=(0.0, 0.092), resolution=(414, 780)))  # 点击使用
                time.sleep(1)
                print_with_space('集结打怪')
                touch(Template(r"icon\tpl1719376765868.png", record_pos=(0.002, 0.705),
                               resolution=(414, 780)))  # 寻找到怪物点击集结
                touch(Template(r"icon\tpl1719376776844.png", record_pos=(0.0, 0.326), resolution=(414, 780)))  # 点击发起集结
                print_with_space('兵力检查')
                if exists(Template(r"icon\tpl1721191349774.png", record_pos=(-0.118, 0.782), resolution=(1080, 1920))):
                    touch(Template(r"icon\tpl1721191349774.png", record_pos=(-0.118, 0.782), resolution=(1080, 1920)))
                    print_with_space('体力检查')
                    if exists(Template(r"icon\tpl1719376787180.png", record_pos=(0.268, 0.824),
                                       resolution=(414, 780))):  # 判断体力是否充足
                        energy()
                    else:
                        print("体力不足，暂停打怪")
                else:
                    print('兵力不足，暂停打怪')
            else:
                print("未找到相关物品，退出任务")
                touch(Template(r"icon\tpl1719198082012.png", threshold=0.5, record_pos=(-0.44, -0.783),
                               resolution=(414, 780))) or touch(
                    Template(r"icon\tpl1719198103804.png", record_pos=(0.442, -0.35), resolution=(414, 780)))
    else:
        print_with_space('未到活动时间，不执行该功能')
# 野兽
def Brush_XG():
    now = datetime.now().time()
    if 17 <= now.hour <= 22:
        print_with_space('打野怪时间，开始出征')
        search_main()
        print_with_space('点击选择普通野兽')
        touch([120, 1373])  # 点击普通野兽
        time.sleep(1)  # 等待1s
        print_with_space('点击等级')
        touch([651, 1573])  # 点击等级3
        time.sleep(1)  # 等待1s
        print_with_space('点击搜索按钮')
        touch([534, 1821])  # 点击搜索
        time.sleep(1)  # 等待1s
        print_with_space('点击出征按钮')
        touch(Template(r"icon\tpl1721191349775.png", rgb=False, record_pos=(0.002, 0.705),
                       resolution=(414, 780)))  # 点击出征怪物
        time.sleep(1)  # 等待1s
        if exists(
                Template(r"icon\tpl1721191349774.png", record_pos=(-0.118, 0.782), resolution=(1080, 1920))):  # 判断是否有兵力
            touch(Template(r"icon\tpl1721191349774.png", record_pos=(-0.118, 0.782), resolution=(1080, 1920)))
            if exists(Template(r"icon\tpl1719376787180.png", record_pos=(0.268, 0.824),
                               resolution=(414, 780))):  # 判断体力是否充足
                energy()
            else:
                print_with_space("体力不足，暂停打野怪")
        else:
            print_with_space('兵力不足，暂停打野怪')
            print_with_space('点击出征按钮')
    else:
        print_with_space('未到时间，暂停打野怪')
# 巨兽活动
def bear():
    now = datetime.now().time()
    if 20 < now.hour < 23:
        print_with_space('当前时间：\033[31m%s\033[0m,巨兽活动进行中' % now.strftime("%H:%M:%S"))
        if exists(Template(r"icon\tpl1721191349777.png", record_pos=(0.26, 0.795), resolution=(1080, 1920))):
            print_with_space('点击活动按钮')
            touch(Template(r"icon\tpl1721191349777.png", record_pos=(0.26, 0.795), resolution=(1080, 1920)))
            time.sleep(2)
            print_with_space('点击集结按钮')
            touch(Template(r'icon\tpl1721784579065.png', record_pos=(0.26, 0.795), resolution=(1080, 1920)))
            if exists(Template(r"icon\tpl1721784579066.png", record_pos=(0.26, 0.795), resolution=(1080, 1920))):
                print_with_space('发起集结')
                touch(Template(r"icon\tpl1721784579066.png", record_pos=(0.26, 0.795), resolution=(1080, 1920)))
                print_with_space('点击出征')
                touch(Template(r"icon\tpl1721784579067.png", record_pos=(0.002, 0.705), resolution=(414, 780)))
                print_with_space('出征成功')
            else:
                print_with_space('集结中')
        else:
            print_with_space('未找到活动图标')
    else:
        # 输出当前时间
        print_with_space('当前时间：\033[31m%s\033[0m,未到巨兽活动时间' % now.strftime("%H:%M"))


# 冰原巨兽
def Brush_WM():
    now = datetime.now().time()
    if now.hour == 10 or now.hour == 18:
        search_main()
        print_with_space('点击选择冰原巨兽')
        touch([365, 1373])  # 点击冰原巨兽
        time.sleep(1)  # 等待1s
        print_with_space('点击等级')
        touch([500, 1573])  # 点击等级3
        time.sleep(1)  # 等待1s
        print_with_space('点击搜索按钮')
        touch([534, 1821])  # 点击搜索
        time.sleep(1)  # 等待1s
        print_with_space('点击集结按钮')
        touch(Template(r"icon\tpl1719376765868.png", record_pos=(0.002, 0.705), resolution=(414, 780)))  # 点击怪物集结
        time.sleep(1)  # 等待1s
        print_with_space('点击发起集结')
        touch(
            Template(r"icon\tpl1719376776844.png", rgb=True, record_pos=(0.0, 0.326), resolution=(414, 780)))  # 点击发起集结
        time.sleep(1)  # 等待0.5s
        if exists(Template(r"icon\tpl1719376787180.png", record_pos=(0.268, 0.824), resolution=(414, 780))):  # 有兵力可出征
            print_with_space('点击出征按钮')
            energy()
        else:  # 判断是否有多余兵力
            print_with_space('不满足条件，无兵力出征')
    else:
        print_with_space('未到时间，暂停打冰原巨兽')


# 采集出兵
def gather():
    touch(Template(r"icon\tpl1720675061569.png", record_pos=(0.002, -0.015), resolution=(1080, 1920)))
    if exists(Template(r"icon\tpl1720675170747.png", record_pos=(0.26, 0.795), resolution=(1080, 1920))):  # 有兵力可出征
        print_with_space('点击出征按钮')
        touch(Template(r"icon\tpl1720675170747.png", record_pos=(0.26, 0.795), resolution=(1080, 1920)))  # 点击出征
        print_with_space('出征成功')
        time.sleep(1)
    else:  # 判断是否有多余兵力
        print_with_space('不满足条件，无兵力出征')
# 打怪出兵
def energy():
    touch(Template(r"icon\tpl1719376787180.png", record_pos=(0.268, 0.824), resolution=(414, 780)))  # 点击出征
    time.sleep(1)
    if exists(Template(r"icon\tpl1720264632282.png", record_pos=(0.301, -0.33), resolution=(1080, 1920))):  # 判断是否有体力
        print_with_space("体力不足，不满足出征条件，开始回到主页")
        print_with_space('关闭补充体力界面')
        touch(Template(r"icon\tpl1719198103804.png", record_pos=(0.442, -0.35), resolution=(414, 780)))
        print_with_space('关闭出征界面')
        touch(Template(r"icon\tpl1719198082012.png", threshold=0.5, record_pos=(-0.44, -0.783), resolution=(414, 780)))
    else:
        print_with_space("出征成功")


# 生肉
def Meat():
    print_with_space('准备采集生肉资源')
    print_with_space('点击搜索图标')
    touch([63, 1314])  # 点击搜索图标
    time.sleep(1)  # 等待1s
    swipe([600, 1370], vector=[-0.4103, 0.0170])  # 滑动
    print_with_space('点击选择肉')
    touch([240, 1373])  # 点击选择肉
    time.sleep(1)  # 等待1s
    print_with_space('点击等级')
    touch([570, 1573])  # 点击等级
    time.sleep(1)  # 等待1s
    print_with_space('点击搜索按钮')
    touch([534, 1821])  # 点击搜索
    time.sleep(3)  # 等待1s
    if exists(Template(r"icon\tpl1720675061569.png", rgb=True, record_pos=(0.002, -0.015), resolution=(1080, 1920))):
        gather()
    else:
        print_with_space('未搜索到生肉资源，结束该任务')


# 木材
def Wood():
    print_with_space('准备采集木材资源')
    print_with_space('点击搜索图标')
    touch([63, 1314])  # 点击搜索图标
    time.sleep(1)  # 等待1s
    swipe([600, 1370], vector=[-0.4103, 0.0170])  # 滑动
    print_with_space('点击选择木材资源')
    touch([476, 1373])  # 点击选择木材
    time.sleep(1)  # 等待1s
    print_with_space('点击等级')
    touch([570, 1573])  # 点击等级
    time.sleep(1)  # 等待1s
    print_with_space('点击搜索按钮')
    touch([534, 1821])  # 点击搜索
    time.sleep(1)  # 等待1s
    if exists(Template(r"icon\tpl1720675061569.png", record_pos=(0.002, -0.015), resolution=(1080, 1920))):
        gather()
    else:
        print_with_space('未搜索到对应资源，结束该任务')


# 煤矿
def Coal():
    print_with_space('准备采集煤矿资源')
    print_with_space('点击搜索图标')
    touch([63, 1314])  # 点击搜索图标
    time.sleep(1)  # 等待1s
    swipe([600, 1370], vector=[-0.4103, 0.0170])  # 滑动
    print_with_space('点击选择煤矿资源')
    touch([710, 1373])  # 点击选择煤矿
    time.sleep(1)  # 等待1s
    print_with_space('点击等级')
    touch([570, 1573])  # 点击等级
    time.sleep(1)  # 等待1s
    print_with_space('点击搜索按钮')
    touch([534, 1821])  # 点击搜索
    time.sleep(1)  # 等待1s
    if exists(Template(r"icon\tpl1720675061569.png", record_pos=(0.002, -0.015), resolution=(1080, 1920))):
        gather()
    else:
        print_with_space('未搜索到煤矿资源，结束该任务')


# 铁矿
def Iron():
    print_with_space('准备采集铁矿资源')
    print_with_space('点击搜索图标')
    touch([63, 1314])  # 点击搜索图标
    time.sleep(1)  # 等待1s
    swipe([600, 1370], vector=[-0.4103, 0.0170])  # 滑动
    print_with_space('点击选择铁矿资源')
    touch([950, 1373])  # 点击选择铁矿
    time.sleep(1)  # 等待1s
    print_with_space('点击等级')
    touch([570, 1573])  # 点击等级
    time.sleep(1)  # 等待1s
    print_with_space('点击搜索按钮')
    touch([534, 1821])  # 点击搜索
    time.sleep(1)  # 等待1s
    if exists(Template(r"icon\tpl1720675061569.png", record_pos=(0.002, -0.015), resolution=(1080, 1920))):
        touch(Template(r"icon\tpl1720675061569.png", record_pos=(0.002, -0.015), resolution=(1080, 1920)))
        if not exists(
                Template(r"icon\tpl1720675170747.png", record_pos=(0.26, 0.795), resolution=(1080, 1920))):  # 判断是否有多余兵力
            print_with_space('不满足条件，无兵力出征')
        else:  # 有兵力可出征
            print_with_space('点击出征按钮')
            touch(Template(r"icon\tpl1720675170747.png", record_pos=(0.26, 0.795), resolution=(1080, 1920)))  # 点击出征
            print_with_space('出征成功')
    else:
        print_with_space('未搜索到铁矿资源，结束该任务')


# 自动采集
def Collection():
    now = datetime.now().time()
    if now.hour == 8:
        if not exists(Template(r"icon\tpl1720145326019.png", record_pos=(0.404, 0.852), resolution=(1080, 1920))):
            print_with_space('不在世界，点击去往世界')
            touch([950, 1850])  # 点击野外
            time.sleep(5)  # 等待5秒
        else:
            print_with_space('在野外，执行采集任务')
            time, sleep(3)
        touch([14, 823])
        time.sleep(1)
        touch([500, 400])
        if not exists(Template(r"icon\tpl1720691682616.png", record_pos=(-0.168, -0.088), resolution=(1080, 1920))):
            print_with_space('有空闲队伍，执行采肉任务')
            time.sleep(1)
            Meat()
        else:
            print_with_space('已有采肉队伍')
        if not exists(Template(r"icon\tpl1720766916044.png", record_pos=(-0.168, -0.088), resolution=(1080, 1920))):
            print_with_space('有空闲队伍，执行采木头任务')
            time.sleep(1)
            Wood()
        else:
            print_with_space('已有采木材队伍')
        if not exists(Template(r"icon\tpl1720766916045.png", record_pos=(-0.168, -0.088), resolution=(1080, 1920))):
            print_with_space('有空闲队伍，执行采煤任务')
            time.sleep(1)
            Coal()
        else:
            print_with_space('已有采煤队伍')
        if not exists(
                Template(r"icon\tpl1720766916046.png", rgb=True, record_pos=(-0.168, -0.088), resolution=(1080, 1920))):
            print_with_space('有空闲队伍，执行采铁任务')
            time.sleep(1)
            Iron()
        else:
            print_with_space('已有采铁队伍')
        touch(
            Template(r"icon\tpl1719552273333.png", threshold=0.9, record_pos=(0.142, -0.126), resolution=(1080, 1920)))
    else:
        print_with_space('当前时间：\033[31m%s\033[0m,未到采集时间' % now.strftime("%H:%M"))
#治疗
def treatment():
    now = datetime.now().time()
    if now.minute == 00:
        if exists(Template(r"icon\tpl1721191349778.png", record_pos=(-0.168, -0.088), resolution=(1080, 1920))):
            print_with_space("点击治疗图标")
            touch(Template(r"icon\tpl1721191349778.png", threshold=0.8, record_pos=(-0.168, -0.088), resolution=(1080, 1920)))
            print_with_space('点击治疗按钮')
            touch(Template(r"icon\tpl1721191349779.png", threshold=0.8, record_pos=(0.142, -0.126),
                           resolution=(1080, 1920)))
            print_with_space('点击联盟互助')
            touch(Template(r"icon\tpl1721191349780.png", threshold=0.8, record_pos=(0.142, -0.126),
                           resolution=(1080, 1920)))
        else:
            print_with_space('没有需要治疗的士兵')

#联盟捐赠
def lmjz():
    now = datetime.now().time()
    if now.hour % 4 ==0:
        touch([500,100])
#设备顶号重连
def re_connet():
    if exists(Template(r"icon\tpl1720766916047.png", rgb=False, record_pos=(-0.168, -0.088), resolution=(1080, 1920))):
        print_with_space('\033[31m在其他设备登录，等待5分钟后重新连接\033[0m')
        time.sleep(300)
        try:
            print('点击重新连接')
            while True:
                touch(
                    Template(r"icon\tpl1720766916047.png", record_pos=(-0.168, -0.088),
                             resolution=(1080, 1920)))
                time.sleep(10)
                if exists(Template(r"icon\tpl1720766916047.png", rgb=False, record_pos=(-0.168, -0.088),
                                   resolution=(1080, 1920))):
                    print('\033[31m重新连接失败，等待1分钟继续尝试\033[0m')
                    time.sleep(60)
                else:
                    print('重新连接成功')
                    break
        except:
            print('\033[31m重新连接失败，稍后尝试\033[0m')
    else:
        print('连接正常')

# 主体代码
def Subject():
    i = 10
    while True:
        if i % 10 == 0:
            print('%d.开始执行训练任务' % i)
            Homepage()  # 主页检查
            try:
                Production_soldiers()  # 训练模块
            except:
                print('\033[31m程序执行异常，结束该任务，执行其他任务\033[0m')
            i += 1
        elif i % 14 == 0:
            print('%d.开始执行建造任务' % i)
            Homepage()  # 主页检查
            try:
                Build()  # 建造模块
            except:
                print('\033[31m程序执行异常，结束该任务，执行其他任务\033[0m')
            i += 1
        elif i % 19 == 0:
            print('%d.开始执行打怪任务' % i)
            Homepage()  # 主页检查
            try:
                Brush_XG()  # 打普通野怪
                Brush_WM()  # 打巨兽模块
                NPC()  # 打雪怪模块
            except:
                print('\033[31m程序执行异常，结束该任务，执行其他任务\033[0m')
            i += 1
        elif i % 29 == 0:
            print('开始执行采集任务')
            Homepage()  # 主页检查
            try:
                Collection()  # 采集资源模块
            except:
                print('\033[31m程序执行异常，结束该任务，执行其他任务\033[0m')
            print('\033[31m执行完成，结束该周期，开始新的周期\033[0m')
            i = 1
        else:
            print('%d.开始执行互助任务' % i)
            Homepage()  # 主页检查
            try:
                Help()  # 互助模块
                bear()  # 巨熊模块
                treatment() #治疗模块
            except:
                print('\033[31m程序执行异常，结束该任务，执行其他任务\033[0m')
            i += 1


def print_with_space(variable, spaces=4):
    print(' ' * spaces + str(variable))


def main():
    Cnnect()
    Subject()
main()
