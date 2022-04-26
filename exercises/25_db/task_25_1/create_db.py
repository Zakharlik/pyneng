# -*- coding: utf-8 -*-
"""
Модуль создания баз данных для хранения информаци о ip dhcp snooping binding
с нескольки коммутаторов"
"""
import os
import re
import sqlite3

def isDbExists(fileName):
    """
    Функция проверки на существование базы данных (существование файда БД)
    """
    if os.path.exists(fileName):
        print('База данных существует')
        return True
    else:
        return False



def createDbFile(dbFileName, schemaFileName):
    """
    Create DataBases in DataBase file acording to Schema
    """
    if not isDbExists(dbFileName):
        print('Создаю базу данных...')
        conn = sqlite3.connect(dbFileName)
        with open(schemaFileName, 'r') as schemaFile:
            schema = schemaFile.read()
        conn.executescript(schema)


if __name__ == "__main__":
    dbFileName = 'dhcp_snooping.db'
    schemaFileName = 'dhcp_snooping_schema.sql'
    createDbFile(dbFileName, schemaFileName)