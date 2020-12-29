from collections import namedtuple

AttackPosition = namedtuple('AttackPosition', ['i', 'j'])
Ship = namedtuple('Ship', ['size'])

class AttackResponse:
    MISS = 1
    HIT = 2
    HIT_AND_DESTROY = 3
    FORFEIT = 0xFF


