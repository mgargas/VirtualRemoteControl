from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from GUI.main_page_widget import MainPageWidget


class StartWidget(QWidget):
    def __init__(self, parent, rooms):
        super(StartWidget, self).__init__(parent)
        self.rooms = rooms
        self.parent = parent
        self.title = QLabel()
        self.title.setText("Virtual Remote Control")
        self.title.setAlignment(Qt.AlignCenter)
        self.picture_label = QLabel(self)
        self.pix_map = QPixmap("remote_control.png")
       # self.pix_map = self.pix_map.scaled(400, 400, Qt.KeepAspectRatio)
        self.picture_label.setPixmap(self.pix_map)
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_button_on_click)
        self.set_layout()

    def start_button_on_click(self):
        if not hasattr(self, 'start_widget'):
            print("kepasa")
            self.main_page_widget = MainPageWidget(self.parent, rooms=self.rooms)
        self.parent.setCentralWidget(self.main_page_widget)
        self.main_page_widget.show()

    def set_layout(self):
        self.layout = QVBoxLayout()
        self.layout.setSpacing(10)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.picture_label)
        self.layout.addWidget(self.start_button)
        self.setLayout(self.layout)