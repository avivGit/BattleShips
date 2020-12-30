from message_manager import MessageManager
from game_elements import AttackResponse
from abc import abstractmethod

from tcp_client import TcpClient
from tcp_server import TcpServer
from consts import NetworkDetails


class Player:
    def __init__(self, socket_holder):
        self.socket_holder = socket_holder
        self.message_manager = MessageManager(self.socket_holder.get_client())
        self.user_handler = None
        self.now_playing = False
        self.game_over = False

    @abstractmethod
    def specific_pregame_routine(self):
        pass

    def pregame_routine(self):
        self.specific_pregame_routine()
        self.message_manager.send_ready()
        self.message_manager.recv_ready()

    def main_loop(self):
        while not self.game_over:
            if self.now_playing:
                self.attack()
            else:
                self.absorb()

    def attack(self):
        attack = self.user_handler.get_attack()
        self.message_manager.send_attack(attack)
        response = self.message_manager.recv_attack_response()
        if AttackResponse.FORFEIT == response:
            self.win()
            return

        if AttackResponse.MISS == response:
            self.now_playing = False

    def absorb(self):
        attack = self.message_manager.recv_attack()
        response = self.user_handler.absorb(attack)
        self.message_manager.send_attack_response(response)
        if AttackResponse.FORFEIT == response:
            self.lose()
            return

        if AttackResponse.MISS == response:
            self.now_playing = True

    def win(self):
        self.user_handler.notify_win()
        self.finish()

    def lose(self):
        self.user_handler.notify_lose()
        self.finish()

    def game_ended_before_started(self):
        self.user_handler.notify_ended_before_started()
        self.finish()

    def finish(self):
        self.socket_holder.close()
        self.game_over = True


class Player1(Player):
    def __init__(self):
        self.socket_holder = TcpServer('0.0.0.0', NetworkDetails.PORT)
        self.now_playing = True
        super().__init__(self.socket_holder)

    def specific_pregame_routine(self):
        ships = self.message_manager.recv_ships()
        self.user_handler.set_ships(ships)


class Player2(Player):
    def __init__(self):
        self.socket_holder = TcpClient(NetworkDetails.IP, NetworkDetails.PORT)
        self.now_playing = False
        super().__init__(self.socket_holder)

    def specific_pregame_routine(self):
        ships = self.user_handler.get_ships()
        self.message_manager.send_ships(ships)
