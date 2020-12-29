class UInt8Element:
    length = 1
    byteorder = 'little'

    @staticmethod
    def serialize(raw_content):
        return raw_content.to_bytes(UInt8Element.length, UInt8Element.byteorder)

    @staticmethod
    def deserialize(bytes_content):
        return int.from_bytes(bytes_content,UInt8Element.byteorder)
