# 功能逻辑
import time
# 避免使用通配符导入，明确导入需要的模块和函数
# 由于 swipe 未定义，
from airtest.core.api import exists, touch, keyevent, ST, swipe, text, find_all
from airtest.core.cv import Template
# 避免通配符导入，明确导入需要的类或函数，这里假设需要导入 Android 类
from airtest.core.android.android import Android
from numpy import random
from Window_UI import settings
from datetime import datetime
import subprocess
import threading
ST.FIND_TIMEOUT = 2.5  # 设置全局识别超时为秒
number_physical_strength = 0
intelligence_number = 0  # 情报次数

stop_event = threading.Event()


# Identification_State = True
# 重写打印
def print_space(variable, spaces=4):
    """
    打印带有指定空格缩进的字符串。
    :param variable: 要打印的变量或字符串。
    :param spaces: 缩进的空格数，默认为4。
    """
    # 使用指定数量的空格进行缩进，并将变量转换为字符串后打印
    print(' ' * spaces + str(variable))


# 检查并点击
#def check_and_touch(templateObj, message="", target_pos=None):
def check_and_touch(templateObj, message="", message_unfind="", target_pos=None):
    # global Identification_State
    # print('等待时间：%s' % timeout)
    pos = exists(templateObj)
    if pos:
        if message:
            print_space(message)
        touch(pos if not target_pos else target_pos)
        return True
    if message_unfind:
        print_space(message_unfind)
    return False


# 主页判断
def Homepage():
    """
    主页判断函数，用于判断当前是否在游戏主页，并根据情况执行相应操作。
    该函数通过检查特定图标是否存在来判断当前是否在主页。如果不在主页，
    则尝试点击不同颜色的返回按钮或关闭按钮，直到达到最大尝试次数或成功返回主页。
    如果达到最大尝试次数，则调用 `re_connet` 函数进行设备顶号重连。

    :return: 无返回值
    """
    if datetime.now().hour == 0 and datetime.now().minute == 0:
        print_space('新的一天开始，重置情报执行次数')
    check_number = 1  # 初始化变量 a 为 1，用于控制循环次数
    try:
        while check_number < 4:  # 循环最多执行 3 次
            # 判断是否存在特定图标，如果存在则打印信息并跳出循环
            # if exists(Template(r"icon\tpl1719198809581.png", rgb=True, record_pos=(-0.441, -0.839), resolution=(1080, 1920))):
            if exists(Template(r"icon\tpl1719198809581.png", rgb=True, record_pos=(-0.441, -0.839), resolution=(1080, 1920))):
                print_space("在主页，准备执行任务")  # 在主界面，执行任务
                break
            else:
                check_number += 1  # 增加 a 的值
                print_space("不在主页，返回上一级")
                # 模拟按下手机的返回键
                keyevent('BACK')
                print_space("成功调用手机的返回按钮")
            '''if stop_event.is_set():
                self.select_stop_button()
                break'''
    except:
        print('执行错误')  # 捕获异常并打印错误信息
    if check_number == 4:  # 如果 a 的值达到 4
        re_connet()  # 调用 re_connet 函数进行设备顶号重连


# 设备顶号重连
def re_connet():
    if exists(Template(r"icon/tpl1720766916047.png", rgb=False, record_pos=(-0.168, -0.088), resolution=(1080, 1920))):
        print('在其他设备登录，等待5分钟后重新连接')
        time.sleep(300)
        try:
            print_space('点击重新连接')
            re = 1
            while re > 0:
                touch(Template(r"icon/tpl1720766916047.png", rgb=False, record_pos=(-0.168, -0.088), resolution=(1080, 1920)))
                time.sleep(10)
                if exists(Template(r"icon/tpl1720766916047.png", rgb=False, record_pos=(-0.168, -0.088), resolution=(1080, 1920))):
                    print('重新连接失败，等待1分钟继续尝试')
                    time.sleep(60)
                else:
                    print_space('重新连接成功')
                    re = 0
        except:
            print('重新连接失败，稍后尝试')
    else:
        print_space('未检查到设备顶号，尝试回到模拟器主界面重启游戏')
        # 模拟按下手机的HOME键
        keyevent('HOME')
        print_space('开始尝试启动游戏')
        touch(Template(r"icon/tpl1719196072757.png", record_pos=(0.112, -0.519), resolution=(414, 780)))
        print_space("启动成功，等待30秒启动时间...")
        time.sleep(30)
        print_space('启动完成')


# 互助功能
def Help(self):
    if stop_event.is_set():  # 在函数开始时检查是否停止
        return  # 如果停止，直接返回
    if exists(Template(r"icon\tpl1718936896202.png", record_pos=(0.248, 0.735), resolution=(1080, 1920))):  # 判断是否有盟员求助
        print_space("有盟员求助，需点击援助按钮")
        if self.checkBox_Random_time.isChecked():
            random_number = random.randint(0, 5)  # 随机数
            print_space('随机等待时间：%s秒' % random_number)
            time.sleep(random_number)  # 等待随机时间后
        record = random.randint(1, 9)
        print_space('随机点击位置：%s' % record)
        if stop_event.is_set():  # 点击前检查是否停止
            return  # 如果停止，直接返回
        check_and_touch(Template(r"icon\tpl1718936896202.png", target_pos=record, record_pos=(0.248, 0.735), resolution=(1080, 1920)))
    else:
        print_space("未找到求助按钮，进行下一个任务")


# 生产士兵
def train(self):
    lv_y = 0  # 设置初始循环次数
    time.sleep(5)  # 等待3秒
    print_space("收取已生产士兵...")
    touch([500, 950])  # 收取已生产的兵
    time.sleep(1)  # 等待1秒
    print_space("点击兵营")
    touch([500, 950])  # 点击兵营
    time.sleep(1)  # 等待1秒
    print_space("点击训练")
    if self.checkBox_maxed_barracks.isChecked():  # 判定是否勾选满级兵营
        touch([623, 1319])  # 点击训练按钮
    else:
        touch([786, 1221])  # 点击训练按钮
    time.sleep(1)  # 等待1秒
    if self.checkBox_jinshen.isChecked():  # 判定是否勾选可优先晋升
        print_space('检查是否有可晋升士兵')
        if exists(Template(r"icon/tpl1721784527077.png", record_pos=(-0.439, 0.078), resolution=(1080, 1920))):
            print_space('点击前往可晋升士兵')
            touch(Template(r"icon/tpl1721784527077.png", record_pos=(-0.439, 0.078), resolution=(1080, 1920)))
            print_space('点击晋升图标')
            touch(Template(r"icon/tpl1721784547262.png", record_pos=(0.399, 0.019), resolution=(1080, 1920)))
            print_space('点击开始晋升士兵')
            touch(Template(r"icon/tpl1727422988298.png", record_pos=(0.216, 0.339), resolution=(1080, 1920)))
            lv_y = 1  # 更新初始循环次数,不会进入可训练士兵检查
        elif exists(Template(r"icon/tpl1721784547262.png", rgb=True, record_pos=(0.399, 0.019), resolution=(1080, 1920))):
            print_space('点击晋升图标')
            touch(Template(r"icon/tpl1721784547262.png", record_pos=(0.399, 0.019), resolution=(1080, 1920)))
            print_space('点击开始晋升士兵')
            touch(Template(r"icon/tpl1727422988298.png", record_pos=(0.216, 0.339), resolution=(1080, 1920)))
            lv_y = 1  # 更新初始循环次数,不会进入可训练士兵检查
        else:
            print_space("上一页没有可晋升低级士兵，检查本页是否有可晋升士兵")
            # swipe([950, 1225], vector=[-0.8, 0.0170])  # 滑动训练兵种（不滑动，预防当前页面不在最高级页面
            time.sleep(1)
            touch([910, 1225])  # 点击最右边兵
            lv_x = 910  # 设置初始x坐标
            lv_y = 5  # 设置初始循环次数
            while lv_y > 0:
                if exists(Template(r"icon/tpl1721784547262.png", rgb=True, record_pos=(0.399, 0.019), resolution=(1080, 1920))):  # 找到晋升图案
                    print_space('点击晋升图标')
                    touch(Template(r"icon/tpl1721784547262.png", record_pos=(0.399, 0.019), resolution=(1080, 1920)))
                    print_space('点击开始晋升士兵')
                    touch(Template(r"icon/tpl1727422988298.png", record_pos=(0.216, 0.339), resolution=(1080, 1920)))
                    break
                else:
                    lv_x = lv_x - 200  # 初始x坐标减200
                    touch([lv_x, 1225])  # 点击开始上一级士兵
                    lv_y -= 1
    if lv_y == 0:  # 当ly_y循环次数为0时，进行训练士兵检查
        swipe([950, 1225], vector=[-0.8, 0.0170])  # 滑动训练兵种至最高级界面
        time.sleep(1)
        touch([910, 1225])  # 点击十级兵
        lv_x_1 = 910  # 设置点击初始x坐标
        lv_y_1 = 10  # 设置初始循环次数
        while True:
            # 判断是否有训练按钮
            if exists(Template(r"icon/tpl17217845790633.png", rgb=True, threshold=0.8, record_pos=(0.22, 0.338), resolution=(
                    1080, 1920))):  # 判断到训练按钮
                print_space("找到训练按钮，开始训练士兵")
                touch([800, 1800])  # 点击开始训练士兵
                break  # 退出该循环
            else:  # 如果没找到训练按钮，就点击上一级士兵
                lv_x_1 = lv_x_1 - 200  # 初始x坐标减200
                print_space("未找到训练按钮，点击上一级士兵")
                touch([lv_x_1, 1225])  # 点击上一级士兵
                lv_y_1 -= 1  # 循环次数减1
                if lv_y_1 == 5:  # 当前页没找到可训练士兵，滑动到前一页进行查找
                    lv_x_1 = 910
                    swipe([115, 1225], vector=[0.7397, 0.0009])  # 滑动训练兵种至前一页
                    touch([910, 1225])  # 点击五级兵
                elif lv_y_1 <= 0:  # 当循环次数小于0时，跳出该循环，避免卡在该循环内（修复卡在循环内的问题）
                    print_space("没有可训练士兵，结束该任务")
                    break  # 退出该循环
    time.sleep(2)  # 等待2秒
    print_space("返回上一级")
    touch([66, 66])  # 使用坐标点击，防止识别错误
    '''if exists(Template(r"icon/tpl1719198082013.png", threshold=0.8, record_pos=(-0.439, -0.835), resolution=(1080, 1920))):
        touch(Template(r"icon/tpl1719198082013.png", threshold=0.8, record_pos=(-0.439, -0.835), resolution=(1080, 1920)))
    elif exists(Template(r"icon/tpl1719198103804.png", record_pos=(0.442, -0.35), resolution=(1080, 1920))):
        touch(Template(r"icon/tpl1719198103804.png", record_pos=(0.442, -0.35), resolution=(1080, 1920)))  # 关闭当前界面
        if exists(Template(r"icon/tpl1719198082013.png", threshold=0.8, record_pos=(-0.439, -0.835), resolution=(1080, 1920))):
            touch(Template(r"icon/tpl1719198082013.png", threshold=0.8, record_pos=(-0.439, -0.835), resolution=(1080, 1920)))
    else:
        print_space('未找到对应图案')'''
    print_space('训练完成')


# 训练检查
def Production_soldiers(self):
    if exists(Template(r"icon/tpl1720145326019.png", record_pos=(0.404, 0.852), resolution=(1080, 1920))):  # 判断是否在城镇，防止队列影响按钮
        print_space('不在城镇，点击去往城镇')
        touch([950, 1850])  # 点击野外
        time.sleep(5)
    touch([2, 812])  # 点击右侧按钮
    time.sleep(1)
    touch([170, 400])
    print_space('检查盾兵训练是否完成')
    # region_1=(560,900,650,1000)
    if exists(Template(r"icon/tpl1719478488282.png", threshold=0.8, rgb=True, record_pos=(-0.189, -0.009), resolution=(1080, 1920))):
        #if exists(Template(r"icon/tpl1742788475470.png", region=region_1, resolution=(1080, 1920))):
        print_space("1跳转到盾兵兵营...")
        touch([600, 840])  # 点击索引到对应兵营
        train(self)
        Homepage()  # 返回主页
        time.sleep(1)  # 等待1秒
        touch([2, 812])
    elif exists(Template(r"icon/tpl1719478488283.png", threshold=0.85, rgb=True, record_pos=(-0.061, -0.131), resolution=(1080, 1920))):
        print_space("跳转到盾兵兵营...")
        touch([600, 840])  # 点击索引到对应兵营
        train(self)
        Homepage()  # 返回主页
        time.sleep(1)  # 等待1秒
        touch([2, 812])
    print_space('检查矛兵训练是否完成')
    if exists(Template(r"icon/tpl1719480722195.png", threshold=0.8, rgb=True, record_pos=(-0.189, -0.009), resolution=(1080, 1920))):
        print_space("1跳转到矛兵兵营...")
        touch([600, 942])  # 点击索引到对应兵营
        train(self)
        Homepage()  # 返回主页
        time.sleep(1)  # 等待1秒
        touch([2, 812])
    elif exists(Template(r"icon/tpl1719480722196.png", threshold=0.85, rgb=True, record_pos=(-0.063, -0.031), resolution=(1080, 1920))):
        print_space("跳转到矛兵兵营...")
        touch([600, 942])  # 点击索引到对应兵营
        train(self)
        Homepage()  # 返回主页
        time.sleep(1)  # 等待1秒
        touch([2, 812])
    print_space('检查射手训练是否完成')
    if exists(Template(r"icon/tpl1719480732965.png", threshold=0.8, rgb=True, record_pos=(-0.192, 0.087), resolution=(1080, 1920))):
        print_space("1跳转到射手兵营...")
        touch([600, 1060])  # 点击索引到对应兵营
        train(self)
    elif exists(Template(r'icon/tpl1719480732966.png', threshold=0.85, rgb=True, record_pos=(-0.064, 0.071), resolution=(1080, 1920))):
        print_space("跳转到射手兵营...")
        touch([600, 1060])  # 点击索引到对应兵营
        train(self)
    else:
        print_space("未找到待收取的兵营，结束该任务")
        touch(Template(r"icon/tpl1719552273333.png", threshold=0.9, record_pos=(0.142, -0.126), resolution=(1080, 1920)))


# 升级资源检查
def build_main():
    touch(Template(r"icon\tpl1719651083870.png", record_pos=(0.0, 0.682), resolution=(1080, 1920)))
    time.sleep(1)
    if exists(Template(r"icon\tpl1739791465219.png", record_pos=(0.012, -0.607), resolution=(1080, 1920))):
        touch(Template(r"icon\tpl1729834190986.png", record_pos=(0.215, 0.556), resolution=(1080, 1920)))
    if exists(Template(r"icon\tpl1719817875178.png", record_pos=(-0.002, 0.683), resolution=(1080, 1920))):
        print_space('一键补齐资源不足，回到首页')
        touch(Template(r"icon\tpl1719198103804.png", record_pos=(0.442, -0.35), resolution=(1080, 1920)))
        touch(Template(r"icon\tpl1719198103804.png", record_pos=(0.442, -0.35), resolution=(1080, 1920)))
    else:
        touch(Template(r"icon\tpl1729834190986.png", record_pos=(0.224, 0.608), resolution=(1080, 1920)))
        touch(Template(r"icon\tpl1739790693448.png", record_pos=(0.224, 0.531), resolution=(1080, 1920)))  # 点击升级
        time.sleep(1)
        touch(Template(r"icon\tpl1719579273500.png", record_pos=(0.001, -0.092), resolution=(1080, 1920)))


# 自动建筑升级
def Build():
    touch([2, 812])
    time.sleep(1)
    touch([170, 400])
    if exists(Template(r"icon\tpl1719643933714.png", threshold=0.85, rgb=True, record_pos=(-0.311, -0.372), resolution=(1080, 1920))):
        print_space('有空闲队列，开始建造')
        touch(Template(r"icon\tpl1719643933714.png", threshold=0.85, rgb=True, record_pos=(-0.306, -0.318), resolution=(
            1080, 1920)))  # 点击跳转到需升级的建筑
        if exists(Template(r"icon\tpl1719580056417.png", record_pos=(-0.36, 0.193), resolution=(1080, 1920))):  # 判断是什么建筑升级升级
            touch([500, 900])
            print_space('升级资源建筑')
            time.sleep(1)  # 等待5s
            # if not exists(Template(r"icon\tpl1719644932718.png", threshold=0.9, record_pos=(0.308, 0.056), resolution=(1080, 1920))):
            while not exists(Template(r"icon\tpl1719645172814.png", record_pos=(0.346, -0.149), resolution=(1080, 1920))):
                print_space('建筑设施未达到升级要求，升级设施')
                touch([900, 1000])
            if exists(Template(r"icon\tpl1719645172814.png", record_pos=(0.346, -0.149), resolution=(1080, 1920))):
                print_space('达到升级条件，开始升级')
            touch(Template(r"icon\tpl1719645172814.png", record_pos=(0.346, -0.149), resolution=(1080, 1920)))  # 点击升级按钮
            touch(Template(r"icon\tpl1739790693448.png", record_pos=(0.234, 0.759), resolution=(1080, 1920)))  # 点击升级
            if exists(Template(r"icon\tpl1719651083870.png", record_pos=(0.0, 0.682), resolution=(1080, 1920))):  # 判断资源是否充足
                print_space("/31资源不足，点击一键补齐")
                build_main()
            else:
                time.sleep(1)
                print_space('资源充足，点击求助')
                touch(Template(r"icon\tpl1719579273500.png", record_pos=(0.003, -0.045), resolution=(1080, 1920)))  # 点击求助
        else:
            print_space('升级功能建筑')
            touch([553, 1333])  # 点击升级按钮
            touch(Template(r"icon\tpl1739790693448.png", record_pos=(0.222, 0.528), resolution=(1080, 1920)))  # 点击升级
            if exists(Template(r"icon\tpl1719651083870.png", record_pos=(0.0, 0.682), resolution=(1080, 1920))):  # 判断资源是否充足
                print_space('资源不足，点击一键补齐')
                build_main()
            else:
                time.sleep(1)
                touch(Template(r"icon\tpl1719579273500.png", record_pos=(0.001, -0.092), resolution=(1080, 1920)))  # 点击求助
    else:
        print_space("没有空闲建筑队列")
        touch(Template(r"icon\tpl1719552273333.png", threshold=0.85, record_pos=(0.143, -0.124), resolution=(1080, 1920)))


# 搜索资源
def search_main():
    if not exists(Template(r"icon/tpl1720145326019.png", record_pos=(0.404, 0.852), resolution=(1080, 1920))):
        print_space('不在世界，点击去往世界')
        touch([950, 1850])  # 点击野外
        time.sleep(5)
    else:
        print_space('找到城镇图案，在世界')
    print_space('点击搜索图标')
    touch([63, 1320])  # 点击搜索图标
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
            print_space("未找到相关物品，返回主页并退出任务")
            keyevent('BACK')


# 野兽等级输入
def XG_lv():
    print_space('首次启动或数据有更新，重新输入等级')
    print_space('点击等级输入框')
    touch([900, 1573])
    time.sleep(1)
    print_space('删除原本等级')
    keyevent('KEYCODE_DEL')  # 每次只能删除一个数字
    keyevent('KEYCODE_DEL')
    time.sleep(1)  # 等待1秒
    print_space('输入新的等级')
    time.sleep(1)
    text(settings.value('世界野怪等级设置', 10, type=str))  # print_space('点击确定按钮')  # time.sleep(1)  # touch(Template(r"icon/sure_button.png", record_pos=(0.404, 0.852), resolution=(1080, 1920))) #第三方库自带确定功能，取消点击确定按钮


# 野兽
def Brush_XG(self):
    print_space('打野怪时间，开始出征')
    search_main()
    swipe([600, 1370], vector=[0.4103, 0.0170])  # 滑动
    time.sleep(1)  # 等待1s
    print_space('点击选择普通野兽')
    touch([120, 1373])  # 点击普通野兽
    time.sleep(1)  # 等待1s
    '''判断本次是否需要执行选择等级'''
    if settings.value('世界野怪等级设置更新', 1):
        settings.setValue('世界野怪等级设置更新', 0)
        XG_lv()
        time.sleep(1)  # 等待1s
    print_space('点击搜索按钮')
    touch([534, 1821])  # 点击搜索
    time.sleep(1)  # 等待1s
    print_space('点击攻击按钮')
    if exists(Template(r"icon\tpl1721191349775.png", rgb=False, record_pos=(0.002, 0.705), resolution=(1080, 1920))):
        touch(Template(r"icon\tpl1721191349775.png", rgb=False, record_pos=(0.002, 0.705), resolution=(1080, 1920)))  # 点击出征怪物
    else:
        print_space('未找到攻击按钮图案，如游戏内有，请检查模拟器和游戏相关设置或使用自助修复')
    time.sleep(1)  # 等待1s
    if exists(Template(r"icon\tpl1721191349774.png", record_pos=(-0.118, 0.782), resolution=(1080, 1920))):  # 判断是否有兵力
        if self.checkBox_XG_average.isChecked():  # 平均兵力选项
            print_space('点击平均配置')
            touch(Template(r"icon\tpl1721191349774.png", record_pos=(-0.118, 0.782), resolution=(1080, 1920)))
        energy()
    else:
        print_space('兵力不足，暂停打野怪')


# 巨熊活动
def bear(self):
    touch([2, 812])   # 点击打开左侧栏，以确保没有陷阱介绍
    if exists(Template(r"icon/tpl1721191349777.png", record_pos=(0.26, 0.795), resolution=(1080, 1920))):
        print_space('点击活动按钮')
        touch(Template(r"icon/tpl1721191349777.png", record_pos=(0.26, 0.795), resolution=(1080, 1920)))
        time.sleep(2)
        print_space('点击集结按钮')
        touch(Template(r'icon/tpl1721784579065.png', record_pos=(0.26, 0.795), resolution=(1080, 1920)))
        if exists(Template(r"icon/tpl1721784579066.png", record_pos=(0.26, 0.795), resolution=(1080, 1920))):
            print_space('发起集结')
            touch(Template(r"icon/tpl1721784579066.png", record_pos=(0.26, 0.795), resolution=(1080, 1920)))
            if self.checkBox_bear_queue.isChecked():  # 巨熊队列选项
                print_space('点击队列1')
                touch([90, 185])
            print_space('点击出征')
            touch(Template(r"icon/tpl1721784579067.png", record_pos=(0.002, 0.705), resolution=(1080, 1920)))
            print_space('出征成功')
        else:
            print_space('集结中')
    else:
        print_space('未找到活动图标')


# 巨兽等级
def WM_lv():  # 冰原巨兽等级输入
    global settings
    print_space('首次启动或数据有更新，重新输入等级')
    print_space('点击等级输入框')
    touch([900, 1573])
    time.sleep(1)
    print_space('删除原本等级')
    keyevent('KEYCODE_DEL')
    time.sleep(1)  #等待1秒
    print_space('输入新的等级')
    # value = settings.value('冰原巨兽等级设置', type=str)
    # print(value)
    time.sleep(1)
    text(settings.value('冰原巨兽等级设置', 6, type=str))  # print_space('点击确定按钮')  # time.sleep(1)  # touch(Template(r"icon/sure_button.png", record_pos=(0.404, 0.852), resolution=(1080, 1920)))#第三方库自带确定功能，取消点击确定按钮


# 冰原巨兽
def Brush_WM(self):
    search_main()
    swipe([600, 1370], vector=[0.4103, 0.0170])  # 滑动
    time.sleep(1)  # 等待1s
    print_space('点击选择冰原巨兽')
    touch([365, 1373])  # 点击冰原巨兽
    time.sleep(1)  # 等待1s
    '''判断本次是否需要执行选择等级'''
    if settings.value('冰原巨兽等级设置更新'):
        settings.setValue('冰原巨兽等级设置更新', 0)
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
            if self.checkBox_WM_average.isChecked():  # 巨兽队列选项
                print_space('点击队列2')
                touch([210, 185])
            elif self.checkBox_WM_simple.isChecked():  # 单兵集结
                print_space('点击全部撤回')
                touch(Template(r"icon\all_withdraw.png", record_pos=(-0.406, 0.781), resolution=(1080, 1920)))  # 点击全部撤回
                if self.checkBox_pet_Unlock.isChecked():  # 是否增益已解锁，解锁增益功能后会导致Y坐标多100
                    touch([711, 990])  # 点击有增益的出征界面盾兵数量输入框
                else:
                    touch([714, 894])  # 点击无增益的出征界面盾兵数量输入框
                print_space('删除原本数量')
                keyevent('KEYCODE_DEL')
                time.sleep(1)  # 等待1秒
                print_space('输入数量1')
                time.sleep(1)
                text('1')
                # print_space('点击确定按钮')
                time.sleep(1)  # touch(Template(r"icon/sure_button.png", record_pos=(0.404, 0.852), resolution=(1080, 1920)))#第三方库自带确定功能，取消点击确定按钮
            print_space('点击出征按钮')
            energy()
        else:  # 判断是否有多余兵力
            print_space('未找到出征按钮，不满足条件，无兵力出征')
    else:
        print_space('未找到发起集结按钮，队伍数不足，无法出征')


# 采集出兵
def gather(self):
    print_space('点击采集按钮')
    touch(Template(r"icon/tpl1720675061569.png", record_pos=(0.002, -0.015), resolution=(1080, 1920)))
    if exists(Template(r"icon/tpl1721191349776.png", record_pos=(0.26, 0.798), resolution=(1080, 1920))):  # 有兵力可出征
        if self.checkBox_Collection_hero.isChecked():  # 采集英雄选项
            print_space('删除英雄')
            # touch([357, 389])  # 点击删除第一个英雄
            if self.checkBox_pet_Unlock.isChecked():  # 是否增益已解锁，解锁增益功能后会导致Y坐标多100
                touch([640, 480])  # 点击删除第二个英雄
                touch([920, 480])  # 点击删除第三个英雄
            else:
                touch([640, 390])  # 点击删除第二个英雄
                touch([920, 390])  # 点击删除第三个英雄
        print_space('点击出征按钮')
        touch(Template(r"icon/tpl1721191349776.png", rgb=True, record_pos=(0.26, 0.798), resolution=(1080, 1920)))  # 点击出征
        print_space('出征成功')
        time.sleep(1)
        touch([2, 812])
    else:  # 判断是否有多余兵力
        print_space('不满足条件，无兵力出征')


# 打怪出兵
def energy():
    touch(Template(r"icon\tpl1719376787180.png", record_pos=(0.263, 0.773), resolution=(1080, 1920)))  # 点击出征
    time.sleep(1)
    if exists(Template(r"icon\tpl1720264632282.png", record_pos=(0.301, -0.33), resolution=(1080, 1920))):  # 判断是否有体力
        print_space("体力不足，不满足出征条件，开始回到主页")
        print_space('关闭补充体力界面')
        time.sleep(1)
        touch(Template(r"icon\tpl1729734622180.png", record_pos=(0.442, -0.35), resolution=(1080, 1920)))
        print_space('关闭出征界面')
        time.sleep(1)
        touch(Template(r"icon\black_return.png", rgb=True, record_pos=(-0.441, -0.839), resolution=(1080, 1920)))
    elif exists(Template(r"icon\tpl1719376787180.png", record_pos=(0.263, 0.773), resolution=(1080, 1920))):
        touch(Template(r"icon\tpl1719376787180.png", record_pos=(0.263, 0.773), resolution=(1080, 1920)))  # 点击出征
        print_space('出征成功')
    else:
        print_space("出征成功")


# 采集等级设置
def collection_lv():
    print_space('首次启动或数据有更新，重新输入等级')
    print_space('点击等级输入框')
    touch([900, 1573])
    time.sleep(1)
    print_space('删除原本等级')
    keyevent('KEYCODE_DEL')
    time.sleep(1)  #等待1秒
    print_space('输入新的等级')
    time.sleep(1)
    # print(set_collection_lv.get())
    # print(settings.value('采集等级设置', type=str))
    text(settings.value('采集资源等级设置', 7, type=str))
    time.sleep(1)  # print_space('点击确定按钮')  #time.sleep(1)  # touch(Template(r"icon\sure_button.png", record_pos=(0.404, 0.852), resolution=(1080, 1920))) #第三方库自带确定功能，取消点击确定按钮


# 生肉
def Meat(self):
    print_space('准备采集生肉资源')
    print_space('点击搜索图标')
    touch([63, 1320])  # 点击搜索图标
    time.sleep(1)  # 等待1s
    swipe([600, 1370], vector=[-0.4103, 0.0170])  # 滑动
    print_space('点击选择肉')
    touch([240, 1373])  # 点击选择肉
    time.sleep(1)  # 等待1s
    '''判断本次是否需要执行选择等级'''
    if settings.value('肉采集等级设置更新', 1):
        settings.setValue('肉采集等级设置更新', 0)
        collection_lv()
        time.sleep(1)  # 等待1s
    print_space('点击搜索按钮')
    touch([534, 1821])  # 点击搜索
    time.sleep(3)  # 等待1s
    if exists(Template(r"icon\tpl1720675061569.png", rgb=True, record_pos=(0.002, -0.015), resolution=(1080, 1920))):
        gather(self)
    else:
        print_space('未找到采集按钮，未搜索到生肉资源，结束该任务')


# 木材
def Wood(self):
    print_space('准备采集木材资源')
    print_space('点击搜索图标')
    touch([63, 1320])  # 点击搜索图标
    time.sleep(1)  # 等待1s
    swipe([600, 1370], vector=[-0.4103, 0.0170])  # 滑动
    print_space('点击选择木材资源')
    touch([476, 1373])  # 点击选择木材
    time.sleep(1)  # 等待1s
    '''判断本次是否需要执行选择等级'''
    if settings.value('木头采集等级设置更新', 1):
        settings.setValue('木头采集等级设置更新', 0)
        collection_lv()
        time.sleep(1)  # 等待1s
    print_space('点击搜索按钮')
    touch([534, 1821])  # 点击搜索
    time.sleep(1)  # 等待1s
    if exists(Template(r"icon\tpl1720675061569.png", record_pos=(0.002, -0.015), resolution=(1080, 1920))):
        gather(self)
    else:
        print_space('未找到采集按钮，未搜索到生肉资源，结束该任务')


# 煤矿
def Coal(self):
    print_space('准备采集煤矿资源')
    print_space('点击搜索图标')
    touch([63, 1320])  # 点击搜索图标
    time.sleep(1)  # 等待1s
    swipe([600, 1370], vector=[-0.4103, 0.0170])  # 滑动
    print_space('点击选择煤矿资源')
    touch([710, 1373])  # 点击选择煤矿
    time.sleep(1)  # 等待1s
    '''判断本次是否需要执行选择等级'''
    if settings.value('煤矿采集等级设置更新', 1):
        settings.setValue('煤矿采集等级设置更新', 0)
        collection_lv()
        time.sleep(1)  # 等待1s
    print_space('点击搜索按钮')
    touch([534, 1821])  # 点击搜索
    time.sleep(1)  # 等待1s
    if exists(Template(r"icon\tpl1720675061569.png", record_pos=(0.002, -0.015), resolution=(1080, 1920))):
        gather(self)
    else:
        print_space('未找到采集按钮，未搜索到生肉资源，结束该任务')


# 铁矿
def Iron(self):
    print_space('准备采集铁矿资源')
    print_space('点击搜索图标')
    touch([63, 1320])  # 点击搜索图标
    time.sleep(1)  # 等待1s
    swipe([600, 1370], vector=[-0.4103, 0.0170])  # 滑动
    print_space('点击选择铁矿资源')
    touch([950, 1373])  # 点击选择铁矿
    time.sleep(1)  # 等待1s
    '''判断本次是否需要执行选择等级'''
    if settings.value('铁矿采集等级设置更新', 1):
        settings.setValue('铁矿采集等级设置更新', 0)
        collection_lv()
        time.sleep(1)  # 等待1s
    print_space('点击搜索按钮')
    touch([534, 1821])  # 点击搜索
    time.sleep(1)  # 等待1s
    if exists(Template(r"icon\tpl1720675061569.png", record_pos=(0.002, -0.015), resolution=(1080, 1920))):
        gather(self)
    else:
        print_space('未找到采集按钮，未搜索到生肉资源，结束该任务')


# 自动采集
def Collection(self):
    if not exists(Template(r"icon\tpl1720145326019.png", record_pos=(-0.191, -0.169), resolution=(1080, 1920))):
        print_space('不在世界，点击去往世界')
        touch([950, 1850])  # 点击野外
        time.sleep(5)  # 等待5秒
    else:
        print_space('在野外，执行采集任务')
        time.sleep(3)
    touch([2, 812])  # 点击左侧栏
    time.sleep(1)
    touch([500, 400])
    if not exists(Template(r"icon\tpl1720691682616.png", record_pos=(-0.188, -0.127), resolution=(1080, 1920))):
        print_space('无采肉队伍，执行采肉任务')
        time.sleep(1)
        Meat(self)
    else:
        print_space('已有采肉队伍')
    Homepage()
    touch([2, 812])
    if not exists(Template(r"icon\tpl1720766916044.png", threshold=0.7, record_pos=(-0.438, -0.163), resolution=(1080, 1920))):
        print_space('无采集木头队伍，执行采木头任务')
        time.sleep(1)
        Wood(self)
    else:
        print_space('已有采木材队伍')
    Homepage()
    touch([2, 812])
    if not exists(Template(r"icon\tpl1720766916045.png", record_pos=(-0.168, -0.088), resolution=(1080, 1920))):
        print_space('无采煤队伍，执行采煤任务')
        time.sleep(1)
        Coal(self)
    else:
        print_space('已有采煤队伍')
    Homepage()
    touch([2, 812])
    if not exists(Template(r"icon\tpl1720766916046.png", record_pos=(-0.168, -0.088), resolution=(1080, 1920))):
        print_space('无采铁队伍，执行采铁任务')
        time.sleep(1)
        Iron(self)
    else:
        print_space('已有采铁队伍')
        touch(Template(r"icon\tpl1719552273333.png", threshold=0.9, record_pos=(0.142, -0.126), resolution=(1080, 1920)))


# 治疗
def treatment():
    if not exists(Template(r"icon/tpl1720145326019.png", record_pos=(0.404, 0.852), resolution=(1080, 1920))):
        print_space('不在世界，点击去往世界')
        touch([950, 1850])  # 点击野外
        time.sleep(5)
    if exists(Template(r"icon/tpl1738728068288.png", record_pos=(0.273, 0.434), resolution=(1080, 1920))):
        print_space("点击治疗图标")
        touch(Template(r"icon/tpl1738728068288.png", record_pos=(0.273, 0.434), resolution=(1080, 1920)))
        print_space('点击治疗按钮')
        touch(Template(r"icon/tpl1738728101302.png", record_pos=(0.219, 0.382), resolution=(1080, 1920)))
        print_space('点击联盟互助')
        touch(Template(r"icon/tpl1738728129307.png", record_pos=(0.219, 0.412), resolution=(1080, 1920)))
        time.sleep(1)
        print_space('点击返回按钮')
        touch([900, 299])
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
            if exists(Template(r"icon\tpl1721784579073.png", rgb=True, record_pos=(0.208, 0.514), resolution=(1080, 1920))):
                print_space('点击捐献')
                touch(Template(r"icon\tpl1721784579073.png", rgb=True, record_pos=(0.208, 0.514), resolution=(1080, 1920)), duration=2)
            else:
                print_space('无捐献次数，结束任务并返回至主页')
                touch([956, 299])  # 点击关闭按钮x
                touch([60, 60])  # 点击黑色返回按钮
                touch(Template(r"icon\black_return.png", threshold=0.8, record_pos=(-0.44, -0.783), resolution=(1080, 1920)))  # 点击黑色返回按钮
                x = 0
    else:
        print_space('无大拇指指引，返回主页')
        touch([60, 60])  # 点击黑色返回按钮
        touch(Template(r"icon\black_return.png", threshold=0.8, record_pos=(-0.44, -0.783), resolution=(1080, 1920)))  # 点击黑色返回按钮


# 探险
def adventure():
    print_space('点击探险')
    touch(Template(r"icon/tpl1719198809581.png", threshold=0.9, record_pos=(-0.398, 0.819), scale_max=800, resolution=(1080, 1920)))
    time.sleep(1)
    print_space('点击宝箱')
    touch([910, 1250])
    if exists(Template(r'icon/tpl1721784579076.png', threshold=0.8, record_pos=(-0.398, 0.819), resolution=(1080, 1920))):
        print_space('点击领取奖励')
        touch(Template(r'icon/tpl1721784579076.png', threshold=0.8, record_pos=(-0.398, 0.819), resolution=(1080, 1920)))
        time.sleep(1)
        print_space('回到主页')
        touch([500, 500])
        touch(Template(r"icon/tpl1719198082012.png", threshold=0.8, record_pos=(-0.44, -0.783), resolution=(1080, 1920)))
    else:
        print_space('没有可领取奖励')


# 招募英雄
def recruit():
    if exists(Template(r"icon\hero.png", threshold=0.9, record_pos=(-0.398, 0.819), scale_max=800, resolution=(1080, 1920))):
        print_space('点击英雄')
        touch(Template(r"icon\hero.png", threshold=0.9, record_pos=(-0.398, 0.819), scale_max=800, resolution=(1080, 1920)))
        print_space('点击英雄招募')
        touch(Template(r"icon\hero_recruit.png", threshold=0.8, record_pos=(-0.438, 0.258), resolution=(1080, 1920)))
        if check_and_touch(Template(r"icon\free_recruit.png", rgb=True, threshold=0.75, record_pos=(
                -0.234, 0.285), scale_max=800, resolution=(1080, 1920)), '点击免费招募'):
            # print_space('点击免费招募')
            # touch(Template(r"icon\free_recruit.png", threshold=0.8, record_pos=(-0.234, 0.285), scale_max=800, resolution=(1080, 1920)))
            time.sleep(5)
            keyevent('BACK')
            time.sleep(1)
            if not exists(Template(r"icon\tpl1729741197970.png", record_pos=(-0.441, -0.836), resolution=(1080, 1920))):
                # 如果没找到返回按钮，模拟按下手机的返回键（考虑抽到英雄的情况）
                keyevent('BACK')
                check_and_touch(Template(r"icon\tpl1729741197970.png", record_pos=(-0.441, -0.836), resolution=(1080, 1920)))
                print_space('点击返回1按钮')
            time.sleep(1)
        else:
            print_space('无免费招募次数')
        print_space('点击返回2按钮')
        check_and_touch(Template(r"icon\return.png", threshold=0.8, record_pos=(-0.44, -0.783), resolution=(1080, 1920)))
        time.sleep(1)
        check_and_touch(Template(r"icon\black_return.png", threshold=0.8, record_pos=(-0.44, -0.783), resolution=(1080, 1920)))


# 攻击检测
def mining_collision():
    # if exists(Template(r"icon\tpl1729833981926.png", rgb=True, record_pos=(0.42, -0.141), resolution=(1080, 1920))):
    if exists(Template(r"icon\tpl1729833981926.png", rgb=True, record_pos=(0.42, -0.141), resolution=(1080, 1920))):
        print_space('检测到被攻击，点击预警图标')
        touch(Template(r"icon\tpl1729833981926.png", record_pos=(0.42, -0.141), resolution=(1080, 1920)))
        find_result = find_all(Template(r"icon\tpl1729834107464.png", record_pos=(0.207, -0.549), resolution=(1080, 1920)))
        length = len(find_result)
        print('被攻击列表数：%s' % length)
        # for i in range(0, length):
        while length > 0:
            print_space('点击前往目标')
            time.sleep(1)
            # touch(results[1]['result']) # 点击字典内第一个坐标，但第一个坐标不一定是排在第一个的目标，废弃
            # touch(Template(r"icon\tpl1729834107464.png", record_pos=(0.207, -0.549), resolution=(1080, 1920)))
            touch([755, 356])  # 使用绝对坐标，点击列表内第一个目标
            time.sleep(1)
            print_space('点击跳转到的目标')
            touch([540, 890])
            time.sleep(2)
            # if exists(Template(r"icon\tpl1729834163624.png", rgb=True, record_pos=(-0.139, 0.607), resolution=(1080, 1920))):
            if exists(Template(r"icon\tpl1729834163624.png", rgb=True, record_pos=(-0.139, 0.607), resolution=(1080, 1920))):
                print_space('撞矿检测，点击召回采矿')
                touch(Template(r"icon\tpl1729834163624.png", record_pos=(-0.139, 0.607), resolution=(1080, 1920)))
                time.sleep(1)
                print_space('点击确认召回队伍')
                touch(Template(r"icon\tpl1729834190986.png", record_pos=(0.212, 0.203), resolution=(1080, 1920)))
                print_space('撤回队伍成功')
                length -= 1  # 循环次数减1
            elif exists(Template(r"icon\tpl1729834914817.png", record_pos=(-0.139, 0.557), resolution=(1080, 1920))):
                print_space('检测到攻击城堡，点击城堡增益准备开启防护罩')
                touch(Template(r"icon\tpl1729834914817.png", record_pos=(-0.139, 0.557), resolution=(1080, 1920)))
                time.sleep(1)
                print_space('点击战争页签')
                touch([280, 170])
                print_space('点击防护罩')
                touch(Template(r"icon\tpl1729834969758.png", record_pos=(-0.372, -0.544), resolution=(1080, 1920)))
                time.sleep(1)
                print_space('点击使用')
                touch(Template(r"icon\tpl1729834989760.png", record_pos=(0.322, -0.336), resolution=(1080, 1920)))
                print_space('开启防护罩成功')
                length -= 1  # 循环次数减1
                if exists(Template(r"icon\tpl1733823336248.png", record_pos=(-0.335, -0.838), resolution=(1080, 1920))):
                    # 防御罩开启后，检查是否在主页
                    print_space('点击黑色返回按钮')
                    touch(Template(r"icon\tpl1733823336248.png", target_pos=4, record_pos=(-0.335, -0.838), resolution=(1080, 1920)))
            if exists(Template(r"icon\tpl1729833981926.png", record_pos=(0.42, -0.141), resolution=(1080, 1920))):
                print_space('再次回到攻击列表')
                time.sleep(1)
                touch(Template(r"icon\tpl1729833981926.png", record_pos=(0.42, -0.141), resolution=(1080, 1920)))  # 回到攻击列表
            if length <= 0:
                break
    else:
        print_space('未检测到攻击')


# 邮件领取功能逻辑
def mail_function():
    print_space('点击邮件图案')
    touch([993, 1582])  # 邮件图案坐标
    print_space('点击联盟邮件')
    touch([333, 180])  # 联盟图案坐标
    print_space('点击一键领取')
    touch([858, 1865])  # 一键领取坐标
    time.sleep(1)  # 等待1秒
    touch([858, 1865])  # 再次点击以关闭奖励弹窗
    print_space('点击系统邮件')
    touch([540, 180])  # 系统图案坐标
    print_space('点击一键领取')
    touch([858, 1865])  # 一键领取坐标
    time.sleep(1)  # 等待1秒
    touch([858, 1865])  # 再次点击以关闭奖励弹窗
    print_space('点击报告邮件')
    touch([740, 180])  # 系统图案坐标
    print_space('点击一键领取')
    touch([858, 1865])  # 一键领取坐标
    time.sleep(1)  # 等待1秒
    touch([858, 1865])  # 再次点击以关闭奖励弹窗
    touch(Template(r"icon\black_return.png", rgb=True, record_pos=(-0.441, -0.839), resolution=(1080, 1920)))  # 点击返回按钮


# 联盟宝箱领取功能
def union_Treasure_Chest():
    print_space('点击联盟图案')
    touch(Template(r"icon\tpl1721784579070.png", record_pos=(-0.168, -0.088), resolution=(1080, 1920)))
    print_space('点击联盟宝箱')
    if exists(Template(r"icon\tpl1734838173842.png", record_pos=(0.214, 0.036), resolution=(1080, 1920))):
        touch(Template(r"icon\tpl1734838173842.png", record_pos=(0.214, 0.036), resolution=(1080, 1920)))
        print_space('点击战利品宝箱')
        touch([290, 600])  # 点击战利品宝箱区域
        if exists(Template(r"icon\tpl1734838244122.png", threshold=0.8, rgb=True, record_pos=(0.005, 0.789), resolution=(1080, 1920))):
            touch(Template(r"icon\tpl1734838244122.png", record_pos=(0.005, 0.789), resolution=(1080, 1920)))
            print_space('领取成功')
            time.sleep(1)  # 等待1s
            touch([540, 1810])  # 点击关闭奖励界面
        else:
            print_space('未找到一键领取按钮，等待下次检查')
        print_space('点击盟友赠礼')
        touch([790, 600])
        if exists(Template(r"icon\tpl1734838244122.png", record_pos=(0.005, 0.789), resolution=(1080, 1920))):
            touch(Template(r"icon\tpl1734838244122.png", record_pos=(0.005, 0.789), resolution=(1080, 1920)))
            print_space('领取成功')
            touch([540, 1810])  # 点击关闭奖励界面
        else:
            print_space('未找到一键领取按钮，等待下次检查')
        touch(Template(r"icon\black_return.png", rgb=True, record_pos=(-0.441, -0.839), resolution=(1080, 1920)))  # 点击返回按钮
    else:
        print_space('未找到联盟宝箱图案，请检查游戏界面或自主修复')
    touch(Template(r"icon\black_return.png", rgb=True, record_pos=(-0.441, -0.839), resolution=(1080, 1920)))  # 点击返回按钮


# 仓库补给
def warehouse(self):
    global number_physical_strength
    now_time = datetime.now()
    if exists(Template(r"icon/tpl1720145326019.png", record_pos=(0.404, 0.852), resolution=(1080, 1920))):
        print_space('不在城镇，点击去往城镇')
        touch([950, 1850])  # 点击城镇
        time.sleep(5)
    touch([2, 812])  # 点击左侧打开隐藏栏
    time.sleep(1)
    touch([170, 400])  # 点击城镇列表
    time.sleep(1)
    swipe([340, 1280], [330, 450])  # 滑动至底部
    time.sleep(1)
    if exists(Template(r"icon/tpl1737088915389.png", threshold=0.9, record_pos=(-0.436, 0.106), resolution=(1080, 1920))):
        print_space('有可领取补给，点击前往')
        touch(Template(r"icon/tpl1737088915389.png", threshold=0.9, record_pos=(-0.436, 0.106), resolution=(1080, 1920)))
        time.sleep(1)
        print_space('点击领取')
        touch([540, 870])  # 点击领取补给
        time.sleep(1)
        touch([660, 300])  # 关闭奖励弹窗
    else:
        print_space('未找到仓库补给，关闭左侧栏')
        touch(Template(r"icon/tpl1719552273333.png", threshold=0.9, record_pos=(0.142, -0.126), resolution=(1080, 1920)))
    # 体力开关判断检测
    if self.checkBox_warehouse_physical_strength.isChecked():
        # 判定是否是刷新时间或本次启动首次执行
        if now_time.hour == 12 or now_time.hour == 19 or number_physical_strength == 0:
            number_physical_strength = 1
            print_space('首次执行任务或体力刷新时间，检查是否有体力可领取')
            time.sleep(1)
            touch([2, 812])  # 点击左侧打开隐藏栏
            time.sleep(1)
            touch([70, 1230])  # 点击科技研究
            time.sleep(1)
            swipe([500, 1000], vector=[0.2, 0.0017])  # 向左滑动
            time.sleep(1)
            if exists(Template(r"icon/tpl1737094428928.png", threshold=0.8, record_pos=(0.002, -0.094), resolution=(1080, 1920))):
                print_space('点击体力罐头')
                touch(Template(r"icon/tpl1737094428928.png", threshold=0.8, record_pos=(0.002, -0.094), resolution=(1080, 1920)))  # 点击体力罐头
                time.sleep(1)
                print_space('点击领取按钮')
                touch([540, 1430])  # 点击领取按钮
                time.sleep(1)
                touch([150, 1300])  # 关闭奖励弹窗
                print_space('领取成功')
            else:
                print_space('未找到体力罐头')


# 情报功能
def intelligence(self):
    global intelligence_number
    """
    情报功能的主函数。
    检查是否在世界地图中，如果不在则点击前往世界地图。
    点击情报按钮，等待加载完成。
    查找金色爪子、蓝色帐篷和金色对战的图标，并根据查找结果执行相应操作。
    """
    '''if self.checkBox_intelligence_number.isChecked() and settings.value('十次情报状态', 0):  # 判断十次情报是否开启及状态是否为不可执行
        print_space('已完成10次情报任务，停止执行')
        # print('当前情报次数：%s' % intelligence_number)
        intelligence_number = 0
    else:'''
        # 检查是否在世界地图中，如果不在则点击前往世界地图
    if not exists(Template(r"icon/tpl1720145326019.png", record_pos=(0.404, 0.852), resolution=(1080, 1920))):
            print_space('不在世界，点击去往世界')
            touch([950, 1850])  # 点击野外
            time.sleep(5)
    # 点击情报按钮
    print_space('点击情报按钮')
    touch(Template(r"icon/tpl1736493661192.png", record_pos=(0.421, 0.309), resolution=(1080, 1920)))  # 点击情报
    time.sleep(1)  # 等待加载
    '''Template(r"情报/tpl1736410865667.png", record_pos=(0.256, -0.327), resolution=(1080, 1920)) # 金色爪子
        Template(r"情报/tpl1736414583724.png", record_pos=(0.044, 0.28), resolution=(1080, 1920))  # 紫色爪子
        Template(r"tpl1742360757043.png", record_pos=(-0.291, -0.065), resolution=(1080, 1920))   # 金色帐篷
        Template(r"tpl1742361255615.png", record_pos=(-0.284, 0.094), resolution=(1080, 1920))   # 紫色帐篷
        Template(r"情报/tpl1736415568618.png", record_pos=(-0.149, 0.076), resolution=(1080, 1920))   # 蓝色帐篷
        Template(r"情报/tpl1736414991579.png", record_pos=(-0.216, -0.009), resolution=(1080, 1920))  # 金色对战
        Template(r"情报/tpl1736414443397.png", record_pos=(-0.035, -0.505), resolution=(1080, 1920))  # 紫色对战'''
    # 检查是否有已完成的情报
    if check_and_touch(Template(r"icon/tpl1742811376103.png", record_pos=(0.264, -0.065), resolution=(
            1080, 1920)), '有已完成的情报，点击领取奖励', '没有已完成的情报'):
        print_space('领取奖励成功')
        intelligence_number += 1
        if intelligence_number >= 10 and self.checkBox_intelligence_number.isChecked():  # 当情报达到一定次数时，十次情报状态变化为不执行
            print_space('情报执行达到10次，十次情报执行状态发生变化')
            settings.setValue('十次情报状态', 1)  # intelligence_number_state = settings.value('十次情报状态', 0)  # print('当前情报状态：%s' % intelligence_number_state)
        time.sleep(1)
        # 模拟按下手机的返回键
        keyevent('BACK')
    # if self.checkBox_intelligence_offer_a_reward.isChecked():  # 判断是否开启悬赏情报
    # 取消悬赏功能
    '''if self.checkBox_intelligence_offer_a_reward.isChecked() and check_and_touch(Template(r"icon/tpl1745923009141.png", rgb=True, record_pos=(
            0.117, -0.329), resolution=(1080, 1920)), "找到悬赏图案，点击图案", "未找到悬赏图案"):  # 判断是否开启悬赏情报:  # 金色爪子及紫色爪子
        time.sleep(1)
        # print_space("找到悬赏图案，点击图案")
        # 判定是否有前往查看按钮
        if exists(Template(r"icon/tpl1745923856051.png", record_pos=(-0.002, 0.324), resolution=(1080, 1920))):
            print_space('正在执行悬赏情报任务，退出情报')
            keyevent('BACK')  # 模拟按下手机的返回键
            time.sleep(1)
            keyevent('BACK')  # 模拟按下手机的返回键
        elif check_and_touch(Template(r"icon/tpl1736414104111.png", record_pos=(-0.003, 0.406), resolution=(
                1080, 1920)), '点击前往查看按钮'):
            # print_space('点击前往查看按钮')
            # touch(Template(r"icon/tpl1736414104111.png", record_pos=(-0.003, 0.406), resolution=(1080, 1920)))  # 前往查看按钮
            time.sleep(1)
            # 点击出征按钮
            touch(Template(r"icon/tpl1736414133437.png", record_pos=(-0.003, -0.039), resolution=(1080, 1920)))  # 大世界出征
            touch(Template(r"icon\tpl1719376787180.png", record_pos=(0.263, 0.773), resolution=(1080, 1920)))  # 点击出征
            time.sleep(1)
            if exists(Template(r"icon\tpl1720264632282.png", record_pos=(0.301, -0.33), resolution=(1080, 1920))):  # 判断是否有体力
                print_space("体力不足，不满足出征条件，开始回到主页")
                print_space('关闭补充体力界面')
                time.sleep(1)
                touch(Template(r"icon\tpl1729734622180.png", record_pos=(0.442, -0.35), resolution=(1080, 1920)))
                print_space('关闭出征界面')
                time.sleep(1)
                touch(Template(r"icon\black_return.png", rgb=True, record_pos=(-0.441, -0.839), resolution=(1080, 1920)))
            else:
                print_space("出征成功")
        else:
            print_space('领取奖励成功')
            intelligence_number += 1'''
    # print_space('未开启/找到悬赏，进入普通情报')
    if self.checkBox_intelligence_version.isChecked():  # 判断是否勾选了火晶版本
        if check_and_touch(Template(r"icon/tpl1736410865667.png", record_pos=(0.115, -0.139), resolution=(1080, 1920)), "找到火晶爪子图案，点击图案", "未找到火晶爪子图案"):  # 金色爪子及紫色爪子
            time.sleep(1)
            # 点击前往查看按钮
            print_space('点击前往查看按钮')
            touch(Template(r"icon/tpl1736414104111.png", record_pos=(-0.003, 0.406), resolution=(1080, 1920)))  # 前往查看按钮
            time.sleep(1)
            # 点击出征按钮
            touch(Template(r"icon/tpl1736414133437.png", record_pos=(-0.003, -0.039), resolution=(1080, 1920)))  # 大世界出征
            touch(Template(r"icon\tpl1719376787180.png", record_pos=(0.263, 0.773), resolution=(1080, 1920)))  # 点击出征
            time.sleep(1)
            if exists(Template(r"icon\tpl1720264632282.png", record_pos=(0.301, -0.33), resolution=(1080, 1920))):  # 判断是否有体力
                print_space("体力不足，不满足出征条件，开始回到主页")
                print_space('关闭补充体力界面')
                time.sleep(1)
                touch(Template(r"icon\tpl1729734622180.png", record_pos=(0.442, -0.35), resolution=(1080, 1920)))
                print_space('关闭出征界面')
                time.sleep(1)
                touch(Template(r"icon\black_return.png", rgb=True, record_pos=(-0.441, -0.839), resolution=(1080, 1920)))
            else:
                print_space("出征成功")
        elif check_and_touch(Template(r"icon/tpl1742360757043.png", record_pos=(-0.291, -0.065), resolution=(1080, 1920)), '找到火晶帐篷图案，点击图案', '未找到火晶帐篷图案'):  # 金色帐篷及紫色帐篷:
            # 点击前往查看按钮
            time.sleep(1)
            touch(Template(r"icon/tpl1736414104111.png", record_pos=(-0.003, 0.406), resolution=(1080, 1920)))  # 前往查看按钮
            time.sleep(1)
            # 点击营救按钮
            touch(Template(r"icon/tpl1736414182861.png", record_pos=(-0.004, -0.039), resolution=(1080, 1920)))  # 营救
            if exists(Template(r"icon\tpl1720264632282.png", record_pos=(0.301, -0.33), resolution=(1080, 1920))):  # 判断是否有体力
                print_space("体力不足，不满足营救条件，开始回到主页")
                print_space('关闭补充体力界面')
            else:
                print_space("营救成功")

        elif check_and_touch(Template(r"icon/tpl1736414991579.png", record_pos=(-0.118, -0.483), resolution=(
                1080, 1920)), '找到火晶对战图案，点击图案', '未找到火晶对战图案'):
            # 点击前往查看按钮
            touch(Template(r"icon/tpl1736414104111.png", record_pos=(-0.003, 0.406), resolution=(1080, 1920)))
            time.sleep(1)
            # 点击探险按钮
            touch(Template(r"icon/tpl1736414216951.png", record_pos=(-0.001, -0.04), resolution=(1080, 1920)))
            # 该处预留体力判断
            if exists(Template(r"icon/tpl1736416044350.png", record_pos=(0.235, 0.779), resolution=(1080, 1920))):
                touch(Template(r"icon/tpl1736416044350.png", record_pos=(0.235, 0.779), resolution=(1080, 1920)))  # 点击战斗
                time.sleep(10)  # 等待战斗结束
                touch([155, 155])  # 点击任意位置

            else:
                print_space('体力不足，无法探险')
                # 模拟按下手机的返回键
                keyevent('BACK')
    else:
        if check_and_touch(Template(r"icon/tpl1736410865667-无火晶版.png", record_pos=(0.115, -0.139), resolution=(1080, 1920)), "找到非火晶狼头图案，点击图案", "未找到非火晶狼头图案"):  # 金色爪子及紫色爪子
            time.sleep(1)
            # 点击前往查看按钮
            print_space('点击前往查看按钮')
            touch(Template(r"icon/tpl1736414104111.png", record_pos=(-0.003, 0.406), resolution=(1080, 1920)))  # 前往查看按钮
            time.sleep(1)
            # 点击出征按钮
            touch(Template(r"icon/tpl1736414133437.png", record_pos=(-0.003, -0.039), resolution=(1080, 1920)))  # 大世界出征
            touch(Template(r"icon\tpl1719376787180.png", record_pos=(0.263, 0.773), resolution=(1080, 1920)))  # 点击出征
            time.sleep(1)
            if exists(Template(r"icon\tpl1720264632282.png", record_pos=(0.301, -0.33), resolution=(1080, 1920))):  # 判断是否有体力
                print_space("体力不足，不满足出征条件，开始回到主页")
                print_space('关闭补充体力界面')
                time.sleep(1)
                touch(Template(r"icon\tpl1729734622180.png", record_pos=(0.442, -0.35), resolution=(1080, 1920)))
                print_space('关闭出征界面')
                time.sleep(1)
                touch(Template(r"icon\black_return.png", rgb=True, record_pos=(-0.441, -0.839), resolution=(1080, 1920)))
            else:
                print_space("出征成功")
        elif check_and_touch(Template(r"icon/tpl1742360757043-旧版.png", record_pos=(-0.284, 0.094), resolution=(1080, 1920)), '找到非火晶帐篷图案，点击图案', '未找到非火晶帐篷图案'):  # 金色帐篷及紫色帐篷:
            # 点击前往查看按钮
            time.sleep(1)
            touch(Template(r"icon/tpl1736414104111.png", record_pos=(-0.003, 0.406), resolution=(1080, 1920)))  # 前往查看按钮
            time.sleep(1)
            # 点击营救按钮
            touch(Template(r"icon/tpl1736414182861.png", record_pos=(-0.004, -0.039), resolution=(1080, 1920)))  # 营救
            if exists(Template(r"icon\tpl1720264632282.png", record_pos=(0.301, -0.33), resolution=(1080, 1920))):  # 判断是否有体力
                print_space("体力不足，不满足营救条件，开始回到主页")
                print_space('关闭补充体力界面')
            else:
                print_space("营救成功")

        elif check_and_touch(Template(r"icon/tpl1736414991579-旧版.png", record_pos=(-0.118, -0.483), resolution=(1080, 1920)), '找到非火晶对战图案，点击图案', '未找到非火晶对战图案'):
            # 点击前往查看按钮
            touch(Template(r"icon/tpl1736414104111.png", record_pos=(-0.003, 0.406), resolution=(1080, 1920)))
            time.sleep(1)
            # 点击探险按钮
            touch(Template(r"icon/tpl1736414216951.png", record_pos=(-0.001, -0.04), resolution=(1080, 1920)))
            # 该处预留体力判断
            if exists(Template(r"icon/tpl1736416044350.png", record_pos=(0.235, 0.779), resolution=(1080, 1920))):
                touch(Template(r"icon/tpl1736416044350.png", record_pos=(0.235, 0.779), resolution=(1080, 1920)))  # 点击战斗
                time.sleep(10)  # 等待战斗结束
                touch([155, 155])  # 点击任意位置

            else:
                print_space('体力不足，无法探险')
                # 模拟按下手机的返回键
                keyevent('BACK')
        # 取消金紫品质功能
        '''elif check_and_touch(Template(r"icon/tpl1736414583724.png", threshold=0.89, rgb=True, record_pos=(0.044, 0.28), resolution=(
                1080, 1920)), "找到紫色爪子图案，点击图案", "未找到紫色爪子图案"):
            time.sleep(1)
            # 点击前往查看按钮
            print_space('点击前往查看按钮')
            touch(Template(r"icon/tpl1736414104111.png", record_pos=(-0.003, 0.406), resolution=(1080, 1920)))  # 前往查看按钮
            time.sleep(1)
            # 点击出征按钮
            touch(Template(r"icon/tpl1736414133437.png", record_pos=(-0.003, -0.039), resolution=(1080, 1920)))  # 大世界出征
            #energy()
            touch(Template(r"icon/tpl1719376787180.png", record_pos=(0.263, 0.773), resolution=(1080, 1920)))  # 点击出征
            time.sleep(1)
            if exists(Template(r"icon\tpl1720264632282.png", record_pos=(0.301, -0.33), resolution=(1080, 1920))):  # 判断是否有体力
                print_space("体力不足，不满足出征条件，开始回到主页")
                print_space('关闭补充体力界面')
                time.sleep(1)
                touch(Template(r"icon\tpl1729734622180.png", record_pos=(0.442, -0.35), resolution=(1080, 1920)))
                print_space('关闭出征界面')
                time.sleep(1)
                touch(Template(r"icon\black_return.png", rgb=True, record_pos=(-0.441, -0.839), resolution=(1080, 1920)))
            else:
                print_space("出征成功")

        elif check_and_touch(Template(r"icon/tpl1742361255615.png", rgb=True, record_pos=(0.011, 0.192), resolution=(
                1080, 1920)), '找到紫色帐篷图案，点击图案', '未找到紫色帐篷图案'):
            # 点击前往查看按钮
            time.sleep(1)
            touch(Template(r"icon/tpl1736414104111.png", record_pos=(-0.003, 0.406), resolution=(1080, 1920)))  # 前往查看按钮
            time.sleep(1)
            # 点击营救按钮
            touch(Template(r"icon/tpl1736414182861.png", record_pos=(-0.004, -0.039), resolution=(1080, 1920)))  # 营救
            if exists(Template(r"icon\tpl1719376787180.png", record_pos=(0.263, 0.773), resolution=(1080, 1920))):  # 判断是否有体力
                print_space("体力不足，不满足营救条件，开始回到主页")
                print_space('关闭补充体力界面')
                # 模拟按下手机的返回键
                keyevent('BACK')
            else:
                print_space("营救成功")

        elif check_and_touch(Template(r"icon/tpl1736414443397.png", threshold=0.8, rgb=True, record_pos=(0.219, -0.337), resolution=(
                1080, 1920)), '找到紫色对战图案，点击图案', '未找到紫色对战图案'):
            # 点击前往查看按钮
            touch(Template(r"icon/tpl1736414104111.png", record_pos=(-0.003, 0.406), resolution=(1080, 1920)))
            time.sleep(1)
            # 点击探险按钮
            touch(Template(r"icon/tpl1736414216951.png", record_pos=(-0.001, -0.04), resolution=(1080, 1920)))
            # 该处预留体力判断
            if exists(Template(r"icon/tpl1736416044350.png", record_pos=(0.235, 0.779), resolution=(1080, 1920))):
                touch(Template(r"icon/tpl1736416044350.png", record_pos=(0.235, 0.779), resolution=(1080, 1920)))  # 点击战斗
                time.sleep(5)  # 等待战斗结束
                touch([155, 155])  # 点击任意位置

            else:
                print_space('体力不足，无法探险')
                # 模拟按下手机的返回键
                keyevent('BACK')
        else:
            if not self.checkBox_intelligence_high_quality.isChecked():  # 如果没勾选
                print_space('未勾选高品质，检查低品质情报')
                # 如果找到金色爪子图标
                if check_and_touch(Template(r"icon/tpl1736410865667.png", record_pos=(0.256, -0.327), resolution=(
                        1080, 1920)), '找到爪子图案，点击图案', '未找到爪子图案'):
                    # 点击前往查看按钮
                    touch(Template(r"icon/tpl1736414104111.png", record_pos=(-0.003, 0.406), resolution=(1080, 1920)))  # 前往查看按钮
                    time.sleep(1)
                    # 点击出征按钮
                    touch(Template(r"icon/tpl1736414133437.png", record_pos=(-0.003, -0.039), resolution=(1080, 1920)))  # 大世界出征
                    #energy()
                    touch(Template(r"icon\tpl1719376787180.png", record_pos=(0.263, 0.773), resolution=(1080, 1920)))  # 点击出征
                    time.sleep(1)
                    if exists(Template(r"icon\tpl1720264632282.png", record_pos=(0.301, -0.33), resolution=(1080, 1920))):  # 判断是否有体力
                        print_space("体力不足，不满足出征条件，开始回到主页")
                        print_space('关闭补充体力界面')
                        time.sleep(1)
                        touch(Template(r"icon\tpl1729734622180.png", record_pos=(0.442, -0.35), resolution=(1080, 1920)))
                        print_space('关闭出征界面')
                        time.sleep(1)
                        touch(Template(r"icon\black_return.png", rgb=True, record_pos=(-0.441, -0.839), resolution=(1080, 1920)))
                    elif exists(Template(r"icon\tpl1719376787180.png", record_pos=(0.263, 0.773), resolution=(1080, 1920))):
                        touch(Template(r"icon\tpl1719376787180.png", record_pos=(0.263, 0.773), resolution=(1080, 1920)))  # 点击出征
                        print_space('出征成功')

                    else:
                        print_space("出征成功")

                # 如果找到金色帐篷图标
                elif check_and_touch(Template(r"icon/tpl1742360757043.png", record_pos=(-0.291, -0.065), resolution=(
                        1080, 1920)), '找到帐篷图案，点击图案', '未找到帐篷图案'):
                    # 点击前往查看按钮
                    touch(Template(r"icon/tpl1736414104111.png", record_pos=(-0.003, 0.406), resolution=(1080, 1920)))  # 前往查看按钮
                    time.sleep(1)
                    # 点击营救按钮
                    touch(Template(r"icon/tpl1736414182861.png", record_pos=(-0.004, -0.039), resolution=(1080, 1920)))  # 营救
                    if exists(Template(r"icon\tpl1719376787180.png", record_pos=(0.263, 0.773), resolution=(1080, 1920))):  # 判断是否有体力
                        print_space("体力不足，不满足营救条件，开始回到主页")
                        print_space('关闭补充体力界面')
                        # 模拟按下手机的返回键
                        keyevent('BACK')
                    else:
                        print_space("营救成功")

                # 如果找到金色对战图标
                elif check_and_touch(Template(r"icon/tpl1736414991579.png", record_pos=(-0.216, -0.009), resolution=(
                        1080, 1920)), '找到对战图案，点击图案', '未找到对战图案'):
                    # 点击前往查看按钮
                    touch(Template(r"icon/tpl1736414104111.png", record_pos=(-0.003, 0.406), resolution=(1080, 1920)))
                    time.sleep(1)
                    # 点击探险按钮
                    touch(Template(r"icon/tpl1736414216951.png", record_pos=(-0.001, -0.04), resolution=(1080, 1920)))
                    # 该处预留体力判断
                    if exists(Template(r"icon/tpl1736416044350.png", record_pos=(0.235, 0.779), resolution=(1080, 1920))):
                        touch(Template(r"icon/tpl1736416044350.png", record_pos=(0.235, 0.779), resolution=(1080, 1920)))  # 点击战斗
                        time.sleep(5)  # 等待战斗结束
                        touch([155, 155])  # 点击任意位置

                    else:
                        print_space('体力不足，无法探险')
                        # 模拟按下手机的返回键
                        keyevent('BACK')
                else:
                    print_space('未找到可执行的高情报任务')
            else:  # 如果勾选了高品质
                print_space('勾选了高品质，不检查低品质情报')
                print_space('未找到可执行的高情报任务')'''


# 炼金实验室
def alchemical_Laboratory():
    print_space('点击打开左侧栏')
    touch([2, 812])
    time.sleep(1)
    print_space('点击矛兵栏')
    touch([350, 950])
    time.sleep(3)
    print_space('滑动屏幕至炼金实验室处于正中')
    swipe([330, 800], vector=[-0.1086, -0.0557])
    time.sleep(1)
    if check_and_touch(Template(r"icon/tpl1747972304994.png", record_pos=(0.117, 0.028), resolution=(
    1080, 1920)), '点击炼金实验室', '未找到可领取火晶图案'):
        print_space('点击炼金按钮')
        x_alchemical = 7
        while x_alchemical > 0:
            check_and_touch(Template(r"icon/tpl1747972327837.png", rgb=True, record_pos=(-0.002, 0.731), resolution=(
            1080, 1920)), '点击炼金按钮', '无提炼次数，结束任务并返回至主页')
            x_alchemical -= 1  # print_space('点击炼金按钮')  # touch(Template(r"icon/tpl1747972327837.png", record_pos=(-0.002, 0.731), resolution=(1080, 1920)))  # print_space('无提炼次数，结束任务并返回至主页')
        keyevent('BACK')


# 每日任务领取
def daily_task_collection():
    if check_and_touch(Template(r"icon/tpl1748339736244.png", record_pos=(-0.442, 0.572), resolution=(1080, 1920)),'点击每日任务图标','未找到每日任务图标'):
        # print_space('点击任务图标')
        # touch([63, 1580])
        print_space('点击每日任务页签')
        touch([700, 1700])
        time.sleep(1)
        if check_and_touch(Template(r"icon/tpl1749013490103.png", record_pos=(-0.442, 0.572), resolution=(1080, 1920)), '点击一键领取', '未找到一键领取'):
            print_space('点击系统返回关闭奖励页')
            time.sleep(2)
            keyevent('BACK')
        print_space('点击系统返回关闭每日任务页')
        keyevent('BACK')


# 生命之树
def tree_of_life():
    print_space('点击左侧收缩按钮')
    touch([2, 812])
    time.sleep(1)
    print_space('点击城镇页签')
    touch([170, 400])
    time.sleep(1)
    print_space('滑动页签至底部')
    swipe([345, 1150], vector=[0, -0.5])
    time.sleep(2)
    if check_and_touch(Template(r"icon/tpl1748341573035.png", threshold=0.9, record_pos=(-0.437, 0.106), resolution=(1080, 1920)), '点击生命之树栏', '未找到生命之树'):
        time.sleep(3)
        touch([530, 1450])
        x = 1
        while x == 1:
            if check_and_touch(Template(r"icon/tpl1749101071430.png", rgb=True, record_pos=(-0.437, 0.106), resolution=(1080, 1920)), '点击收取水晶', '未找到水晶'):
                time.sleep(1)
                x = 1
            else:
                x = 0
        touch([70, 45])


# 晨曦回礼
def morning_light_returns_gift():
    print_space('点击左侧收缩按钮')
    touch([2, 812])
    time.sleep(1)
    print_space('点击城镇页签')
    touch([170, 400])
    time.sleep(1)
    print_space('滑动页签至底部')
    swipe([345, 1150], vector=[0, -0.5])
    time.sleep(2)
    if check_and_touch(Template(r"icon/tpl1749808771192.png", record_pos=(-0.437, 0.108), resolution=(1080, 1920)), '点击晨曦回礼', '未找到晨曦回礼'):
    # print_space('点击晨曦回礼栏')
    # touch([340, 1240])
        if check_and_touch(Template(r"icon/tpl1749013597740.png", record_pos=(-0.437, 0.106), resolution=(1080, 1920)), '点击领取回礼', '未找到领取按钮'):
            keyevent('BACK')