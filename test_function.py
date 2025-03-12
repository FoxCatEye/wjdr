import logging
import time

from airtest.core.api import *
from main_function import energy, check_and_touch

logging.getLogger('airtest').setLevel(logging.ERROR)
connect_device('android://127.0.0.1:5037')


intelligence_number = 0

# 情报功能
def intelligence():
    """
    情报功能的主函数。
    检查是否在世界地图中，如果不在则点击前往世界地图。
    点击情报按钮，等待加载完成。
    查找金色爪子、蓝色帐篷和金色对战的图标，并根据查找结果执行相应操作。
    """
    # 检查是否在世界地图中，如果不在则点击前往世界地图
    if not exists(Template(r"icon/tpl1720145326019.png", record_pos=(0.404, 0.852), resolution=(1080, 1920))):
        print_space('不在世界，点击去往世界')
        touch([950, 1850])  # 点击野外
        time.sleep(5)
    # 点击情报按钮
    touch(Template(r"情报/tpl1736493661192.png", record_pos=(0.421, 0.309), resolution=(1080, 1920)))  # 点击情报
    time.sleep(1)  # 等待加载
    # Template(r"情报/tpl1736410865667.png", record_pos=(0.256, -0.327), resolution=(1080, 1920)) # 金色爪子
    # Template(r"情报/tpl1736414583724.png", record_pos=(0.044, 0.28), resolution=(1080, 1920))  # 紫色爪子
    # Template(r"情报/tpl1736415568618.png", record_pos=(-0.149, 0.076), resolution=(1080, 1920))  # 蓝色帐篷
    # Template(r"情报/tpl1736414991579.png", record_pos=(-0.216, -0.009), resolution=(1080, 1920))  # 金色对战
    # Template(r"情报/tpl1736414443397.png", record_pos=(-0.035, -0.505), resolution=(1080, 1920))  # 紫色对战
    if adsa.isCheck():  # 如果勾选了高品质
        if check_and_touch(Template(r"情报/tpl1736410865667.png", rgb=True, record_pos=(0.256, -0.327), resolution=(1080, 1920)) or check_and_touch(Template(r"情报/tpl1736414583724.png", rgb=True, record_pos=(0.044, 0.28), resolution=(1080, 1920))):  # 金色爪子及紫色爪子
            # 点击前往查看按钮
            touch(Template(r"情报/tpl1736414104111.png", record_pos=(-0.003, 0.406), resolution=(1080, 1920)))  # 前往查看按钮
            time.sleep(1)
            # 点击出征按钮
            touch(Template(r"情报/tpl1736414133437.png", record_pos=(-0.003, -0.039), resolution=(1080, 1920)))  # 大世界出征
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
                intelligence_number += 1
            else:
                print_space("出征成功")
                intelligence_number += 1
        print_space('勾选了')
    else:          # 如果没勾选
        # 如果找到金色爪子图标
        if check_and_touch(Template(r"情报/tpl1736410865667.png", record_pos=(0.256, -0.327), resolution=(1080, 1920)),'找到爪子图案，点击图案'):
            # 点击前往查看按钮
            touch(Template(r"情报/tpl1736414104111.png", record_pos=(-0.003, 0.406), resolution=(1080, 1920)))  # 前往查看按钮
            time.sleep(1)
            # 点击出征按钮
            touch(Template(r"情报/tpl1736414133437.png", record_pos=(-0.003, -0.039), resolution=(1080, 1920)))  # 大世界出征
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
                intelligence_number += 1
            else:
                print_space("出征成功")
                intelligence_number += 1
        # 如果找到蓝色帐篷图标
        elif check_and_touch(Template(r"情报/tpl1736415568618.png", record_pos=(-0.149, 0.076), resolution=(1080, 1920)),'找到帐篷图案，点击图案'):
            # 点击前往查看按钮
            touch(Template(r"情报/tpl1736414104111.png", record_pos=(-0.003, 0.406), resolution=(1080, 1920)))  # 前往查看按钮
            time.sleep(1)
            # 点击营救按钮
            touch(Template(r"情报/tpl1736414182861.png", record_pos=(-0.004, -0.039), resolution=(1080, 1920)))  # 营救
            if exists(Template(r"icon\tpl1719376787180.png", record_pos=(0.263, 0.773), resolution=(1080, 1920))):  # 判断是否有体力
                print_space("体力不足，不满足营救条件，开始回到主页")
                print_space('关闭补充体力界面')
            else:
                print_space("营救成功")
                intelligence_number += 1
        # 如果找到金色对战图标
        elif check_and_touch(Template(r"情报/tpl1736414991579.png", record_pos=(-0.216, -0.009), resolution=(1080, 1920)),'找到对战图案，点击图案'):
        # 点击前往查看按钮
        touch(Template(r"情报/tpl1736414104111.png", record_pos=(-0.003, 0.406), resolution=(1080, 1920)))
        time.sleep(1)
        # 点击探险按钮
        touch(Template(r"情报/tpl1736414216951.png", record_pos=(-0.001, -0.04), resolution=(1080, 1920)))
        # 该处预留体力判断
        if exists(Template(r"情报/tpl1736416044350.png", record_pos=(0.235, 0.779), resolution=(1080, 1920))):
            touch(Template(r"情报/tpl1736416044350.png", record_pos=(0.235, 0.779), resolution=(1080, 1920)))  # 点击战斗
            time.sleep(5)  # 等待战斗结束
            touch([155, 155])  # 点击任意位置
            intelligence_number += 1
        else:
            print('体力不足，无法探险')
    # 如果找到金色爪子图标
    '''if XG_search_result:
        img = XG_search_result[1]  # 获取字典内第一个元素
        # print(img['result'])
        coordinate = img['result']  # 获取坐标元组
        x = coordinate[0]  # 获取x坐标
        y = coordinate[1]  # 获取y坐标
        # print(x, y)
        touch([x, y])  # 点击坐标'''

