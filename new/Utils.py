# 画面向左
from airtest.core.api import swipe


def swipe_left():
    swipe([100, 1200], [1000, 1200])


# 画面向右
def swipe_right():
    swipe([800, 800], [100, 800])


# 画面向下
def swipe_down():
    swipe([500, 1500], [500, 200])


# 画面向上
def swipe_up():
    swipe([500, 200], [500, 1500])
