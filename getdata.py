# -*- coding: utf-8 -*-
 
import requests
import json
import datetime
from pytz import timezone
import pytz
from datetime import date

#6173331 - Vancouver
def getdata():

	# Get data from Vancouver lat=38.429 lon=-123.358
	response = requests.get("http://api.openweathermap.org/data/2.5/weather?id=6173331&APPID=f0654c69c01c9b88a55ec593248dc7b3")


	# Get the response data as a python object.  Verify that it's a dictionary.
	data = response.json()

	#read and assign values to the important variables
	weathertype = data['weather'][0]['main'] #ex. clear 
	weatherdesc = data['weather'][0]['description'] #ex clear sky 
	pres = data['main']['pressure'] 
	degc = data['main']['temp']
	humidity = data['main']['humidity']
	clouds = data['clouds']['all'] 
	ws = 3.6*data['wind']['speed']
	wd = data['wind']['deg']
	trise = data['sys']['sunrise']
	tset = data['sys']['sunset']
	tdata = data['dt'] #convert from UTC
	#rain = data.get['rain'] add this 
	goldenhour = 0
	potential = "low"


	#convert unix to UTC
	utrise = datetime.datetime.utcfromtimestamp(trise)
	print('rise time utc',utrise)
	utset = datetime.datetime.utcfromtimestamp(tset)
	print utset

	date_format='%H:%M:%S'

	#split time into its components 
	utrise = utrise.strftime(date_format)
	print utrise
	from datetime import date
	hr,mn,sec = utrise.split(':')
	print hr,mn,sec

	#split time into its components
	utset = utset.strftime(date_format)
	print utset
	hr1,mn1,sec1 = utset.split(':')
	print hr1,mn1,sec1

	#change hour from UTC to PST
	ihr = int(hr)
	ihr = (ihr+5)%12
	print ihr

	ihr1 = int(hr1)
	ihr1 = (ihr1-7)%12
	print ihr1

	#determine goldenhour potential 
	#rain in last 3hrs == true (add criteria)
	if clouds <= 70: 	#clouds < 70
		if clouds >= 30:
			goldenhour = goldenhour + 1
		if pres >= 1000: 				# pressure high >= 1000 hPa 
			goldenhour = goldenhour + 1
		if ws <= 20:					# ws < 20km/h
			goldenhour = goldenhour + 1
		if humidity <= 70:				# low humidity
			goldenhour = goldenhour + 1
	if goldenhour >= 3:
		potential = 'HIGH' #high potential 
	if goldenhour < 3 and goldenhour > 0:
		potential = 'MED'
	if goldenhour == 0:
		potential = 'LOW'

	#find wind direction
	if wd >= 337.5 and wd <= 22.5: 
	  wd = 'N'
	if wd > 22.5 and wd < 67.5:
	  wd = 'NE'
	if wd >= 67.5 and wd <= 112.5:
	  wd = 'E'
	if wd >112.5 and wd < 157.5:
	  wd = 'SE'
	if wd >= 157.5 and wd <= 202.5:
	  wd = 'S'
	if wd > 202.5 and wd < 247.5:
	  wd = 'SW'
	if wd >= 247.5 and wd <= 292.5: 
	  wd = 'W'
	if wd > 292.5 and wd < 337.5:
	  wd = "NW"

	#write tweet to txt file
	f = open('weatherapp.txt','w')
	f.write('Golden hour potential today is {} '.format(potential))
	f.write('Current Conditions: {} '.format(weatherdesc))
	f.write('Wind speed: {} km/hr {} '.format(ws,wd))
	f.write('Sunset {}:{}:{} PST '.format(ihr1,mn1,sec1))
	f.write('Sunrise {}:{}:{} PST '.format(ihr,mn,sec))
	f.write('Happy Shooting!')
	f.close
	return
