from .scrambler import generate_scramble


def main() -> None:
    scramble = generate_scramble()
    print(scramble)
