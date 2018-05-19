from GUI.start_widget import StartWidget
from GUI.main_page_widget import MainPageWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class StartWindow(QMainWindow):

    def __init__(self, rooms, parent=None):
        super(StartWindow, self).__init__(parent)
        self.rooms = rooms
        self.initUI()

    def initUI(self):
        self.resize(500, 600)
        self.setWindowTitle('Virtual Remote Control')
        self.setWindowIcon(QIcon('remote_control.png'))
        self.center()
        self.set_start_widget()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def set_start_widget(self):
        self.start_widget = StartWidget(self, rooms=self.rooms)
        layout = QVBoxLayout()
        layout.addWidget(self.start_widget)
        self.setCentralWidget(self.start_widget)

