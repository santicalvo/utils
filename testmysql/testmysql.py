# -*- coding: utf-8 -*-
import MySQLdb

def checkTableExists(dbcon, tablename):
    dbcur = dbcon.cursor()
    check_db_exist_sql = "select count(*) from information_schema.SCHEMATA where SCHEMA_NAME='%s';" % tablename
    print check_db_exist_sql
    dbcur.execute(check_db_exist_sql)
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        return True
    dbcur.close()
    return False

def create_database():
    create = """SET NAMES utf8;
    SET time_zone = '+00:00';
    SET foreign_key_checks = 0;
    SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

    CREATE DATABASE IF NOT EXISTS `pruebas`  /*!40100 DEFAULT CHARACTER SET latin1 */;
    USE `pruebas`;

    CREATE TABLE IF NOT EXISTS `tabla1`  (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `col1` text NOT NULL,
      `col2` text NOT NULL,
      `col3` text NOT NULL,
      `col4` text NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=latin1;"""
    try:
        c = db.cursor()
        c.execute(create,[])
        try:
            c.close()
            db.commit()
            print 'database pruebas creada'
        except:
            print 'algo sucedio... a ver si sigo'

        db.close()
    except Exception as ex:
        print 'en excepcion 1', ex

def insert_rows():
    try:
        print 'vuelvo a conectar'
        insert = """INSERT INTO tabla1 (col1, col2, col3, col4) VALUES (%s, %s, %s, %s)"""
        db = MySQLdb.connect(host="localhost",user="root",passwd="root", db='pruebas')
        rows = []
        for n in xrange(1, 100):
            rows.append(( 'texto_1_{0}'.format(n), 'texto_2_{0}'.format(n), 'texto_3_{0}'.format(n), 'texto_4_{0}'.format(n) ))
        print 'trato de insertar ', rows
        c = db.cursor()
        c.executemany(insert, rows)
        c.close()
        db.commit()
    except Exception as ex1:
        print 'Exception 2', ex1

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost",user="root",passwd="root")
    database = 'pruebas'
    if not checkTableExists(db, database):
        create_database()
    insert_rows()
    print 'continuo'
