# 功能逻辑
import time
from airtest.core.api import exists, touch, swipe, text, keyevent, find_all, sleep
from airtest.core.cv import Template
from airtest.core.android.android import *
from numpy import random
from Window_UI import settings
from datetime import datetime
import sys
import importlib
from global_vars import stop_event


# 设置默认编码为 utf-8
importlib.reload(sys)
sys.setdefaultencoding = "utf-8"
# 确保输出编码为 UTF-8
sys.stdout = open(sys.stdout.fileno(), mode="w", encoding="utf-8", buffering=1)
sys.stderr = open(sys.stderr.fileno(), mode="w", encoding="utf-8", buffering=1)


def check_stop_event(func):
    if stop_event.is_set():
        return

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"执行错误: {e}")

    return wrapper


@check_stop_event
def catch_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"执行错误: {e}")

    return wrapper


@check_stop_event
def goHomepage(func):
    def wrapper(*args, **kwargs):
        Homepage()
        return func(*args, **kwargs)

    return wrapper


@catch_exceptions
def check_and_touch(templateObj, message="", target_pos=None):
    if exists(templateObj):
        if message:
            print_space(message)
        if target_pos:
            touch(target_pos)
        else:
            touch(templateObj)
        sleep(0.5)
        return True
    return False


@check_stop_event
def check_and_go_outside(func):
    def wrapper(*args, **kwargs):
        print_space("检查是否在城镇,去野外")
        check_and_touch(
            Template(
                os.path.join("icon", r"tpl1739024627263.png"),
                record_pos=(0.396, 0.788),
                resolution=(1080, 1920),
                threshold=0.9,
            ),
            "检查到在城镇,去野外",
        )
        sleep(3)
        return func(*args, **kwargs)

    return wrapper


number_physical_strength = 0


# 重写打印
def print_space(variable, spaces=4):
    """
    打印带有指定空格缩进的字符串。

    :param variable: 要打印的变量或字符串。
    :param spaces: 缩进的空格数，默认为4。
    """
    # 使用指定数量的空格进行缩进，并将变量转换为字符串后打印
    print(" " * spaces + str(variable))


# 主页判断
@catch_exceptions
def Homepage():
    for i in range(10):
        if stop_event.is_set():
            return
        print_space(f"第{i+1}次判断是否在主页")
        # 判断是否在城镇,面板是否回收,
        if exists(
            Template(
                os.path.join("icon", r"tpl1739024627263.png"),
                record_pos=(0.396, 0.788),
                resolution=(1080, 1920),
                threshold=0.9,
            )
        ) and exists(
            Template(
                os.path.join("icon", r"tpl1739008819108.png"),
                record_pos=(-0.483, -0.11),
                resolution=(1080, 1920),
                threshold=0.9,
            )
        ):
            print_space("在城镇，面板已回收")
            return
        else:
            if check_and_touch(
                Template(
                    os.path.join("icon", r"tpl1739008721692.png"),
                    record_pos=(0.403, 0.815),
                    resolution=(1080, 1920),
                    threshold=0.9,
                ),
                "检查到在野外并点击去往城镇",
            ):
                continue
            if check_and_touch(
                Template(
                    os.path.join("icon", r"tpl1739012192856.png"),
                    record_pos=(-0.444, -0.844),
                    resolution=(1080, 1920),
                    threshold=0.9,
                ),
                "检查到返回按钮并点击",
                [50, 50],
            ):
                continue
            if check_and_touch(
                Template(
                    os.path.join("icon", r"tpl1739010465874.png"),
                    record_pos=(0.151, -0.125),
                    resolution=(1080, 1920),
                    threshold=0.9,
                ),
                "检查到面板未回收并点击",
            ):
                continue
            if check_and_touch(
                Template(
                    os.path.join("icon", r"tpl1739011457290.png"),
                    record_pos=(-0.328, -0.71),
                    resolution=(1080, 1920),
                    threshold=0.9,
                ),
                "检查到弹窗并点击",
                [50, 50],
            ):
                continue

            print_space("未知情况，固定点击返回")
            touch([50, 50])
            sleep(0.5)
            touch([50, 50])
            sleep(0.5)
    re_connet()


# 设备顶号重连
@catch_exceptions
def re_connet():
    if exists(
        Template(
            os.path.join("icon", r"tpl1720766916047.png"),
            rgb=False,
            record_pos=(-0.168, -0.088),
            resolution=(1080, 1920),
        )
    ):
        print("在其他设备登录，等待5分钟后重新连接")
        time.sleep(300)
        try:
            print_space("点击重新连接")
            re = 1
            while re > 0:
                touch(
                    Template(
                        os.path.join("icon", r"tpl1720766916047.png"),
                        rgb=False,
                        record_pos=(-0.168, -0.088),
                        resolution=(1080, 1920),
                    )
                )
                time.sleep(10)
                if exists(
                    Template(
                        os.path.join("icon", r"tpl1720766916047.png"),
                        rgb=False,
                        record_pos=(-0.168, -0.088),
                        resolution=(1080, 1920),
                    )
                ):
                    print("重新连接失败，等待1分钟继续尝试")
                    time.sleep(60)
                else:
                    print_space("重新连接成功")
                    re = 0
        except:
            print("重新连接失败，稍后尝试")
    else:
        print_space("连接正常")


# 互助功能
@catch_exceptions
@goHomepage
def Help(self):
    if exists(
        Template(
            os.path.join("icon", r"tpl1718936896202.png"),
            record_pos=(0.248, 0.735),
            resolution=(1080, 1920),
        )
    ):  # 判断是否有盟员求助
        print_space("有盟员求助，需点击援助按钮")
        if self.checkBox_Random_time.isChecked():
            random_number = random.randint(0, 5)  # 随机数
            print_space("随机等待时间：%s秒" % random_number)
            time.sleep(random_number)  # 等待随机时间后
        record = random.randint(1, 9)
        print_space("随机点击位置：%s" % record)
        touch(
            Template(
                os.path.join("icon", r"tpl1718936896202.png"),
                target_pos=record,
                record_pos=(0.248, 0.735),
                resolution=(1080, 1920),
            )
        )
    else:
        print_space("未找到求助按钮，进行下一个任务")


# 生产士兵
@catch_exceptions
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
    touch([786, 1221])  # 点击训练按钮
    time.sleep(1)  # 等待1秒
    if self.checkBox_jinshen.isChecked():  # 判定是否勾选可优先晋升
        print_space("检查是否有可晋升士兵")
        if exists(
            Template(
                os.path.join("icon", r"tpl1721784527077.png"),
                record_pos=(-0.439, 0.078),
                resolution=(1080, 1920),
            )
        ):
            print_space("点击前往可晋升士兵")
            touch(
                Template(
                    os.path.join("icon", r"tpl1721784527077.png"),
                    record_pos=(-0.439, 0.078),
                    resolution=(1080, 1920),
                )
            )
            print_space("点击晋升图标")
            touch(
                Template(
                    os.path.join("icon", r"tpl1721784547262.png"),
                    record_pos=(0.399, 0.019),
                    resolution=(1080, 1920),
                )
            )
            print_space("点击开始晋升士兵")
            touch(
                Template(
                    os.path.join("icon", r"tpl1727422988298.png"),
                    record_pos=(0.216, 0.339),
                    resolution=(1080, 1920),
                )
            )
            lv_y = 1  # 更新初始循环次数,不会进入可训练士兵检查
        elif exists(
            Template(
                os.path.join("icon", r"tpl1721784547262.png"),
                rgb=True,
                record_pos=(0.399, 0.019),
                resolution=(1080, 1920),
            )
        ):
            print_space("点击晋升图标")
            touch(
                Template(
                    os.path.join("icon", r"tpl1721784547262.png"),
                    record_pos=(0.399, 0.019),
                    resolution=(1080, 1920),
                )
            )
            print_space("点击开始晋升士兵")
            touch(
                Template(
                    os.path.join("icon", r"tpl1727422988298.png"),
                    record_pos=(0.216, 0.339),
                    resolution=(1080, 1920),
                )
            )
            lv_y = 1  # 更新初始循环次数,不会进入可训练士兵检查
        else:
            print_space("上一页没有可晋升低级士兵，检查本页是否有可晋升士兵")
            # swipe([950, 1225], vector=[-0.8, 0.0170])  # 滑动训练兵种（不滑动，预防当前页面不在最高级页面
            time.sleep(1)
            touch([910, 1225])  # 点击最右边兵
            lv_x = 910  # 设置初始x坐标
            lv_y = 5  # 设置初始循环次数
            while lv_y > 0:
                if exists(
                    Template(
                        os.path.join("icon", r"tpl1721784547262.png"),
                        rgb=True,
                        record_pos=(0.399, 0.019),
                        resolution=(1080, 1920),
                    )
                ):  # 找到晋升图案
                    print_space("点击晋升图标")
                    touch(
                        Template(
                            os.path.join("icon", r"tpl1721784547262.png"),
                            record_pos=(0.399, 0.019),
                            resolution=(1080, 1920),
                        )
                    )
                    print_space("点击开始晋升士兵")
                    touch(
                        Template(
                            os.path.join("icon", r"tpl1727422988298.png"),
                            record_pos=(0.216, 0.339),
                            resolution=(1080, 1920),
                        )
                    )
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
            if exists(
                Template(
                    os.path.join("icon", r"tpl17217845790633.png"),
                    rgb=True,
                    threshold=0.8,
                    record_pos=(0.22, 0.338),
                    resolution=(1080, 1920),
                )
            ):  # 判断到训练按钮
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
                elif (
                    lv_y_1 <= 0
                ):  # 当循环次数小于0时，跳出该循环，避免卡在该循环内（修复卡在循环内的问题）
                    print_space("没有可训练士兵，结束该任务")
                    break  # 退出该循环
    time.sleep(2)  # 等待2秒
    print_space("返回上一级")
    touch([66, 66])  # 使用坐标点击，防止识别错误
    """if exists(Template(os.path.join("icon", r"tpl1719198082013.png"), threshold=0.8, record_pos=(-0.439, -0.835), resolution=(1080, 1920))):
        touch(Template(os.path.join("icon", r"tpl1719198082013.png"), threshold=0.8, record_pos=(-0.439, -0.835), resolution=(1080, 1920)))
    elif exists(Template(os.path.join("icon", r"tpl1719198103804.png"), record_pos=(0.442, -0.35), resolution=(1080, 1920))):
        touch(Template(os.path.join("icon", r"tpl1719198103804.png"), record_pos=(0.442, -0.35), resolution=(1080, 1920)))  # 关闭当前界面
        if exists(Template(os.path.join("icon", r"tpl1719198082013.png"), threshold=0.8, record_pos=(-0.439, -0.835), resolution=(1080, 1920))):
            touch(Template(os.path.join("icon", r"tpl1719198082013.png"), threshold=0.8, record_pos=(-0.439, -0.835), resolution=(1080, 1920)))
    else:
        print_space('未找到对应图案')"""
    print_space("训练完成")


# 训练检查
@goHomepage
@catch_exceptions
def Production_soldiers(self):
    if exists(
        Template(
            os.path.join("icon", r"tpl1720145326019.png"),
            record_pos=(0.404, 0.852),
            resolution=(1080, 1920),
        )
    ):  # 判断是否在城镇，防止队列影响按钮
        print_space("不在城镇，点击去往城镇")
        touch([950, 1850])  # 点击野外
        time.sleep(5)
    touch([14, 823])
    time.sleep(1)
    touch([170, 400])
    print_space("检查盾兵训练是否完成")
    if exists(
        Template(
            os.path.join("icon", r"tpl1719478488282.png"),
            threshold=0.8,
            rgb=True,
            record_pos=(-0.189, -0.009),
            resolution=(1080, 1920),
        )
    ):
        print_space("1跳转到盾兵兵营...")
        touch([600, 840])  # 点击索引到对应兵营
        train(self)
        Homepage()  # 返回主页
        time.sleep(1)  # 等待1秒
        touch([14, 823])
    elif exists(
        Template(
            os.path.join("icon", r"tpl1719478488283.png"),
            threshold=0.9,
            rgb=True,
            record_pos=(-0.066, -0.111),
            resolution=(1080, 1920),
        )
    ):
        print_space("跳转到盾兵兵营...")
        touch([600, 840])  # 点击索引到对应兵营
        train(self)
        Homepage()  # 返回主页
        time.sleep(1)  # 等待1秒
        touch([14, 823])
    print_space("检查矛兵训练是否完成")
    if exists(
        Template(
            os.path.join("icon", r"tpl1719480722195.png"),
            threshold=0.8,
            rgb=True,
            record_pos=(-0.189, -0.009),
            resolution=(1080, 1920),
        )
    ):
        print_space("1跳转到矛兵兵营...")
        touch([600, 942])  # 点击索引到对应兵营
        train(self)
        Homepage()  # 返回主页
        time.sleep(1)  # 等待1秒
        touch([14, 823])
    elif exists(
        Template(
            os.path.join("icon", r"tpl1719480722196.png"),
            threshold=0.8,
            rgb=True,
            record_pos=(-0.314, -0.01),
            resolution=(1080, 1920),
        )
    ):
        print_space("跳转到矛兵兵营...")
        touch([600, 942])  # 点击索引到对应兵营
        train(self)
        Homepage()  # 返回主页
        time.sleep(1)  # 等待1秒
        touch([14, 823])
    print_space("检查射手训练是否完成")
    if exists(
        Template(
            os.path.join("icon", r"tpl1719480732965.png"),
            threshold=0.8,
            rgb=True,
            record_pos=(-0.192, 0.087),
            resolution=(1080, 1920),
        )
    ):
        print_space("1跳转到射手兵营...")
        touch([600, 1060])  # 点击索引到对应兵营
        train(self)
    elif exists(
        Template(
            os.path.join("icon", r"tpl1719480732966.png"),
            threshold=0.8,
            rgb=True,
            record_pos=(-0.021, -0.003),
            resolution=(1080, 1920),
        )
    ):
        print_space("跳转到射手兵营...")
        touch([600, 1060])  # 点击索引到对应兵营
        train(self)
    else:
        print_space("没有兵营已完成生产，结束该任务")
        touch(
            Template(
                os.path.join("icon", r"tpl1719552273333.png"),
                threshold=0.9,
                record_pos=(0.142, -0.126),
                resolution=(1080, 1920),
            )
        )


# 升级资源检查
@catch_exceptions
def build_main():
    touch(
        Template(
            os.path.join("icon", r"tpl1719651083870.png"),
            record_pos=(0.001, 0.731),
            resolution=(1080, 1920),
        )
    )
    time.sleep(1)
    if exists(
        Template(
            os.path.join("icon", r"tpl1719817875178.png"),
            record_pos=(-0.002, 0.683),
            resolution=(1080, 1920),
        )
    ):
        print_space("一键补齐资源不足，回到首页")
        touch(
            Template(
                os.path.join("icon", r"tpl1719198103804.png"),
                record_pos=(0.442, -0.35),
                resolution=(1080, 1920),
            )
        )
        touch(
            Template(
                os.path.join("icon", r"tpl1719198103804.png"),
                record_pos=(0.442, -0.35),
                resolution=(1080, 1920),
            )
        )
    else:
        touch(
            Template(
                os.path.join("icon", r"tpl1719651144335.png"),
                record_pos=(0.224, 0.608),
                resolution=(1080, 1920),
            )
        )
        touch(
            Template(
                os.path.join("icon", r"tpl1719578558005.png"),
                record_pos=(0.003, -0.045),
                resolution=(1080, 1920),
            )
        )  # 点击升级
        time.sleep(1)
        touch(
            Template(
                os.path.join("icon", r"tpl1719579273500.png"),
                record_pos=(0.002, -0.08),
                resolution=(1080, 1920),
            )
        )


# 自动建筑升级
@catch_exceptions
@goHomepage
def Build():
    touch([14, 823])
    time.sleep(1)
    touch([170, 400])
    if exists(
        Template(
            os.path.join("icon", r"tpl1719643933714.png"),
            rgb=True,
            record_pos=(-0.311, -0.372),
            resolution=(1080, 1920),
        )
    ):
        print_space("有空闲队列，开始建造")
        touch(
            Template(
                os.path.join("icon", r"tpl1719643933714.png"),
                record_pos=(-0.306, -0.318),
                resolution=(1080, 1920),
            )
        )  # 点击跳转到需升级的建筑
        if exists(
            Template(
                os.path.join("icon", r"tpl1719580056417.png"),
                record_pos=(-0.362, 0.238),
                resolution=(1080, 1920),
            )
        ):  # 判断是什么建筑升级升级
            print_space("升级资源建筑")
            time.sleep(5)  # 等待5s
            if not exists(
                Template(
                    os.path.join("icon", r"tpl1719644932718.png"),
                    threshold=0.9,
                    record_pos=(0.308, 0.056),
                    resolution=(1080, 1920),
                )
            ):
                print_space("建筑设施未达到升级要求，升级设施")
                while not exists(
                    Template(
                        os.path.join("icon", r"tpl1719645172814.png"),
                        record_pos=(0.248, -0.102),
                        resolution=(1080, 1920),
                    )
                ):
                    touch([900, 1000])
                    if exists(
                        Template(
                            os.path.join("icon", r"tpl1719645172814.png"),
                            record_pos=(0.248, -0.102),
                            resolution=(1080, 1920),
                        )
                    ):
                        print_space("达到升级条件，开始升级")
            touch([900, 800])  # 点击升级按钮
            touch([800, 1800])  # 点击升级
            if exists(
                Template(
                    os.path.join("icon", r"tpl1719651083870.png"),
                    record_pos=(0.001, 0.731),
                    resolution=(1080, 1920),
                )
            ):  # 判断资源是否充足
                print_space("/31资源不足，点击一键补齐")
                build_main()
            else:
                time.sleep(1)
                touch(
                    Template(
                        os.path.join("icon", r"tpl1719579273500.png"),
                        record_pos=(0.003, -0.045),
                        resolution=(1080, 1920),
                    )
                )  # 点击求助
        else:
            print_space("升级功能建筑")
            touch([553, 1333])  # 点击升级按钮
            touch(
                Template(
                    os.path.join("icon", r"tpl1719578558005.png"),
                    record_pos=(0.003, -0.045),
                    resolution=(1080, 1920),
                )
            )  # 点击升级
            if exists(
                Template(
                    os.path.join("icon", r"tpl1719651083870.png"),
                    record_pos=(0.001, 0.731),
                    resolution=(1080, 1920),
                )
            ):  # 判断资源是否充足
                print_space("资源不足，点击一键补齐")
                build_main()
            else:
                time.sleep(1)
                touch(
                    Template(
                        os.path.join("icon", r"tpl1719579273500.png"),
                        record_pos=(0.002, -0.08),
                        resolution=(1080, 1920),
                    )
                )  # 点击求助
    else:
        print_space("没有空闲建筑队列")
        touch(
            Template(
                os.path.join("icon", r"tpl1719552273333.png"),
                threshold=0.9,
                record_pos=(0.142, -0.126),
                resolution=(1080, 1920),
            )
        )


# 搜索资源
@catch_exceptions
def search_main():
    if not exists(
        Template(
            os.path.join("icon", r"tpl1720145326019.png"),
            record_pos=(0.404, 0.852),
            resolution=(1080, 1920),
        )
    ):
        print_space("不在世界，点击去往世界")
        touch([950, 1850])  # 点击野外
        time.sleep(5)
    else:
        print_space("找到城镇图案，在世界")
    print_space("点击搜索图标")
    touch([63, 1314])  # 点击搜索图标
    time.sleep(1)  # 等待1s


# 打雪怪功能
@catch_exceptions
@goHomepage
def NPC():
    print_space("打雪怪时间，开始集结雪怪")
    print_space("打开背包")
    touch([460, 1836])  # 点击打开背包
    time.sleep(1)
    if exists(
        Template(
            os.path.join("icon", r"tpl1719376487523.png"),
            record_pos=(0.449, -0.78),
            resolution=(1080, 1920),
        )
    ):  # 判断背包是否打开成功
        touch([949, 171])  # 点击其他跳转至该页
        print_space("查看活动道具")
        if exists(
            Template(
                os.path.join("icon", r"tpl1719376586643.png"),
                record_pos=(0.106, -0.476),
                resolution=(1080, 1920),
            )
        ):  # 判断是否有该道具
            print_space("使用活动道具")
            touch(
                Template(
                    os.path.join("icon", r"tpl1719376586643.png"),
                    record_pos=(0.106, -0.476),
                    resolution=(1080, 1920),
                )
            )  # 点击道具
            touch(
                Template(
                    os.path.join("icon", r"tpl1719376629723.png"),
                    record_pos=(0.0, 0.092),
                    resolution=(1080, 1920),
                )
            )  # 点击使用
            time.sleep(1)
            print_space("集结打怪")
            touch(
                Template(
                    os.path.join("icon", r"tpl1719376765868.png"),
                    record_pos=(0.002, 0.705),
                    resolution=(1080, 1920),
                )
            )  # 寻找到怪物点击集结
            touch(
                Template(
                    os.path.join("icon", r"tpl1719376776844.png"),
                    record_pos=(0.0, 0.326),
                    resolution=(1080, 1920),
                )
            )  # 点击发起集结
            print_space("兵力检查")
            if exists(
                Template(
                    os.path.join("icon", r"tpl1721191349774.png"),
                    record_pos=(-0.118, 0.782),
                    resolution=(1080, 1920),
                )
            ):
                touch(
                    Template(
                        os.path.join("icon", r"tpl1721191349774.png"),
                        record_pos=(-0.118, 0.782),
                        resolution=(1080, 1920),
                    )
                )
                print_space("体力检查")
                if exists(
                    Template(
                        os.path.join("icon", r"tpl1719376787180.png"),
                        record_pos=(0.263, 0.773),
                        resolution=(1080, 1920),
                    )
                ):  # 判断体力是否充足
                    energy()
                else:
                    print_space("体力不足，暂停打怪")
            else:
                print_space("兵力不足，暂停打怪")
        else:
            print_space("未找到相关物品，退出任务")
            touch(
                Template(
                    os.path.join("icon", r"tpl1719198082012.png"),
                    threshold=0.5,
                    record_pos=(-0.44, -0.783),
                    resolution=(1080, 1920),
                )
            ) or touch(
                Template(
                    os.path.join("icon", r"tpl1719198103804.png"),
                    record_pos=(0.442, -0.35),
                    resolution=(1080, 1920),
                )
            )


# 野兽等级输入
@catch_exceptions
def XG_lv():
    print_space("首次启动或数据有更新，重新输入等级")
    print_space("点击等级输入框")
    touch([900, 1573])
    time.sleep(1)
    print_space("删除原本等级")
    keyevent("KEYCODE_DEL")  # 每次只能删除一个数字
    keyevent("KEYCODE_DEL")
    time.sleep(1)  # 等待1秒
    print_space("输入新的等级")
    time.sleep(1)
    text(settings.value("世界野怪等级设置", 10, type=str))
    print_space("点击确定按钮")
    time.sleep(1)
    touch(
        Template(
            os.path.join("icon", r"sure_button.png"),
            record_pos=(0.404, 0.852),
            resolution=(1080, 1920),
        )
    )


# 野兽
@catch_exceptions
@goHomepage
def Brush_XG(self):
    print_space("打野怪时间，开始出征")
    search_main()
    swipe([600, 1370], vector=[0.4103, 0.0170])  # 滑动
    time.sleep(1)  # 等待1s
    print_space("点击选择普通野兽")
    touch([120, 1373])  # 点击普通野兽
    time.sleep(1)  # 等待1s
    """判断本次是否需要执行选择等级"""
    if settings.value("世界野怪等级设置更新", type=bool):
        settings.setValue("世界野怪等级设置更新", 0)
        XG_lv()
        time.sleep(1)  # 等待1s
    print_space("点击搜索按钮")
    touch([534, 1821])  # 点击搜索
    time.sleep(1)  # 等待1s
    print_space("点击攻击按钮")
    if exists(
        Template(
            os.path.join("icon", r"tpl1721191349775.png"),
            rgb=False,
            record_pos=(0.002, 0.705),
            resolution=(1080, 1920),
        )
    ):
        touch(
            Template(
                os.path.join("icon", r"tpl1721191349775.png"),
                rgb=False,
                record_pos=(0.002, 0.705),
                resolution=(1080, 1920),
            )
        )  # 点击出征怪物
    else:
        print_space("未找到攻击按钮图案，如游戏内有，请检查模拟器和游戏相关设置")
    time.sleep(1)  # 等待1s
    if exists(
        Template(
            os.path.join("icon", r"tpl1721191349774.png"),
            record_pos=(-0.118, 0.782),
            resolution=(1080, 1920),
        )
    ):  # 判断是否有兵力
        if self.checkBox_XG_average.isChecked():  # 平均兵力选项
            print_space("点击平均配置")
            touch(
                Template(
                    os.path.join("icon", r"tpl1721191349774.png"),
                    record_pos=(-0.118, 0.782),
                    resolution=(1080, 1920),
                )
            )
        energy()
    else:
        print_space("兵力不足，暂停打野怪")


# 巨熊活动
@catch_exceptions
@goHomepage
def bear():
    if exists(
        Template(
            os.path.join("icon", r"tpl1721191349777.png"),
            record_pos=(0.26, 0.795),
            resolution=(1080, 1920),
        )
    ):
        print_space("点击活动按钮")
        touch(
            Template(
                os.path.join("icon", r"tpl1721191349777.png"),
                record_pos=(0.26, 0.795),
                resolution=(1080, 1920),
            )
        )
        time.sleep(2)
        print_space("点击集结按钮")
        touch(
            Template(
                os.path.join("icon", r"tpl1721784579065.png"),
                record_pos=(0.26, 0.795),
                resolution=(1080, 1920),
            )
        )
        if exists(
            Template(
                os.path.join("icon", r"tpl1721784579066.png"),
                record_pos=(0.26, 0.795),
                resolution=(1080, 1920),
            )
        ):
            print_space("发起集结")
            touch(
                Template(
                    os.path.join("icon", r"tpl1721784579066.png"),
                    record_pos=(0.26, 0.795),
                    resolution=(1080, 1920),
                )
            )
            print_space("点击出征")
            touch(
                Template(
                    os.path.join("icon", r"tpl1721784579067.png"),
                    record_pos=(0.002, 0.705),
                    resolution=(414, 780),
                )
            )
            print_space("出征成功")
        else:
            print_space("集结中")
    else:
        print_space("未找到活动图标")


# 巨兽等级
@catch_exceptions
def WM_lv():  # 冰原巨兽等级输入
    print_space("首次启动或数据有更新，重新输入等级")
    print_space("点击等级输入框")
    touch([900, 1573])
    time.sleep(1)
    print_space("删除原本等级")
    keyevent("KEYCODE_DEL")
    time.sleep(1)  # 等待1秒
    print_space("输入新的等级")
    # value = settings.value('冰原巨兽等级设置', type=str)
    # print(value)
    time.sleep(1)
    text(settings.value("冰原巨兽等级设置", 5, type=str))
    print_space("点击确定按钮")
    time.sleep(1)
    touch(
        Template(
            os.path.join("icon", r"sure_button.png"),
            record_pos=(0.404, 0.852),
            resolution=(1080, 1920),
        )
    )


# 冰原巨兽
@catch_exceptions
@goHomepage
def Brush_WM(self):
    search_main()
    swipe([600, 1370], vector=[0.4103, 0.0170])  # 滑动
    time.sleep(1)  # 等待1s
    print_space("点击选择冰原巨兽")
    touch([365, 1373])  # 点击冰原巨兽
    time.sleep(1)  # 等待1s
    """判断本次是否需要执行选择等级"""
    if settings.value("冰原巨兽等级设置更新", type=bool):
        settings.setValue("冰原巨兽等级设置更新", 0)
        WM_lv()
        time.sleep(1)  # 等待1s
    print_space("点击搜索按钮")
    touch([534, 1821])  # 点击搜索
    time.sleep(1)  # 等待1s
    print_space("点击集结按钮")
    touch(
        Template(
            os.path.join("icon", r"tpl1719376765868.png"),
            record_pos=(-0.003, -0.227),
            resolution=(1080, 1920),
        )
    )  # 点击怪物集结
    time.sleep(1)  # 等待1s
    if exists(
        Template(
            os.path.join("icon", r"tpl1719376776844.png"),
            record_pos=(0.0, 0.326),
            resolution=(1080, 1920),
        )
    ):
        print_space("点击发起集结")
        touch(
            Template(
                os.path.join("icon", r"tpl1719376776844.png"),
                rgb=True,
                record_pos=(0.0, 0.326),
                resolution=(1080, 1920),
            )
        )  # 点击发起集结
        time.sleep(1)  # 等待0.5s
        if exists(
            Template(
                os.path.join("icon", r"tpl1719376787180.png"),
                record_pos=(0.263, 0.773),
                resolution=(1080, 1920),
            )
        ):  # 有兵力可出征
            if self.checkBox_WM_average.isChecked():  # 平均兵力选项
                touch(
                    Template(
                        os.path.join("icon", r"tpl1721191349774.png"),
                        record_pos=(-0.118, 0.782),
                        resolution=(1080, 1920),
                    )
                )
            elif self.checkBox_WM_simple.isChecked():  # 单兵集结
                print_space("点击全部撤回")
                touch(
                    Template(
                        os.path.join("icon", r"all_withdraw.png"),
                        record_pos=(-0.406, 0.781),
                        resolution=(1080, 1920),
                    )
                )  # 点击全部撤回
                touch([714, 894])  # 点击盾兵数量输入框
                print_space("删除原本数量")
                keyevent("KEYCODE_DEL")
                time.sleep(1)  # 等待1秒
                print_space("输入数量1")
                time.sleep(1)
                text("1")
                print_space("点击确定按钮")
                time.sleep(1)
                touch(
                    Template(
                        os.path.join("icon", r"sure_button.png"),
                        record_pos=(0.404, 0.852),
                        resolution=(1080, 1920),
                    )
                )
            print_space("点击出征按钮")
            energy()
        else:  # 判断是否有多余兵力
            print_space("未找到出征按钮，不满足条件，无兵力出征")
    else:
        print_space("未找到发起集结按钮，队伍数不足，无法出征")


# 采集出兵
@catch_exceptions
def gather(self):
    print_space("点击采集按钮")
    touch(
        Template(
            os.path.join("icon", r"tpl1720675061569.png"),
            record_pos=(0.002, -0.015),
            resolution=(1080, 1920),
        )
    )
    if exists(
        Template(
            os.path.join("icon", r"tpl1721191349776.png"),
            record_pos=(0.26, 0.798),
            resolution=(1080, 1920),
        )
    ):  # 有兵力可出征
        if self.checkBox_Collection_hero.isChecked():  # 采集英雄选项
            print_space("删除英雄")
            # touch([357, 389])  # 点击删除第一个英雄
            touch([640, 389])  # 点击删除第二个英雄
            touch([920, 389])  # 点击删除第三个英雄
        """if self.checkBox_ty_caiji_average.isChecked():  # 平均兵力选项
            touch(Template(os.path.join("icon", r"tpl1721191349774.png"), record_pos=(-0.118, 0.782), resolution=(1080, 1920)))"""  # 弃用该功能
        print_space("点击出征按钮")
        touch(
            Template(
                os.path.join("icon", r"tpl1721191349776.png"),
                rgb=True,
                record_pos=(0.26, 0.798),
                resolution=(1080, 1920),
            )
        )  # 点击出征
        print_space("出征成功")
        time.sleep(1)
        touch([14, 823])
    else:  # 判断是否有多余兵力
        print_space("不满足条件，无兵力出征")


# 打怪出兵
@catch_exceptions
def energy():
    touch(
        Template(
            os.path.join("icon", r"tpl1719376787180.png"),
            record_pos=(0.263, 0.773),
            resolution=(1080, 1920),
        )
    )  # 点击出征
    time.sleep(1)
    if exists(
        Template(
            os.path.join("icon", r"tpl1720264632282.png"),
            record_pos=(0.301, -0.33),
            resolution=(1080, 1920),
        )
    ):  # 判断是否有体力
        print_space("体力不足，不满足出征条件，开始回到主页")
        print_space("关闭补充体力界面")
        time.sleep(1)
        touch(
            Template(
                os.path.join("icon", r"tpl1729734622180.png"),
                record_pos=(0.442, -0.35),
                resolution=(1080, 1920),
            )
        )
        print_space("关闭出征界面")
        time.sleep(1)
        touch(
            Template(
                os.path.join("icon", r"black_return.png"),
                rgb=True,
                record_pos=(-0.441, -0.839),
                resolution=(1080, 1920),
            )
        )
    elif exists(
        Template(
            os.path.join("icon", r"tpl1719376787180.png"),
            record_pos=(0.263, 0.773),
            resolution=(1080, 1920),
        )
    ):
        touch(
            Template(
                os.path.join("icon", r"tpl1719376787180.png"),
                record_pos=(0.263, 0.773),
                resolution=(1080, 1920),
            )
        )  # 点击出征
        print_space("出征成功")
    else:
        print_space("出征成功")


# 采集等级设置
@catch_exceptions
def collection_lv():
    print_space("首次启动或数据有更新，重新输入等级")
    print_space("点击等级输入框")
    touch([900, 1573])
    time.sleep(1)
    print_space("删除原本等级")
    keyevent("KEYCODE_DEL")
    time.sleep(1)  # 等待1秒
    print_space("输入新的等级")
    time.sleep(1)
    # print(set_collection_lv.get())
    # print(settings.value('采集等级设置', type=str))
    text(settings.value("采集资源等级设置", 7, type=str))
    time.sleep(1)
    print_space("点击确定按钮")
    # time.sleep(1)
    touch(
        Template(
            os.path.join("icon", r"sure_button.png"),
            record_pos=(0.404, 0.852),
            resolution=(1080, 1920),
        )
    )


# 生肉
@catch_exceptions
@goHomepage
@check_and_go_outside
def Meat(self):
    print_space("准备采集生肉资源")
    print_space("点击搜索图标")
    touch([63, 1314])  # 点击搜索图标
    time.sleep(1)  # 等待1s
    swipe([600, 1370], vector=[-0.4103, 0.0170])  # 滑动
    print_space("点击选择肉")
    touch([240, 1373])  # 点击选择肉
    time.sleep(1)  # 等待1s
    """判断本次是否需要执行选择等级"""
    if settings.value("肉采集等级设置更新", type=bool):
        settings.setValue("肉采集等级设置更新", 0)
        collection_lv()
        time.sleep(1)  # 等待1s
    print_space("点击搜索按钮")
    touch([534, 1821])  # 点击搜索
    time.sleep(3)  # 等待1s
    if exists(
        Template(
            os.path.join("icon", r"tpl1720675061569.png"),
            rgb=True,
            record_pos=(0.002, -0.015),
            resolution=(1080, 1920),
        )
    ):
        gather(self)
    else:
        print_space("未找到采集按钮，未搜索到生肉资源，结束该任务")


# 木材
@catch_exceptions
@goHomepage
@check_and_go_outside
def Wood(self):
    print_space("准备采集木材资源")
    print_space("点击搜索图标")
    touch([63, 1314])  # 点击搜索图标
    time.sleep(1)  # 等待1s
    swipe([600, 1370], vector=[-0.4103, 0.0170])  # 滑动
    print_space("点击选择木材资源")
    touch([476, 1373])  # 点击选择木材
    time.sleep(1)  # 等待1s
    """判断本次是否需要执行选择等级"""
    if settings.value("木头采集等级设置更新", type=bool):
        settings.setValue("木头采集等级设置更新", 0)
        collection_lv()
        time.sleep(1)  # 等待1s
    print_space("点击搜索按钮")
    touch([534, 1821])  # 点击搜索
    time.sleep(1)  # 等待1s
    if exists(
        Template(
            os.path.join("icon", r"tpl1720675061569.png"),
            record_pos=(0.002, -0.015),
            resolution=(1080, 1920),
        )
    ):
        gather(self)
    else:
        print_space("未找到采集按钮，未搜索到生肉资源，结束该任务")


# 煤矿
@catch_exceptions
@goHomepage
@check_and_go_outside
def Coal(self):
    print_space("准备采集煤矿资源")
    print_space("点击搜索图标")
    touch([63, 1314])  # 点击搜索图标
    time.sleep(1)  # 等待1s
    swipe([600, 1370], vector=[-0.4103, 0.0170])  # 滑动
    print_space("点击选择煤矿资源")
    touch([710, 1373])  # 点击选择煤矿
    time.sleep(1)  # 等待1s
    """判断本次是否需要执行选择等级"""
    if settings.value("煤矿采集等级设置更新", type=bool):
        settings.setValue("煤矿采集等级设置更新", 0)
        collection_lv()
        time.sleep(1)  # 等待1s
    print_space("点击搜索按钮")
    touch([534, 1821])  # 点击搜索
    time.sleep(1)  # 等待1s
    if exists(
        Template(
            os.path.join("icon", r"tpl1720675061569.png"),
            record_pos=(0.002, -0.015),
            resolution=(1080, 1920),
        )
    ):
        gather(self)
    else:
        print_space("未找到采集按钮，未搜索到生肉资源，结束该任务")


# 铁矿
@catch_exceptions
@goHomepage
@check_and_go_outside
def Iron(self):
    print_space("准备采集铁矿资源")
    print_space("点击搜索图标")
    touch([63, 1314])  # 点击搜索图标
    time.sleep(1)  # 等待1s
    swipe([600, 1370], vector=[-0.4103, 0.0170])  # 滑动
    print_space("点击选择铁矿资源")
    touch([950, 1373])  # 点击选择铁矿
    time.sleep(1)  # 等待1s
    """判断本次是否需要执行选择等级"""
    if settings.value("铁矿采集等级设置更新", type=bool):
        settings.setValue("铁矿采集等级设置更新", 0)
        collection_lv()
        time.sleep(1)  # 等待1s
    print_space("点击搜索按钮")
    touch([534, 1821])  # 点击搜索
    time.sleep(1)  # 等待1s
    if exists(
        Template(
            os.path.join("icon", r"tpl1720675061569.png"),
            record_pos=(0.002, -0.015),
            resolution=(1080, 1920),
        )
    ):
        gather(self)
    else:
        print_space("未找到采集按钮，未搜索到生肉资源，结束该任务")


# 自动采集
@catch_exceptions
@goHomepage
def Collection(self):
    if not check_and_touch(
        Template(
            os.path.join("icon", r"tpl1739024627263.png"),
            record_pos=(0.396, 0.788),
            resolution=(1080, 1920),
            threshold=0.9,
        ),
        "检查到在城镇,去野外采集",
    ):
        print_space("检查到在野外,准备采集")
    sleep(3)
    touch([14, 823])
    time.sleep(1)
    touch([500, 400])
    if not exists(
        Template(
            os.path.join("icon", r"tpl1720691682616.png"),
            record_pos=(-0.188, -0.127),
            resolution=(1080, 1920),
        )
    ):
        print_space("无采肉队伍，执行采肉任务")
        time.sleep(1)
        Meat(self)
    else:
        print_space("已有采肉队伍")
    Homepage()
    touch([14, 823])
    if not exists(
        Template(
            os.path.join("icon", r"tpl1720766916044.png"),
            threshold=0.7,
            record_pos=(-0.438, -0.163),
            resolution=(1080, 1920),
        )
    ):
        print_space("无采集木头队伍，执行采木头任务")
        time.sleep(1)
        Wood(self)
    else:
        print_space("已有采木材队伍")
    Homepage()
    touch([14, 823])
    if not exists(
        Template(
            os.path.join("icon", r"tpl1720766916045.png"),
            record_pos=(-0.168, -0.088),
            resolution=(1080, 1920),
        )
    ):
        print_space("无采煤队伍，执行采煤任务")
        time.sleep(1)
        Coal(self)
    else:
        print_space("已有采煤队伍")
    Homepage()
    touch([14, 823])
    if not exists(
        Template(
            os.path.join("icon", r"tpl1720766916046.png"),
            rgb=True,
            record_pos=(-0.168, -0.088),
            resolution=(1080, 1920),
        )
    ):
        print_space("无采铁队伍，执行采铁任务")
        time.sleep(1)
        Iron(self)
    else:
        print_space("已有采铁队伍")
        touch(
            Template(
                os.path.join("icon", r"tpl1719552273333.png"),
                threshold=0.9,
                record_pos=(0.142, -0.126),
                resolution=(1080, 1920),
            )
        )


# 治疗
@catch_exceptions
@goHomepage
def treatment():
    check_and_touch(
        Template(
            os.path.join("icon", r"tpl1720145326019.png"),
            record_pos=(0.404, 0.852),
            resolution=(1080, 1920),
        ),
        "找到城镇图案点击并前往",
    )
    if exists(
        Template(
            os.path.join("icon", r"tpl1738728068288.png"),
            record_pos=(0.273, 0.434),
            resolution=(1080, 1920),
        )
    ) or exists(
        Template(
            os.path.join("icon", r"tpl1739028844307.png"),
            record_pos=(-0.035, -0.13),
            resolution=(1080, 1920),
        )
    ):
        check_and_touch(
            Template(
                os.path.join("icon", r"tpl1738728068288.png"),
                record_pos=(0.273, 0.434),
                resolution=(1080, 1920),
            ),
            "找到黑色治疗图标点击",
        )
        check_and_touch(
            Template(
                os.path.join("icon", r"tpl1739028844307.png"),
                record_pos=(-0.035, -0.13),
                resolution=(1080, 1920),
            ),
            "找到白色治疗图标点击",
        )
        print_space("点击治疗按钮")
        touch(
            Template(
                os.path.join("icon", r"tpl1738728101302.png"),
                record_pos=(0.219, 0.382),
                resolution=(1080, 1920),
            )
        )
        print_space("点击联盟互助")
        check_and_touch(
            Template(
                os.path.join("icon", r"tpl1739030020921.png"),
                record_pos=(-0.253, -0.504),
                resolution=(1080, 1920),
            ),
            "找到联盟互助图标点击",
        )
    else:
        print_space("没有需要治疗的士兵")


# 联盟捐赠
@catch_exceptions
@goHomepage
def donate():
    print_space("开始执行联盟捐献任务")
    print_space("点击联盟图案")
    touch(
        Template(
            os.path.join("icon", r"tpl1721784579070.png"),
            record_pos=(-0.168, -0.088),
            resolution=(1080, 1920),
        )
    )
    print_space("点击联盟科技")
    touch(
        Template(
            os.path.join("icon", r"tpl1721784579071.png"),
            record_pos=(-0.168, -0.088),
            resolution=(1080, 1920),
        )
    )
    if exists(
        Template(
            os.path.join("icon", r"tpl1721784579072.png"),
            record_pos=(-0.168, -0.088),
            resolution=(1080, 1920),
        )
    ):
        print_space("点击大拇指科技")
        touch(
            Template(
                os.path.join("icon", r"tpl1721784579072.png"),
                record_pos=(-0.168, -0.088),
                resolution=(1080, 1920),
            )
        )
        x = 1
        while x > 0:
            if exists(
                Template(
                    os.path.join("icon", r"tpl1721784579073.png"),
                    rgb=True,
                    record_pos=(0.208, 0.514),
                    resolution=(1080, 1920),
                )
            ):
                print_space("点击捐献")
                touch(
                    Template(
                        os.path.join("icon", r"tpl1721784579073.png"),
                        rgb=True,
                        record_pos=(0.208, 0.514),
                        resolution=(1080, 1920),
                    ),
                    duration=2,
                )
            else:
                print_space("无捐献次数，结束任务并返回至主页")
                touch([956, 299])  # 点击关闭按钮x
                touch([60, 60])  # 点击黑色返回按钮
                touch(
                    Template(
                        os.path.join("icon", r"black_return.png"),
                        threshold=0.8,
                        record_pos=(-0.44, -0.783),
                        resolution=(1080, 1920),
                    )
                )  # 点击黑色返回按钮
                x = 0
    else:
        print_space("无大拇指指引，返回主页")
        touch([60, 60])  # 点击黑色返回按钮
        touch(
            Template(
                os.path.join("icon", r"black_return.png"),
                threshold=0.8,
                record_pos=(-0.44, -0.783),
                resolution=(1080, 1920),
            )
        )  # 点击黑色返回按钮


# 探险
@catch_exceptions
@goHomepage
def adventure():
    print_space("点击探险")
    touch(
        Template(
            os.path.join("icon", r"tpl1719198809581.png"),
            threshold=0.9,
            record_pos=(-0.398, 0.819),
            scale_max=800,
            resolution=(1080, 1920),
        )
    )
    time.sleep(1)
    print_space("点击宝箱")
    touch([910, 1250])
    if exists(
        Template(
            os.path.join("icon", r"tpl1721784579076.png"),
            threshold=0.8,
            record_pos=(-0.398, 0.819),
            resolution=(1080, 1920),
        )
    ):
        print_space("点击领取奖励")
        touch(
            Template(
                os.path.join("icon", r"tpl1721784579076.png"),
                threshold=0.8,
                record_pos=(-0.398, 0.819),
                resolution=(1080, 1920),
            )
        )
        time.sleep(1)
        print_space("回到主页")
        touch([500, 500])
        touch(
            Template(
                os.path.join("icon", r"tpl1719198082012.png"),
                threshold=0.8,
                record_pos=(-0.44, -0.783),
                resolution=(1080, 1920),
            )
        )
    else:
        print_space("没有可领取奖励")


# 招募英雄
@catch_exceptions
@goHomepage
def recruit():
    if check_and_touch(
        Template(
            os.path.join("icon", r"hero.png"),
            threshold=0.9,
            record_pos=(-0.398, 0.819),
            scale_max=800,
            resolution=(1080, 1920),
        ),
        "查找到英雄并点击",
    ):
        if check_and_touch(
            Template(
                os.path.join("icon", r"hero_recruit.png"),
                threshold=0.8,
                record_pos=(-0.398, 0.819),
                scale_max=800,
                resolution=(1080, 1920),
            ),
            "查找到英雄招募并点击",
        ):
            if check_and_touch(
                Template(
                    os.path.join("icon", r"tpl1739026421641.png"),
                    record_pos=(-0.235, 0.803),
                    resolution=(1080, 1920),
                ),
                "找到免费次数,第1次领取",
            ):
                sleep(1)
                if check_and_touch(
                    Template(
                        os.path.join("icon", r"tpl1739012192856.png"),
                        record_pos=(-0.444, -0.844),
                        resolution=(1080, 1920),
                        threshold=0.9,
                    ),
                    "检查到返回按钮并点击",
                    [50, 50],
                ):
                    if check_and_touch(
                        Template(
                            os.path.join("icon", r"tpl1739026421641.png"),
                            record_pos=(-0.235, 0.803),
                            resolution=(1080, 1920),
                        ),
                        "找到免费次数,第2次领取",
                    ):
                        sleep(1)
                        check_and_touch(
                            Template(
                                os.path.join("icon", r"tpl1739012192856.png"),
                                record_pos=(-0.444, -0.844),
                                resolution=(1080, 1920),
                                threshold=0.9,
                            ),
                            "检查到返回按钮并点击",
                            [50, 50],
                        )
                        touch[50, 50]
                        return
                    return
                touch[50, 50]
                return
            return
        print_space("无免费招募次数")
        return


# 攻击检测
@catch_exceptions
@goHomepage
def mining_collision():
    if exists(
        Template(
            os.path.join("icon", r"tpl1729833981926.png"),
            record_pos=(0.42, -0.141),
            resolution=(1080, 1920),
        )
    ):
        print_space("检测到被攻击，点击预警图标")
        touch(
            Template(
                os.path.join("icon", r"tpl1729833981926.png"),
                record_pos=(0.42, -0.141),
                resolution=(1080, 1920),
            )
        )
        find_result = find_all(
            Template(
                os.path.join("icon", r"tpl1729834107464.png"),
                record_pos=(0.207, -0.549),
                resolution=(1080, 1920),
            )
        )
        length = len(find_result)
        print("被攻击列表数：%s" % length)
        # for i in range(0, length):
        while length > 0:
            print_space("点击前往目标")
            time.sleep(1)
            # touch(results[1]['result']) # 点击字典内第一个坐标，但第一个坐标不一定是排在第一个的目标，废弃
            # touch(Template(os.path.join("icon", r"tpl1729834107464.png"), record_pos=(0.207, -0.549), resolution=(1080, 1920)))
            touch([755, 356])  # 使用绝对坐标，点击列表内第一个目标
            time.sleep(1)
            print_space("点击跳转到的目标")
            touch([540, 890])
            time.sleep(2)
            if exists(
                Template(
                    os.path.join("icon", r"tpl1729834163624.png"),
                    rgb=True,
                    record_pos=(-0.139, 0.607),
                    resolution=(1080, 1920),
                )
            ):
                print_space("撞矿检测，点击召回采矿")
                touch(
                    Template(
                        os.path.join("icon", r"tpl1729834163624.png"),
                        record_pos=(-0.139, 0.607),
                        resolution=(1080, 1920),
                    )
                )
                time.sleep(1)
                print_space("点击确认召回队伍")
                touch(
                    Template(
                        os.path.join("icon", r"tpl1729834190986.png"),
                        record_pos=(0.212, 0.203),
                        resolution=(1080, 1920),
                    )
                )
                print_space("撤回队伍成功")
                length -= 1  # 循环次数减1
            elif exists(
                Template(
                    os.path.join("icon", r"tpl1729834914817.png"),
                    record_pos=(-0.139, 0.557),
                    resolution=(1080, 1920),
                )
            ):
                print_space("检测到攻击城堡，点击城堡增益准备开启防护罩")
                touch(
                    Template(
                        os.path.join("icon", r"tpl1729834914817.png"),
                        record_pos=(-0.139, 0.557),
                        resolution=(1080, 1920),
                    )
                )
                time.sleep(1)
                print_space("点击防护罩")
                touch(
                    Template(
                        os.path.join("icon", r"tpl1729834969758.png"),
                        record_pos=(-0.372, -0.544),
                        resolution=(1080, 1920),
                    )
                )
                time.sleep(1)
                print_space("点击使用")
                touch(
                    Template(
                        os.path.join("icon", r"tpl1729834989760.png"),
                        record_pos=(0.322, -0.336),
                        resolution=(1080, 1920),
                    )
                )
                print_space("开启防护罩成功")
                length -= 1  # 循环次数减1
                if exists(
                    Template(
                        os.path.join("icon", r"tpl1733823336248.png"),
                        record_pos=(-0.335, -0.838),
                        resolution=(1080, 1920),
                    )
                ):
                    # 防御罩开启后，检查是否在主页
                    print_space("点击黑色返回按钮")
                    touch(
                        Template(
                            os.path.join("icon", r"tpl1733823336248.png"),
                            target_pos=4,
                            record_pos=(-0.335, -0.838),
                            resolution=(1080, 1920),
                        )
                    )
            if exists(
                Template(
                    os.path.join("icon", r"tpl1729833981926.png"),
                    record_pos=(0.42, -0.141),
                    resolution=(1080, 1920),
                )
            ):
                print_space("再次回到攻击列表")
                time.sleep(1)
                touch(
                    Template(
                        os.path.join("icon", r"tpl1729833981926.png"),
                        record_pos=(0.42, -0.141),
                        resolution=(1080, 1920),
                    )
                )  # 回到攻击列表
            if length <= 0:
                break
    else:
        print_space("未检测到攻击")


# 邮件领取功能逻辑
@catch_exceptions
@goHomepage
def mail_function():
    print_space("点击邮件图案")
    touch([993, 1582])  # 邮件图案坐标
    print_space("点击联盟邮件")
    touch([333, 180])  # 联盟图案坐标
    print_space("点击一键领取")
    touch([858, 1865])  # 一键领取坐标
    time.sleep(1)  # 等待1秒
    touch([858, 1865])  # 再次点击以关闭奖励弹窗
    print_space("点击系统邮件")
    touch([540, 180])  # 系统图案坐标
    print_space("点击一键领取")
    touch([858, 1865])  # 一键领取坐标
    time.sleep(1)  # 等待1秒
    touch([858, 1865])  # 再次点击以关闭奖励弹窗
    print_space("点击报告邮件")
    touch([740, 180])  # 系统图案坐标
    print_space("点击一键领取")
    touch([858, 1865])  # 一键领取坐标
    time.sleep(1)  # 等待1秒
    touch([858, 1865])  # 再次点击以关闭奖励弹窗
    touch(
        Template(
            os.path.join("icon", r"black_return.png"),
            rgb=True,
            record_pos=(-0.441, -0.839),
            resolution=(1080, 1920),
        )
    )  # 点击返回按钮


# 联盟宝箱领取功能
@catch_exceptions
@goHomepage
def union_Treasure_Chest():
    print_space("点击联盟图案")
    touch(
        Template(
            os.path.join("icon", r"tpl1721784579070.png"),
            record_pos=(-0.168, -0.088),
            resolution=(1080, 1920),
        )
    )
    print("点击联盟宝箱")
    if exists(
        Template(
            os.path.join("icon", r"tpl1734838173842.png"),
            record_pos=(0.214, 0.036),
            resolution=(1080, 1920),
        )
    ):
        touch(
            Template(
                os.path.join("icon", r"tpl1734838173842.png"),
                record_pos=(0.214, 0.036),
                resolution=(1080, 1920),
            )
        )
        print_space("点击战利品宝箱")
        touch([290, 600])  # 点击战利品宝箱区域
        if exists(
            Template(
                os.path.join("icon", r"tpl1734838244122.png"),
                threshold=0.8,
                rgb=True,
                record_pos=(0.005, 0.789),
                resolution=(1080, 1920),
            )
        ):
            touch(
                Template(
                    os.path.join("icon", r"tpl1734838244122.png"),
                    record_pos=(0.005, 0.789),
                    resolution=(1080, 1920),
                )
            )
            print_space("领取成功")
            time.sleep(1)  # 等待1s
            touch([540, 1810])  # 点击关闭奖励界面
        else:
            print_space("未找到一键领取按钮，等待下次检查")
        print("点击盟友赠礼")
        touch([790, 600])
        if exists(
            Template(
                os.path.join("icon", r"tpl1734838244122.png"),
                record_pos=(0.005, 0.789),
                resolution=(1080, 1920),
            )
        ):
            touch(
                Template(
                    os.path.join("icon", r"tpl1734838244122.png"),
                    record_pos=(0.005, 0.789),
                    resolution=(1080, 1920),
                )
            )
            print_space("领取成功")
            touch([540, 1810])  # 点击关闭奖励界面
        else:
            print_space("未找到一键领取按钮，等待下次检查")
    else:
        print_space("未找到联盟宝箱图案，请检查游戏界面或自主修复")
    touch([50, 50])  # 点击返回按钮


# 仓库补给
@catch_exceptions
@goHomepage
def warehouse():
    global number_physical_strength
    now_time = datetime.now()
    if exists(
        Template(
            os.path.join("icon", r"tpl1720145326019.png"),
            record_pos=(0.404, 0.852),
            resolution=(1080, 1920),
        )
    ):
        print_space("不在城镇，点击去往城镇")
        touch([950, 1850])  # 点击城镇
        time.sleep(5)
    touch([14, 823])  # 点击左侧打开隐藏栏
    time.sleep(1)
    touch([170, 400])  # 点击城镇列表
    time.sleep(1)
    swipe([340, 1280], [330, 450])  # 滑动至底部
    time.sleep(1)
    if exists(
        Template(
            os.path.join("icon", r"tpl1737088915389.png"),
            threshold=0.9,
            record_pos=(-0.436, 0.106),
            resolution=(1080, 1920),
        )
    ):
        print_space("有可领取补给，点击前往")
        touch(
            Template(
                os.path.join("icon", r"tpl1737088915389.png"),
                record_pos=(-0.436, 0.106),
                resolution=(1080, 1920),
            )
        )
        time.sleep(1)
        print_space("点击领取")
        touch([540, 870])  # 点击领取补给
        time.sleep(1)
        touch([660, 300])  # 关闭奖励弹窗
    else:
        print_space("未找到仓库补给，关闭左侧栏")
        touch(
            Template(
                os.path.join("icon", r"tpl1719552273333.png"),
                threshold=0.9,
                record_pos=(0.142, -0.126),
                resolution=(1080, 1920),
            )
        )
    # 判定是否是刷新时间或本次启动首次执行
    if now_time.hour == 12 or now_time.hour == 17 or number_physical_strength == 0:
        number_physical_strength = 1
        print_space("首次执行任务或体力刷新时间，检查是否有体力可领取")
        time.sleep(1)
        touch([14, 823])  # 点击左侧打开隐藏栏
        time.sleep(1)
        touch([70, 1230])  # 点击科技研究
        time.sleep(1)
        swipe([500, 1000], vector=[0.2, 0.0017])  # 向左滑动
        time.sleep(1)
        if exists(
            Template(
                os.path.join("icon", r"tpl1737094428928.png"),
                record_pos=(0.002, -0.094),
                resolution=(1080, 1920),
            )
        ):
            print_space("点击体力罐头")
            touch(
                Template(
                    os.path.join("icon", r"tpl1737094428928.png"),
                    record_pos=(0.002, -0.094),
                    resolution=(1080, 1920),
                )
            )  # 点击体力罐头
            time.sleep(1)
            print_space("点击领取按钮")
            touch([540, 1430])  # 点击领取按钮
            time.sleep(1)
            touch([150, 1300])  # 关闭奖励弹窗
            print_space("领取成功")
        else:
            print_space("未找到体力罐头")
