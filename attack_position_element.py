from collections import namedtuple
from uint8_element import UInt8Element

AttackPosition = namedtuple('AttackPosition', ['i', 'j'])


class AttackPositionElement:
    base = 16

    @staticmethod
    def serialize(position: AttackPosition):
        position_as_number = AttackPositionElement.base * position.i + position.j
        return UInt8Element.serialize(position_as_number)

    @staticmethod
    def deserialize(bytes_content):
        position_as_number = UInt8Element.deserialize(bytes_content)
        return AttackPosition(i=position_as_number // AttackPositionElement.base,
                              j=position_as_number % AttackPositionElement.base)
