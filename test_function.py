import logging
import time

from airtest.core.api import *
from main_function import energy

logging.getLogger('airtest').setLevel(logging.ERROR)
connect_device('android://127.0.0.1:5037')


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
    # exists(Template(r"情报/tpl1736414443397.png", record_pos=(-0.035, -0.505), resolution=(1080, 1920)))  # 紫色对战
    # exists(Template(r"情报/tpl1736414583724.png", record_pos=(0.044, 0.28), resolution=(1080, 1920)))  # 紫色爪子
    # 查找金色爪子图标
    XG_search_result = find_all(Template(r"情报/tpl1736410865667.png", record_pos=(0.256, -0.327), resolution=(1080, 1920)))  # 金色爪子
    # 查找蓝色帐篷图标
    rescue_search_result = find_all(Template(r"情报/tpl1736415568618.png", record_pos=(-0.149, 0.076), resolution=(1080, 1920)))  # 蓝色帐篷
    # 查找金色对战图标
    battle_search_result = find_all(Template(r"情报/tpl1736414991579.png", record_pos=(-0.216, -0.009), resolution=(1080, 1920)))  # 金色对战
    # 如果找到金色爪子图标
    if XG_search_result:
        img = XG_search_result[1]  # 获取字典内第一个元素
        # print(img['result'])
        coordinate = img['result']  # 获取坐标元组
        x = coordinate[0]  # 获取x坐标
        y = coordinate[1]  # 获取y坐标
        # print(x, y)
        touch([x, y])  # 点击坐标
        # 点击前往查看按钮
        touch(Template(r"情报/tpl1736414104111.png", record_pos=(-0.003, 0.406), resolution=(1080, 1920)))  # 前往查看按钮
        time.sleep(1)
        # 点击出征按钮
        touch(Template(r"情报/tpl1736414133437.png", record_pos=(-0.003, -0.039), resolution=(1080, 1920)))  # 出征
        energy()
    # 如果找到蓝色帐篷图标
    elif rescue_search_result:
        img_1 = rescue_search_result[1]  # 获取字典内第一个元素
        # print(img_1['result'])
        coordinate = img_1['result']  # 获取坐标元组
        x = coordinate[0]  # 获取x坐标
        y = coordinate[1]  # 获取y坐标
        # print(x, y)
        touch([x, y])  # 点击坐标
        # 点击前往查看按钮
        touch(Template(r"情报/tpl1736414104111.png", record_pos=(-0.003, 0.406), resolution=(1080, 1920)))  # 前往查看按钮
        time.sleep(1)
        # 点击营救按钮
        touch(Template(r"情报/tpl1736414182861.png", record_pos=(-0.004, -0.039), resolution=(1080, 1920)))  # 营救
    # 如果找到金色对战图标
    elif battle_search_result:
        img_1 = battle_search_result[1]  # 获取字典内第一个元素
        # print(img_1['result'])
        coordinate = img_1['result']  # 获取坐标元组
        x = coordinate[0]  # 获取x坐标
        y = coordinate[1]  # 获取y坐标
        # print(x, y)
        touch([x, y])  # 点击坐标
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
        else:
            print('体力不足，无法探险')



