from PyQt5.QtWidgets import *


class RoomsWidget(QWidget):
    def __init__(self, parent):
        super(RoomsWidget, self).__init__(parent)
        horizontal_layout = QHBoxLayout()
        rooms_button = QPushButton("Rooms")
        search_button = QPushButton("Search")
        horizontal_layout.addWidget(rooms_button)
        horizontal_layout.addWidget(search_button)
        content_frame = QFrame()
        vertical_layout = QVBoxLayout()
        vertical_layout.addLayout(horizontal_layout)
        vertical_layout.addWidget(content_frame)
        self.setLayout(vertical_layout)
