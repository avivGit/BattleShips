import socket


class TcpClient:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.client = None

    def get_client(self):
        self.close()
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.ip, self.port))
        return self.client

    def close(self):
        if self.client:
            self.client.close()
