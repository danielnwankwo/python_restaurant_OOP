# creat menu class and initialise. create the attribute
class Menu:
    def __init__(self):
        self.Menu = {"chicken Breast": 12.00, "Pork Chops": 18.00, "Seafood": 9.00, "Fried Rice": 18.00, "Steak": 20.00, "Coca Cola": 1.20, "Fanta": 1.50}
        # self.menu = ["chicken breast", "seafood", "pork chops", "steak", "fried rice", "coke", "fanta"]



# create and define the function for dsiplaying the menu for the customer




    def menu_display(self):
        for key, val in self.Menu.items():
            print(key + ": " + str(val))



# create the object for the class



object_menu = Menu()



# print the object

print(object_menu.menu_display())

