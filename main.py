import yaml
import os
from room import Room
from item import Item
from GUI.start_window import StartWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys

def parse_yaml(file):
    data = []
    with open(file, 'r') as stream:
        try:
            data = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    return sorted([Room(room[0][0], sorted([Item(id, description) for id, description in room[1:]]))
                   for room in map(lambda x: list(x.items()), data)])


def main():
    rooms = parse_yaml(os.path.dirname(__file__) + "/configuration.yaml")
    print([room.name for room in rooms])
    app = QApplication(sys.argv)
    win = StartWindow(rooms)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()