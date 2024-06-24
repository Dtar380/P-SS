########################################
#####  CODE                        #####
########################################

#####  FUNCTIONS

def cPrint(text: str, text_color: tuple = None, background_color: tuple = None) -> None:

    """
    Prints a given text with a given color.\n
    Colors must be stated in RGB values inside a tuple.\n
    If no colors passed, it will work as a normal print
    """

    if text_color:
        text_color: str = f'\033[38;2;{text_color[0]};{text_color[1]};{text_color[2]}m'
    else:
        text_color: str = ''

    if background_color:
        background_color: str = f'\033[48;2;{background_color[0]};{background_color[1]};{background_color[2]}m'
    else:
        background_color: str = ''

    print(text_color + background_color + text + '\033[0m')

cPrint('YES')