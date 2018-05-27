import yaml
import os
from Model.room import Room
from Model.item import Item
from GUI.start_window import StartWindow
from PyQt5.QtWidgets import *
import sys


def parse_yaml(file):
    data = []
    with open(file, 'r') as stream:
        try:
            data = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    return sorted([Room([(k, v) for (k, v) in room if not v][0][0], sorted([Item(id, description) for id, description in room if description]))
                   for room in map(lambda x: list(x.items()), data)])


def main():
    rooms = parse_yaml(os.path.dirname(__file__) + "/configuration.yaml")
    app = QApplication(sys.argv)
    win = StartWindow(rooms)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()