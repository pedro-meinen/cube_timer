"""
Implementação minima de um algoritimo de geração de embaralhamento de cubo magico
"""

from random import choice

NORMAL_MOVES = "R", "L", "U", "D", "F", "B"
PRIME_MOVES = "R'", "L'", "U'", "D'", "F'", "B'"
DOBLE_MOVES = "R2", "L2", "U2", "D2", "F2", "B2"

MOVESETS = NORMAL_MOVES, PRIME_MOVES, DOBLE_MOVES


def parse_move(move: str) -> tuple[str, str]:
    move_direction, move_type = move[0], move[-1]

    if move_direction == move_type:
        move_type = ""

    return move_direction, move_type


def check_move(current_move: str, last_move: str | None) -> str | None:
    if not last_move:
        return current_move

    current_move_direction, current_move_type = parse_move(current_move)
    last_move_direction, last_move_type = parse_move(last_move)

    if last_move_direction != current_move_direction:
        return current_move
    if (last_move_type == "" and current_move_type == "'") or (
        last_move_type == "'" and current_move_type == ""
    ):
        return None
    if last_move_type == current_move_type:
        return current_move_direction + "2"
    if (last_move_type == "'" and current_move_type == "2") or (
        last_move_type == "2" and current_move_type == "'"
    ):
        return current_move_direction
    return current_move


def generate_scramble() -> str:
    scramble: list[str] = []

    while len(scramble) < 20:
        current_moveset = choice(MOVESETS)
        move = choice(current_moveset)

        try:
            last_move = scramble[-1]
        except IndexError:
            last_move = None

        actual_move = check_move(move, last_move)

        if not actual_move:
            continue

        scramble.append(actual_move)

    return ", ".join(scramble)


def main() -> None:
    for _ in range(100):
        scramble = generate_scramble()
        print(scramble)


if __name__ == "__main__":
    main()
