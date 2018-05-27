from GUI.start_widget import StartWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class StartWindow(QMainWindow):

    def __init__(self, rooms, parent=None):
        super().__init__(parent)
        self.rooms = rooms
        self.initUI()

    def initUI(self):
        self.resize(500, 600)
        self.setWindowTitle('Virtual Remote Control')
        self.setWindowIcon(QIcon('Resources/remote_control_icon.png'))
        self.__center()
        self.__set_start_widget()
        self.__init_menu_bar()
        self.show()

    def __center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def __set_start_widget(self):
        self.start_widget = StartWidget(self, rooms=self.rooms)
        layout = QVBoxLayout()
        layout.addWidget(self.start_widget)
        self.setCentralWidget(self.start_widget)

    def __init_menu_bar(self):
        menu = self.menuBar()
        self.menu_bar = menu.addMenu("Options")

        switch_all_on = QAction("Switch all on", self)
        switch_all_on.setShortcut("Ctrl+N")
        switch_all_on.triggered.connect(self.start_widget.main_page_widget.switch_all_on)
        self.menu_bar.addAction(switch_all_on)

        switch_all_off = QAction("Switch all off", self)
        switch_all_off.setShortcut("Ctrl+F")
        switch_all_off.triggered.connect(self.start_widget.main_page_widget.switch_all_off)
        self.menu_bar.addAction(switch_all_off)

        exit_action = QAction('&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(qApp.quit)
        self.menu_bar.addAction(exit_action)


    def closeEvent(self, event):
        quit_msg = "Are you sure you want to exit the remote control?"
        reply = QMessageBox.question(self, 'Message',
                                           quit_msg, QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

