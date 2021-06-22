from pymongo import MongoClient

try:
    connection = MongoClient()
    print("Successfull connected")
except:
    print("could not connect to mongodb")

#MED.MedConSquad eeb800d2-66fc-41a2-b1f9-2320740e045a Medical ART content pipeline team


db = connection['opsgenie_db']
teams = db['teams']

document1 = {
    "name":"MED.MedConSquad",
    "opsgenie_id":"eeb800d2-66fc-41a2-b1f9-2320740e045a"
}

teams.insert_one(document1)

cursor = teams.find()
for record in cursor:
    print(record)

connection.close()