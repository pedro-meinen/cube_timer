from .app import Timer
from .scrambler import generate_scramble


def main() -> None:
    scramble = generate_scramble()
    print(scramble)

    app = Timer()
    app.run()
