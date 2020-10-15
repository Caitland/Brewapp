import io
import csv
import pymysql
from classes.datastoreclass import Sqldb
from classes.receipt_class import Customer_receipt
from classes.favourite import Favourites
#from core.table import table
from tabulate import tabulate

ORDER_ARG = 1
ADD_DRINKS = 2
FAV_DRINK_ARG = 3
RECEIPTS_ARG = 4
EXIT_ARG = 5
MENU = '''
Welcome to BrewApp!

[1] Make an order
[2] Add drink
[3] Favourite drinks list
[4] Customer reciepts
[5] Exit
'''

#Data sources
PEOPLE_FILE_PATH = r'C:\Users\mylaptop\Desktop\brew_app\data\people.txt' 
DRINKS_FILE_PATH = r'C:\Users\mylaptop\Desktop\brew_app\data\drinks.txt'
ORDER_FILE_PATH = r'C:\Users\mylaptop\Desktop\brew_app\data\order_file.csv'
#DATASTORE_FILE_PATH = r'C:\Users\mylaptop\Desktop\brew_app\core\datastoreclass.py'

#App data

prices = {'Coffee' : 2.50, 'Tea' : 2.00, 'Green Tea' : 2.00, 'Water' : 1.00}

orders = []
total = []
name = ''
customer_receipt = Customer_receipt()
favourites = Favourites()
receipts_list = []
                  
#Wait and return to menu
def wait():
    input('Press ENTER to return to the menu')
    
#Welcome back regulars
def welcome_handle(name, sql_db):   
    if name in sql_db.load_favourites():
        get_fav_drink = sql_db.load_favourites().get(name)
        user_input = input(f'\nWelcome back {name}!\nWould you like to order a {get_fav_drink[0]}?\n\nYES or NO\n').lower()
        if user_input == "no":
            pass
#Add regular drink and total to lists
        elif user_input == 'yes':
            customer_receipt.name = name
            orders.append(get_fav_drink[0])
            total.append(float(int(get_fav_drink[1])))
#Add new customer name to receipt
    else: 
        print(f'\nWelcome {name}!')
        customer_receipt.name = name

def not_in_price_list():
    print('''
                                                           Sorry we don\'t sell that here.
                                        You can add a drink by selecting the "ADD DRINK" option on the main menu.\n\n''')

#Checks drink and customer name can be saved to db
def choice_handle(user_input, sql_db):
    user_input = input(f'\nType a drink from the price list to add to your order: {prices}\nOtherwise type \'done\' when finished adding drinks.\n').title()

    if user_input == 'Done':
        
        try:
            save_order(sql_db)
        
        except:
            user_input = input('\nWe already have your name in our system please update this.\nMaybe try - \'Your Name1 etc\':\n').title()
            customer_receipt.name = user_input
            save_order(sql_db)

#If drink not in price list
    elif user_input not in prices:
        not_in_price_list()
        choice_handle(user_input, sql_db)
#Offer menu again for another drink             
    elif user_input in prices:
        add_to_lists(user_input)
        choice_handle(user_input, sql_db)
                      
#Adds total and orders to lists
def add_to_lists(user_input): 
    if user_input in prices:
        orders.append(user_input)
        total.append(prices[user_input])

#Save order to db
def save_order(sql_db):
        orders_str = ', '.join(orders)
        customer_receipt.drinks = (orders_str)
        customer_receipt.total_sum = (sum(total))
        sql_db.insert_order(customer_receipt.name, customer_receipt.drinks, customer_receipt.total_sum)
        print(f'\nThank you {customer_receipt.name}! \nYour order is: {customer_receipt.drinks} and the total price is £{customer_receipt.total_sum}.\n\nWe hope to see you again!')
        wait()
        
#Add favourites info to db
def save_favourites(new_name, fav_drink, sql_db):
        favourites.drink = fav_drink
        favourites.name = new_name
        favourites.price = prices[fav_drink]
        sql_db.insert_favourite(favourites.name, favourites.drink, favourites.price)
        print(f'{favourites.name}\'s order is now saved as \'{favourites.drink.lower()}\'.')

def favourite_handle(new_name, sql_db):
    fav_drink = input(f'\'{new_name}\' has been added...\n\nNow type {new_name}\'s favourite drink from the price list: {prices} \n').title()
    if fav_drink in prices:
        save_favourites(new_name, fav_drink, sql_db)
        wait()

    elif fav_drink not in prices:
        not_in_price_list()
        favourite_handle(new_name, sql_db)
   

def start():
    sql_db = Sqldb(host='127.0.0.1', db='Brewapp', port=33066, user='root', password='password')
    run(sql_db)

def run(sql_db):
    while True:
        print(MENU)
        try: 
            user_selection = int(input('Enter your selection: '))
            print(user_selection)

        except ValueError:
            print('Not an option.')
            wait()
            continue
        
#IF USER SELECTS 1 FROM MENU:
        if user_selection == ORDER_ARG:
            user_input = (input('\nWhat is your name?:\n').title())
            welcome_handle(user_input, sql_db)
            user_input = input(f'\nWould you like to add an order?\n YES or NO\n').lower()

            if user_input == 'no':
                try:
                    save_order(sql_db)
        
                except:
                    user_input = input('\nWe already have your name in our system please update this.\nMaybe try - \'Your Name1 etc\':\n').title()
                    customer_receipt.name = user_input
                    save_order(sql_db)
                
            elif user_input == 'yes':
                choice_handle(user_input, sql_db)
                    
            else:
                user_input != 'no' or 'yes'
                print('Your order has been cancelled')
                wait()

#IF USER SELECTS 2 FROM MENU:
        if user_selection == ADD_DRINKS:
            user_input = input('\nPlease note the default price for all custom drinks is £3.00\nType the drink you would like to add:\n').title()
            print (f'You can now choose \'{user_input}\' when making an order or adding your favourite drink.\n')
            prices[user_input] = 3.0
            wait()
         
#IF USER SELECTS 3 FROM MENU:
        if user_selection == FAV_DRINK_ARG:
            print(sql_db.load_favourites())
            user_input = input('Would you like to add to this? \nYES or NO: \n').lower()
            if user_input == 'yes':
                new_name = input('Type in a name: \n').title()
                while new_name in sql_db.load_favourites():
                    new_name = input(f'\'{new_name}\' already exists on our system\n\nPlease type in name:\n').title()

                if new_name not in sql_db.load_favourites():
                    favourite_handle(new_name, sql_db)

            elif user_input == 'no':
                wait()        
#IF USER SELECTS 4 FROM MENU:
        elif user_selection == RECEIPTS_ARG:
            user_input = input('Type in customer name: ').title()
            if user_input in sql_db.load_orders():
                get_receipt = sql_db.load_orders().get(user_input)
                receipt_total = '£' + str(get_receipt[1]) 
                print(tabulate({'NAME': [user_input], 'ORDER': [get_receipt[0]], 'TOTAL': [receipt_total]}, headers="keys", tablefmt="fancy_grid"))
                wait()

            else:
                print('That person does not exist in our system')
                wait()
            
#IF USER SELECTS 5 FROM MENU:
        elif user_selection == EXIT_ARG:
            print("Goodbye!")
            exit()

#Entry point
if __name__ == "__main__":
    start()