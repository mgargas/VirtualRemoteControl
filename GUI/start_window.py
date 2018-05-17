from GUI.start_widget import StartWidget
from GUI.rooms_widget import RoomsWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys
import os


class StartWindow(QMainWindow):

    def __init__(self, parent=None):
        super(StartWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.resize(500, 600)
        self.setWindowTitle('Virtual Remote Control')
        self.setWindowIcon(QIcon('remote_control.png'))
        self.center()
        start_widget = StartWidget(self)
        layout = QVBoxLayout()
        layout.addWidget(start_widget)
        self.setCentralWidget(start_widget)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


def main():
    app = QApplication(sys.argv)
    win = StartWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()