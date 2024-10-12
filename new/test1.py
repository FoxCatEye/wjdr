from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPalette, QBrush, QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("背景图片示例")
        self.set_background_image('11(1).png')  # 替换为您的图片路径

    def set_background_image(self, image_path):
        # 设置窗口的背景图片
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap(image_path)))
        self.setPalette(palette)
    def toggle_checkbox(self):
        # 切换复选框的选中状态
        self.checkBox_help.setChecked(True)
        self.checkBox_XG.setChecked(True)
        self.checkBox_WM.setChecked(True)

self.select_stop.setVisible(False)

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPalette, QBrush, QPixmap

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MyApp()
    mainWindow.show()
    sys.exit(app.exec_())