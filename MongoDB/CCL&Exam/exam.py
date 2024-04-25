
from pymongo import MongoClient
from pprint import pprint
import re
from datetime import datetime, date

client = MongoClient(
    host="127.0.0.1",
    port = 27017,
    username = 'admin',
    password = 'pass'
)

### Connection à la base de donnée

#Exercice A & B
#Affichage de la liste des bases de données disponibles
#print(client.list_database_names())

#---

#Exercice C
#Affichage de la liste des collections disponibles dans la BDD "sample"
#print(client['sample'].list_collection_names())

#---

#Exercice D
#Affichage d'un des documents de la collection "books" avec pprint
#pprint(client['sample']['books'].find_one())

#---

#Exercice E
#Affichage du nombre de documents dans cette collection
#count = len(list(client['sample']['books'].find()))
#print(f'La collection books comporte {count} document(s)')

### Exploration de la base 

col = client['sample']['books']

#Exercice A

"""
result1 = len(
    list(
        col.find(
            {
                'pageCount':{'$gt':400}
            }
        )
    )
)

result2 = len(
    list(
        col.find(
            {
                '$and':
                [
                    {'pageCount':{'$gt':400}},
                    {'status':'PUBLISH'}
                ]
            }
        )
    )
)

print(f'Nombre de livres avec plus de 400 pages dans la base : {result1}. Dont {result2} sont publiés.')
"""

#Exercice B

"""
result = len(
    list(
        col.find(
            {
                '$or':
                [
                    {'shortDescription':{'$regex':'(?i)A(?-i)ndroid'}},
                    {'longDescription':{'$regex':'(?i)A(?-i)ndroid'}}
                ]
            },
            {
            '_id':1
            }
        )
    )
)

print(f'Le nombre de documents dont la description, courte ou longue, contient la chaine "Android" est : {result}')
"""

#Exercice C

"""
result = col.aggregate([
    {
        '$group':
        {
            '_id':0,
            'categorie_0': {'$addToSet': {'$arrayElemAt': ['$categories', 0]}},
            'categorie_1': {'$addToSet': {'$arrayElemAt': ['$categories', 1]}}
        }
    }
])

pprint(list(result))
"""

#Exercice D
"""
result1 = len(
    list(
        col.find(
            {
                'longDescription':{'$regex':'(Python|Java|C\+\+|Scala)'}
            },
            {
            '_id':1
            }
        )
    )
)

print(f'Le nombre de documents dont la description longue contient les chaines "Python","Java","C++" ou "Scala" est : {result1}')
"""

#Exercice E
"""
result = col.aggregate([
    {
        '$unwind':'$categories'
    },
    {
        '$group':
        {
            '_id':'$categories',
            'pages_max': {'$max': '$pageCount'}, 
            'pages_min': {'$min': '$pageCount'},
            'pages_moyen': {'$avg': '$pageCount'}
        }
    }
    
])

pprint(list(result))
"""

#Exercice F
"""
result = col.aggregate([
    {
        '$project':
        {
            '_id':0,
            'publishedYear':{'$year':{'$toDate':'$publishedDate'}},
            'publishedMonth':{'$month':{'$toDate':'$publishedDate'}},
            'publishedDay':{'$dayOfMonth':{'$toDate':'$publishedDate'}}
        }
    },
    {
        '$match':
        {
            'publishedYear':{'$gt':2009}
        }
    },
    {
        '$limit':20
    }
])

pprint(list(result))
"""

#Exercice G

"""
operation = [
    {
        '$project': 
        {
            '_id': 0,
            'authors': 1,
            'publishedDate': 1
        }
    },
    {
        '$sort': {'publishedDate': 1}
    },
    {
        '$limit': 20
    },
    {
        '$addFields': 
        {
            'nb_authors': {'$size': '$authors'} 
        }
    }
]


for i in range(1, 100):
    operation.append(
        {
            '$addFields': 
            {
                f'author_{i}': 
                {
                    '$arrayElemAt': ['$authors', i-1]
                }
            }
        }
    )

pprint(list(col.aggregate(operation)))
"""

#Exercice H
"""
result = col.aggregate([
    {
        '$project': 
        {
            '_id': 0,
            'first_author': {'$arrayElemAt': ['$authors', 0]}
        }
    },
    {
        '$group': 
        {
            '_id': '$first_author',
            'count': {'$sum': 1}
        }
    },
    {
        '$sort': {'count': -1}
    },
    {
        '$limit': 10
    }
])

pprint(list(result))
"""
