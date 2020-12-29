from attack_position_element import AttackPositionElement
from uint8_element import UInt8Element
from ships_element import ShipsElement
from consts import PreGameConsts


class MessageManager:
    def __init__(self, client):
        self.client = client

    def send_ships(self, ships):
        num_ships = len(ships)
        message = UInt8Element.serialize(num_ships) + ShipsElement.serialize(ships)
        self.client.send(message)

    def recv_ships(self):
        num_ships = UInt8Element.deserialize(self.client.recv(1))
        ships = ShipsElement.deserialize(self.client.recv(num_ships))
        return ships

    def send_ready(self):
        self.client.send(UInt8Element.serialize(PreGameConsts.READY))

    def recv_ready(self):
        return UInt8Element.deserialize(self.client.recv(1)) == PreGameConsts.READY

    def send_attack(self, attack_position):
        self.client.send(AttackPositionElement.serialize(attack_position))

    def recv_attack(self):
        return AttackPositionElement.deserialize(self.client.recv(1))

    def send_attack_response(self, response):
        self.client.send(UInt8Element.serialize(response))

    def recv_attack_response(self):
        return UInt8Element.deserialize(self.client.recv(1))

    def close(self):
        self.client.close()
