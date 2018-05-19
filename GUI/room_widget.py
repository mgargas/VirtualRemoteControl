from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from GUI.item_widget import ItemWidget


class RoomWidget(QWidget):
    def __init__(self, room):
        super(RoomWidget, self).__init__()
        self.room = room
        self.room_label = QLabel(room.name)
        self.items = [ItemWidget(item) for item in room.items]
        self.__init_on_off_buttons()
        self.__init_layout()

    def __init_on_off_buttons(self):
        self.all_on_button = QPushButton("ALL ON")
        self.all_on_button.clicked.connect(lambda: self.change_all_items_state(state=True))
        self.all_off_button = QPushButton("ALL OFF")
        self.all_off_button.clicked.connect(lambda: self.change_all_items_state(state=False))

    def __init_layout(self):
        self.layout = QVBoxLayout()
        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.addWidget(self.all_on_button)
        self.buttons_layout.addWidget(self.all_off_button)
        self.layout.addWidget(self.room_label, alignment=Qt.AlignCenter)
        self.layout.addLayout(self.buttons_layout)
        for item in self.items:
            self.layout.addWidget(item)
        self.setLayout(self.layout)

    def change_all_items_state(self, state):
        for item in self.items:
            if state:
                item.switch_on()
            else:
                item.switch_off()
