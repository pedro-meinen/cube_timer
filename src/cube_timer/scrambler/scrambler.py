from random import choice

from .generate import generate_moves
from .moves import Move

MOVESETS = generate_moves()


def _check_move(current_move: Move, last_move: Move | None) -> tuple[bool, Move | None]:
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

        try:
            last_move = scramble[-1]
        except IndexError:
            last_move = None

        new_move, actual_move = _check_move(move, last_move)

        if not actual_move:
            continue

        if new_move:
            scramble.append(actual_move)
        else:
            scramble[-1] = actual_move

    return ", ".join(str(m) for m in scramble)
