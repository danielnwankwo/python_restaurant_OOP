from restaurant_OOP import Menu

class Waiter(Menu): # create waiter function and initialise and let it inherit menu
    def __init__(self):
        super().__init__()



# create a function to allow the coustmer (user) to make an order
    def order(self):

        order_list = []   # create an empty list which will take the order of the customer

        customer_order = True # boolean statement for th while loop so if the customer is ordering then the loop begins

# while loop to handle taking the order and creating the list
        while customer_order:

            customer_input = input("What will you be having? ")  # the customer will now begin to respond to the prompt to begin the order

            if customer_input in self.Menu.keys():  # if statement for if the order not price (key) is on the menu then add to list

                order_list.append(customer_input)

                continue # continue until either blank is returned or something out of scope is said then break
            else:

                break



        return order_list    # returns the newly created list







customer_1 = Waiter()
print(customer_1.order())
