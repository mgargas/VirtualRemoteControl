import locale
from socket import *


class Item:

    def __init__(self, id, description, state=False):
        self.id = id
        self.description = description
        self.state = state

    def __lt__(self, other):
        return locale.strxfrm(self.description) < locale.strxfrm(other.description)

    def send_to_socket(self):
        message = ("on " if self.state else "off ") + self.id
        udp_sock = socket(AF_INET, SOCK_DGRAM)
        udp_sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        udp_sock.sendto(message.encode('utf8'), ("255.255.255.255", 2018))
        udp_sock.close()

