import colorama
from colorama import Fore

colorama.init(autoreset=True)
colors = dict(enumerate(sorted(Fore.__dict__.keys())))


def display_colors() -> None:
    for i in colors:
        print(str(i) + ". " + colors[i])