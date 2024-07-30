# -*- encoding=utf8 -*-
__author__ = "猫耳小刻晴"

import subprocess
import threading

import threading
import sys
from wjdr import *
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
from tkinter.scrolledtext import ScrolledText

def create_window():
    # 创建主窗口
    window = tk.Tk()
    window.title("无尽冬日")  # 设置窗口标题
    window.geometry("500x600")  # 设置窗口大小

    bt = tkFont.Font(family="Helvetica", size=14, weight=tkFont.BOLD)
    tk.Label(window,text='无尽冬日',anchor='center',font=bt).pack()

    # 创建一个单选项并添加选项
    tk.Label(window,text='开启互助功能').place(x=100,y=100)
    option = tk.IntVar()
    option.set(1)
    option1 = tk.Radiobutton(window,text='是',variable=option,value=1)
    option2 = tk.Radiobutton(window,text='否',variable=option,value=2)
    option_button = ttk.Button(window, text="执行",command=lambda:simle(1))
    option1.place(x=200,y=100)
    option2.place(x=300,y=100)
    option_button.place(x=350, y=100)

    # 创建一个单选项并添加选项
    tk.Label(window, text='开启2功能').place(x=100, y=130)
    checkbutton = tk.IntVar()
    checkbutton.set(1)
    checkbutton2 = tk.Radiobutton(window, text='是', variable=checkbutton, value=1)
    checkbutton3 = tk.Radiobutton(window, text='否', variable=checkbutton, value=2)
    checkbutton_button = ttk.Button(window, text="执行", command=lambda: simle(2))
    checkbutton2.place(x=200, y=130)
    checkbutton3.place(x=300, y=130)
    checkbutton_button.place(x=350, y=130)


    # 创建一个单选项并添加选项
    tk.Label(window, text='开启3功能').place(x=100, y=160)
    opti = tk.IntVar()
    opti1 = tk.Radiobutton(window, text='是', variable=opti, value=0)
    opti2 = tk.Radiobutton(window, text='否', variable=opti, value=1)
    opti1.place(x=200, y=160)
    opti2.place(x=250, y=160)
    # 创建标签和输入框
    entry_arg1 = ttk.Entry(window,width=5)
    entry_arg1.place(x=300, y=160)
    label_arg2 = ttk.Label(window, text="<小时数<")
    label_arg2.place(x=350, y=160)
    entry_arg2 = ttk.Entry(window,width=5)
    entry_arg2.place(x=410, y=160)


    # 创建开始按钮
    start_button = ttk.Button(window, text="开始" ,command=start_function)
    start_button.place(x=150,y=380)
    # 创建停止按钮
    stop_button = ttk.Button(window, text="停止(待开发）", command=stop_function)
    stop_button.place(x=250,y=380)
    # 创建一个ScrolledText控件作为输出框
    def redirect_print(text_widget):
        def print_redirect(*args):
            str_args = " ".join(str(arg) for arg in args)
            text_widget.configure(state="normal")
            text_widget.insert("end", str_args + "")#换行显示
            text_widget.see("end")#显示最底部内容
            text_widget.configure(state="disabled")
        return print_redirect
    tk.Label(window, text='输出:').place(x=10, y=400)
    output_box = ScrolledText(window, width=65, height=10)
    output_box.place(x=10,y=420)
    sys.stdout.write = redirect_print(output_box)

    # 开始Tkinter事件循环
    tk.mainloop()
def simle(button_id):
    if button_id == 1:
        thread_Help.start()

def start_function():
    print("程序开始执行...")
    # 这里放置程序开始时需要执行的代码
    thread_main.start()

def stop_function():
    print("程序停止执行...")
    # 这里放置程序停止时需要执行的代码
    button_id.clear()

def help_simple():
    cnnect()
    while True:
        try:
            Help()
        except:
            print('错误')
#窗口线程
thread_window = threading.Thread(target=create_window)
#主线程
thread_main = threading.Thread(target=main)
#帮助单线程
thread_Help = threading.Thread(target=help_simple)
#xx单线程

thread_window.start()
