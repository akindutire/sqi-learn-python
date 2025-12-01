import os
from dotenv import load_dotenv
import mysql.connector as sql
class Config:
    def __init__(self):
        load_dotenv(override=True)
        self.__host = os.getenv("DB_HOST")
        self.__user = os.getenv("DB_USER"),
        self.__password = os.getenv("DB_PASSWORD")
        self.__database = os.getenv("DB_NAME")            
    
    def get_db_cursor(self):
        try:
            db = sql.connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                database=self.__database
            )
            return db.cursor()
        except sql.Error as e:
            print("Error connecting to database:", e)
            exit()
            return None
        