import sqlite3
from sqlite3 import Error

def setupTable(dbFilePath):
    connObj = None

    try:
        connObj = sqlite3.connect(dbFilePath)
        print(sqlite3.version)
        return connObj

    except Error as e:
        print(e)

    return connObj

def createTable(connObj):
    
    sqlCommand_CreatePersonsTable = """ CREATE TABLE IF NOT EXISTS persons (
                                            PersonID integer PRIMARY KEY AUTOINCREMENT,
                                            LastName text NOT NULL,
                                            FirstName text NOT NULL,
                                            PhoneNumber txt NOT NULL
                                        );"""

    try:
        cur = connObj.cursor()
        cur.execute(sqlCommand_CreatePersonsTable)
        print("Table Created")

    except Error as e:
        print(e)
        return None

def addUser(connObj, userInfo):
    
    sqlCommand_InsertUser = "INSERT INTO persons(LastName, FirstName, PhoneNumber) VALUES (?,?,?)"

    try:
        cur = connObj.cursor()
        cur.execute(sqlCommand_InsertUser, userInfo)
        connObj.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return None


def updateUser(connObj, userInfo):
    
    sqlCommand_UpdateUser = """ UPDATE persons
                                SET LastName = ?,
                                    FirstName = ?,
                                    PhoneNumber = ?
                                WHERE PersonID = ?"""

    try:
        cur = connObj.cursor()
        cur.execute(sqlCommand_UpdateUser, userInfo)
        connObj.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return None


def deleteUser(connObj, id):
    
    sqlCommand_DeleteUser = "DELETE FROM persons WHERE PersonID = ?"

    try:
        cur = connObj.cursor()
        cur.execute(sqlCommand_DeleteUser, (id,))
        connObj.commit()
        return cur.lastrowid

    except Error as e:
        print(e)
        return None

def getAllUsers(connObj):
    
    sqlCommand_GetUsers = 'SELECT * FROM persons'

    try:
        cur = connObj.cursor()
        cur.execute(sqlCommand_GetUsers)
        users = cur.fetchall()
        if len(users) == 0:
            return None
        else:
            return users


    except Error as e:
        print(e)
        return None


if __name__ == '__main__':
    connObj = setupTable("practice.db")

    if connObj is not None:
        
        createTable(connObj)

        userInfo = "Picard", "Jean-Luc", "555-555-5555"
        addUser(connObj, userInfo)
        userInfo = "Paris", "Tom", "555-555-5556"
        addUser(connObj, userInfo)
        userInfo = "Janeway", "Kathy", "555-555-5557"
        addUser(connObj, userInfo)

        # userInfo = "Unimatrix 1001", "Locutus", "555-555-5555", 1
        # updateUser(connObj, userInfo)

        # rowID = 1
        # deleteUser(connObj, rowID)

        users = getAllUsers(connObj)

        print(type(users))
        print(type(users[0]))

        for user in users:
            print(user)
        print()