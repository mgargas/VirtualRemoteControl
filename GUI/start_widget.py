from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from GUI.main_page_widget import MainPageWidget


class StartWidget(QWidget):
    def __init__(self, parent, rooms):
        super(StartWidget, self).__init__(parent)
        self.rooms = rooms
        self.parent = parent
        self.main_page_widget = MainPageWidget(self.parent, rooms=self.rooms)
        self.__init_title_label()
        self.__init_picture_label()
        self.__init_start_button()
        self.__init_layout()

    def __init_title_label(self):
        self.title = QLabel()
        self.title.setText("\nVIRTUAL REMOTE CONTROL\n Be the boss in your house!\n")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFrameShape(QFrame.Panel)
        self.title.setFrameShadow(QFrame.Sunken)
        self.title.setLineWidth(3)

    def __init_picture_label(self):
        self.picture_label = QLabel(self)
        self.pix_map = QPixmap("Resources/remote_control.png")
        self.picture_label.setPixmap(self.pix_map)

    def __init_start_button(self):
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_button_on_click)

    def __init_layout(self):
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.title)
        self.layout.addStretch()
        self.layout.addWidget(self.picture_label, alignment=Qt.AlignCenter)
        self.layout.addStretch()
        self.layout.addWidget(self.start_button)
        self.layout.addStretch()
        self.setLayout(self.layout)

    def start_button_on_click(self):
        self.parent.setCentralWidget(self.main_page_widget)
        self.main_page_widget.show()