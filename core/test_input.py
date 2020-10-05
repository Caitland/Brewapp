import unittest
from unittest.mock import Mock, patch
from brewapp2 import handle_favourite_drinks, customer_order

#def handle_favourite_drinks(new_name, new_drink, drinks):
 #   while new_drink not in prices:
  #      new_drink = input(f'\nSorry we don\'t sell that here.\nPlease type a drink from the price list:{prices}:\n').title()
  #  if new_drink in prices:
   #     drinks.append(new_drink)
    #    print(f'{new_name}\'s order is now saved as \'{new_drink.lower()}\'.')

class Test_Methods(unittest.TestCase):
      @patch('builtins.input')
      def test_handle_favourite_drinks(self, mock_input):

      #arrange
            new_name = 'caitland'
            mock_input = 'Tea'
            new_drink = 'Tea'
            drinks = []
            prices = ['Tea']
            #act
            handle_favourite_drinks(new_name, new_drink, drinks)
            #assert
            assert drinks == ['Tea']

#def customer_order(user_input):
#    user_input = input(f'''\nType a drink from the price list to add to your order: {prices}\n 
#                                (Type \'done\' when you have finished adding to your order.)\n''').title()
#    if user_input in prices:
#        for key, value in prices.items():
#            if key == user_input:
#                orders.append(key)
#                total.append(value)
#                print (total)
#                print (orders)
#                return customer_order(user_input)

#    elif user_input == 'Done':
#        total_sum = sum(total)
#        print(f'\nThank you {name}! \nYour order is: {orders} and the total price is £{total_sum}.\n\nWe hope to see you again!')
#        wait()
    
#    else:
#        user_input not in prices
#        print(f'Sorry we don\'t sell that here.')
#        return customer_order(user_input)

if __name__ == "__main__":
      unittest.main()