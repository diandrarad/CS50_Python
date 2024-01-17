import pyfiglet
import random
import sys


def get_font(argv):
    if len(argv) == 1:
        return random.choice(pyfiglet.FigletFont.getFonts())
    elif len(argv) == 3 and (argv[1] ==  '-f' or argv[1] == '--font'):
        font_name = argv[2]
        if font_name in pyfiglet.FigletFont.getFonts():
            return font_name
    sys.exit('Invalid usage')


def main(argv):
    font = get_font(argv)
    text = input('Input: ')
    figlet = pyfiglet.Figlet(font=font)
    print(figlet.renderText(text))


if __name__ == '__main__':
    main(sys.argv)