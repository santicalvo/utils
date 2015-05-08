# -*- coding: utf-8 -*-
import MySQLdb

def checkTableExists(dbcon, tablename):
    dbcur = dbcon.cursor()
    check_db_exist_sql = "select count(*) from information_schema.SCHEMATA \
                                where SCHEMA_NAME='%s';" \
                               % tablename
    print check_db_exist_sql
    dbcur.execute(check_db_exist_sql)
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        return True
    dbcur.close()
    return False

db = MySQLdb.connect(host="localhost",user="root",passwd="root")
print checkTableExists(db, 'pruebass')