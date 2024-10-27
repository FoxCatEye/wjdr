# 打包windows程序
```pyinstaller --onefile \
  --icon='/Users/zhangjiuxing/PycharmProjects/Wjdr/new/log.png' \
  --add-data '/Users/zhangjiuxing/PycharmProjects/Wjdr/venv/bin/airtest:airtest' \
  '/Users/zhangjiuxing/PycharmProjects/Wjdr/new/coldmoon_cycle.py'
```

# 打包mac app程序
```
pyinstaller --onefile \
  --windowed \
  --icon='/Users/zhangjiuxing/PycharmProjects/Wjdr/new/log.png' \
  --add-data '/Users/zhangjiuxing/PycharmProjects/Wjdr/venv/bin/airtest:airtest' \
  '/Users/zhangjiuxing/PycharmProjects/Wjdr/new/coldmoon_cycle.py'
```
