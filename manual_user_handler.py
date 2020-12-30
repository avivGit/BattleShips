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
            x = int(input("enter ship size\n"))
            if not x:
                break
            ships.append(Ship(size=x))
        return ships

    @staticmethod
    def get_attack():
        print("enter attack position")
        i,j = map(int,input().split())
        return AttackPosition(i,j)

    @staticmethod
    def absorb(attack_position):
        print(attack_position)
        print("enter response")
        response = int(input())
        return response

    @staticmethod
    def notify_win():
        print("you won!")

    @staticmethod
    def notify_lose():
        print("you lose!")

    @staticmethod
    def notify_ended_before_started():
        print("never started")
