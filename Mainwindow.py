from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPainter, QColor, QPalette
from PyQt5 import QtGui, QtWidgets
import sys


class Ges(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建按钮
        startbutn = QPushButton('开始创作')
        hisworkbutn = QPushButton('我的作品')
        settingbutn = QPushButton('设置')
        helpbutn = QPushButton('教程')
        quitbutn = QPushButton('退出')
        # 为按钮添加功能
        startbutn.clicked.connect(self.changeWindow)
        hisworkbutn.clicked.connect(self.hisworkWindow)
        settingbutn.clicked.connect(self.settingWindow)
        helpbutn.clicked.connect(self.helpWindow)
        quitbutn.clicked.connect(self.close)
        # 设置按钮外观
        startbutn.setFixedSize(200, 50)
        hisworkbutn.setFixedSize(200, 50)
        settingbutn.setFixedSize(200, 50)
        helpbutn.setFixedSize(200, 50)
        quitbutn.setFixedSize(200, 50)

        myfont = QtGui.QFont('楷体', 18)
        myfont.setBold(True)
        startbutn.setFont(myfont)
        hisworkbutn.setFont(myfont)
        settingbutn.setFont(myfont)
        helpbutn.setFont(myfont)
        quitbutn.setFont(myfont)

            #设置背景图
        #quitbutn.setStyleSheet("QPushButton{border-image: url(butn3.png)}")

        """按钮透明
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0)
        quitbutn.setGraphicsEffect(op)
        """
        # 窗口布局
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(startbutn)
        vbox.addWidget(hisworkbutn)
        vbox.addWidget(settingbutn)
        vbox.addWidget(helpbutn)
        vbox.addWidget(quitbutn)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(vbox)

        self.setLayout(hbox)

        # 设置背景图片
        self.mysetBackImage()
        self.setFixedSize(1360, 768)  # 固定窗口大小
        self.setWindowTitle("Gesmuse")
        self.show()

    def mysetBackImage(self):
        mypalette = QtGui.QPalette()
        mypalette.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('MainBack.jpg')))
        self.setPalette(mypalette)

    # 跳转到创作页面
    def changeWindow(self):
        pass

    # 跳转到历史作品页面
    def hisworkWindow(self):
        pass

    def settingWindow(self):
        pass

    def helpWindow(self):
        pass




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ges = Ges()
    # ges.showFullScreen()
    sys.exit(app.exec_())
