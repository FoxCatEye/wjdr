import tkinter as tk
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
root.mainloop()
