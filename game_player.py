from message_manager import MessageManager
from game_elements import AttackResponse


class Player:
    def __init__(self, message_manager: MessageManager, player1=True):
        self.message_manager = message_manager
        self.user_handler = None
        self.now_playing = player1
        self.player1 = player1
        self.game_over = False

    def player1_pregame_routine(self):
        ships = self.message_manager.recv_ships()
        self.user_handler.set_ships(ships)

    def player2_pregame_routine(self):
        ships = self.user_handler.get_ships()
        self.message_manager.send_ships(ships)

    def pregame_routine(self):
        if self.player1:
            self.player1_pregame_routine()
        else:
            self.player2_pregame_routine()

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
        response = self.user_handler.attack(attack)
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
        self.message_manager.close()
        self.game_over = True
