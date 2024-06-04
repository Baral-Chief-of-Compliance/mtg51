import sqlite3
from dotenv import load_dotenv
import os




#класс для взаимодейтсвия с базой данных
class DBControler(object):

    #подключение к базе данных
    connection : sqlite3.Connection

    #курсок для запроса к базе данных
    cursor : sqlite3.Cursor

    #изменение состояние базы данных
    changeState : bool 

    #текст запроса к базе данных
    sqlQueri : str

    #параметры к запросу
    sqlParams : tuple

    #статус один резульатат или много
    manyResult : bool

    #статус есть ли результаты от запроса
    resultState : bool

    #функция подключение к базе данных
    def connectToDB(self) -> None:
        load_dotenv()
        
        try:
            self.connection = sqlite3.connect(os.getenv('DB_NAME'))
            self.cursor = self.connection.cursor()

        except Exception as error:
            print(error)


    #функция закрыти подключение
    def closeConnectionDB(self) -> None:
        if self.changeState:
            self.connection.commit()
        
        self.cursor.close()
        self.connection.close()

    #конструктор класса
    def __init__(self):
        self.connectToDB()
        # print('подлюкчение к базе выполнено')

    
    #метод выполнение запроса 
    def makeQueri(
            self, 
            sqlQueri: str, 
            sqlParams: tuple = (), 
            changeState: bool = False,
            resultState: bool = True,
            manyResult: bool = True
        ) -> tuple or None:
        
        self.sqlQueri = sqlQueri
        self.sqlParams = sqlParams
        self.changeState = changeState
        self.resultState = resultState
        self.manyResult = manyResult

        result = None


        #при условие что мы хотим получить результат от запроса
        if self.resultState:
            #условие если нету параметров для запроса
            if self.sqlParams == ():
                self.cursor.execute(self.sqlQueri)

                #условие если мы хотим получить много строк из базы
                if self.manyResult:
                    result = self.cursor.fetchall()
                    return result

                #услоивие если мы хотим получить одну строку из базы
                else:
                    result = self.cursor.fetchone()
                    return result
            
            #услоиве если есть параметры для запросов
            else:
                self.cursor.execute(self.sqlQueri, self.sqlParams)

                #условие если мы хотим получить много строк из базы
                if self.manyResult:
                    result = self.cursor.fetchall()
                    return result

                #услоивие если мы хотим получить одну строку из базы
                else:
                    result = self.cursor.fetchone()
                    return result

        #при условие что мы не хотим получать результат
        else:
            if self.sqlParams == ():
                self.cursor.execute(self.sqlQueri)
            
            else:
                self.cursor.execute(self.sqlQueri, self.sqlParams)

            return None
            

    #деструктор класса
    def __del__(self):
        self.closeConnectionDB()
        # print('отключение к базе выполнено')


#код к созданию базы данных
# dbControler = DBControler()
# dbControler.makeQueri(sqlQueri='''
#                       create table CardOrders(
#                         order_id INTEGER primary key AUTOINCREMENT,
#                         card_name_RU TEXT,
#                         card_name_EU TEXT,
#                         count INTEGER,
#                         date_add TEXT,
#                         user_name TEXT,
#                         order_status TEXT
#                       )
#                       ''', changeState=True, resultState=False)
# del dbControler