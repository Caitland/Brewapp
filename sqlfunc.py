import pymysql
import csv

def main():
    connection = pymysql.connect(host = "localhost", port = 33066, user = "root", password = "password", db = "Brewapp"
    )

    cursor = connection.cursor()
    cursor.execute("SELECT name, drink FROM favourites")
    rows = cursor.fetchall()

    for row in rows:
        print(row) 

    cursor.close()
    connection.close()

def insert()
  connection = pymysql.conect(
  connection = pymysql.connect(host = "localhost", port = 33066, user = "root", password = "password", db = "Brewapp"
  )
  cursor = connection.cursor()
  args =(people, drinks)
  cursor.execute("INSERT INTO favourites (name, drinks) VALUES (%s, %s)", args)
  connection.commit()
  cursor.close()
  connection.close()

def main():
    connection = pymysql.connect(host = "localhost", port = 33066, user = "root", password = "password", db = "Brewapp"
    )

    cursor = connection.cursor()
    cursor.execute("SELECT name, drink FROM favourites")
    rows = cursor.fetchall()

    for row in rows:
        print(row) 

    cursor.close()
    connection.close()

def insert()
  connection = pymysql.conect(
  connection = pymysql.connect(host = "localhost", port = 33066, user = "root", password = "password", db = "Brewapp"
  )
  cursor = connection.cursor()
  args =(people, drinks)
  cursor.execute("INSERT INTO favourites (name, drinks) VALUES (%s, %s)", args)
  connection.commit()
  cursor.close()
  connection.close()

if __name__ == '__main__':
  main() 