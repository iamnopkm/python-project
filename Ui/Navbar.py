from Gui import Navbar as guiNav, BasicColors


class Navbar(guiNav):
    def __init__(self, master, links: list[tuple[str, str]], redirect_funtion):
        super().__init__(master, BasicColors.MAROON, links, BasicColors.WHITE, redirect_funtion)