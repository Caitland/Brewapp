import csv

ORDER_FILE_PATH = r'C:\Users\mylaptop\Desktop\brew_app\data_\order_file.csv'

def read_csv():
    with open(ORDER_FILE_PATH, 'r') as file:
        reader = csv.reader(file)
        temp_dict = {}
        for row in reader:
            temp_dict[row[0]] = [row[1]]

'Coffee' == '2.50'
'Tea' == '2.00'
'Green Tea' == '2.00'
'Water' == '1.00'

print(file.values())