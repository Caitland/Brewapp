import csv
import pymysql

NAME_INDEX = 0
ORDERS_INDEX = 1
TOTAL_INDEX = 2

RECEIPTS = "customer_receipts"

NAME_COLUMN = 'name'
ORDERS_COLUMN = 'orders'
TOTAL_COLUMN = 'total_sum'

class SQLDB():

#Data persistence
    def __init__(self, host='localhost', db='brewapp', port=3306, user='root', password='password'):
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
    
  #  def read(self):
   #     print ("read")
    #    cursor = connection.cursor()
     #   cursor.execute("SELECT name, drink FROM favourites")
      #  for row in cursor:
       #     print(row)

    def load_orders(self, customer_receipts):
    data = []
    connection = self.__make_connection()
    try:
        with connection.cursor() as cursor:
            sql = f'SELECT * FROM {ORDERS}'
            cursor.execute(sql)
            while True:
                order_data = cursor.fetchone()
                if not order_data:
                    break
                    data.append(RECEIPTS(
                    order_data[NAME_INDEX],
                    order_data[ORDERS_INDEX,]
                    order_data[TOTAL_INDEX],
                ))
            connection.commit()
        finally:
            connection.close()
            return data

    def insert_order(self, customer_receipts):
        connection = self.__make_connection()
        try:
            with connection.cursor() as cursor:
                data = [name, orders, total_sum]
                sql = f' INSERT INTO {RECEIPTS} ({NAME_COLUMN}, {ORDERS_COLUMN}, {TOTAL_COLUMN}) VALUES (%s, %s, %s, %s)'
                cursor.execute(sql, data)
                connection.commit()
            finally:
                connection.close()
