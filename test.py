import tkinter as tk


def toggle_controls(value):
    if value == "option1":
        label1.pack(anchor="w")
        entry1.pack(anchor="w")
        label2.pack_forget()
        entry2.pack_forget()
    elif value == "option2":
        label1.pack_forget()
        entry1.pack_forget()
        label2.pack(anchor="w")
        entry2.pack(anchor="w")


root = tk.Tk()
# 初始化变量
v = tk.StringVar()
v.set("option1")  # 默认选中Option 1
# 创建单选按钮
radio1 = tk.Radiobutton(root, text="Option 1", variable=v, value="option1", command=lambda: toggle_controls("option1"))
radio1.pack(anchor="w")
radio2 = tk.Radiobutton(root, text="Option 2", variable=v, value="option2", command=lambda: toggle_controls("option2"))
radio2.pack(anchor="w")



# 创建与Option 1相关的控件
label1 = tk.Label(root, text="Label for Option 1")
entry1 = tk.Entry(root)

# 创建与Option 2相关的控件
label2 = tk.Label(root, text="Label for Option 2")
entry2 = tk.Entry(root)

# 默认显示Option 1的控件
toggle_controls("option1")

root.mainloop()
# import subprocess
#
#
# def is_emulator_connected():
#     try:
#         # 执行adb devices命令
#         result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#         # 获取命令的输出
#         output = result.stdout
#         # 检查输出中是否有模拟器设备
#         return "emulator-" in output
#     except Exception as e:
#         print(f"Error checking for emulator: {e}")
#         return False
#
#
# # 使用函数检查模拟器是否连接
# if __name__ == "__main__":
#     if is_emulator_connected():
#         print("模拟器已连接。")
#     else:
#         print("模拟器未连接。")
# #
# #
# # import tkinter as tk
# #
# #
# # def on_radio_button_changed():
# #     # 获取当前选中的单选按钮
# #     selected_value = radio_value.get()
# #     print("选中的单选按钮:", selected_value)  # 根据选中的值执行相应的操作
# #
# #
# # root = tk.Tk()
# # root.title("单选按钮示例")
# #
# # # 创建一个StringVar对象来跟踪单选按钮的值
# # radio_value = tk.StringVar()
# # radio_value.set("1")  # 设置默认选中的单选按钮值
# #
# # # 创建单选按钮，并绑定变量和命令
# # tk.Radiobutton(root, text="选项 1", variable=radio_value, value="1", command=on_radio_button_changed).pack()
# # tk.Radiobutton(root, text="选项 2", variable=radio_value, value="2", command=on_radio_button_changed).pack()
# # tk.Radiobutton(root, text="选项 3", variable=radio_value, value="3", command=on_radio_button_changed).pack()
# #
# # root.mainloop()
# #
# #
# # import tkinter as tk
# #
# #
# # def select_all():
# #     for checkbox in checkboxes:
# #         checkbox.select()
# #
# #
# # root = tk.Tk()
# # root.title("设置复选框")
# #
# # # 创建一个列表来保存复选框
# # checkboxes = []
# #
# # # 设置我的复选框
# # for i in range(1, 6):
# #     var = tk.IntVar()
# #     checkbox = tk.Checkbutton(root, text=f"我的{i}", variable=var, onvalue=1, offvalue=0)
# #     checkbox.grid(row=0, column=(i - 1) % 4, sticky=tk.W)
# #     checkboxes.append(checkbox)
# #
# # # 设置你的复选框
# # for i in range(1, 6):
# #     var = tk.IntVar()
# #     checkbox = tk.Checkbutton(root, text=f"你的{i}", variable=var, onvalue=1, offvalue=0)
# #     checkbox.grid(row=1, column=(i - 1) % 4, sticky=tk.W)
# #     checkboxes.append(checkbox)
# #
# # # ...以此类推，设置他的/她的/它的复选框...
# #
# # # 添加一键勾选所有复选框的按钮
# # select_all_button = tk.Button(root, text="一键勾选", command=select_all)
# # select_all_button.grid(row=2, column=0, sticky=tk.W)
# #
# # root.mainloop()
# #
# # import tkinter as tk
# #
# #
# # def button_clicked():
# #     print("按钮被点击")
# #
# #
# # # 创建主窗口
# # root = tk.Tk()
# # root.title("Canvas 按钮示例")
# #
# # # 创建 Canvas，设置宽度和高度
# # canvas = tk.Canvas(root, width=200, height=200)
# # canvas.pack()
# #
# # # 在 Canvas 上绘制一个矩形框
# # frame_id = canvas.create_rectangle(10, 10, 190, 190, width=2, fill="blue")
# #
# # # 在矩形框内创建一个按钮
# # canvas.create_window(5, 5, window=tk.Button(canvas, text="点击我", command=button_clicked))
# #
# # # 启动事件循环
# # root.mainloop()