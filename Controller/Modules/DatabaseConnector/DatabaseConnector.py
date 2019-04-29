import MySQLdb as sql
import MySQLdb.cursors as cur

def getDatabaseObject():
    db = sql.connect(host="yofueldb.cbbjfhnlihgx.us-east-2.rds.amazonaws.com",
                     port=3306,user="server_backend", passwd="mypassword.net52005", db="FuelDummy")
    return db

db = getDatabaseObject()

def runQuery(query):
    db.query(query)
    result = db.store_result()
    result = result.fetch_row(0, how = 1)
    return result

def run(query):
    db.query(query)
    result = db.store_result()
    return result

def runInsertQuery(query):
    db.query(query)
    db.commit()

def getData(SELECT, FROM, WHERE = ""):
    q = "SELECT " + SELECT + " FROM " + FROM
    if(WHERE != ""):
        q += " WHERE " + WHERE
    return runQuery(q)

