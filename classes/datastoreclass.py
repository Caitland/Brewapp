import pymysql

class Sqldb():

#Data persistence
    def __init__(self, host='localhost', db='Brewapp', port=3306, user='root', password='password'):
        self.__host = host
        self.__db = db
        self.__port = port
        self.__user = user 
        self.__password = password

    def __make_connection(self):
        return pymysql.connect(host=self.__host,
                               user=self.__user,
                               password=self.__password,
                               db=self.__db,
                               port=self.__port)

    def insert_order(self, name, drinks, total_sum):
        connection = self.__make_connection()

        try:
            with connection.cursor() as cursor:
                data = [name, drinks, total_sum]
                sql = f'INSERT INTO receipts (name, drinks, total) VALUES (%s, %s, %s)'
                cursor.execute(sql, data)
            connection.commit()
        finally:
            connection.close()

    def insert_favourite(self, name, drinks, price):
        connection = self.__make_connection()

        try:
            with connection.cursor() as cursor:
                data = [name, drinks, price]
                sql = f'INSERT INTO favourites (name, drink, price) VALUES (%s, %s, %s)'
                cursor.execute(sql, data)
            connection.commit()
        finally:
            connection.close()

    def load_orders(self):
        data = {}
        connection = self.__make_connection()
        try:
            with connection.cursor() as cursor:
                sql = 'SELECT * from receipts'
                cursor.execute(sql)
             #   for line in data
                while True:
                    order_data = cursor.fetchone()
                    if not order_data:
                        break
                    else:
                        data[order_data[0]] = [order_data[1], order_data[2]]
                connection.commit()
        finally:
            connection.close()
        return data

    def load_favourites(self):
        data = {}
        connection = self.__make_connection()
        try:
            with connection.cursor() as cursor:
                sql = 'SELECT * from favourites'
                cursor.execute(sql)
             #   for line in data
                while True:
                    fav_data = cursor.fetchone()
                    if not fav_data:
                        break
                    else:
                        data[fav_data[0]] = [fav_data[1], fav_data[2]]
                connection.commit()
        finally:
            connection.close()
        return data