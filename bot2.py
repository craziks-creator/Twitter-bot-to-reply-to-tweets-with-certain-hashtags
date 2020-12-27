#!/usr/bin/env python
import tweepy, random, time
#from our keys module (keys.py), import the keys dictionary
from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


ids_replied_to = []
with open('E:\\hopebot\\chpp\ids_replied_to.txt', 'r') as filehandle:
    filecontents = filehandle.readlines()

    for line in filecontents:
        # remove linebreak which is the last character of the string
        current_place = line[:-1]
        # add item to the list
        ids_replied_to.append(current_place)
        # This searches Tweets
print('')
print('GeekTechStuff Twitter Search Python Program')
print('')

 
twt = api.search("#hatebot33",result_type="mixed",count=25) 

id = result['id']


if id in ids_replied_to:
    print('')
    print('Skipped as already replied to')
    print('')
        
            
else:        
 for s in twt:
    print(s.id)
    sn = s.user.screen_name
    m = "@%s hello " % (sn)
    api.update_status(status=m, in_reply_to_status_id = s.id)
    time.sleep(20)
print("Done!!!")

