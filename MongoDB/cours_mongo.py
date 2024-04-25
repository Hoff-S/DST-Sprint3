from pymongo import MongoClient

client = MongoClient(
    host="127.0.0.1",
    port = 27017
)

#print(client.list_database_names())

#---------------------------------------------------------------------------------------------------------

sample = client['sample']
c_zips = sample['zips']

#print(c_zips.find_one())

#---------------------------------------------------------------------------------------------------------

#rand = sample.create_collection(name='rand')

#---------------------------------------------------------------------------------------------------------

data = [
  {"name": "Melthouse","bread":"Wheat","sauce": "Ceasar"},
  {"name": "Italian BMT", "extras": ["pickles","onions","lettuce"],"sauce":["Chipotle", "Aioli"]},
  {"name": "Steakhouse Melt","bread":"Parmesan Oregano"}, 
  {"name": "Germinal", "author":"Emile Zola"}, 
  {"pastry":"cream puff","flavour":"chocolate","size":"big"}
]

#sample['rand'].insert_many(data)

#print(sample['rand'].find_one())

#---------------------------------------------------------------------------------------------------------

zips = client["sample"]["zips"]

#for i in list(zips.find({},{"_id":0,"city":1})):
#    print(i)

#---------------------------------------------------------------------------------------------------------

from pprint import pprint

#pprint(zips.find().distinct("state"))

#---------------------------------------------------------------------------------------------------------

import re 

zips = client["sample"]["zips"]

exp = re.compile("^[0-9]*$")
#pprint(list(zips.find({"city": exp}, {"city": 1})))

#---------------------------------------------------------------------------------------------------------

"""
pprint(
    list(
        client['sample']['cie'].aggregate(
            [
                {'$match': {'acquisitions.company.name':'Tumblr'}},
                {'$project': {'_id':1, 'societey':'$name'}}
            ]
        )
    )
)
"""

#---------------------------------------------------------------------------------------------------------

