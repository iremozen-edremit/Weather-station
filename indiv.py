from datetime import datetime
from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
import cloudant
import pandas as pd
from collections import Counter

serviceUsername = "xxxxxxxx--bluemix"
servicePassword = "xxxxxxxxxxxxxxxxxxxxxx"
serviceURL =  "https://xxxxx-bluemix:xxxxxxxxxxxxxxxxxx-bluemix.cloudant.com"
client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
client.connect()

# 3rd party modules
from flask import (
    make_response,
    abort
)

database1 = client['comfort'] #choose an database from cloudant
database2 = client['users'] #choose an database from cloudant

#result_collection = Result(database2.all_docs, include_docs=True)
#print("users of this house: ")
#print("\t")
#for result in result_collection:
 #   print(result['id'])

person = input("choose an user above: ") #mduffield
print(person)
person1 = "barbarar"

def username():
    return person1

selector1 = { '$and': [{'user_id': {'$eq': person1}},{'happiness' : {'$eq': True}}]}
resp = database1.get_query_result(selector1, raw_result=True, limit=2000)
conf = pd.DataFrame(resp['docs'])

selector1 = { '$and': [{'user_id': {'$eq': person1}},{'happiness' : {'$eq': False}}]}
resp = database1.get_query_result(selector1, raw_result=True, limit=2000)
unconf = pd.DataFrame(resp['docs'])

cols = ['date','module_name', 'location','tempature','humidity','user_id','co2']
lst = []

for index, val in conf['location'].items():
    if val == 'hotDeskArea':
        lst.append([conf['date'][index],conf['netatmoData'][index]['devices'][1]['module_name'],conf['location'][index], conf['netatmoData'][index]['devices'][1]['dashboard_data']['Temperature'],conf['netatmoData'][index]['devices'][1]['dashboard_data']['Humidity'], conf['user_id'][index],conf['netatmoData'][index]['devices'][1]['dashboard_data']['CO2']])
    if val == 'supportServices':
        lst.append([conf['date'][index],conf['netatmoData'][index]['devices'][1]['module_name'],conf['location'][index], conf['netatmoData'][index]['devices'][0]['dashboard_data']['Temperature'],conf['netatmoData'][index]['devices'][0]['dashboard_data']['Humidity'], conf['user_id'][index],conf['netatmoData'][index]['devices'][0]['dashboard_data']['CO2']])
    if val == 'trainingRoom':
        lst.append([conf['date'][index],conf['netatmoData'][index]['devices'][1]['modules'][1]['module_name'],conf['location'][index], conf['netatmoData'][index]['devices'][1]['modules'][1]['dashboard_data']['Temperature'], conf['netatmoData'][index]['devices'][1]['modules'][1]['dashboard_data']['Humidity'], conf['netatmoData'][index]['devices'][1]['modules'][1]['dashboard_data']['CO2']])
    if val == 'boardRoom':
        lst.append([conf['date'][index],conf['netatmoData'][index]['devices'][1]['modules'][2]['module_name'],conf['location'][index], conf['netatmoData'][index]['devices'][1]['modules'][2]['dashboard_data']['Temperature'],conf['netatmoData'][index]['devices'][1]['modules'][2]['dashboard_data']['Humidity'],conf['netatmoData'][index]['devices'][1]['modules'][2]['dashboard_data']['CO2']])
    if val == 'directorsRoom':
        lst.append([conf['date'][index],conf['netatmoData'][index]['devices'][1]['modules'][3]['module_name'],conf['location'][index], conf['netatmoData'][index]['devices'][1]['modules'][3]['dashboard_data']['Temperature'],conf['netatmoData'][index]['devices'][1]['modules'][3]['dashboard_data']['Humidity'],conf['netatmoData'][index]['devices'][1]['modules'][3]['dashboard_data']['CO2']])
    if val == 'home':
        lst.append([conf['date'][index],conf['netatmoData'][index]['devices'][1]['modules'][0]['module_name'],conf['location'][index], conf['netatmoData'][index]['devices'][1]['modules'][0]['dashboard_data']['Temperature'],conf['netatmoData'][index]['devices'][1]['modules'][0]['dashboard_data']['Humidity'],conf['user_id'][index]])
    if val == 'client':
        lst.append([conf['date'][index],conf['netatmoData'][index]['devices'][0]['modules'][0]['module_name'],conf['location'][index], conf['netatmoData'][index]['devices'][0]['modules'][0]['dashboard_data']['Temperature'],conf['netatmoData'][index]['devices'][0]['modules'][0]['dashboard_data']['Humidity'],conf['user_id'][index]])

outputcomf = pd.DataFrame(lst, columns=cols)


cols2 = ['date','module_name', 'location','tempature','humidity','user_id','co2']
lst2 = []
for index, val in unconf['location'].items():
    if val == 'hotDeskArea':
        lst2.append([unconf['date'][index],unconf['netatmoData'][index]['devices'][1]['module_name'],unconf['location'][index], unconf['netatmoData'][index]['devices'][1]['dashboard_data']['Temperature'],unconf['netatmoData'][index]['devices'][1]['dashboard_data']['Humidity'], unconf['user_id'][index], unconf['netatmoData'][index]['devices'][1]['dashboard_data']['CO2']])
    if val == 'supportServices':
        lst2.append([unconf['date'][index],unconf['netatmoData'][index]['devices'][1]['module_name'],unconf['location'][index], unconf['netatmoData'][index]['devices'][0]['dashboard_data']['Temperature'],unconf['netatmoData'][index]['devices'][0]['dashboard_data']['Humidity'], unconf['user_id'][index], unconf['netatmoData'][index]['devices'][0]['dashboard_data']['CO2']])
    if val == 'trainingRoom':
        lst2.append([unconf['date'][index],unconf['netatmoData'][index]['devices'][1]['modules'][1]['module_name'],unconf['location'][index], unconf['netatmoData'][index]['devices'][1]['modules'][1]['dashboard_data']['Temperature'], unconf['netatmoData'][index]['devices'][1]['modules'][1]['dashboard_data']['Humidity'], unconf['netatmoData'][index]['devices'][1]['modules'][1]['dashboard_data']['CO2']])
    if val == 'boardRoom':
        lst2.append([unconf['date'][index],unconf['netatmoData'][index]['devices'][1]['modules'][2]['module_name'],unconf['location'][index], unconf['netatmoData'][index]['devices'][1]['modules'][2]['dashboard_data']['Temperature'],unconf['netatmoData'][index]['devices'][1]['modules'][2]['dashboard_data']['Humidity'],unconf['netatmoData'][index]['devices'][1]['modules'][2]['dashboard_data']['CO2']])
    if val == 'directorsRoom':
        lst2.append([unconf['date'][index],unconf['netatmoData'][index]['devices'][1]['modules'][3]['module_name'],unconf['location'][index], unconf['netatmoData'][index]['devices'][1]['modules'][3]['dashboard_data']['Temperature'],unconf['netatmoData'][index]['devices'][1]['modules'][3]['dashboard_data']['Humidity'],unconf['netatmoData'][index]['devices'][1]['modules'][3]['dashboard_data']['CO2']])
    if val == 'home':
        lst2.append([unconf['date'][index],unconf['netatmoData'][index]['devices'][1]['modules'][0]['module_name'],unconf['location'][index], unconf['netatmoData'][index]['devices'][1]['modules'][0]['dashboard_data']['Temperature'],unconf['netatmoData'][index]['devices'][1]['modules'][0]['dashboard_data']['Humidity'],unconf['user_id'][index]])
    if val == 'client':
        lst2.append([unconf['date'][index],unconf['netatmoData'][index]['devices'][0]['modules'][0]['module_name'],unconf['location'][index], unconf['netatmoData'][index]['devices'][0]['modules'][0]['dashboard_data']['Temperature'],unconf['netatmoData'][index]['devices'][0]['modules'][0]['dashboard_data']['Humidity'],unconf['user_id'][index]])

outputuncomf = pd.DataFrame(lst2, columns=cols2)

def confTempature():
    return outputcomf["tempature"].mean()

def confHumAv():
    return outputcomf["humidity"].mean()

def confCO2Av(): 
    return outputcomf["co2"].mean()

def coonfRoom ():
    return outputcomf['module_name'].value_counts().idxmax()

def unconfTempAv():
    return outputuncomf["tempature"].mean()

def unconfHumAv():
    return outputuncomf["humidity"].mean()

def unconfCO2Av():
    return outputuncomf["co2"].mean()

def unconfRoom():
    return outputuncomf['module_name'].value_counts().idxmax()


PEOPLE = {
    "comfortable": {
    	"user": username(),
        "comfortable" : "True",
        "module_name": coonfRoom (),
        "tempature": confTempature(),
        "humidity": confHumAv(),
        "co2": confCO2Av()
    },
    "Uncomfortable": {
    	"user" : username(),
        "comfortable": "False",
        "module_name": unconfRoom(),
        "tempature": unconfTempAv(),
        "humidity": unconfHumAv(),
        "co2": unconfCO2Av()
    }
}


def read_one(user):
    """
    This function responds to a request for /api/people/{user}
    with one matching person from people
    :param user:   last name of person to find
    :return:        person matching last name
    """
    # Does the person exist in people?
    if user in PEOPLE:
        person = PEOPLE.get(user)

    # otherwise, nope, not found
    else:
        abort(404, 'Person with last name {user} not found'.format(
            user=user))

    return person
