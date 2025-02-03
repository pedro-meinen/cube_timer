"""
Implementação minima de um algoritimo de geração de embaralhamento de cubo magico
"""

from random import choice

from .moves import Move, generate_moves

MOVESETS = generate_moves()


def check_move(current_move: Move, last_move: Move | None) -> tuple[bool, Move | None]:
    if not last_move:
        return True, current_move

    if current_move.should_invert(last_move):
        return False, current_move.inverted_move

    if current_move.should_double(last_move):
        return False, current_move.doubled_move

    if current_move.should_skip(last_move):
        return False, None

    return True, current_move


def generate_scramble() -> str:
    scramble: list[Move] = []

    while len(scramble) < 20:
        current_moveset = choice(MOVESETS)
        move = choice(current_moveset)
        print(move)

        try:
            last_move = scramble[-1]
        except IndexError:
            last_move = None

        new_move, actual_move = check_move(move, last_move)

        if not actual_move:
            continue

        if new_move:
            scramble.append(actual_move)
        else:
            scramble[-1] = actual_move

    return ", ".join(str(m) for m in scramble)


def scramble() -> None:
    scramble = generate_scramble()
    print(scramble)
