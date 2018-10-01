# Weather-station

Database: IBM CLoudant
Language: Python


1)The first step of the project is to pre-process data which is taken from users and
weather station devices which is formatted JSON.
Users submit their happiness according to environment variables such as temperature,
noise, wind. The device takes the information of the temperate, noise, pressure, co2 and
time at the same time with user's submission. Every person also has to submit their room
name in the system. But the device which uses cannot separate the rooms. That's why every
each submission has a long and complexity. (pls send a mail to see an example of the Json data)

2) Every room must be matched with true temperature variables based location
information in the device data. That’s why every submission must be cleaned other
rooms information. To realize it I code a Python API script which includes Pandas
library. 

3) At the end of analyzing every desired threshold variables can be reached based
on the location from the website.


to make the flask profited by https://realpython.com/flask-connexion-rest-api/ page
