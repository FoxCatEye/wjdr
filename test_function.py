import sys
import ctypes
from PyQt5.QtWidgets import (QApplication, QMainWindow, QSystemTrayIcon, QAction, QMenu, QMessageBox)
from PyQt5.QtGui import QIcon


class Win11TrayApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Windows 应用标识设置（Win11必须）
        self.appid = 'com.yourcompany.yourapp.1.0'  # 需要唯一标识
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(self.appid)

        # 主窗口初始化
        self.setWindowTitle('Win11 托盘演示')
        self.setGeometry(300, 300, 400, 200)

        # 系统托盘初始化
        self.init_tray()

        # 初始显示
        self.show()

    def init_tray(self):
        """初始化系统托盘组件"""
        # 加载图标（推荐使用ICO格式）
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("app_icon.ico"))  # 准备一个Win11风格的ico文件

        # 创建上下文菜单（适配Win11圆角风格）
        self.tray_menu = QMenu()
        self.tray_menu.setStyleSheet("""
            QMenu {
                background-color: #f3f3f3;
                border-radius: 6px;
                padding: 8px;
                border: 1px solid #e0e0e0;
            }
            QMenu::item {
                padding: 8px 24px 8px 16px;
                color: #202020;
            }
            QMenu::item:selected {
                background-color: #e8f0fe;
                border-radius: 4px;
                color: #1967d2;
            }
        """)

        # 菜单项
        show_action = QAction(QIcon("show.ico"), "显示主窗口", self)
        exit_action = QAction(QIcon("exit.ico"), "退出程序", self)

        # 连接信号
        show_action.triggered.connect(self.show_normal)
        exit_action.triggered.connect(self.clean_exit)

        # 构建菜单
        self.tray_menu.addAction(show_action)
        self.tray_menu.addSeparator()
        self.tray_menu.addAction(exit_action)

        # 设置托盘属性
        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.activated.connect(self.tray_activated)
        self.tray_icon.show()

    def tray_activated(self, reason):
        """处理托盘交互（适配Win11点击行为）"""
        if reason == QSystemTrayIcon.DoubleClick:
            self.show_normal()
        elif reason == QSystemTrayIcon.Trigger:
            pass  # Win11单击通常不处理，保持与系统一致

    def show_normal(self):
        """Win11风格窗口显示"""
        if self.isMinimized():
            self.showNormal()
        self.show()
        self.activateWindow()
        self.raise_()

    def clean_exit(self):
        """安全退出"""
        self.tray_icon.hide()
        self.close()
        QApplication.quit()

    def closeEvent(self, event):
        """Win11关闭处理（最小化到托盘）"""
        event.ignore()
        self.hide()
        # Win11风格通知
        self.tray_icon.showMessage("后台运行中", "程序仍在系统托盘继续运行", QSystemTrayIcon.Information, 2000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)  # 重要：避免关闭最后一个窗口退出程序

    # 设置应用图标（Win11需要）
    app.setWindowIcon(QIcon("app_icon.ico"))

    window = Win11TrayApp()
    sys.exit(app.exec_())
