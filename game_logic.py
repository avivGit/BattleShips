from game_elements import AttackResponse


class GameLogic:
    def __init__(self):
        self.player = None
        self.num_ships_to_destroy = 0
        self.player_destroyed_ships = 0
        self.enemy_destroyed_ships = 0

        self.attacker_actions = {
            AttackResponse.MISS: self.attacker_miss,
            AttackResponse.HIT: self.attacker_hit,
            AttackResponse.HIT_AND_DESTROY: self.attacker_hit_and_destroy,
            AttackResponse.FORFEIT: self.attacker_forfeit
        }
        self.attacked_action = {
            AttackResponse.MISS: self.attacked_miss,
            AttackResponse.HIT: self.attacked_hit,
            AttackResponse.HIT_AND_DESTROY: self.attacked_hit_and_destroy,
            AttackResponse.FORFEIT: self.attacked_forfeit
        }

    def set_player(self, player):
        self.player = player

    def set_ships(self, ships):
        self.num_ships_to_destroy = len(ships)

    def attacker_miss(self):
        self.player.now_playing = False

    def attacker_hit(self):
        pass

    def attacker_hit_and_destroy(self):
        self.destroy_enemy_ship()

    def attacker_forfeit(self):
        self.player.win()

    def attacked_miss(self):
        self.player.now_playing = True

    def attacked_hit(self):
        pass

    def attacked_hit_and_destroy(self):
        self.destroy_player_ship()

    def attacked_forfeit(self):
        self.player.lose()

    def check_response_attacker(self, response):
        self.attacker_actions[response]()

    def check_response_attacked(self, response):
        self.attacked_action[response]()

    def destroy_enemy_ship(self):
        self.enemy_destroyed_ships += 1
        if self.enemy_destroyed_ships >= self.num_ships_to_destroy:
            self.player.win()

    def destroy_player_ship(self):
        self.player_destroyed_ships += 1
        if self.player_destroyed_ships >= self.num_ships_to_destroy:
            self.player.lose()
