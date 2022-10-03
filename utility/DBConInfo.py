from datetime import datetime
import psycopg2
import pandas as pd

class dbConInfo():
    def __init__(self, host, user, password, dbname, sslmode):
        self.__host = host
        self.__user = user
        self.__password  = password
        self.__dbname = dbname
        self.__sslmode  = sslmode
    
    def __dbcnt(self):
        return psycopg2.connect(host=self.__host,user=self.__user,password=self.__password,dbname=self.__dbname,sslmode=self.__sslmode)
        
    def readSQL(self,sql_list):
        try:
            db = self.__dbcnt()
            data=pd.read_sql(sql_list,db)
        except Exception as e:
            print(f"{datetime.now()} [err] -> {sql_list} : {e}")
            raise Exception(e)
        finally:
            db.commit()
            db.close()

        return data