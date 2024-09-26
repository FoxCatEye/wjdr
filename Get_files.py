import os
import subprocess
import sys
import threading
import time
from configparser import ConfigParser
from tkinter.scrolledtext import ScrolledText
import requests
import zipfile
import tkinter as tk


'''读取设置'''
def load_options():
    set_version.set(config.get('Options', 'version'))


def download_update():
    print('准备开始下载更新文件...')
    update_url = "http://fukesihu.gnway.cc:80/files.zip"
    response = requests.get(update_url,stream=True)
    # 确保请求成功
    if response.status_code == 200:
        total_length = response.headers.get('Content-Length')
        if total_length is None:  # 如果Content-Length不可用，可以省略进度显示
            with open('./files.zip', 'wb') as f:
                for chunk in response.iter_content(chunk_size=51200):  # 每次读取1KB数据
                    if chunk:  # 过滤掉空的chunk
                        print(f"Downloading {update_url}")
                        f.write(chunk)
        else:  # 如果Content-Length可用，显示下载进度
            with open('./files.zip', 'wb') as f:
                downloaded = 0
                total = int(total_length)
                print(f"Downloading {update_url}")
                for chunk in response.iter_content(chunk_size=51200):  # 每次读取1KB数据
                    downloaded += len(chunk)
                    f.write(chunk)
                    percentage = (downloaded / total) * 100
                    formatted_num = format(percentage, '.2f')#保留小数点2位
                    #sys.stdout.write(f"\r下载进度: {percentage:.2f}%") # 显示下载进度
                    #sys.stdout.flush() # 刷新输出缓冲区，确保进度显示及时更新
                    print("下载进度: %s"%formatted_num+'%')#写入输出框
                print('下载完成')
        extract_zip(zip_filename)
    else:
        print(f"无法下载 ，状态码：{response.status_code}")


def extract_zip(zip_filename):
    print('开始解压文件')
    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        for filename in zip_ref.namelist():
            zip_ref.extractall(os.path.dirname(zip_filename))
    os.remove(zip_filename)
    print('文件解压完成。')
zip_filename = 'files.zip'  # 之前下载的压缩文件名

def print(text_1):
    #    str_args = " ".join(str(arg) for arg in args)
    output_box.configure(state="normal")
    output_box.insert('end','\n'+ text_1)  # 换行显示
    output_box.see("end")  # 显示最底部内容
    output_box.configure(state="disabled")
def center_window(root, width, height):
    # 获取屏幕尺寸
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 计算窗口居中位置
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    # 设置窗口在屏幕上的位置
    root.geometry(f"{width}x{height}+{x}+{y}")
def replace_process(executable, *args):
    try:
        os.execvp(executable, [executable] + list(args))
    except FileNotFoundError:
        sys.exit("无法找到可执行文件：" + executable)

window = tk.Tk()
window.title("更新检查")  # 设置窗口标题
# window.geometry("500x600")  # 设置窗口大小
icon = tk.PhotoImage(file="icon\log.png")  # 设置窗口图标
window.iconphoto(True, icon)
# 设置窗口不能调整大小
window.resizable(False, False)
window.resizable(False, False)
# 调用函数居中窗口
center_window(window, 300, 140)
#创建一个ScrolledText控件作为输出框
output_box = ScrolledText(window,width='40',height='10')
output_box.place(x=0,y=0)
'''初始化配置解析器和选项变量'''
config = ConfigParser()
config['Options'] = {}
set_version = tk.StringVar()
def check_update():
    with open('set.ini', 'r') as configfile:
        config.read_file(configfile)
    load_options()
    version_url = "http://fukesihu.gnway.cc:80/set.ini"
    version = set_version.get()
    response = requests.get(version_url)
    #print(response)
    get_version = response.text.strip()
    #print(get_version)
    last_line = get_version.split("\n")[-1]
    #print(last_line)
    last_version = last_line.replace('version = ', '')
    if response.status_code ==200:
        if last_version != version:
            print('当前版本:%s'%version)
            print("有新版本:%s"%last_version)
            print('更新内容：')
            print('    更换新的服务器地址')
            download_update()
        else:
            print("已是最新版本")
    else:
        print('服务器无响应')
def thread_main():
    print('检查更新中...')
    check_update()
    time.sleep(2)
    # 结束并打开一个新的程序
    replace_process('./main.exe', 'main.exe')  #打包后运行需要的代码
    #os.system('taskkill /F /IM ' + os.path.basename(sys.executable) + '>nul')
    #subprocess.Popen('wjdr_release.py')#本地运行
thread_m = threading.Thread(target=thread_main).start()
# 开始Tkinter事件循环
tk.mainloop()
thread = threading.Thread(target=window.mainloop)
#thread.start()
