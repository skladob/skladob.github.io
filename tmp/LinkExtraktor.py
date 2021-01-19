import re
import sqlite3

import link_extractor
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_URL = 'https://sivik.ru'
SQL_file = 'dev/newDataBase.db'
QUERY = 'INSERT INTO href VALUES (?);'


def create_connection(connection):
    connect = None
    try:
        with sqlite3.connect(connection) as connect:
            cursor = connect.cursor()
            print("Установлно соединение с SQLite")
            return cursor
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


def get_links(url):
    links = link_extractor.getLinks(url)
    cursor = create_connection(SQL_file)
    for link in links:
        i = "'" + link + "'"
        print(type(i))
        print(i)
        cursor.execute(QUERY, 'https://sivik.ru/catalog/balansirovochnoe_oborudovanie/')

get_links(BASE_URL)





# def reading_from_base(connection, query):
#     cursor = create_connection(connection)
#     cursor.execute(query)
#     for result in cursor:
#         print(result)


# if __name__ == "__main__":
#     reading_from_base(SQL_file, QUERY_reader_host)
#     # print (row)
