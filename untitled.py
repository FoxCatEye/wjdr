import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fixed Size Window")
        self.setFixedSize(600, 400)  # 设置固定大小

        # 创建一个QWidget作为中心控件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 创建布局
        layout = QVBoxLayout()  # 使用垂直布局
        layout.addWidget(QPushButton("Button 1"))
        layout.addWidget(QPushButton("Button 2"))
        layout.addWidget(QPushButton("Button 3"))

        # 设置布局到QWidget
        central_widget.setLayout(layout)

    def resizeEvent(self, event):
        # 重写resizeEvent，使得窗口大小保持固定
        self.setFixedSize(self.width(), self.height())
        super().resizeEvent(event)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())