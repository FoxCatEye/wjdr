def start_exe():
    while True:
        try:
            print('开始启动雷电模拟器')
            #subprocess.Popen('E:\leidian\LDPlayer9\dnplayer.exe')
            subprocess.Popen('%s' % set_address.get())
            print('启动成功')
            break
        except:
            print_space('未找到模拟器，5s后重新尝试启动')
            time.sleep(5)