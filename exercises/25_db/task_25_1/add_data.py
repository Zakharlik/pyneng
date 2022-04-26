"""
Adding data to dhcp snooping DB
"""
import re
import yaml
import sqlite3
import os

def readDataFile(dataFileName):
    """
    Read date file. Parse it. Return list of lists of data.
    """
    result = []
    # Regex for parse data lines and skeep header lines:
    regex = re.compile(r'(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
    with open(dataFileName, 'r') as dataFile:
        for line in dataFile:
            match = regex.search(line)
            if match:
                result.append(match.groups())
    return result

def readSwitchesFile(switchesFileName):
    """
    Read list of switches from YAML file
    """
    with open(switchesFileName, 'r') as switchesFile:
        switchesList = yaml.safe_load(switchesFile)
        print(switchesList['switches'])
    return switchesList['switches']

def insertData(tableName, dbFileName, dataList):
    """
    !!! Not used in this project. Too dificult to prepare data !!!
    Inserts data from 'dataList' to 'tableName' table in DB.
    tableName - string - Name of table
    dataList - list of lists. Rectangle matrix. Internal lists is a row in table.
               Each row must contains exect the same number of items.
    """
    conn = sqlite3.connect(dbFileName)
    try:
        cols = len(dataList[0])
        query = f"insert into {tableName} values ({'?, '*(cols - 1)} ?)"
        for row in dataList:
            try:
                with conn:
                    conn.execute(query, row)
            except sqlite3.IntegrityError as e:
                print ('Error code: ', e)
        conn.close()
    except Exception as e:
        print('Неправильный список!!', e)

def insertSwitchesData(tableName, dbFileName, dataDict):
    """
    Inserts data from 'dataDict' to 'tableName' table in DB.
    tableName - string - Name of table
    dataDict - list of dicts.
    """
    conn = sqlite3.connect(dbFileName)
        for item in dataDict:
            query = f"insert into {tableName} values {item}, {item.value})"
            try:
                with conn:
                    conn.execute(query)
            except sqlite3.IntegrityError as e:
                print ('Error code: ', e)
        conn.close()
    except Exception as e:
        print('Неправильный список!!', e)


if __name__ == '__main__':
    insertData('switches', 'dhcp_snooping.db', readSwitchesFile('switches.yml'))
    for file in os.listdir():
        if file.startswith('sw') and file.endswith('.txt'):
            dataList = [file[:3]]
            for item in readDataFile(file):
                dataList.append(item)
            print(dataList)
            insertData('dhcp', 'dhcp_snooping.db', dataList)
