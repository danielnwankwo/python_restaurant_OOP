# create a menu
# create a program that helps a waiter with his menu and his orders.



# Summary

- Now that we've created had some time to use our lists, time to make something more useful.

- You are going to make a program that helps a waiter with his menu and his orders.

- See tasks for the user stories.




# Task
## User Stories

###1
# AS a User I want to be able to see the menu in a formated way, so that I can order my meal.

###2
# AS a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten

###3
# As a user, I want to have my order read back to me in formated way so I know what I ordered.

# Acceptance Criteria

- its own project on your laptop and Github
- be git tracked
- have 5 commits mininum!
- has documentation
- follows best practices


# Step 1 - create the class for menu 

# create menu class and initialise. create the attribute


```
class Menu:
    def __init__(self):
        self.Menu = {"chicken Breast": 12.00, "Pork Chops": 18.00, "Seafood": 9.00, "Fried Rice": 18.00, "Steak": 20.00, "Coca Cola": 1.20, "Fanta": 1.50}
```
  
  
  
 # create and define the function for displaying the menu for the customer 
    
    
    
```    
    def menu_display(self):
        for key, val in self.Menu.items():
            print(key + ": " + str(val)) 
```
  
  
  
  
  

# create the object for the class


```
object_menu = Menu()  
``` 
  
# print

```
print(object_menu.menu_display())  
```
  
# Step create the class for the waiter to take order by inheriting the menu class (codes are in file)

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  