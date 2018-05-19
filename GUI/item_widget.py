from PyQt5.QtWidgets import *


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
        self.off_button.clicked.connect(self.switch_off)
        self.rb_layout.addWidget(self.off_button, 0, 0)

        self.on_button = QRadioButton("ON")
        self.on_button.clicked.connect(self.switch_on)
        self.rb_layout.addWidget(self.on_button, 0, 1)

    def __init_layout(self):
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.item_label)
        self.layout.addLayout(self.rb_layout)
        self.setLayout(self.layout)

    def switch_on(self):
        self.on_button.setChecked(True)
        self.item.state = True
        self.item.send_to_socket()

    def switch_off(self):
        self.off_button.setChecked(True)
        self.item.state = False
        self.item.send_to_socket()



