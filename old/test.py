'''import tkinter as tk
from PIL import Image, ImageTk


def center_window(root, width, height):
    # 获取屏幕尺寸
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 计算窗口位置
    x = (screen_width - width) / 2
    y = (screen_height - height) / 2

    # 设置窗口位置
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))

root = tk.Tk()
center_window(root, 960, 540)  # 设置窗口初始位置

# 加载并缩放背景图片
image_path = 'icon/11.png'  # 背景图片路径
image = Image.open(image_path)
image = image.resize((960, 540))
image = ImageTk.PhotoImage(image)

# 创建背景标签
background_label = tk.Label(root, image=image)
background_label.image = image  # 防止图片被垃圾回收
background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.mainloop()'''
import os
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


auto_setup(__file__)
logging.getLogger('airtest').setLevel(logging.ERROR)


#print('地址：android:// %s')
connect_device('android://127.0.0.1:5037')
# 训练检查
def Production_soldiers():
    touch([14, 823])
    time.sleep(1)
    touch([170, 400])
    if exists(Template(r"icon\tpl1719478488282.png", threshold=0.9, rgb=True, record_pos=(-0.186, -0.058), resolution=(414, 780))):
        print_space("1跳转到盾兵兵营...")
        touch([600, 840])  # 点击索引到对应兵营
        time.sleep(5)
        touch([14, 823])
    elif exists(Template(r"icon\tpl1719478488283.png", threshold=0.95, record_pos=(-0.437, 0.046), resolution=(414, 780))):
        print_space("2跳转到盾兵兵营...")
        touch([600, 840])  # 点击索引到对应兵营
        time.sleep(5)
        touch([14, 823])
    if exists(Template(r"icon\tpl1719480722195.png", threshold=0.9, rgb=True, record_pos=(-0.437, 0.046), resolution=(414, 780))):
        print_space("跳转到矛兵兵营...")
        touch([600, 942])  # 点击索引到对应兵营
        time.sleep(5)
        touch([14, 823])
    elif exists(Template(r'icon\tpl1719480722196.png', threshold=0.95, record_pos=(-0.437, 0.046), resolution=(414, 780))):
        print_space("跳转到矛兵兵营...")
        touch([600, 942])  # 点击索引到对应兵营
        time.sleep(5)
        touch([14, 823])
    if exists(Template(r"icon\tpl1719480732965.png", threshold=0.9, rgb=True, record_pos=(-0.437, 0.145), resolution=(414, 780))):
        print_space("跳转到射手兵营...")
        touch([600, 1060])  # 点击索引到对应兵营
        time.sleep(5)
        touch([14, 823])
    elif exists(Template(r'icon\tpl1719480732966.png', threshold=0.95, record_pos=(-0.437, 0.046), resolution=(414, 780))):
        print_space("跳转到射手兵营...")
        touch([600, 1060])  # 点击索引到对应兵营
        time.sleep(5)
        touch([14, 823])
    else:
        print_space("没有兵营已完成生产，结束该任务")
        touch(Template(r"icon\tpl1719552273333.png", threshold=0.9, record_pos=(0.142, -0.126), resolution=(1080, 1920)))
def print_space(variable, spaces=4):
    print(' ' * spaces + str(variable))

swipe([950, 1225], vector=[-0.8, 0.0170])  # 滑动训练兵种