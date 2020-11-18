'''
表格布局
'''
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QGridLayout

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建表格布局
        grid = QGridLayout()
        self.setLayout(grid)

        # 按钮标签
        names = ['Cls', 'Bck', ' ', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+'
                 ]
        # 按钮位置
        positions = [(i,j) for i in range(5) for j in range(4)]

        # 创建按钮并添加到布局中

        for position,name in zip(positions,names):
            if name == '':
                continue

            # 创建按钮
            btn = QPushButton(name)
            # 将按钮添加到布局中
            grid.addWidget(btn,*position)

        self.move(300,15)
        self.setWindowTitle('计算器')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Example()
    sys.exit(app.exec_())




