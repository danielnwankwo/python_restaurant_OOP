
class Menu:
    def __init__(self):
        self.Menu = {"chicken Breast": "12.00", "Pork Chops": "18.00", "Seafood": "9.00", "Fried Rice": "18.00", "Steak": "20.00", "Coca Cola": "1.20", "Fanta": "1.50"}
        # self.menu = ["chicken breast", "seafood", "pork chops", "steak", "fried rice", "coke", "fanta"]




    def menu_display(self):
        for key, val in self.Menu.items():
            print(key + ": " + val)




object_menu = Menu()

# print(object_menu.menu)

print(object_menu.menu_display())

