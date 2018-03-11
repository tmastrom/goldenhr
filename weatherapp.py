#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy, time, sys
from time import sleep
import getdata
 
argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'Vd6EoPPrRX8FGa6dOkzkvOhHP'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'Sa7uD8JN2ySYno9dtBuodNNrSSFkNS6BMZMNflHZaRtfCfGDLF'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '972524990175199232-gKQ3DorQhfnqQLMNJWWTb3hkjBExfDq'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'hWUQtzykXB1pI1VTDxuewqC7O30CW6SyglNJATbPNWrRU'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

getdata.getdata() 
filename=open(argfile,'r')
f=filename.readlines()
filename.close()
 
for status in tweepy.Cursor(api.user_timeline).items():
    try:
        api.destroy_status(status.id)
    except:
        pass

for line in f:
    api.update_status(line)
    time.sleep(60)#Tweet every 15 minutes