

prices = {'Coffee' : '£2.50', 'Tea' : '£2.00', 'Green Tea' : "£2.00", 'Water' : '£1.00'}

'Coffee' = int('2.50')
'Tea' = int('2.00')
'Green Tea' = int('2.00')
'Water' = int('1.00')

class orders():
    def __init___(self, person_name, names, drinks_order, price, total):
        self.person_name = person_name
        self.names = names
        self.drinks_order = drinks_order
        self.price = price
        self.total = total
        

#print(receipts())

#total price = prices[user_input]