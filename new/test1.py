import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('config.ui', self)
        self.read_config()
        self.show()

    def read_config(self):
        # 假设已经有了get_config函数来读取配置文件
        config = get_config('config.ini')
        # 根据配置文件中的选项来设置界面上的复选框
        self.checkBox_1.setChecked(config.getboolean('options', 'option_1'))
        self.checkBox_2.setChecked(config.getboolean('options', 'option_2'))  # ... 设置其他选项


def get_config(config_path):
    # 这里应该是读取配置文件的逻辑，返回一个配置对象
    # 为了示例，这里使用一个虚构的get_config函数
    return MockConfig()


class MockConfig:
    def getboolean(self, section, option):
        # 根据section和option返回一个布尔值
        # 这里的逻辑应该是从配置文件中读取值
        return option == 'option_1'  # 假设option_1是存在的


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())