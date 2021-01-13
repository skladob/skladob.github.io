import re
import sqlite3

import link_extractor

SQL_file = 'dev/newDataBase.db'
QUERY_reader_host = 'SELECT host FROM Manufacturers'


def create_connection(connection):
    connect = None
    try:
        with sqlite3.connect(connection) as connect:
            cursor = connect.cursor()
            print("Установлно соединение с SQLite")
            return cursor
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


def reading_from_base(connection, query):
    cursor = create_connection(connection)
    cursor.execute(query)
    for result in cursor:
        print(result)








    # for row in cursor.fetchone():
    #     # return row
    #     links = link_extractor.getLinks(row)
    #     for link in links:
    #         result = link_extractor.getLinks(link)
    #         for a in result:
    #             print(a)


if __name__ == "__main__":
    reading_from_base(SQL_file, QUERY_reader_host)
    # print (row)
