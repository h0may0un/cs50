
from pyfiglet import Figlet
import sys
import random
def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    if len(sys.argv) not in [1,3]:
        sys.exit('invalid number of arguments')
    if len(sys.argv) == 1:
        font = random.choice(fonts)
    else:
        if sys.argv[1] != '-f' and sys.argv[1] != '--font':
            sys.exit('invalid argument : '+sys.argv[1])
        if sys.argv[2] not in fonts:
            sys.exit('font not found')
        font = sys.argv[2]
    figlet.setFont(font=font)
    print(figlet.renderText(input('type something: ')))
main()
