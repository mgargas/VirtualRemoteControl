from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ItemWidget(QWidget):
    def __init__(self, item):
        super(ItemWidget, self).__init__()
        self.item = item
        self.item_label = QLabel(item.description)
        self.__init_radio_buttons()
        self.__init_layout()

    def __init_radio_buttons(self):
        self.rb_layout = QGridLayout()
        self.off_button = QRadioButton("OFF")
        self.off_button.setChecked(True)
        self.off_button.clicked.connect(self.on_click)
        self.rb_layout.addWidget(self.off_button, 0, 0)

        self.on_button = QRadioButton("ON")
        self.on_button.clicked.connect(self.on_click)
        self.rb_layout.addWidget(self.on_button, 0, 1)

    def on_click(self):
        if self.on_button.isChecked():
            self.item.state = True
            self.item.send_to_socket()
        else:
            self.item.state = False
            self.item.send_to_socket()

    def __init_layout(self):
        hbox = QHBoxLayout()
        hbox.addWidget(self.item_label)
        hbox.addLayout(self.rb_layout)
        self.setLayout(hbox)

