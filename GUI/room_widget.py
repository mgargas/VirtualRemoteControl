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
        self.init_layout()
        print("eldddd")

    def init_layout(self):
        self.layout = QVBoxLayout()
        for item in self.items:
            self.layout.addWidget(item)
        self.setLayout(self.layout)
