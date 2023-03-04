import pymongo

client = pymongo.MongoClient("mongodb+srv://root:sumit1234@cluster.lmppirl.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    'name': 'sumit',
    'email':'sumit@123',
    'surname': 'kumar'
}
db1=client['mongo_data']
coll=db1['dict']
coll.insert_one(d)