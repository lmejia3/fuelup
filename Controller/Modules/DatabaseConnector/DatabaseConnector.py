import MySQLdb as sql

def getDatabaseObject():
    db = sql.connect(host="yofueldb.cbbjfhnlihgx.us-east-2.rds.amazonaws.com",
                     port=3306,user="server_backend",passwd="mypassword.net52005",db="FuelTest")
    return db

def runQuery(query):
    db = getDatabaseObject()
    db.query(query)
    return db.use_result().fetch_row(0, how=1)


"""demonstration:"""
q = "SELECT * FROM Login_Info"
data = runQuery(q)
print(data)
