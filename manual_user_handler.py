from game_elements import Ship, AttackPosition, AttackResponse


class ManualUserHandler:
    @staticmethod
    def set_ships(ships):
        for ship in ships:
            print(ship, end=',')
        print()

    @staticmethod
    def get_ships():
        ships = []
        while True:
            x = input("enter ship size\n")
            if not x.isdigit():
                break
            x = int(x)
            if x <= 0:
                break
            ships.append(Ship(size=x))
        return ships

    @staticmethod
    def get_attack():
        print("enter attack position")
        i, j = map(int, input().split())
        return AttackPosition(i, j)

    @staticmethod
    def absorb(attack_position):
        print(attack_position)
        print("enter response")
        response = int(input())
        return response

    @staticmethod
    def notify_response(response):
        print({AttackResponse.MISS: "Miss", AttackResponse.HIT: "Hit", AttackResponse.HIT_AND_DESTROY: "Destroy",
               AttackResponse.FORFEIT: "FF"}.get(response, "Unknown"))

    @staticmethod
    def notify_win():
        print("you win!")

    @staticmethod
    def notify_lose():
        print("you lose!")

    @staticmethod
    def notify_ended_before_started():
        print("never started")
