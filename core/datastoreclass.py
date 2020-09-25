import csv

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
    for order in load_list_from_file(ORDER_FILE_PATH):
       order.append(order)
 

#def save_data():
#Save people
    with open(PEOPLE_FILE_PATH, 'w') as file:
        file.writelines([f'{person}\n' for person in people])
#Save drinks
    with open(DRINKS_FILE_PATH, 'w') as file:
        file.writelines([f'{drink}\n' for drink in drinks])
#Save orders
    with open(ORDER_FILE_PATH, 'w') as file:
        file.writelines([f'{order}\n' for order in orders])
##################################################

    # data is expected to be a list of lists
    def save_to_csv(self, data):
        try:
            with open(self.path, 'w') as file:
                writer = csv.writer(file)
                writer.writerows(data)
        except FileNotFoundError as e:
            print(
                f'File "{self.path}" cannot be found with error: {str(e)} - exiting')

    # Returns list of lists
    def read_csv(self):
        try:
            with open(self.path, 'r') as file:
                data = []
                reader = csv.reader(file, delimiter=',')
                for row in reader:
                    data.append(row)
                return data
        except FileNotFoundError as e:
            print(
                f'File "{self.path}" cannot be found with error: {str(e)} - exiting')
        
    people = load_list_from_file(PEOPLE_FILE_PATH)
    drinks = load_list_from_file(DRINKS_FILE_PATH)
    favourites = dict(zip(people, drinks))