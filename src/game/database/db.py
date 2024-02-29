import sqlite3


class DataBase:
    def __init__(self, path: str) -> None:
        self.__connection = sqlite3.connect(path)
        self.__cursor = self.__connection.cursor() 

    def exist_user_with_id(self, user_id):
        self.__cursor.execute("SELECT EXISTS(SELECT * FROM user where id = ?)", (user_id,))
        result = self.__cursor.fetchone()

        return result[0]

    def get_user_by_nickname(self, nickname):
        self.__cursor.execute("SELECT * FROM user WHERE nickname = ?", (nickname, ))
        user = self.__cursor.fetchone()

        return user
    
    def registred_user(self, nickname):
        self.__cursor.execute("INSERT INTO user(nickname) VALUES (?)", (nickname,))