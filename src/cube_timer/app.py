from textual.app import App, ComposeResult
from textual.widgets import Footer, Header


class Timer(App[object]):
    BINDINGS = [("d", "dnf", "DNF"), ("p", "plus_two", "+2")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

    def action_dnf(self) -> None:
        pass

    def action_plus_two(self) -> None:
        pass
