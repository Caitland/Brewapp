import io
import csv
import pymysql
#from datastoreclass import datastore
#from data_.receipts import customer_receipts

ORDER_ARG = 1
ADD_DRINKS = 2
FAVE_DRINK_ARG = 3
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
PEOPLE_FILE_PATH = r'C:\Users\mylaptop\Desktop\brew_app\data_\people.txt' 
DRINKS_FILE_PATH = r'C:\Users\mylaptop\Desktop\brew_app\data_\drinks.txt'
ORDER_FILE_PATH = r'C:\Users\mylaptop\Desktop\brew_app\data_\order_file.csv'
#DATASTORE_FILE_PATH = r'C:\Users\mylaptop\Desktop\brew_app\core\datastoreclass.py'

#App data

prices = {'Coffee' : 2.50, 'Tea' : 2.00, 'Green Tea' : 2.00, 'Water' : 1.00}

orders = []
total = []
name = ''
total_sum = 0

#Data persistence
def load_list_from_file(path):
        data = []  
        try:
            with open(path, 'r') as file:
                for line in file.readlines():
                    data.append(line.strip())
                return data
#Incase of errors
        except FileNotFoundError:
            print(f'Unable to load necessary data from: {path}')
            exit()
        
        except Exception as e:
            print(f'Unable to lead necessary data from: {path}. Error: {str(e)}')

#Load from file function    
def loader_func():
    print("loading data")
    for person in load_list_from_file(PEOPLE_FILE_PATH):
        people.append(person)
    for drink in load_list_from_file(DRINKS_FILE_PATH):
        drinks.append(drink)      

#def read_csv():
 #   with open(ORDER_FILE_PATH, 'r') as csv_file:
  #      reader = csv.reader(csv_file)
   #     temp_dict = {}
    #    for row in reader:
     #       temp_dict[0] = [1] [2]

def save_data():
#Save people
    with open(PEOPLE_FILE_PATH, 'w') as file:
        file.writelines([f'{person}\n' for person in people])
#Save drinks
    with open(DRINKS_FILE_PATH, 'w') as file:
        file.writelines([f'{drink}\n' for drink in drinks])
#Save orders
    with open(ORDER_FILE_PATH, 'a') as csv_file:
        myfile = csv.writer(csv_file)
        myfile.writerow(['name', 'orders'])
        myfile.writerow([name, orders, total_sum])
        
                
#Wait and return to menu
def wait():
    input('Press ENTER to return to the menu')
    return(MENU)

#Welcome back regulars and offer their favourite drink
def regular_welcome(favourites, name):
    if name in people:
        user_input = input(f'\nWelcome back {name}!\nWould you like to order a {(favourites[name])}?\n\nYES or NO\n').lower()
        if user_input == "no":
            pass

        elif user_input == 'yes':
            if  favourites[name] in prices:
                for key, value in prices.items():
                    if key == favourites[name]:
                        orders.append(key)
                        total.append(value)         
#Welcome and save new customer names
def new_customer_welcome(name, people):
    if name not in people:
        print(f'\nWelcome {name}!')

def customer_order(user_input):
    user_input = input(f'''\nType a drink from the price list to add to your order: {prices}\n 
                                (Type \'done\' when you have finished adding to your order.)\n''').title()
    if user_input in prices:
        for key, value in prices.items():
            if key == user_input:
                orders.append(key)
                total.append(value)
                print (total)
                print (orders)
                return customer_order(user_input)

    elif user_input == 'Done':
        total_sum = sum(total)
        print(f'\nThank you {name}! \nYour order is: {orders} and the total price is £{total_sum}.\n\nWe hope to see you again!')
        wait()
    
    else:
        user_input not in prices
        print(f'Sorry we don\'t sell that here.')
        return customer_order(user_input)
 
#Add drink if drink in price list
def handle_favourite_drinks(new_name, new_drink, drinks):
    while new_drink not in prices:
        new_drink = input(f'\nSorry we don\'t sell that here.\nPlease type a drink from the price list:{prices}:\n').title()
    if new_drink in prices:
        drinks.append(new_drink)
        print(f'{new_name}\'s order is now saved as \'{new_drink.lower()}\'.')

#Create favourites dictionary with people and drinks
people = load_list_from_file(PEOPLE_FILE_PATH)
drinks = load_list_from_file(DRINKS_FILE_PATH)
favourites = dict(zip(people, drinks))

def start():
  #  Datastore
    loader_func()
    run()

def run():
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
            name = (input('\nWhat is your name?:\n').title())
            regular_welcome(favourites, name)
            new_customer_welcome(name, people)
            user_input = input(f'\nWould you like to add an order?\n YES or NO\n').lower()
            if user_input == 'no':
                total_sum = sum(total)
                print(f'\nThank you {name}! \nYour order is: {orders} and the total price is £{total_sum}.\n\nWe hope to see you again!')
                wait()
            elif user_input == 'yes':
                customer_order(user_input)
            else:
                user_input != 'no' or 'yes'
                print('Your order has been cancelled')
                wait()

#IF USER SELECTS 2 FROM MENU:
        if user_selection == ADD_DRINKS:
            user_input = input('Type a drink you would like to add\n').title()
            print (f'You can now choose \'{user_input}\' when you make an order.\n')
            new_price = int(input('How much does this drink cost?\n'))
            prices[user_input] = new_price
            wait()
         
#IF USER SELECTS 3 FROM MENU:
        if user_selection == FAVE_DRINK_ARG:
            print(favourites)
            user_input = input('Would you like to add to this? \nYES or NO: \n').lower()
            if user_input == 'yes':
                new_name = input('Type in a name: \n').title()
                if new_name in people:
                    new_name = input(f'\'{new_name}\' already exists on our system\n\nPlease type in name:\n').title()

                elif new_name not in people:
                    people.append(new_name)
                    new_drink = input(f'\'{new_name}\' has been added...\n\nNow type {new_name}\'s favourite drink from the price list: {prices} \n').title()
                    handle_favourite_drinks(new_name, new_drink, drinks)
                    wait()
            elif user_input == 'no':
                wait()        

#IF USER SELECTS 4 FROM MENU:
        elif user_selection == RECEIPTS_ARG:
            get_customer_receipt = input('Type in a name: ').title()
            if get_customer_receipt in read_csv():
                print(f'Name: {[0]} Order: {[1]} Total: {[2]}')
           # customer_receipt = input("Type in a name: ").title()
           # print(people(customer_receipt)
            #wait()

        #def name_search(user_input):
 #   try: 
  #      print(f'{people_search}\'s favourite drink is: {favourites[user_input.title()]}') 
  #  except:
   #     print('This name does not exist')


#IF USER SELECTS 5 FROM MENU:
        elif user_selection == EXIT_ARG:
            print('Saving data...')
            save_data()
         #   insert()
            print("Goodbye!")
            exit()
#entry point
if __name__ == "__main__":
    start()