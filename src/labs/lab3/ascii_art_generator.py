import colorama
import pyfiglet
from colorama import Fore

colorama.init(autoreset=True)

fonts = dict(enumerate(sorted(pyfiglet.FigletFont.getFonts())))
colors = dict(enumerate(sorted(Fore.__dict__.keys())))


def display_fonts() -> None:
    for i in fonts:
        print(str(i) + ". " + fonts[i])


def display_colors() -> None:
    for i in colors:
        print(str(i) + ". " + colors[i])


def get_text(text, font, color_position, width) -> str:
    fig = pyfiglet.Figlet(font)
    fig.width = width
    formatted_text = fig.renderText(text)
    return Fore.__getattribute__(colors[color_position]) + formatted_text


def write_into_file(file_path, text) -> None:
    with open(file_path, "w") as file:
        file.write(text)


def read_from_file(file_path) -> str:
    with open(file_path, "r") as file:
        return file.read()


while True:
    try:
        initial_text = str(input("Enter text containing all ASCII characters in order to display: "))
        if not initial_text.isascii():
            print("Text must contain only ASCII characters")
            continue
        display_fonts()
        font_position = int(input("Enter position of font you would like to use: "))
        display_colors()
        color_position = int(input("Enter position of color you would like to use: "))
        width = int(input("Enter width of text you would like to display: "))
        modified_text = get_text(initial_text, fonts[font_position], color_position, width)
        print(modified_text)
        write_into_file("output.txt", modified_text)

        if input(
                "Would you like to continue? Enter 'Y' or 'y' if you do, or anything else if you don't. Your response is ").lower() == "y":
            continue
        else:
            break
    except ValueError as e:
        print("Cannot be parsed into int value")
    except KeyError:
        print("You have entered a wrong value for key of fonts or color")
    except pyfiglet.CharNotPrinted as e:
        print(str(e))
