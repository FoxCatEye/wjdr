from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QToolTip
from PyQt5.QtGui import QIcon, QMouseEvent, QPixmap  # 导入 QPixmap
import sys


class ToolTipDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('ToolTip Demo')
        self.setGeometry(100, 100, 300, 200)

        # 创建带图标的标签
        icon = QIcon('icon/wenhao.png')
        pixmap = icon.pixmap(15, 15)  # 将 QIcon 转换为 QPixmap

        # 创建并初始化标签
        self.label = self._create_label(pixmap, 50, 50, "这是个提示文本", "点击提示内容\n四大行较好的")
        self.label_1 = self._create_label(pixmap, 150, 50, "这是个提示文本", "这是第二条\n四大行较好的")

    def _create_label(self, pixmap, x, y, hover_text, click_text):
        """
        创建并初始化一个带图标的标签，设置悬停提示和鼠标事件。

        :param pixmap: 图标对应的 QPixmap 对象
        :param x: 标签的 x 坐标
        :param y: 标签的 y 坐标
        :param hover_text: 悬停提示文本
        :param click_text: 点击提示文本
        :return: 初始化好的 QLabel 对象
        """
        label = QLabel(self)
        label.setPixmap(pixmap)
        label.setGeometry(x, y, 64, 64)

        # 设置悬停提示
        label.setToolTip(hover_text)
        label.setToolTipDuration(5000)  # 提示显示5秒

        # 绑定鼠标事件
        def show_tooltip(event):
            if event.buttons() == Qt.LeftButton:
                QToolTip.showText(event.globalPos(), click_text, label)
            else:
                QToolTip.hideText()

        label.mousePressEvent = show_tooltip
        label.mouseMoveEvent = show_tooltip


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ToolTipDemo()
    ex.show()
    sys.exit(app.exec_())