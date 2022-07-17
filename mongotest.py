import pymongo


# client = pymongo.MongoClient("mongodb+srv://Praveen:Prvn$766@cyrus.pnrelqq.mongodb.net/?retryWrites=true&w=majority")
# db = client.test
# print(db)

client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"praveen",
    "email":"prvn07tiwari@gmail.com",
    "surname":"kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )
