
from enum import Enum, auto


class Directions(Enum):
    rigth = auto()
    left = auto()
    up = auto()
    down = auto()


def move(direction):
    if not isinstance(direction, Directions):
        return ValueError('No move this direction')

    # pode pegar o direction.value tambem que vai ser o valor de fato dae
    return f'Moving {direction.name}'


print(move(Directions.rigth))
print(move(Directions.left))
print(move(Directions.up))
print(move('aaaaa'))
