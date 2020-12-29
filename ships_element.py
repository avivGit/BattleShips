from collections import namedtuple
from uint8_element import UInt8Element

Ship = namedtuple('Ship', ['size'])


class ShipsElement:
    @staticmethod
    def serialize(ships):
        return b''.join(UInt8Element.serialize(ship.size) for ship in ships)

    @staticmethod
    def deserialize(bytes_content):
        return [Ship(num) for num in bytes_content]
