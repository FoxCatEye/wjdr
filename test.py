import tkinter as tk


def select_all():
    for checkbox in checkboxes:
        checkbox.select()


root = tk.Tk()
root.title("设置复选框")

# 创建一个列表来保存复选框
checkboxes = []

# 设置我的复选框
for i in range(1, 6):
    var = tk.IntVar()
    checkbox = tk.Checkbutton(root, text=f"我的{i}", variable=var, onvalue=1, offvalue=0)
    checkbox.grid(row=0, column=(i - 1) % 4, sticky=tk.W)
    checkboxes.append(checkbox)

# 设置你的复选框
for i in range(1, 6):
    var = tk.IntVar()
    checkbox = tk.Checkbutton(root, text=f"你的{i}", variable=var, onvalue=1, offvalue=0)
    checkbox.grid(row=1, column=(i - 1) % 4, sticky=tk.W)
    checkboxes.append(checkbox)

# ...以此类推，设置他的/她的/它的复选框...

# 添加一键勾选所有复选框的按钮
select_all_button = tk.Button(root, text="一键勾选", command=select_all)
select_all_button.grid(row=2, column=0, sticky=tk.W)

root.mainloop()

import tkinter as tk


def button_clicked():
    print("按钮被点击")


# 创建主窗口
root = tk.Tk()
root.title("Canvas 按钮示例")

# 创建 Canvas，设置宽度和高度
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

# 在 Canvas 上绘制一个矩形框
frame_id = canvas.create_rectangle(10, 10, 190, 190, width=2, fill="blue")

# 在矩形框内创建一个按钮
button_id = canvas.create_window(100, 100, window=tk.Button(canvas, text="点击我", command=button_clicked))

# 启动事件循环
root.mainloop()