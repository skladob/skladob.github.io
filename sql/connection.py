SQL_SERVER = 'localhost'
SQL_USER = 'romansyroezhkin'
SQL_PASSWORD = 'y34$dNWm5Q#'
SQL_DATABASE = 'SKLADOB'


if __name__ == "__main__":
    import pymysql
    from my_settings import SQL_DATABASE, SQL_PASSWORD, SQL_SERVER, SQL_USER

    def create_connection():
        connect = None
        try:
            connect = pymysql.connect  (host=SQL_SERVER,
                                        user=SQL_USER,
                                        password=SQL_PASSWORD,
                                        db=SQL_DATABASE,
                                        charset='utf8mb4')
            cursor = connect.cursor()
            print("Установлно соединение с базой данных SKLADOB")
            return cursor
        except pymysql.Error as error:
            print("Ошибка при работе с MySQL", error)

    create_connection()
