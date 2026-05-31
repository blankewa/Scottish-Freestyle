#Database code used to generate and run databases

import sqlite3
import json

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

#read JSONS
def readCompetitionJSON(database, connection):
    with open("./jsons/competition.json", "r") as data:
        competitions = json.load(data)
        for competition in competitions:
            database.execute(f"SELECT EXISTS(SELECT 1 FROM competition WHERE competitionID={competition['competitionID']})")
            if database.fetchone()[0] == 0:
                database.execute(f"INSERT INTO competition (competitionID, name, organiser, location, bigAir, railEvent, slopeStyle) VALUES ('{competition["competitionID"]}', '{competition["name"]}', '{competition["organiser"]}', '{competition["location"]}', '{competition["bigAir"]}', '{competition["railEvent"]}', '{competition["slopeStyle"]}')")
                print("Compeition inserted")
            else:
                print(f"Compeition with ID {competition['competitionID']} already exists")
    connection.commit()
    print("loaded competition data")   

def readResultsJSON(database, connection):
    with open("./jsons/results.json", "r") as data:
        results = json.load(data)
        for result in results:
            database.execute(f"SELECT EXISTS(SELECT 1 FROM results WHERE competitionID={result['competitionID']})")
            if database.fetchone()[0] == 0:
                database.execute(f"INSERT INTO results (competitionID, event, ageCategory, genderCategory, first, second, third) VALUES ('{result['competitionID']}', '{result['eventType']}', '{result['ageCategory']}', '{result['genderCategory']}', '{result['first']}', '{result['second']}', '{result['third']}')")
                print("Result inserted")
            else:
                print(f"Result with ID {result['competitionID']} already exists")
    connection.commit()
    print("loaded results data")