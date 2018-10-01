from datetime import datetime
from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
import cloudant
import pandas as pd
from collections import Counter

serviceUsername = "xxxxxxxxxxxxxxxxxxxxxxxxxx-bluemix"
servicePassword = "xxxxxxxxxxxxxxxxxxxx"
serviceURL =  "https://xxxxxxxxxx-bluemix:xxxxxxxxxxxxxxxxxxxx-bluemix.cloudant.com"
client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
client.connect()
database1 = client['comfort'] #choose an database from cloudant

selector1 ={'happiness': {'$eq' : True}}
resp1 = database1.get_query_result(selector1, raw_result=True)
conf = pd.DataFrame(resp1['docs'])
#Uncomfortable Table
selector2 = {'happiness': {'$eq' : False}}
resp2 = database1.get_query_result(selector2, raw_result=True)
unconf = pd.DataFrame(resp2['docs'])

    #A new dataset is created which includes which columns wanted to see to keep dataset more organized and to make it easier to read
    #This dataset is for comfortable inputs
cols = ['date','module_name', 'location','tempature','humidity','user_id','co2']
lst = []

#If this code wants to be applied to another house, below locations must be changed.
#In this part every 'location' column is being pointed out equal 'module_name' which is nested JSON data. So correct temperature values that locations have can be determined.
#If there must be changes on locaiton. Number between of ['modules'] and ['module_name'] columns must be changed. Or "vall" equal value in the if loop can be changed for this kind of changes
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


#Same process is applied for uncomfortable variables
#This second dataset is for Uncomfortable inputs
cols2 = ['date','module_name', 'location','tempature','humidity','user_id','co2']
lst2 = []
for index, val in unconf['location'].items():
    if val == 'hotDeskArea':
        lst2.append([unconf['date'][index],unconf['netatmoData'][index]['devices'][1]['module_name'],unconf['location'][index], unconf['netatmoData'][index]['devices'][1]['dashboard_data']['Temperature'],unconf['netatmoData'][index]['devices'][1]['dashboard_data']['Humidity'], unconf['user_id'][index]])
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


# Data to serve with our API
PEOPLE = {
    "comfortable": {
        "comfortable" : "True",
        "module_name": coonfRoom (),
        "tempature": confTempature(),
        "humidity": confHumAv(),
        "co2": confCO2Av()
    },
    "Uncomfortable": {
        "comfortable": "False",
        "module_name": unconfRoom(),
        "tempature": unconfTempAv(),
        "humidity": unconfHumAv(),
        "co2": unconfCO2Av()
    }
}

# Create a handler for our read (GET) people
def read():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        sorted list of people
    """
    # Create the list of people from our data
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]