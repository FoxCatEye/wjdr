import logging
from airtest.core.api import *
from airtest.core.android.android import *
logging.getLogger('airtest').setLevel(logging.ERROR)

connect_device("android://127.0.0.1:5037")
number_brush = 0
def lv():
    global number_brush
    number_brush += 1
    print('本次启动首次打')
    print('点击等级输入框')
    touch([900,1573])
    print('删除原本等级')
    keyevent('KEYCODE_DEL')
    time.sleep(1)
    print('输入新的等级')
    text('5',enter=True)
    print('点击确定按钮')
    touch(Template(r"icon\sure_button.png",record_pos=(0.404, 0.852), resolution=(1080, 1920)))
def search_main():
    if not exists(Template(r"icon\tpl1720145326019.png", record_pos=(0.404, 0.852), resolution=(1080, 1920))):
        print('不在世界，点击去往世界')
        touch([950, 1850])  # 点击野外
        time.sleep(5)
    print('点击搜索图标')
    touch([63, 1314])  # 点击搜索图标
    time.sleep(1)  # 等待1s
search_main()
swipe([600, 1370], vector=[0.4103, 0.0170])  # 滑动
time.sleep(1)  # 等待1s
print('点击选择冰原巨兽')
touch([365, 1373])  # 点击冰原巨兽
time.sleep(1)  # 等待1s
'''判断本次启动是否执行过，执行过就不在选择等级'''
if number_brush == 0:
    lv()
    time.sleep(1)  # 等待1s
print('点击搜索按钮')
touch([534, 1821])  # 点击搜索



# import tkinter as tk
# from tkinter import ttk
#
#
# def on_radio_change():
#     # 获取选中的单选框值
#     selected_value = radio_value.get()
#     # 根据单选框值设置下拉框的选项
#     if selected_value == "A":
#         combo_box["values"] = ("1", "2", "3")
#     elif selected_value == "B":
#         combo_box["values"] = ("4", "5", "6")
#     elif selected_value == "C":
#         combo_box["values"] = ("7", "8", "9")
#     # 设置下拉框的默认选项
#     combo_box.current(0)
#
#
# root = tk.Tk()
# root.title("下拉框与单选框匹配")
#
# # 创建一个字符变量，用于存储单选框的值
# radio_value = tk.StringVar()
#
# # 创建单选框
# radio_button_a = tk.Radiobutton(root, text="A", variable=radio_value, value="A", command=on_radio_change)
# radio_button_a.pack()
# radio_button_b = tk.Radiobutton(root, text="B", variable=radio_value, value="B", command=on_radio_change)
# radio_button_b.pack()
# radio_button_c = tk.Radiobutton(root, text="C", variable=radio_value, value="C", command=on_radio_change)
# radio_button_c.pack()
#
# # 初始化下拉框的选项
# combo_box_values = ("1", "2", "3")
#
# # 创建下拉框
# combo_box = ttk.Combobox(root, values=combo_box_values)
# combo_box.current(0)
# combo_box.pack()
#
# root.mainloop()
# # import tkinter as tk
# # from tkinter import ttk
# #
# #
# # def print_selection(event):
# #     # 获取选中的索引
# #     selected_index = combobox.current()
# #     # 获取选中的值
# #     selected_value = combobox.get()
# #     # 打印选中的索引
# #     print(f"Selected index: {selected_index}, value: {selected_value}")
# #
# #
# # root = tk.Tk()
# # root.title("下拉框示例")
# #
# # # 创建一个下拉框
# # combobox = ttk.Combobox(root)
# # # 设置默认选项
# # combobox["value"] = ["选项1", "选项2", "选项3", "选项4"]
# # combobox.current(0)  # 默认选中第一个选项
# # combobox.grid(row=0, column=0)
# #
# # # 绑定事件，当选项变化时触发
# # combobox.bind("<<ComboboxSelected>>", print_selection)
# #
# # root.mainloop()
# # #
# # # # 保存按钮
# # # def save_config():
# # #     # 更新配置文件
# # #     config['dropdown'][dropdown_var.get()] = entry_var.get()
# # #     with open('config.ini', 'w') as configfile:
# # #         config.write(configfile)
# # #
# # #
# # # button = tk.Button(root, text="保存", command=save_config)
# # # button.pack()
# # #
# # # root.mainloop()
# # #
# # #
# # # # import tkinter as tk
# # # # from tkinter import ttk
# # # #
# # # #
# # # # def on_switch_change(checked):
# # # #     if checked:
# # # #         print("开关打开")
# # # #     else:
# # # #         print("开关关闭")
# # # #
# # # #
# # # # def on_scale_change(value):
# # # #     print(f"音量设置为 {value}")
# # # #
# # # #
# # # # def on_combobox_change(event):
# # # #     print(f"选择的语言是: {combo_box.get()}")
# # # #
# # # #
# # # # def on_entry_change(event):
# # # #     print(f"输入的文本是: {entry_box.get()}")
# # # #
# # # #
# # # # def on_button_click():
# # # #     print("按钮被点击")
# # # #
# # # #
# # # # root = tk.Tk()
# # # # root.title("设置示例")
# # # #
# # # # # 创建单选开关
# # # # switch_var = tk.BooleanVar()
# # # # switch = ttk.Checkbutton(root, text="开关", variable=switch_var, command=lambda: on_switch_change(switch_var.get()))
# # # # switch.pack()
# # # #
# # # # # 创建滑块选择音量
# # # # scale = ttk.Scale(root, from_=0, to=100, command=on_scale_change)
# # # # scale.pack()
# # # #
# # # # # 创建下拉选择语言的组合框
# # # # combo_box_values = ["English", "Spanish", "Chinese"]
# # # # combo_box = ttk.Combobox(root, values=combo_box_values, state="readonly")
# # # # combo_box.current(0)
# # # # combo_box.bind("<<ComboboxSelected>>", on_combobox_change)
# # # # combo_box.pack()
# # # #
# # # # # 创建文本输入框
# # # # entry_box = ttk.Entry(root)
# # # # entry_box.bind("<Return>", on_entry_change)
# # # # entry_box.pack()
# # # #
# # # # # 创建按钮
# # # # button = ttk.Button(root, text="确认", command=on_button_click)
# # # # button.pack()
# # # #
# # # # root.mainloop()
# # # # # import configparser
# # # # # from tkinter import Tk, Label, Entry, Button, END
# # # # #
# # # # # # 初始化Tk
# # # # # root = Tk()
# # # # # root.title("INI Editor")
# # # # #
# # # # # # 配置文件对象
# # # # # config = configparser.ConfigParser()
# # # # #
# # # # # # 输入框和按钮
# # # # # label = Label(root, text="Key:")
# # # # # label.pack()
# # # # #
# # # # # entry_key = Entry(root)
# # # # # entry_key.pack()
# # # # #
# # # # # label_value = Label(root, text="Value:")
# # # # # label_value.pack()
# # # # #
# # # # # entry_value = Entry(root)
# # # # # entry_value.pack()
# # # # #
# # # # #
# # # # # def save_to_ini():
# # # # #     key = entry_key.get()
# # # # #     value = entry_value.get()
# # # # #     config[section] = {key: value}
# # # # #     with open('config.ini', 'w') as configfile:
# # # # #         config.write(configfile)
# # # # #
# # # # #
# # # # # # 按钮保存
# # # # # button_save = Button(root, text="Save", command=save_to_ini)
# # # # # button_save.pack()
# # # # #
# # # # # # 设置section
# # # # # section = "DEFAULT"
# # # # #
# # # # # root.mainloop()
# # # # # # import tkinter as tk
# # # # # # from configparser import ConfigParser
# # # # # # from tkinter import ttk
# # # # # #
# # # # # # # 创建Tkinter窗口和控件
# # # # # # root = tk.Tk()
# # # # # # root.title("设置保存示例")
# # # # # #
# # # # # # # 配置文件对象
# # # # # # config = ConfigParser()
# # # # # # config_file = "settings.ini"
# # # # # #
# # # # # # # 读取配置文件或使用默认设置
# # # # # # if not config.read(config_file, encoding="utf-8"):
# # # # # #     config["Settings"] = {
# # # # # #         "option1": "default value 1",
# # # # # #         "option2": "default value 2",
# # # # # #     }
# # # # # #
# # # # # # # 从配置文件中获取设置
# # # # # # option1_var = tk.StringVar(value=config["Settings"]["option1"])
# # # # # # option2_var = tk.StringVar(value=config["Settings"]["option2"])
# # # # # #
# # # # # # # 保存设置的函数
# # # # # # def save_settings():
# # # # # #     config["Settings"]["option1"] = "1" if option1_var.get() else "0"
# # # # # #     config["Settings"]["option2"] = "1" if option2_var.get() else "0"
# # # # # #     with open(config_file, "r") as configfile:
# # # # # #         config.write(configfile)
# # # # # # # 创建选项控件
# # # # # # option1_checkbox = tk.Checkbutton(root, text="Option 1", variable=option1_var)
# # # # # # option2_checkbox = tk.Checkbutton(root, text="Option 2", variable=option2_var)
# # # # # # butt = ttk.Button(root,text='开始',command=save_settings)
# # # # # #
# # # # # # # 布局控件
# # # # # # option1_checkbox.pack()
# # # # # # option2_checkbox.pack()
# # # # # # butt.pack()
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # # # 启动Tkinter事件循环
# # # # # # root.mainloop()
# # # # # # # import configparser
# # # # # # # import tkinter as tk
# # # # # # #
# # # # # # #
# # # # # # # # 创建Tkinter窗口和选项
# # # # # # # def create_gui():
# # # # # # #     root = tk.Tk()
# # # # # # #
# # # # # # #     def save_options():
# # # # # # #         config.set('Options', 'option1', var1.get())
# # # # # # #         config.set('Options', 'option2', var2.get())
# # # # # # #         with open('config.ini', 'w') as configfile:
# # # # # # #             config.write(configfile)
# # # # # # #
# # # # # # #     def load_options():
# # # # # # #         var1.set(config.get('Options', 'option1'))
# # # # # # #         var2.set(config.get('Options', 'option2'))
# # # # # # #
# # # # # # #     # 初始化配置解析器和选项变量
# # # # # # #     #global config, var1, var2
# # # # # # #     config = configparser.ConfigParser()
# # # # # # #     config['Options'] = {}
# # # # # # #     var1 = tk.StringVar()
# # # # # # #     var2 = tk.StringVar()
# # # # # # #
# # # # # # #     # 尝试加载先前保存的选项
# # # # # # #     try:
# # # # # # #         with open('config.ini', 'r') as configfile:
# # # # # # #             config.read_file(configfile)
# # # # # # #         load_options()
# # # # # # #     except IOError:
# # # # # # #         print('No saved options found.')
# # # # # # #
# # # # # # #     # 创建选项控件
# # # # # # #     option1 = tk.Checkbutton(root, text='Option 1', variable=var1,command=save_options)
# # # # # # #     option2 = tk.Checkbutton(root, text='Option 2', variable=var2,command=save_options)
# # # # # # #     #save_button = tk.Button(root, text='Save Options', command=save_options)
# # # # # # #
# # # # # # #     # 布局选项控件
# # # # # # #     option1.pack()
# # # # # # #     option2.pack()
# # # # # # #     #save_button.pack()
# # # # # # #
# # # # # # #     root.mainloop()
# # # # # # #
# # # # # # #
# # # # # # # create_gui()
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # # # import tkinter as tk
# # # # # # # #
# # # # # # # #
# # # # # # # # def toggle_controls(value):
# # # # # # # #     if value == "option1":
# # # # # # # #         label1.pack(anchor="w")
# # # # # # # #         entry1.pack(anchor="w")
# # # # # # # #         label2.pack_forget()
# # # # # # # #         entry2.pack_forget()
# # # # # # # #     elif value == "option2":
# # # # # # # #         label1.pack_forget()
# # # # # # # #         entry1.pack_forget()
# # # # # # # #         label2.pack(anchor="w")
# # # # # # # #         entry2.pack(anchor="w")
# # # # # # # #
# # # # # # # #
# # # # # # # # root = tk.Tk()
# # # # # # # # # 初始化变量
# # # # # # # # v = tk.StringVar()
# # # # # # # # v.set("option1")  # 默认选中Option 1
# # # # # # # # # 创建单选按钮
# # # # # # # # radio1 = tk.Radiobutton(root, text="Option 1", variable=v, value="option1", command=lambda: toggle_controls("option1"))
# # # # # # # # radio1.pack(anchor="w")
# # # # # # # # radio2 = tk.Radiobutton(root, text="Option 2", variable=v, value="option2", command=lambda: toggle_controls("option2"))
# # # # # # # # radio2.pack(anchor="w")
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # # # 创建与Option 1相关的控件
# # # # # # # # label1 = tk.Label(root, text="Label for Option 1")
# # # # # # # # entry1 = tk.Entry(root)
# # # # # # # #
# # # # # # # # # 创建与Option 2相关的控件
# # # # # # # # label2 = tk.Label(root, text="Label for Option 2")
# # # # # # # # entry2 = tk.Entry(root)
# # # # # # # #
# # # # # # # # # 默认显示Option 1的控件
# # # # # # # # toggle_controls("option1")
# # # # # # # #
# # # # # # # # root.mainloop()
# # # # # # # # # import subprocess
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # def is_emulator_connected():
# # # # # # # # #     try:
# # # # # # # # #         # 执行adb devices命令
# # # # # # # # #         result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
# # # # # # # # #         # 获取命令的输出
# # # # # # # # #         output = result.stdout
# # # # # # # # #         # 检查输出中是否有模拟器设备
# # # # # # # # #         return "emulator-" in output
# # # # # # # # #     except Exception as e:
# # # # # # # # #         print(f"Error checking for emulator: {e}")
# # # # # # # # #         return False
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # # 使用函数检查模拟器是否连接
# # # # # # # # # if __name__ == "__main__":
# # # # # # # # #     if is_emulator_connected():
# # # # # # # # #         print("模拟器已连接。")
# # # # # # # # #     else:
# # # # # # # # #         print("模拟器未连接。")
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # import tkinter as tk
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # def on_radio_button_changed():
# # # # # # # # # #     # 获取当前选中的单选按钮
# # # # # # # # # #     selected_value = radio_value.get()
# # # # # # # # # #     print("选中的单选按钮:", selected_value)  # 根据选中的值执行相应的操作
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # root = tk.Tk()
# # # # # # # # # # root.title("单选按钮示例")
# # # # # # # # # #
# # # # # # # # # # # 创建一个StringVar对象来跟踪单选按钮的值
# # # # # # # # # # radio_value = tk.StringVar()
# # # # # # # # # # radio_value.set("1")  # 设置默认选中的单选按钮值
# # # # # # # # # #
# # # # # # # # # # # 创建单选按钮，并绑定变量和命令
# # # # # # # # # # tk.Radiobutton(root, text="选项 1", variable=radio_value, value="1", command=on_radio_button_changed).pack()
# # # # # # # # # # tk.Radiobutton(root, text="选项 2", variable=radio_value, value="2", command=on_radio_button_changed).pack()
# # # # # # # # # # tk.Radiobutton(root, text="选项 3", variable=radio_value, value="3", command=on_radio_button_changed).pack()
# # # # # # # # # #
# # # # # # # # # # root.mainloop()
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # import tkinter as tk
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # def select_all():
# # # # # # # # # #     for checkbox in checkboxes:
# # # # # # # # # #         checkbox.select()
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # root = tk.Tk()
# # # # # # # # # # root.title("设置复选框")
# # # # # # # # # #
# # # # # # # # # # # 创建一个列表来保存复选框
# # # # # # # # # # checkboxes = []
# # # # # # # # # #
# # # # # # # # # # # 设置我的复选框
# # # # # # # # # # for i in range(1, 6):
# # # # # # # # # #     var = tk.IntVar()
# # # # # # # # # #     checkbox = tk.Checkbutton(root, text=f"我的{i}", variable=var, onvalue=1, offvalue=0)
# # # # # # # # # #     checkbox.grid(row=0, column=(i - 1) % 4, sticky=tk.W)
# # # # # # # # # #     checkboxes.append(checkbox)
# # # # # # # # # #
# # # # # # # # # # # 设置你的复选框
# # # # # # # # # # for i in range(1, 6):
# # # # # # # # # #     var = tk.IntVar()
# # # # # # # # # #     checkbox = tk.Checkbutton(root, text=f"你的{i}", variable=var, onvalue=1, offvalue=0)
# # # # # # # # # #     checkbox.grid(row=1, column=(i - 1) % 4, sticky=tk.W)
# # # # # # # # # #     checkboxes.append(checkbox)
# # # # # # # # # #
# # # # # # # # # # # ...以此类推，设置他的/她的/它的复选框...
# # # # # # # # # #
# # # # # # # # # # # 添加一键勾选所有复选框的按钮
# # # # # # # # # # select_all_button = tk.Button(root, text="一键勾选", command=select_all)
# # # # # # # # # # select_all_button.grid(row=2, column=0, sticky=tk.W)
# # # # # # # # # #
# # # # # # # # # # root.mainloop()
# # # # # # # # # #
# # # # # # # # # # import tkinter as tk
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # def button_clicked():
# # # # # # # # # #     print("按钮被点击")
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # # 创建主窗口
# # # # # # # # # # root = tk.Tk()
# # # # # # # # # # root.title("Canvas 按钮示例")
# # # # # # # # # #
# # # # # # # # # # # 创建 Canvas，设置宽度和高度
# # # # # # # # # # canvas = tk.Canvas(root, width=200, height=200)
# # # # # # # # # # canvas.pack()
# # # # # # # # # #
# # # # # # # # # # # 在 Canvas 上绘制一个矩形框
# # # # # # # # # # frame_id = canvas.create_rectangle(10, 10, 190, 190, width=2, fill="blue")
# # # # # # # # # #
# # # # # # # # # # # 在矩形框内创建一个按钮
# # # # # # # # # # canvas.create_window(5, 5, window=tk.Button(canvas, text="点击我", command=button_clicked))
# # # # # # # # # #
# # # # # # # # # # # 启动事件循环
# # # # # # # # # # root.mainloop()