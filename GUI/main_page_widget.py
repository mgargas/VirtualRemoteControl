from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from GUI.room_widget import RoomWidget


class MainPageWidget(QWidget):
    def __init__(self, parent, rooms):
        super(MainPageWidget, self).__init__(parent)
        self.rooms = rooms
        self.parent = parent
        self.room_widgets = [RoomWidget(room) for room in self.rooms]
        self.title_label = QLabel("Virtual Remote Control")
        self.select_room = QComboBox()
        self.scroll_area = QScrollArea()
        self.scroll_widget = QWidget()

        self.scroll_widget_layout = QVBoxLayout()
        for room_widget in self.room_widgets:
            self.scroll_widget_layout.addWidget(room_widget)
        self.scroll_widget.setLayout(self.scroll_widget_layout)
        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_area.setWidgetResizable(True)
        self.select_room.addItems(['ALL'] + [room.name for room in self.rooms])

        self.select_room.activated[str].connect(self.on_activated)
        self.init_layout()

    def on_activated(self, text):
        for room in self.room_widgets:
            if room.room.name == text or text == 'ALL':
                room.show()
            else:
                room.hide()


    def init_layout(self):
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.title_label)
        vertical_layout.addWidget(self.select_room)
        vertical_layout.addWidget(self.scroll_area)
        self.setLayout(vertical_layout)
