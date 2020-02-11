import sqlite3

def execute(databaseFilePath, sqlCommand, parameters=None):
    try:
        conn = sqlite3.connect(databaseFilePath)

        if(parameters != None):
            conn.execute(sqlCommand, parameters)
        else:
            conn.execute(sqlCommand)

        conn.commit()
    finally:
        conn.close()

