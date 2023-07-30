import pymongo

client = pymongo.MongoClient("mongodb+srv://root:sumit1234@cluster.lmppirl.mongodb.net/?retryWrites=true&w=majority")
db = client.test

data={
    'name': 'sumit',
    'email':'sumit@123',
    'surname': 'kumar',
    'name1': 'sumit',
    'email2': 'sumit@123',
    'surname3': 'kumar'

}

Jshon_income=[
    {'name': 'sumit',
    'email':'sumit@123',
    'surname': 'kumar',
     },
    {'name': 'sumit',
    'email':'sumit@123',
    'surname': 'kumar',
    },
    {
    'name': 'sumit',
    'email':'sumit@123',
    'surname': 'kumar',
    }
]
database=client['info']
collection1=database['dict']
collection1.insert_one(data)
collection2=database['Jshon_doc']



##collection2.insert_many(Jshon_income)
##record=collection1.find()
##record=collection2.find({'name1': {'gt': 't'}})
#record=collection1.find({'name1':'sumit'})
for i in record:
    print(i)

