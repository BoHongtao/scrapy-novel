import pymysql.cursors
from dingdian import settings
MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB
MYSQL_CHARACTERS = settings.MYSQL_CHARACTERS
# 获取游标
connect = pymysql.Connect(user=MYSQL_USER,password=MYSQL_PASSWORD,host=MYSQL_HOSTS,database=MYSQL_DB,charset=MYSQL_CHARACTERS)
cur = connect.cursor()
class Sql:
    @classmethod
    def insert(cls,name,author,category,novelurl,new):
        sql = "INSERT INTO novel (id,name,category,author,detail,new) VALUES ( '%s', '%s', '%s' ,'%s', '%s', '%s')"
        value = ('0',name, category,author,novelurl,new)
        cur.execute(sql % value)
        connect.commit()
    @classmethod
    def selecct(self,name):
        sql = "select exists(select 1 from novel where name=%(name)s)"
        value = {
            'name':name
        }
        cur.execute(sql,value)
        return cur.fetchall()[0]
