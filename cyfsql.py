import sqlite3 as dbapi
class CyfSQL():
    def __init__(self, filename):
        self.db = filename
    def load(self):
        self.bbdd = dbapi.connect(self.db)
        self.cursor = self.bbdd.cursor()
    def save(self):
        self.bbdd.commit()
    def close(self):
        self.cursor.close()
        self.bbdd.close()
    def query(self, query):
        self.cursor.execute(query)
    def fetchall(self):
        return self.cursor.fetchall()
    def createtable(self, name, values):
        q= "create table " + name + " ("
        for x in values:
            q = q + x + ","
        q = q[:len(q)-1]
        q = q + ")"
        return q