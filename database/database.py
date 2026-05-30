#Database code used to generate and run databases

import sqlite3

#connect to db
def connectDb():
    try:
        connection = sqlite3.connect("./snowsports.db", check_same_thread=False)
        database = connection.cursor()
        print("Connected to results database")
        return database, connection
    except:
        return None
    
#create tables for comp pages
def createResultsTable(database, connection):
    createTable = 'CREATE TABLE IF NOT EXISTS results (competitionID INTEGER NOT NULL PRIMARY KEY, eventType TEXT NOT NULL, ageCategory TEXT NOT NULL, genderCategory TEXT NOT NULL, first TEXT, second TEXT, third TEXT, FOREIGN KEY(competitionID) REFERENCES competition(userID))'
    database.execute(createTable)
    connection.commit()

def createCompetitionTable(database, connection):
    createTable = 'CREATE TABLE IF NOT EXISTS competition (competitionID INTEGER NOT NULL, name TEXT NOT NULL, organiser TEXT NOT NULL, location TEXT NOT NULL, bigAir INTEGER, railEvent INTEGER, slopeStyle INTEGER'
    database.execute(createTable)
    connection.commit()

#Create all tables code
def createTables(database, connection):
    createResultsTable(database, connection)
    createCompetitionTable(database, connection)
    print("Tables Created / Tables Already Exist")


