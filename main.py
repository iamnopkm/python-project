from Gui import GUI, BasicColors
from Ui import MainScreen, Navbar, ProductScreen, CustomerScreen
from Operations import ShopController

class ManagementApp(GUI):
    def __init__(self):
        """Initialize GUi"""
        self.shopController = ShopController()
        super().__init__(
            "mobile shop management system",
            resizable=(True, True), 
            geometry="900x750",
            icon="./Image/mobile_store.png",
            on_close=self.shopController.quit
        )

        self.init_navbar(Navbar(self, 
            [
                ("home", "Home"), 
                ("product", "Product"),
                ("customer", "Customer")
            ],
            self.change_screen
        ))
        self.add_screen("home", MainScreen(self))
        self.add_screen("product", ProductScreen(self, self.shopController))
        self.add_screen("customer", CustomerScreen(self, self.shopController))

        self.show_screen("home")

        
if __name__ == "__main__":
    m = ManagementApp()
    m.mainloop()