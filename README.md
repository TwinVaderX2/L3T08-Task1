# Simple Inventory app using Python OOP
This is a very primitive app to manage stock/ inventory. The goal of the program is to teach the programmer to use OOP.

## Task description/ Instructions
Description:
Code a Python program that will read from the text file inventory.txt and perform the following on the data, to prepare for presentation to your managers:
* We've provided a template for you in a file named inventory.py.
* Inside this file, you will find a class named Shoe with the following attributes:
    * country,
    * code,
    * product,
    * cost, and
    * quantity.
* Inside this class define the following methods:
    * get_cost - Returns the cost of the shoes.
    * get_quantity - Returns the quantity of the shoes.
    * __str__ - This method returns a string representation of a class.
* Outside this class create a variable with an empty list. This variable will be used to store a list of shoes objects
* Then you must define the following functions outside the class:
    * read_shoes_data - This function will open the file inventory.txt and read the data from this file, then create a
        shoes object with this data and append this object into the shoes list. One line in this file represents data to create one object of shoes. You must use the try-except in this function for error handling. Remember to skip the first line using your code.
    * capture_shoes - This function will allow a user to capture data about a shoe and use this data to create a shoe object and append this object inside the shoe list.
    * view_all - This function will iterate over the shoes list and print the details of the shoes returned from the __str__ function. Optional: you can organise your data in a table format by using Python's tabulate module.
    * re_stock - This function will find the shoe object with the lowest quantity, which are the shoes that need to be re-stocked. Ask the user if they want to add this quantity of shoes and then update it. This quantity should be updated on the file for this shoe.
    * seach_shoe - This function will search for a shoe from the list using the shoe code and return this object so that it will be printed.
    * value_per_item - This function will calculate the total value for each item . Please keep the formula for value in mind;
        value = cost * quantity. Print this information on the console for all the shoes. 
    * highest_qty - Write code to determine the product with the highest quantity and print this shoe as being for sale.

### Requirements
Python 3

### Installation
1. Clone Repository

### Running the program
1. cd into directory ./src/app
2. run using command python3 inventory.py

### Using docker
1. cd into directory ./ (Root)
2. run Docker Desktop
3. build image using command (docker build -t [image_name] .)
4. run image using command (docker run -ti [image_name])

## USER GUIDE
The user is presented with a menu of options to choose from. Enter the corresponding number for the task you wish to perform.

1 - View All (Displays all items in the inventory)
2 - Add Item (Allows user to add item to the inventory)
3 - Search Item (Allows user to search for item using either: item code/ item description/ country)
4 - Sale Item (view item that the system recommends to be put on sale)
5 - Restock Item (view item with the lowest stock on hand value, user is prompted to restock or exit function)
6 - View Stock Values (Displays a list of all items including their stock values)
7 - Exit program

Follow the prompts to perform specified tasks.
