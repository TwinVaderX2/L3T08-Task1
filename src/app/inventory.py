# This app is a simple inventory management system, using basic UI.

# Templates for classes and functions have been provided by Hyperiondev.com as part
# of the course task requirements.

# import libraries/modules
import os

#============== Create Classes =====================

class Shoe:
    
    def __init__(self,country,code,product,cost,qty):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.qty = qty
    
    # method to change country for item
    def change_country(self,country):
        self.country = country
        
    # method to change code for item    
    def change_code(self,code):
        self.code = code
    
    # method to change product description for item
    def change_product(self,product):
        self.product = product
    
    # method to change price for item
    def change_price(self,price):
        self.cost = price
    
    # method to change quantity of item
    def change_qty(self,qty):
        self.qty = qty

    # method to display as string
    def __str__(self):
        return f"Shoe information: Product code:{self.code}, Product description: {self.product}, Product quantity: {self.qty}"

class Inventory:
    
    def __init__(self):
        self.inventory_list = []

    def __str__(self):
        return f"{self.inventory_list}"
        
    # method to add item to inventory list
    def add_item(self,country,code,product,cost,qty):
        self.inventory_list.append(Shoe(country, code, product, cost, qty))
        
    # method to search for given country and return a list of index numbers
    def search_country(self,country):
        
        search_index = []
        
        for idx in self.inventory_list:
            if idx.country == country:
                search_index.append(self.inventory_list.index(idx))
       
        return search_index
    
    # method to search for given code and return a list of index numbers
    def search_code(self,code):
        
        search_index = []
        
        for idx in self.inventory_list:
            if idx.code == code:
                search_index.append(self.inventory_list.index(idx))
       
        return search_index
    
    # method to search for given product and return a list of index numbers
    def search_product(self,product):
        
        search_index = []
        
        for idx in self.inventory_list:
            if idx.product == product:
                search_index.append(self.inventory_list.index(idx))
       
        return search_index
    
    # method to create dictionary of product_codes and product_names
    def product_discription_dict(self):
        
        #create list of all codes in inventory
        code_list = []
        for idx in self.inventory_list:
            code_list.append(idx.code)
                
        # create a list of discription of all products discriptions in inventory
        discript_list = []
        for idx in self.inventory_list:
            discript_list.append(idx.product)
        # create a dictionary from two lists
        prod_discript_dict = dict(zip(code_list,discript_list))
        
        return prod_discript_dict
    
    # method to create dictionary of product_codes and product_prices
    def product_price_dict(self):
            
        #create list of all codes in inventory
        code_list = []
        for idx in self.inventory_list:
            code_list.append(idx.code)
                
        # create a list of all product prices in inventory
        price_list = []
        for idx in self.inventory_list:
            price_list.append(idx.cost)
            
        # create dictionary from two lists
        prod_price_dict = dict(zip(code_list,price_list))
        
        return prod_price_dict
    
    #method to create dictionary of product_codes and product_qty
    def product_qty_dict(self):
        
        #create list of all codes in inventory
        code_list = []
        for idx in self.inventory_list:
            code_list.append(idx.code)
            
        # create dictionary from two lists
        prod_qty_dict = dict.fromkeys(code_list,0)
        
        # if multiple entries for specified item, add qty totals
        for idx in self.inventory_list:
            prod_qty_dict[idx.code] = prod_qty_dict[idx.code]+idx.qty
        
        return prod_qty_dict
    
    # method to determine product with the highest stock_qty
    def highest_stock_on_hand(self):
        
        item_code = ""
        stock_val = 0
        
        for idx in self.inventory_list:
            if stock_val < idx.qty:
                stock_val = idx.qty
                item_code = idx.code
        
        return item_code
    
    # method to determine product with the lowest stock_qty
    def lowest_stock_on_hand(self):
        
        item_code = ""
        stock_val = 100000000
        
        for idx in self.inventory_list:
            if stock_val > idx.qty:
                stock_val = idx.qty
                item_code = idx.code
        
        return item_code

#==========Main Menu=============

def main_menu():
    main_menu = """
                Welcome

                This is an inventory management system for a local shoe store.

                Please make you selection from the menu below:
                1 - View All
                2 - Add Item
                3 - Search Item
                4 - Sale Item
                5 - Restock Item
                6 - View Stock Values
                7 - Exit program

                """
    while True:
        # request user input, test if valid, if invalid display error message
        try:
            user_input = int(input(main_menu))
        except ValueError:
            print("You have made an invalid input.")
        
        # test user input, if within range return input
        if user_input <= 7:
            return user_input
            break
        
        # if user input is out of range, display error message
        elif user_input > 7:
            print("Please select an option from the main menu between 1 - 7")

# ================= Add item Function ==================

def add_item(inventory):
    code = input("Please provide item code \n")
    product = input("Please provide item description \n")
    cost = round(float(input("Please provide price for the item \n")),2)
    qty = int(input("Please indicate the quantity of stock on hand for the item \n"))
    country = input("Please indicate the country where the item is made \n")

    inventory.add_item(country,code,product,cost,qty)

# ================== CREATE INVENTORY ================
# import inventory items from external source
source = os.path.abspath('../textfiles/inventory.txt')

def get_inventory(source):
    """
    Function returns an inventory of items.
    Gathers information from source (txt file)
    If file cannot be found, return error message

    Parameters
    ----------
    root : Window (Tk)
        Root window for program.

    Returns
    -------
    inventory : LIST
        List of items (Shoe).

    """
    
    data_list = []
    country = ""
    code = ""
    product = ""
    cost = 0
    qty = 0
    
    try:
        with open(source,"r") as f:
            for line in f:
                data_list.append(line.split(","))
                
        data_list = data_list[1:]
        
    except FileNotFoundError:
        print("Error: file not found")

    inventory = Inventory()

    for idx in data_list:
        country = idx[0]
        code = idx[1]
        product = idx[2]
        cost = float(idx[3])
        qty = int(idx[4])
        inventory.add_item(country, code, product, cost, qty)
    
    return inventory

new_inventory = get_inventory(source)


# ============ Print Functions ============
def headings():
    """
        Function prints headings with specified spacing
    """
    print(f"{'Product Code' :<15} {'Product Description' :<25} {'Price' :<15} {'Quantity' :<10} {'Country' :<15}")

def stock_value_headings():
    '''
        Function prints headings with specified spacing
        Headings include total stock value
    '''
    print(f"{'Product Code' :<15} {'Product Description' :<25} {'Price' :<15} {'Quantity' :<10} {'Country' :<15} {'Total Value' :<15}")

def stock_value_item(item):
    """
        Function prints item from inventory with specified spacing.
        Includes total value for stock on hand

        Parameter:
            item: Shoe Class

        Return: Null
    """
    print(f"{item.code :<15} {item.product :<25} {'R ' + str(item.cost) :<15} {item.qty :<10} {item.country :<15} {'R ' + str(item.cost*item.qty) :<15}")

def print_item(item):
    """
        Function prints item with specified spacing

        Parameter:
            item: Shoe class

        Return: NULL
    """
    print(f"{item.code :<15} {item.product :<25} {'R ' + str(item.cost) :<15} {item.qty :<10} {item.country :<15}")


# ================== RUN PROGRAM ====================

user_input = 0
while user_input != 7:
    user_input = main_menu()

    # execute program options base on selection/ user input
    if user_input == 1:
        # code to view all items in inventory
        headings()
        for idx in new_inventory.inventory_list:
            print_item(idx)
 
    elif user_input == 2:
        # code to add item to inventory
        add_item(new_inventory)
        
    
    elif user_input == 3:
        # code to allow user to select method of search for item in inventory
        while True:
            try:
                method_selection = int(input("""
                                            Please indicate the method of search you would like to use:
                                        
                                            1 - Search using product code
                                            2 - Search using product description
                                            3 - Search using country
                                            4 - Return to main menu
                                        """))
            except ValueError:
                print("You've made an invalid selection, please choose from the list.")
            
            if method_selection == 1:
                print("You've selected to search using product code.")
                code = input("Please enter the product code \n")
                
                # retrieve list of items that meets the criteria entered
                search_index = new_inventory.search_code(code)
                # display all items in the list
                for idx in search_index:
                    print(new_inventory.inventory_list[idx])
                
            elif method_selection == 2:
                print("You've selected to search using product description.")
                product = input("Please enter the product description \n")
                
                search_index = new_inventory.search_product(product)
                for idx in search_index:
                    print(new_inventory.inventory_list[idx])

            elif method_selection == 3:
                print("You've selected to search using country.")
                country = input("Please enter the country \n")
                
                search_index = new_inventory.search_country(country)
                for idx in search_index:
                    print(new_inventory.inventory_list[idx])

            elif method_selection == 4:
                print("Returning to main menu")
                break
    
    elif user_input == 4:
        # determine item with the highest amount of stock on hand using method
        item_code = new_inventory.highest_stock_on_hand()
        
        #display item with message to place on sale
        print("The following item has the highest stock value and should be placed on sale.")
        headings()
        print_item(new_inventory.inventory_list[new_inventory.search_code(item_code)[0]])
    
    elif user_input == 5:
        # code to restock item with lowest stock value
        while True:
            item_code = new_inventory.lowest_stock_on_hand()
            print("The following item has the lowest stock value.")
            headings()
            print_item(new_inventory.inventory_list[new_inventory.search_code(item_code)[0]])

            try:
                user_option = int(input("Would you like to restock this item? (select: 1 - Yes 2 - No) \n"))
            except ValueError:
                print("You've made an invalid selection")
            
            if user_option == 1:
                # update stock value
                while True:
                    try:
                        new_qty = int(input("Please enter the new stock value. \n"))
                        if new_qty > 0:
                            new_inventory.inventory_list[new_inventory.search_code(item_code)[0]].change_qty(new_qty)
                            print("The item's stock quantity has been successfully updated.")
                            break
                        else:
                            print("Please enter a value greater than zero.")
                    except ValueError:
                        print("You have made an invalid input.")

            elif user_option == 2:
                # return user to main menu
                print("You have selected to return to the main menu.")
                break
            else:
                print("You've made an invalid selection.")
        
        

    elif user_input == 6:
        stock_value_headings()
        for idx in new_inventory.inventory_list:
            stock_value_item(idx)

    elif user_input:
        print("Good buy")