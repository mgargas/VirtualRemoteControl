from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from GUI.room_widget import RoomWidget
import re


class MainPageWidget(QWidget):
    def __init__(self, parent, rooms):
        super(MainPageWidget, self).__init__(parent)
        self.rooms = rooms
        self.parent = parent
        self.room_widgets = [RoomWidget(room) for room in self.rooms]
        self.__init_title_label()
        self.__init_buttons()
        self.__init_search_line()
        self.__init_select_room_combobox()
        self.__init_scroll_area()
        self.__init_layout()

    def __init_title_label(self):
        self.title_label = QLabel("Virtual Remote Control")
        self.title_label.setAlignment(Qt.AlignCenter)

    def __init_buttons(self):
        self.rooms_button = QPushButton("ROOMS")
        self.rooms_button.clicked.connect(self.rooms_button_clicked)
        self.search_button = QPushButton("SEARCH")
        self.search_button.clicked.connect(self.search_button_clicked)

    def __init_search_line(self):
        self.search_line = QLineEdit()
        self.search_line.hide()
        self.search_line.textChanged[str].connect(self.update_search_results)

    def __init_select_room_combobox(self):
        self.select_room = QComboBox()
        self.select_room.addItems(['ALL'] + [room.name for room in self.rooms])
        self.select_room.activated[str].connect(self.show_selected_room)

    def __init_scroll_area(self):
        self.scroll_area = QScrollArea()
        self.scroll_widget = QWidget()
        self.scroll_widget_layout = QVBoxLayout()
        for room_widget in self.room_widgets:
            self.scroll_widget_layout.addWidget(room_widget)
        self.scroll_widget.setLayout(self.scroll_widget_layout)
        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_area.setWidgetResizable(True)

    def __init_layout(self):
        vertical_layout = QVBoxLayout()
        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.addWidget(self.rooms_button)
        self.buttons_layout.addWidget(self.search_button)
        vertical_layout.addWidget(self.title_label)
        vertical_layout.addLayout(self.buttons_layout)
        vertical_layout.addWidget(self.select_room)
        vertical_layout.addWidget(self.search_line)
        vertical_layout.addWidget(self.scroll_area)
        self.setLayout(vertical_layout)

    def show_selected_room(self, text):
        for room in self.room_widgets:
            if room.room.name == text or text == 'ALL':
                room.show()
                for item in room.items:
                    item.show()
            else:
                room.hide()

    def search_button_clicked(self):
        self.search_line.show()
        self.select_room.hide()
        self.update_search_results(text=self.search_line.text())

    def rooms_button_clicked(self):
        self.search_line.hide()
        self.select_room.show()
        self.show_selected_room(text=self.select_room.currentText())

    def update_search_results(self, text):
        for room in self.room_widgets:
            if re.search(text, room.room.name, re.IGNORECASE):
                room.show()
                for item in room.items:
                    item.show()
            else:
                counter = 0
                for item in room.items:
                    if re.search(text, item.item.description, re.IGNORECASE):
                        item.show()
                        counter += 1
                    else:
                        item.hide()
                if counter > 0:
                    room.show()
                else:
                    room.hide()

    def show_all_rooms(self):
        for room in self.room_widgets:
            room.show()
            for item in room.items:
                item.show()

    def switch_all_on(self):
        for room in self.room_widgets:
            room.change_all_items_state(True)

    def switch_all_off(self):
        for room in self.room_widgets:
            room.change_all_items_state(False)