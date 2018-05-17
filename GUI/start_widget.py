from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from GUI.rooms_widget import RoomsWidget


class StartWidget(QWidget):
    def __init__(self, parent):
        super(StartWidget, self).__init__(parent)
        self.__mainWindow = parent
        title = QLabel()
        title.setText("Virtual Remote Control")
        title.setAlignment(Qt.AlignCenter)
        start_button = QPushButton("Start")
        start_button.clicked.connect(self.start_button_on_click)
        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addWidget(start_button)
        self.setLayout(layout)

    def start_button_on_click(self):
        if not hasattr(self, 'start_widget'):
            self.start_widget = RoomsWidget(self.__mainWindow)
        self.start_widget.show()