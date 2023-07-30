import pymongo

data=[
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]

client = pymongo.MongoClient("mongodb+srv://user:root@cluster.a5ybbld.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database= client['database']
collection=database['Collection']
#collection.insert_many(data)
#d=collection.find()
#d=collection.find({'status':'A'})
#d=collection.find({'status':{'$in':['A','P']}})
#d=collection.find({'status':{'$gt':'C'}})              #greater than
#d=collection.find({'qty':{'$gte':75}})                  #greater than equals too
#d=collection.find({'qty':95,'item':'sketch pad'})
#d=collection.find({'qty':{'$gte':75},'item':'sketch pad'})
#d=collection.find({'$or':[{'qty':{'$gte':75},'item':'sketch pad'}]})    #or function
#d=collection.update_one({'item':'canvas'},{'$set':{'item':'sumit'}})
#d=collection.find({'item':'sumit'})
#collection.delete_one({'item':'sumit'})
#d=collection.find({'item':'sumit'})
for i in d:
    print(i)