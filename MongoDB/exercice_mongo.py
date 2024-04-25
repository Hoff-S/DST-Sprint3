# Do not forget to create a variable in your console with the export command
# You can choose the city of your choice, you only need to write the name in english

# You will need to create a variable WEATHER with your key of OpenWeatherMap

import os 
import requests
from pprint import pprint
from datetime import datetime
from pymongo import MongoClient


KEY = os.getenv("WEATHER")
CITY = "COURBEVOIE"

r = requests.get(
    url="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(
        CITY, KEY
    )
)

data = r.json()

clean_data = {i: data[i] for i in ['weather','main']}

clean_data["weather"] = clean_data["weather"][0]

#---------------------------------------------------------------------------------------------------------

current = datetime.now().strftime('%H:%M:%S')

clean_data['time'] = current
clean_data['city'] = CITY

#---------------------------------------------------------------------------------------------------------

client = MongoClient(
    host="127.0.0.1",
    port = 27017
)

#sample = client['sample']
#col = sample.create_collection(name='weather')
#sample['weater'].insert_one(clean_data)

#---------------------------------------------------------------------------------------------------------

cities = ['Paris','Sens','Carpentras','Avignon']

#Créer une fonction qui permet d'ajouter les data météorologiques de l'API pour une ville 

def make_data(city):
    r = requests.get(url="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, KEY))
    data = r.json()
    clean_data = {i: data[i] for i in ['weather','main']}
    clean_data['weather']=clean_data['weather'][0]
    return clean_data

#Créer une fonction qui permet d'ajouter la ville et la date au document

def add_key(data, city):
    current = datetime.now().strftime('%H:%M:%S')
    data['time'] = current
    data['city'] = city
    return data

#Créer une fonction qui injecte le résultat des deux premières fonctions dans le document

def add_data(client, cities):

    col = client['sample']['weather']

    for city in cities:
        make_data(city)
        add_key(data,city)
        col.insert_one(data)
    

#add_data(client, ['paris','carpentras','avignon','sens'])

col = client['sample']['weather']

for i in list(col.find({'weather.main':'Clear'},{'_id':0,'city':1})):
    print(i)