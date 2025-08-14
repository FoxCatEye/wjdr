def task1(stop_event):
    while not stop_event.is_set():
        print("T1执行中...")
        # 第一步
        time.sleep(1)
        # 第二步
        time.sleep(0.8)
        # 第三步
        time.sleep(0.8)
        # 第四步
        time.sleep(0.8)
        # 第五步
        time.sleep(0.8)
        # 第六步
        time.sleep(0.8)
        # 第七步
        time.sleep(0.8)
    print("T1已停止")