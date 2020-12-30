import socket


class TcpServer:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.current_client = None
        self.start_server()

    def start_server(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind((self.ip, self.port))
        self._socket.listen(5)

    def get_client(self):
        self.current_client, _ = self._socket.accept()
        return self.current_client

    def close(self):
        if self.current_client:
            self.current_client.close()
        self._socket.close()
